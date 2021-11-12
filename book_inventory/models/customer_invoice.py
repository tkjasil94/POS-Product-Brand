from odoo import api, fields, models


class SaleOrderReservedProduct(models.Model):
    _inherit = 'res.partner'

    def test_button_function(self):
        print("clicked")

    # need_invoice = fields.Boolean(string="Need Invoice")
    # need_dn = fields.Boolean(string="Need DN")


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_order_line_count = fields.Integer(
        string='Sale order line count',
        compute='_compute_sale_order_line_count'
    )


