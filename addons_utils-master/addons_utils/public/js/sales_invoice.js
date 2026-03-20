// Copyright (c) 2024, D-codE and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Invoice', {
    setup: function(frm){
        frappe.db.get_single_value("Addons Utils Settings", "enable_uom_filter").then((value) => {
            if(value) {
                frm.set_query("uom", "items", function(doc, cdt, cdn) {
                    var d = locals[cdt][cdn];
                    if(!d.item_code) {
                        frappe.throw(_('Please Select Item Code'));
                    }           
                    return{
                            query: "addons_utils.overrides.queries.get_item_uoms",
                            filters: {
                                'item_code': d.item_code,
                            }
                    }; 
                });
            }                           
        }); 
    },
});


frappe.ui.form.on('Sales Invoice Item', {
	item_code: function(frm, cdt, cdn) {
		const d = locals[cdt][cdn];
        frappe.call({
            method: "addons_utils.overrides.queries.rate_hide_validation",
            args: {
                "item_code": d.item_code,
            },
            callback: function(r) {
                var child = locals[cdt][cdn];
                console.log(r.message)
                if (r.message == true ){
                    frappe.model.set_value(d.doctype, d.name, "custom_dummy", 1);
                }
            },
        });
	},

    rate: function(frm, cdt, cdn) {
		const d = locals[cdt][cdn];
        frappe.call({
            method: "addons_utils.overrides.queries.rate_price_list_validation",
            args: {
                "item_code": d.item_code,
                "rate": d.rate,
                "price_list_rate": d.price_list_rate,
            },
            callback: function(r) {
                if (r.message == false ){
                    frappe.model.set_value(d.doctype, d.name, "rate", d.price_list_rate);
                    frappe.throw("The Rate Should Not be Lessthan Price List Rate")
                }
            },
        });
	},
});

// frappe.ui.form.on('Sales Invoice Item', {
    // items_add: function(frm, cdt, cdn) {
    //     var d = locals[cdt][cdn];
    //     frm.set_df_property('items', 'read_only', 0, frm.docname, 'rate', child.name)
    // },
    // item_code: function(frm, cdt, cdn) {

    //     var d = locals[cdt][cdn];
    //     if (d.item_code) {
    //         frappe.call({
    //             method: "addons_utils.overrides.queries.rate_hide_validation",
    //             args: {
    //                 "item_code": d.item_code,
    //             },
    //             callback: function(r) {
    //                 var child = locals[cdt][cdn];
    //                 console.log(r.message)
    //                 if (r.message == true ){
    //                     frm.set_df_property('items', 'read_only', 1, frm.docname, 'rate', child.name)
    //                     refresh_field("items");
    //                 }
    //                 else{
    //                     frm.set_df_property('items', 'read_only', 0, frm.docname, 'rate', child.name)
    //                     refresh_field("items");
    //                 }
    //             },
    //         });
//         }
// 	}
// })

// refresh: function(frm){
    //     frappe.db.get_value('Addons Utils Settings', undefined, 'rate_readonly_role').then(({ message }) => {
    //         if (frappe.user.has_role(message.rate_readonly_role)) {
    //             frm.fields_dict["items"].grid.toggle_enable("rate", false);
    //         }
    //     });
    // } 