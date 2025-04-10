from odoo import models
from collections import defaultdict

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @classmethod
    def _split_procurements_by_category(cls, procurements):
        grouped = defaultdict(list)
        for procurement in procurements:
            category = procurement.product_id.categ_id.id
            grouped[category].append(procurement)
        return grouped
