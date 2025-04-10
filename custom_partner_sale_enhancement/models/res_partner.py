from odoo import models, api, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    copy_text = fields.Char(string="Copy Text")


    @api.depends('name', 'ref')
    def _compute_display_name(self):
        for partner in self:
            partner.display_name = False if not partner.name else (
                '{}{}'.format(
                    partner.name, partner.ref and '[%s] ' % partner.ref or ''
                ))

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None, order=None):
        args = args or []
        domain = ["|", ("ref", operator, name), ("name", operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid, order=order)
