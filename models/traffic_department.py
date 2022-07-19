from odoo import models, fields, api


class TrafficDepartment(models.Model):
    _name = "traffic.department"
    _description = "Traffic Department Model"

    department_name = fields.Char(string="Name")

    def name_get(self):
        return [(record.id, record.department_name) for record in self]
