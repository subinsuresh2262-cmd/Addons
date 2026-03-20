// Copyright (c) 2024, D-codE and contributors
// For license information, please see license.txt

frappe.ui.form.on('Purchase Receipt', {
    setup: function(frm){
        frappe.db.get_single_value("Addons Utils Settings", "enable_purchase_receipt_uom_filter").then((value) => {
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
