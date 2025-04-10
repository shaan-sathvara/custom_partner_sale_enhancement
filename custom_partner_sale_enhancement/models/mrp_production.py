from odoo import models, api, fields
from odoo.exceptions import UserError, ValidationError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    # def write(self, vals):
    #     if self.state == 'confirmed' and 'product_qty' in vals:
    #         raise UserError('Cannot change quantity after confirmation.')
    #     return super().write(vals)

    # def write(self, vals):
    #     for rec in self:
    #         if rec.state in ['confirmed'] and 'product_qty' in vals:
    #             if vals['product_qty'] != rec.product_qty:
    #                 raise ValidationError("Changing quantity is not allowed after confirmation.")
    #     return super().write(vals)
