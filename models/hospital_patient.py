
from odoo import models ,fields

class hospital_patient(models.Model):
    _name ="hospital.patient"
    _description = 'Patient'

    national_id = fields.Char(string="National Id")
    birth_date  = fields.Char(string="Birth Date")
    blood_type  = fields.Char(string="Blood Type")
    emergency_contact = fields.Char(string="Emergency Contact") 
    medical_history = fields.Text(string="Medical History") 
    appointment_ids = fields.One2many("hospital.appointment" , "patient_id")