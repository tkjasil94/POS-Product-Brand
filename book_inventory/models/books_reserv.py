from odoo import api, fields, models


class ReservationBooks(models.Model):
    _name = "reservation.books"

    _description = "Books Reservation"

    _rec_name = "name_seq1"

    name_reservation = fields.Char(string='Name of Reservation', required=True)
    customer = fields.Many2one('res.partner', string="Customer", store=True)
    product_lines = fields.One2many('product.reservation.lines',
                                    'customer_id', string='Add Product')
    active = fields.Boolean(string="Active", default=True)
    expiry_date = fields.Date(string="Expiry Date")
    note = fields.Text(string='Description')
    name_seq1 = fields.Char('Order Reference', required=True, index=True,
                            copy=False, default='New')
    field_related = fields.Many2one('res.users', string='Responsible User',
                                    default=lambda self: self.env.user)

    def check_expiry_date(self):
        self.env['reservation.books'].search([('expiry_date', '<=',
                                               fields.Date.today())]).write(
            {'active': False})

        # today = fields.Date.today()
        # reservation_ids = self.env['reservation.books'].search([])
        # for reservation in reservation_ids:
        #     if reservation.expiry_date < today:
        #         reservation_ids.active = True
        #     else:
        #         reservation_ids.active = False

    @api.model
    def create(self, vals):
        vals['name_seq1'] = self.env['ir.sequence'].next_by_code(
            'reservation.books')
        return super(ReservationBooks, self).create(vals)


class ProductReservationLines(models.Model):
    _name = "product.reservation.lines"
    _description = "Product Reservation Lines"

    add_product = fields.Many2one('product.product', string="Add Product")
    add_quantity = fields.Integer(string="Quantity")
    add_price = fields.Float(string=" Sales Price")
    customer_id = fields.Many2one('reservation.books', string="Customer ID")
