{
    "name": "Partner and Sales Enhancements",
    "version": "17.0.1.0.0",
    "summary": "Enhancements for Partner, Sales, Delivery, MRP and Purchase modules",
    "description": """
Custom Module for:
- Search Partner by Ref in all Many2one fields
- Display Partner as NAME [REF] in Many2one
- Copy tags from Sale Order to Delivery Orders
- Search and conditionally show tags in Delivery Orders
- Lock MRP qty on confirmation
- Split Purchase Orders based on Product Category
- Email Salesperson on Delivery Done
- Enforce unique Product Category name
- New OWL widget to copy Char field to clipboard
- Default filter to show confirmed and done Sales Orders

Developed by: Your Name Here
""",
    "author": "Your Name Here",
    "depends": [
        "sale_management",
        "stock",
        "mrp",
        "purchase",
        "base"
    ],
    "data": [
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
        "views/product_category_views.xml",
        "views/manufacturing.xml",
        "data/automated_action.xml"
    ],
    "assets": {
        "web.assets_backend": [
            # "custom_partner_sale_enhancement/static/src/js/clipboard_widget.js",
            # "custom_partner_sale_enhancement/static/src/xml/clipboard_template.xml"
        ]
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3"
}