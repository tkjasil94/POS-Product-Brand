from odoo import api, fields, models


class Search(models.Model):
    _inherit = 'res.partner'

    def get_reservations(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reservations',
            'view_mode': 'tree',
            'res_model': 'reservation.books',
            'domain': [('customer', '=', self.name)],
            'context': "{'create': False}"
        }
