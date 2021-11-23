from odoo import api, fields, models


class CustomerInvoice(models.Model):
    _inherit = 'res.partner'

    # need_invoice = fields.Boolean(string="Need Invoice")
    # need_dn = fields.Boolean(string="Need DN")

    def create_invoice(self):
        invoice_data = self.env['reservation.books'].search([(
            'customer', '=', self.name)])

        invoice_lines = []
        for line in invoice_data.product_lines:
            val = {
                'product_id': line.add_product,
                'quantity': line.add_quantity,
                'price_unit': line.add_price
            }
            invoice_lines.append((0, 0, val))

        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': invoice_data.customer,
            'invoice_date': fields.Date.today(),
            'state': 'draft',
            'invoice_line_ids': invoice_lines
        })
        invoice.action_post()

    def test_button_function(self):
        print("test")



