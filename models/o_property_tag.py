# -*- coding: utf-8 -*-

from odoo import models, fields, api


class o_property_tag(models.Model):
    _name = 'o.property.tag'
    _description = 'Tag'

    name = fields.Char(required=True)
    description = fields.Text()


