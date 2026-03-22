

from odoo  import models ,fields

class hospital_doctor(models.Model): 
    _inherit = "hr.employee"
    _name = "hospital.doctor"
    _description = "hospital doctor" 

    _inherit = ["mail.thread", "mail.activity.mixin"]

    ref = fields.Char()
    active = fields.Boolean(default=True)
    name = fields.Char(string="Doctor Name")
    user_id = fields.Many2one("res.users" ,"user")
    specialty_id = fields.Many2one("hospital.specialty")

    consultation_fee = fields.Float(default=5.00)
    license_no = fields.Char(string="License No")
    avalible_days = fields.Selection([
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("saturday", "Saturday"),
        ("sunday", "Sunday"),
    ])

