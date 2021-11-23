from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        partner_data = self.env['reservation.books'].search([(
            'customer', '=', self.partner_id.id)])
        for rec in self:
            lines = [(5, 0, 0)]
            for line in partner_data.product_lines:
                vals = {
                    'product_id': line.add_product.id,
                    'product_uom_qty': line.add_quantity,
                    'price_unit': line.add_price,
                }
                lines.append((0, 0, vals))
            rec.order_line = lines



