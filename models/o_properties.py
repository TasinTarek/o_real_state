# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from odoo.exceptions import UserError, ValidationError

class o_properties(models.Model):
    _name = 'o.properties'
    _description = 'Real State'

    name = fields.Char(required=True)
    postcode = fields.Char()
    date_availability = fields.Date()
    description = fields.Text()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean(default=False)
    garden_area = fields.Float()
    living_area = fields.Float()
    total_area = fields.Float(compute="_compute_total_area")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    active = fields.Boolean(default=True)
    state= fields.Selection([
        ('new', 'New'),
        ('received', 'Received')
    ])
    post_code = fields.Char()
    best_price = fields.Float(compute="_compute_best_price")

    customer_id = fields.Many2one('res.partner', string="Customer")
    sales_person_id = fields.Many2one('res.users', string='Sales Person', default=lambda self: self.env.user)
    property_type_id = fields.Many2one('o.property.type', string="Property Type", required=True)
    property_tag_ids = fields.Many2many('o.property.tag', string='Property Tag')
    offer_ids = fields.One2many('o.property.offer', 'properties_id')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sold', 'Sold'),
        ('cancel', 'Cancel'),
    ], default='draft')
    
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for rec in self:
            rec.best_price = max(rec.offer_ids.mapped("price")) if rec.offer_ids else 0


    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden == True:
            self.garden_area = 10  
            self.garden_orientation = 'north'
            return {'warning': {
                'title': _("Warning"),
                'message': ('HA AHA HA ')}}


    def action_sold(self):
        for rec in self:
            if rec.state == 'cancel':
                raise UserError("A Cancelled property cannot be Sold !")
            rec.state = 'sold'


    def action_cancel(self):
        for rec in self:
            if rec.state == 'sold':
                raise UserError("A Sold property cannot be Cancelled !")
            else: 
                rec.state = 'cancel'


    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
