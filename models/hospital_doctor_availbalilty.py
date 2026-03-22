

from odoo import models , fields
class hospital_doctor_availbalilty(models.Model):

    _name ="hospital.doctor.availbalilty"
    _description ="Hospital Doctor Availbalilty"    

    doctor_id = fields.Many2one("hospital.doctor" , string='Doctor', required=True)

    day = fields.Selection([
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("saturday", "Saturday"),
        ("sunday", "Sunday"),
    ], string='Day', required=True)
    
    start_time = fields.Float(string='Start Time', required=True)  # store as float hours e.g., 9.5 = 09:30
    end_time = fields.Float(string='End Time', required=True)

