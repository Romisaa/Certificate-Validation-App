from odoo import models, fields, api


class YearsOptions(models.Model):
    _name = "years.options"
    _description = "Years Option Model"

    year_input = fields.Integer(string="Year Input")

    def name_get(self):
        return [(record.id, record.year_input) for record in self]
    #
    # @api.onchange('year_input')
    # def set_dynamic_domain_for_scheduled_option_whatsapp(self):
    #     years_list = []
    #     for i in range(self.year_input - 20, self.year_input):
    #         print('for')
    #         years_list.append(i)
    #         print('out')
    #     print(years_list)
    #
    # years_var = set_dynamic_domain_for_scheduled_option_whatsapp()

