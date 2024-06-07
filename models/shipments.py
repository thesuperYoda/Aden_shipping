# -*- coding: utf-8 -*-

from odoo import models, fields , api
from datetime import datetime


class shipping(models.Model):
    _name = 'shipping.object'

    

    shipment_pickup_branch =   fields.Many2one('branch.object')
    shipment_pickup_Time = fields.Datetime(default = datetime.now())
    shipment_number_of_pieces = fields.Integer()
    shipment_color = fields.Char()
    shipment_type = fields.Char()
    shipment_description = fields.Text()
    shipment_sender_name = fields.Char()
    shipment_recipient_name = fields.Char()
    shipment_sender_number = fields.Char()
    shipment_recipient_number = fields.Char()
    shipment_delivery_brach = fields.Many2one('branch.object')
    shipment_delivery_date = fields.Datetime(default = datetime.now())
    shipment_cost = fields.Integer()
    shipment_payment_method=fields.Selection([("prepayed","Prepayed"),("at_deleviry","At_Deleviry")])
    drivers_id = fields.Many2one('drivers.object')
    shipment_secondary_delivery_destenation =fields.Char()

    state = fields.Selection([
        ("canceled","Canceled"),
        ("draft","Draft"),
        ("ready_to_be_shiped","Ready_To_Be_Shiped"),
        ("with_driver","with_driver"),
        ("ready_to_be_picked","Ready_To_Be_Picked"),
        ("deliverd","Deliverd")
        ],default="draft")
    

    #@api.onchange(res.partner.title)
            
    def action_draft(self):
        for rec in self:
            
            rec.state="ready_to_be_shiped"      

    def action_ready_to_be_shiped(self):
        for rec in self:

            rec.state="with_driver"

    def action_with_driver(self):
        for rec in self:

            rec.state="ready_to_be_picked"

            
    def action_ready_to_be_picked(self):
        for rec in self:

            rec.state="deliverd"


    def action_canceled(self):
        for rec in self:

            rec.state="canceled"


#   def action_open_shipment_cancellation_wizard(self):
#       action = self.env['ir.actions.action']._for_xml_id('Aden_shipping.shipment_cancellation_wizard_action')
#       action['context'] = {'default_shipments_id': self.id}
#       return action

  #  @api.constrains("shipment_description")



#class user_branch(models.Model):
#   _inherit = 'res.users'
#   _columns = {
#       'x_branch': fields.Many2one(related="branch.object",store=True),
#       }

