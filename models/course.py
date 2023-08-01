from odoo import api, fields, models
from odoo.exceptions import ValidationError 

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
    
    "Como la sesion en many2one aqui es one2many su opuesto"
    
    sesion_ids=fields.One2many(comodel_name="odoo_training.session", string="Session", 
                               inverse_name="course_id") 
    "el inverse_name es el nombre del id de la relacion del otro modelo"
    
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", default=lambda self:self.env.company.currency_id.id)
    base_price = fields.Monetary(string="Base Price", currency_field="currency_id")
    additional_fee = fields.Monetary(string="Additional Fee", currency_field="currency_id")
    total_price = fields.Monetary(string="Total Price", currency_field="currency_id", compute="_compute_total_price", store=True)
    
    @api.depends("base_price", "additional_fee")
    def _compute_total_price(self):
        for record in self:
            if(record.base_price <0):
                raise ValidationError("Base Price can not be Negative")
            record.total_price = record.base_price + record.additional_fee
    