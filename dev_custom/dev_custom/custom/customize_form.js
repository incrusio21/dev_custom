// Copyright (c) 2025, incrusio21 and contributors
// MIT License. See license.txt


frappe.customize_form.module_app = frappe.boot.default_module_app

frappe.ui.form.off("Customize Form", "setup_export")
frappe.ui.form.on("Customize Form", {
    refresh: function (frm) {
		var dev_custom = $('<div class="inner-group-button dev-custom"></div>').prependTo(frm.page.custom_actions)
        let field = frappe.ui.form.make_control({
            df: {
                fieldtype: "Link",
                fieldname: "module_export",
                options: "Module Def",
                label: __("Module"),
                change: () => {
                    var data = field.$input.val()
                    if(data){
                        frappe.customize_form.module_app = data
                    }
                },
            },
            parent: dev_custom,
            render_input: 1,
        });

        field.toggle_label(false);
		field.toggle_description(false)
        field.$input.val(frappe.customize_form.module_app)
	},
    setup_export(frm) {
		if (frappe.boot.developer_mode) {
			frm.add_custom_button(
				__("Export Customizations"),
				function () {
					frappe.prompt(
						[
							{
								fieldtype: "Link",
								fieldname: "module",
								options: "Module Def",
								label: __("Module to Export"),
                                default: frappe.customize_form.module_app,
								reqd: 1,
							},
							{
								fieldtype: "Check",
								fieldname: "sync_on_migrate",
								label: __("Sync on Migrate"),
								default: 1,
							},
							{
								fieldtype: "Check",
								fieldname: "with_permissions",
								label: __("Export Custom Permissions"),
								description: __(
									"Exported permissions will be force-synced on every migrate overriding any other customization."
								),
								default: 0,
							},
						],
						function (data) {
							frappe.call({
								method: "frappe.modules.utils.export_customizations",
								args: {
									doctype: frm.doc.doc_type,
									module: data.module,
									sync_on_migrate: data.sync_on_migrate,
									with_permissions: data.with_permissions,
								},
							});
						},
						__("Select Module")
					);
				},
				__("Actions")
			);
		}
	}
})

frappe.customize_form.save_customization = function (frm) {
	if (frm.doc.doc_type) {
		return frm.call({
			doc: frm.doc,
			freeze: true,
			freeze_message: __("Saving Customization..."),
			btn: frm.page.btn_primary,
            args: {"module": this.module_app},
			method: "save_customization",
			callback: function (r) {
				if (!r.exc) {
					frappe.customize_form.clear_locals_and_refresh(frm);
					frm.script_manager.trigger("doc_type");
				}
			},
		});
	}
};

