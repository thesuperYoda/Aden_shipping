# -*- coding: utf-8 -*-

from odoo import models, fields



class branch(models.Model):
    _name = 'branch.object'

    name = fields.Char()
    branch_phone_number = fields.Char(size = 9)
    