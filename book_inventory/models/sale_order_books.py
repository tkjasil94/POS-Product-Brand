from odoo import fields, models, api


class SaleOrderBooks(models.Model):
    _inherit = "sale.order"
    _inherit = "res.partner"
    _inherit = "product.product"

    @api.model
    def _compute_lines_for_books(self, line):
        return {
            'add_product': line.prod,
            'add_price': line.price,
            'add_quantity': line.quant

        }

    @api.onchange('customer_id')
    def onchange_customer_id(self):
        temp = self.partner_id

        self.partner_id = temp.customer_id

        lines = [(5, 0, 0)]
        for line in temp.add_product:
            data = self._compute_lines_for_books(line)
            lines.append((0, 0, data))
        self.order_line = lines
