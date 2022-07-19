from odoo import models, fields, api


class Customers(models.Model):
    _name = 'customers.app'
    _description = 'Customers Model'

    customer_name = fields.Char('Name')
    customer_phone = fields.Integer('Phone Number')

    def name_get(self):
        return [(record.id, record.customer_name) for record in self]


    # write function to check phone number "Regex"
