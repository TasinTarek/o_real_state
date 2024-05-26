# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class o_properties(models.Model):
    _name = 'o.property.offer'
    _description = 'Offer'

    price = fields.Float()
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ])
    partner_id = fields.Many2one('res.partner', required=True) 
    properties_id = fields.Many2one('o.properties', required=True) 
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(string='Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline', store=True)

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date:
                duration = (record.date_deadline - record.create_date).days
            else:
                duration = (record.date_deadline - fields.Date.today()).days
            record.validity = duration if duration > 0 else 0

    
        

