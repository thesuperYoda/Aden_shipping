from odoo import models , fields

class user_branch(models.Model):
    _inherit = 'res.users'
    x_branch_id = fields.Many2one('branch.object' ,string="branch")

    
