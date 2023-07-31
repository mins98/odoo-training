from odoo import fields, models

class Course(models.Model):
    _name="odoo_training.course"
    _description="Course info"
    
    #Campos reservados
    name=fields.Char(string="Title", required=True)
    active = fields.Boolean(string="active", default=True)
    
    #propios
    description=fields.Text()
    level=fields.Selection(string="Level",
                           selection=[
                               ('beginner','Beginner'),
                               ('intermediate','Intermediate'),
                               ('advance','Advance'),
                           ], copy=False)
    