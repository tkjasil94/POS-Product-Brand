from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order.line"
    _inherit = "sale.order"
    product_lines = fields.One2many('product.reservation.lines',
                                    'partner_id', string='Add Product')
    partner_id = fields.Many2one('sale.order', 'res.partner')


    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for self.partner_id:








class ProductReservationLines(models.Model):
    _name = "product.reservation.lines"
    _description = "Product Reservation Lines"

    add_product = fields.Many2one('product.product', string="Add Product")
    add_quantity = fields.Integer(string="Quantity")
    add_price = fields.Float(string=" Sales Price")
    customer_id = fields.Many2one('reservation.books', string="Customer ID")
    partner_id = fields.Many2one('sale.order.line', string="Partner ID")






 # @api.onchange('partner_id')
    # def onchange_partner_id(self):
    #     self.product_lines = self.env['sale.order.line']. \
    #         search([('product_lines', '=', self.partner_id)])



# @api.model
# def _compute_lines_for_books(self, line):
#     return {
#         'add_product': line.add_product,
#         'add_price': line.add_price,
#         'add_quantity': line.add_quantity
#
#     }

# @api.onchange('partner_id')
# def onchange_customer_id(self):
#
#     temp = self.partner_id.with_context(lang=self.partner_id.lang)
#
#     self.partner_id = temp.customer_id
#
#     lines = [(5, 0, 0)]
#     for line in temp.add_product:
#         data = self._compute_lines_for_books(line)
#         lines.append((0, 0, data))
#     self.order_line = lines

# @api.onchange('partner_id')
# def onchange_partner_id(self):
#     temp = self.partner_id.with_context(lang=self.partner_id.lang)
#     self.partner_id = temp.customer_id
#
#     if temp.customer_id:
#         for line in self.order_line:
#             line.write(
#                 {'product_id': temp.customer_id.add_product,
#                  'product_uom_qty': temp.customer_id.add_quantity,
#                  'price_unit': temp.customer_id.add_price})
