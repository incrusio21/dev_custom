# Copyright (c) 2026, incrucio21 and contributors
# License: MIT. See LICENSE

import frappe 
from erpnext.setup.doctype.transaction_deletion_record.transaction_deletion_record import TransactionDeletionRecord

class DevTransactionDeletionRecord(TransactionDeletionRecord):
    def delete_child_tables(self, doctype, reference_doc_names):
        child_tables = frappe.get_all(
            "DocField", filters={"fieldtype": "Table", "parent": doctype}, pluck="options"
        )

        child_tables_custom = frappe.get_all(
            "Custom Field", filters={"fieldtype": "Table", "dt": doctype}, pluck="options"
        )

        for table in child_tables + child_tables_custom:
            frappe.db.delete(table, {"parent": ["in", reference_doc_names]})