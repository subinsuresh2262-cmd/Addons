app_name = "addons_utils"
app_title = "Addons Utils"
app_publisher = "D-codE"
app_description = "App for Addons"
app_email = "mailtodecode@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/addons_utils/css/addons_utils.css"
# app_include_js = "/assets/addons_utils/js/addons_utils.js"

# include js, css files in header of web template
# web_include_css = "/assets/addons_utils/css/addons_utils.css"
# web_include_js = "/assets/addons_utils/js/addons_utils.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "addons_utils/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Sales Invoice" : "public/js/sales_invoice.js",   
    "Sales Order" : "public/js/sales_order.js",
    "Quotation" : "public/js/quotation.js",
    "Delivery Note" : "public/js/delivery_note.js",
    "Material Request" : "public/js/material_request.js",
    "Purchase Order" : "public/js/purchase_order.js",
    "Purchase Invoice" : "public/js/purchase_invoice.js",
    "Purchase Receipt" : "public/js/purchase_receipt.js",
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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
# 	"methods": "addons_utils.utils.jinja_methods",
# 	"filters": "addons_utils.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "addons_utils.install.before_install"
# after_install = "addons_utils.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "addons_utils.uninstall.before_uninstall"
# after_uninstall = "addons_utils.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "addons_utils.utils.before_app_install"
# after_app_install = "addons_utils.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "addons_utils.utils.before_app_uninstall"
# after_app_uninstall = "addons_utils.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "addons_utils.notifications.get_notification_config"

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

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"validate": [
                    "addons_utils.overrides.queries.validate_max_item_discount_amount",
                    "addons_utils.overrides.queries.validate_max_inv_discount_amount",
                    "addons_utils.overrides.queries.validate_rate_and_price_list",
                    ]
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"addons_utils.tasks.all"
# 	],
# 	"daily": [
# 		"addons_utils.tasks.daily"
# 	],
# 	"hourly": [
# 		"addons_utils.tasks.hourly"
# 	],
# 	"weekly": [
# 		"addons_utils.tasks.weekly"
# 	],
# 	"monthly": [
# 		"addons_utils.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "addons_utils.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "addons_utils.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "addons_utils.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["addons_utils.utils.before_request"]
# after_request = ["addons_utils.utils.after_request"]

# Job Events
# ----------
# before_job = ["addons_utils.utils.before_job"]
# after_job = ["addons_utils.utils.after_job"]

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
# 	"addons_utils.auth.validate"
# ]

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
				"Sales Invoice Item-custom_dummy",
                ],
            ],
        ],
    },
    {
        "doctype": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [
				"Sales Invoice Item-rate-read_only_depends_on",
                ],
            ],
        ],
    },
]