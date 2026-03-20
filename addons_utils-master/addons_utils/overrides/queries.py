# Copyright (c) 2024, D-codE and contributors
# For license information, please see license.txt

import frappe

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_item_uoms(doctype, txt, searchfield, start, page_len, filters):
	if not filters:
		filters = {}
	condition = ""
	condition += f"parent = '{filters.get('item_code')}'"
	return frappe.db.sql(
		"""select uom from `tabUOM Conversion Detail`
			where 
			{condition}
			order by name""".format(
			condition=condition, 
		),)

def validate_max_item_discount_amount(doc,method=None):
	settings =  frappe.get_doc("Addons Utils Settings")
	if settings.enable_max_discount_amount:
		if settings.discount_amount_bypass_role in frappe.get_roles(frappe.session.user):
			return
		max_dis = settings.max_discount_limit
		for it in doc.items:
			if it.discount_amount > max_dis:
				frappe.throw("Discount rate for item {0} cannot be greater than {1}".format(it.item_code,max_dis))

def validate_max_inv_discount_amount(doc,method=None):
	settings =  frappe.get_doc("Addons Utils Settings")
	if settings.enable_max_siv_discount:
		if settings.role in frappe.get_roles(frappe.session.user):
			return
		max_dis = settings.discount_limit
		if doc.discount_amount:
			if doc.discount_amount > max_dis:
				frappe.throw("Discount Amount cannot be greater than {0}".format(max_dis))

@frappe.whitelist()
def rate_hide_validation(item_code):
	if frappe.get_doc("Addons Utils Settings").enable_rate_hide:
		item_group = frappe.db.get_value("Item",item_code, "item_group")
		settings =  frappe.get_doc("Addons Utils Settings")
		items = [d["item_code"] for d in frappe.get_all("Addons Utils Settings Items",fields=["item_code"])]
		item_groups  = [d["item_group"] for d in frappe.get_all("Addons Utils Settings Item Groups",fields=["item_group"])]
		if settings.rate_readonly_role in frappe.get_roles(frappe.session.user):
			if  item_code in items:
				return True
			elif item_group in item_groups:
				return True
			else:
				return False
	else:
		return False

@frappe.whitelist()
def rate_price_list_validation(item_code,rate,price_list_rate):
	if frappe.get_doc("Addons Utils Settings").enable_sales_invoice_rate_validation:
		item_group = frappe.db.get_value("Item",item_code, "item_group")
		settings =  frappe.get_doc("Addons Utils Settings")
		items = [d["item_code"] for d in frappe.get_all("Addons Utils Settings Items Validation",fields=["item_code"])]
		item_groups  = [d["item_group"] for d in frappe.get_all("Addons Utils Settings Item Groups Validation",fields=["item_group"])]
		if settings.sales_invoice_rate_validation_role in frappe.get_roles(frappe.session.user):
			if  item_code in items:
				if float(rate) < float(price_list_rate):
					return False
			elif item_group in item_groups:
				if float(rate) < float(price_list_rate):
					return False
			else:
				return True
	else:
		return True


def validate_rate_and_price_list(doc,method=None):
	if frappe.get_doc("Addons Utils Settings").enable_sales_invoice_rate_validation:
		settings =  frappe.get_doc("Addons Utils Settings")
		if settings.sales_invoice_rate_validation_role in frappe.get_roles(frappe.session.user):
			items = [d["item_code"] for d in frappe.get_all("Addons Utils Settings Items Validation",fields=["item_code"])]
			item_groups  = [d["item_group"] for d in frappe.get_all("Addons Utils Settings Item Groups Validation",fields=["item_group"])]
			for it in doc.items:
				item_group = frappe.db.get_value("Item",it.item_code, "item_group")
				if  it.item_code in items:
					if float(it.rate) < float(it.price_list_rate):
						frappe.throw("{0} - Rate cannot be less than {1}".format(it.item_code,it.price_list_rate))
				elif item_group in item_groups:
					if float(it.rate) < float(it.price_list_rate):
						frappe.throw("{0} - Rate cannot be less than {1}".format(it.item_code,it.price_list_rate))



# old method to fetch uoms not using now
# @frappe.whitelist()
# @frappe.validate_and_sanitize_search_inputs
# def get_item_uom(doctype, txt, searchfield, start, page_len, filters):
# 	if not filters:
# 		filters = {}
# 	condition = ""
# 	if frappe.get_doc("Addons Utils Settings").enable_uom_filter:
# 		condition += f"parent = '{filters.get('item_code')}'"
# 		return frappe.db.sql(
# 			"""select uom from `tabUOM Conversion Detail`
# 				where 
# 				{condition}
# 				order by name""".format(
# 				condition=condition, 
# 			),)
# 	return frappe.db.sql(
# 			"""select name from `tabUOM`
# 				order by name""")
