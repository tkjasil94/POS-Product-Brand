from odoo import api, fields, models


class SaleOrderReservedProduct(models.Model):
    _inherit = "res.partner"

    def test_button_function(self):
        print("clicked")
