from odoo import models, fields, api


class CarBrand(models.Model):
    _name = 'car.brand'
    _description = 'Car Brand Model'

    brand_name = fields.Char('Brand')

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{}".format(record.brand_name)))
        return result
