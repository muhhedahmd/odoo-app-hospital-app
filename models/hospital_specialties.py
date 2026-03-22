

from odoo import models , fields

from odoo  import models 

class hospital_specialty(models.Model): 
    _name = "hospital.specialty"
    _description = "hospital specialty" 


    name = fields.Char(default="nothing")
    doctor_ids = fields.One2many("hospital.doctor", "specialty_id")

