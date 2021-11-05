# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Inventory Books',
    'version': '1.0',
    'summary': 'Books Management',
    'sequence': 10,
    'description': """Books Management Software""",
    'category': 'Productivity',
    'depends': ['product', 'sale', 'contacts', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/book_sequence.xml',
        'views/books.xml',
        'views/books_invent.xml',
        'views/books_reserv.xml',
        'views/smart_button_reserv.xml',
        'views/sale_order_books.xml',
        'views/customer_invoice.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
