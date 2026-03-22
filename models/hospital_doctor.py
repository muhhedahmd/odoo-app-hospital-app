

from odoo  import models ,fields

class hospital_doctor(models.Model): 
    _name = "hospital.doctor"
    _description = "hospital doctor" 

    _inherit = ["mail.thread", "mail.activity.mixin"]

    ref = fields.Char()
    active = fields.Boolean(default=True)
    name = fields.Char(string="Doctor Name")
    user_id = fields.Many2one("res.users" ,"user")
    specialty_id = fields.Many2one("hospital.specialty")
    consultation_fee = fields.Float(default=0.00)
    available = fields.Boolean(default=True)

