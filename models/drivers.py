# -*- coding: utf-8 -*-

from odoo import models, fields



class driver(models.Model):
    _name = 'drivers.object'

    name = fields.Char()
    driver_number = fields.Char()
    