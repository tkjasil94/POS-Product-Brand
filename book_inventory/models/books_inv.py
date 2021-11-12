from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"
    related_books = fields.Many2one('inventory.books', string="Related Books")

    default_code = fields.Char(related='related_books.isbn_number',
                               tracking=True)
    list_price = fields.Float(related='related_books.book_price',
                              tracking=True)


class ResPartner(models.Model):
    _inherit = "res.partner"
    is_book_owner = fields.Boolean(String="Is Book Owner")






