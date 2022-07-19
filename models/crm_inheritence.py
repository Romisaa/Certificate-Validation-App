from odoo import models, fields, api
from odoo.odoo.exceptions import UserError


class CrmInheritance(models.Model):
    _inherit = 'res.partner'

    related_customer_id = fields.Many2one('customers.app', string="Customers")


