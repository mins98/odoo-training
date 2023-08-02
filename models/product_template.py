from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_session_product = fields.Boolean(string='Use as a Session Product',
                                        help="Check this box to use this as a product for Session Fee",
                                        default=False)