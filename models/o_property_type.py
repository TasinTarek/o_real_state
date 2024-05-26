# -*- coding: utf-8 -*-

from odoo import models, fields, api


class o_property_type(models.Model):
    _name = 'o.property.type'
    _description = 'Type'

    name = fields.Char(required=True)
    description = fields.Text()