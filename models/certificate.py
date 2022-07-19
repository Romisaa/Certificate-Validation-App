from datetime import datetime, timedelta, date
from collections import OrderedDict
from odoo import models, fields, api


# from odoo.odoo.addons.base.models.res_partner import _lang_get


class Certificate(models.Model):
    _name = 'certificate.app'
    _description = 'This is Certificate Checker App'
    _rec_name = "customer_name"

    vehicle_type = fields.Selection(
        [('car', 'Car'), ('bus', 'Bus'), ('minibus', 'Mini Bus'), ('microbus', 'Micro Bus')], string="Vehicle Type")

    certificate_type_id = fields.Many2one('certificate.type', string="Certificate Type")
    traffic_department_id = fields.Many2one('traffic.department', string="Traffic Department")
    customers_id = fields.Many2one('customers.app', string="Customer")
    customer_name = fields.Char(string="Customer", related="customers_id.customer_name")
    serial_number = fields.Char(string="Serial Number")
    price = fields.Integer(string="Price")
    motor_number = fields.Integer(string="Motor Number")
    chassis_number = fields.Char(string="Chassis Number")  # create regex to check validation
    car_brand_id = fields.Many2one('car.brand', string="Brand")
    car_model = fields.Char()
    today = fields.Date(default=fields.Date.context_today)
    certificate_ids = fields.One2many('user.print', 'user_id')

    year_input = fields.Integer(string="Year Input")

    @api.onchange('year_input')
    def set_dynamic_list(self):
        years_list = []
        for i in range(self.year_input - 20, self.year_input):
            print('for')
            years_list.append(i)
            print('out')
        print(years_list)

    years_options = fields.Many2one('years.options', domain=set_dynamic_list, string='Scheduled Options',
                                    tracking=True)

    # def get_list(self):
    #     pass
    #
    # communication_channel = fields.Selection(get_list, string='Comm. Channel',
    #                                          tracking=True
    #                                          )

    # Serial Number Function Creation
    @api.model
    def create(self, vals):
        vals['serial_number'] = self.env['ir.sequence'].next_by_code('certificate.app')
        return super(Certificate, self).create(vals)

    is_printed = fields.Boolean()

    def _add_log(self):
        self.env["user.group.print"].create({
            "description": f"the report printed",
            "user_id": self.id
        })

    def printed(self):
        self.is_printed = True
        self._add_log()

    def print_report(self):
        print('In')
        return self.env.ref('validation_app_task.report_details_id').report_action(self)
        print('Done')

    def reprint_report(self):
        self.is_printed = False


class UserPrint(models.Model):
    name = "user.print"
    description = "Model User Print"

    user_id = fields.Many2one('certificate.app')
