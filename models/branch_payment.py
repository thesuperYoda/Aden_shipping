# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime


class branch_payment(models.Model):
    _name = 'branch_payment.object'

    name = fields.Char()
    amount = fields.Integer()
    time = fields.Datetime(default = datetime.now())

    