# Copyright (c) 2022, incrucio21 and contributors
# License: MIT. See LICENSE

import frappe
from frappe import _
from frappe.core.doctype.doctype.doctype import (
	check_email_append_to,
	validate_autoincrement_autoname,
	validate_fields_for_doctype,
	validate_series,
)
from frappe.custom.doctype.property_setter.property_setter import delete_property_setter

from frappe.custom.doctype.customize_form.customize_form import CustomizeForm, docfield_properties
from dev_custom.modules.utils import export_customizations

class CustomizeForm(CustomizeForm):
    
    # tambahan pemilihan nama module
    @frappe.whitelist()
    def save_customization(self, module=None):
        if not self.doc_type:
            return

        self.flags.module = module

        validate_series(self, self.autoname, self.doc_type)
        validate_autoincrement_autoname(self)
        self.flags.update_db = False
        self.flags.rebuild_doctype_for_global_search = False
        self.set_property_setters()
        self.update_custom_fields()
        self.set_name_translation()
        validate_fields_for_doctype(self.doc_type)
        check_email_append_to(self)

        if self.flags.update_db:
            try:
                frappe.db.updatedb(self.doc_type)
            except Exception as e:
                if frappe.db.is_db_table_size_limit(e):
                    frappe.throw(
                        _("You have hit the row size limit on database table: {0}").format(
                            "<a href='https://docs.erpnext.com/docs/v14/user/manual/en/customize-erpnext/articles/maximum-number-of-fields-in-a-form'>"
                            "Maximum Number of Fields in a Form</a>"
                        ),
                        title=_("Database Table Row Size Limit"),
                    )
                raise

        if not hasattr(self, "hide_success") or not self.hide_success:
            frappe.msgprint(_("{0} updated").format(_(self.doc_type)), alert=True)
        frappe.clear_cache(doctype=self.doc_type)
        self.fetch_to_customize()

        if self.flags.rebuild_doctype_for_global_search:
            frappe.enqueue(
                "frappe.utils.global_search.rebuild_for_doctype",
                doctype=self.doc_type,
                enqueue_after_commit=True,
            )

        if module:
            export_customizations(module, self.doc_type, sync_on_migrate=1, message=0)
	
    # tambahan module untuk setter baru 
    def make_property_setter(self, prop, value, property_type, fieldname=None, apply_on=None, row_name=None):
        delete_property_setter(self.doc_type, prop, fieldname, row_name)

        property_value = self.get_existing_property_value(prop, fieldname)

        if property_value == value:
            return

        if not apply_on:
            apply_on = "DocField" if fieldname else "DocType"

        # create a new property setter
        frappe.make_property_setter(
            {
                "doctype": self.doc_type,
                "doctype_or_field": apply_on,
                "module": self.flags.module,
                "fieldname": fieldname,
                "row_name": row_name,
                "property": prop,
                "value": value,
                "property_type": property_type,
            },
            is_system_generated=False,
        )

    # tambahan module untuk field baru
    def add_custom_field(self, df, i):
        d = frappe.new_doc("Custom Field")

        d.dt = self.doc_type
        d.module = self.flags.module
        for prop in docfield_properties:
            d.set(prop, df.get(prop))

        if i != 0:
            d.insert_after = self.fields[i - 1].fieldname
        d.idx = i

        d.insert()
        df.fieldname = d.fieldname

        if df.get("in_global_search"):
            self.flags.rebuild_doctype_for_global_search = True
                     