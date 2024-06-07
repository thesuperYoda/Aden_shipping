# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime


class passenger(models.Model):
    _name = 'passenger.object'

    name = fields.Char()
    passenger_number = fields.Char()
    passenger_pickup_datetime = fields.Datetime(default = datetime.now())

    passenger_delivery_place = fields.Char()
    trip_cost = fields.Integer()
    trip_driver = fields.Char()


