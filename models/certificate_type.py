from odoo import models, fields, api


class CertificateType(models.Model):
    _name = "certificate.type"
    _description = "Certificate Class for Drop Down List in Certificate View"

    types_name = fields.Char()

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{}".format(record.types_name)))
        return result
