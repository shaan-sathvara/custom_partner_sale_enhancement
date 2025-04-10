from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _create_delivery_orders(self):
        pickings = super()._create_delivery_orders()
        for picking in pickings:
            picking.tag_ids = [(6, 0, self.tag_ids.ids)]
        return pickings
