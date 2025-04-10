from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    tag_ids = fields.Many2many('crm.tag', string="Tags")
    is_salesperson_notified = fields.Boolean(default=False)

    @api.model
    def notify_salesperson_on_delivery(self):
        pickings = self.search([
            ('state', '=', 'done'),
            ('is_salesperson_notified', '=', False),
            ('sale_id', '!=', False),
        ])
        template = self.env.ref('custom_partner_sale_enhancement.mail_template_delivery_done_notify')

        for picking in pickings:
            if template and picking.sale_id.user_id.partner_id.email:
                template.send_mail(picking.id, force_send=True)
                picking.is_salesperson_notified = True

    @api.model
    def create(self, vals):
        picking = super().create(vals)
        if picking.origin:
            sale = self.env['sale.order'].search([('name', '=', picking.origin)], limit=1)
            if sale:
                picking.tag_ids = [(6, 0, sale.tag_ids.ids)]
        return picking


    @api.model
    def _search_tag_ids(self, operator, value):
        return [('tag_ids.name', operator, value)]
