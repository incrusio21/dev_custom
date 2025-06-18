app_name = "dev_custom"
app_title = "Dev Custom"
app_publisher = "incrsuio21"
app_description = "Tool to ease custom Frappe customization for developers"
app_email = "abdul.malik.ahmad997@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "dev_custom",
# 		"logo": "/assets/dev_custom/logo.png",
# 		"title": "Dev Custom",
# 		"route": "/dev_custom",
# 		"has_permission": "dev_custom.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_js = "/assets/dev_custom/js/dev_custom.js"
app_include_css = [
	"dev_custom.bundle.css",
]

# include js, css files in header of web template
# web_include_css = "/assets/dev_custom/css/dev_custom.css"
# web_include_js = "/assets/dev_custom/js/dev_custom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dev_custom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Customize Form" : "dev_custom/custom/customize_form.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "dev_custom/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "dev_custom.utils.jinja_methods",
# 	"filters": "dev_custom.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dev_custom.install.before_install"
# after_install = "dev_custom.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dev_custom.uninstall.before_uninstall"
# after_uninstall = "dev_custom.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "dev_custom.utils.before_app_install"
# after_app_install = "dev_custom.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "dev_custom.utils.before_app_uninstall"
# after_app_uninstall = "dev_custom.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dev_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Customize Form": "dev_custom.overrides.customize_form.CustomizeForm"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dev_custom.tasks.all"
# 	],
# 	"daily": [
# 		"dev_custom.tasks.daily"
# 	],
# 	"hourly": [
# 		"dev_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dev_custom.tasks.weekly"
# 	],
# 	"monthly": [
# 		"dev_custom.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "dev_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"frappe.modules.utils.export_customizations": "dev_custom.modules.utils.export_customizations"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dev_custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["dev_custom.utils.before_request"]
# after_request = ["dev_custom.utils.after_request"]

# Job Events
# ----------
# before_job = ["dev_custom.utils.before_job"]
# after_job = ["dev_custom.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"dev_custom.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

extend_bootinfo = [
	"dev_custom.startup.boot.bootinfo",
]