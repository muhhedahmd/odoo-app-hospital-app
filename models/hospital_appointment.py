


from odoo import models , fields

class hospital_appointment(models.Model):
    _name ="hospital.appointment"
    _inherit = "calendar.event"
    _description = "Hospital Appointment"

    doctor_id = fields.Many2one("hospital.doctor" )
    patient_id = fields.Many2one("hospital.patient")

    # Inherited from calendar.event, but need to redefine Many2many relation tables
    # so they don't look at the same table as the parent model.
    categ_ids = fields.Many2many(
        'calendar.event.type', 'hospital_appointment_type_rel',
        'appointment_id', 
        'type_id',
         string='Tags')
         
    partner_ids = fields.Many2many(
        'res.partner',
        'hospital_appointment_partner_rel',
        'appointment_id', 
        'partner_id', string='Attendees')

    alarm_ids = fields.Many2many(
        'calendar.alarm', 'hospital_appointment_alarm_rel',
        'appointment_id', 'alarm_id', string='Reminders')

    state = fields.Selection([
        ("draft" , "Draft"),
        ("confirm" , "Confirm"),
        ("done" , "Done"),
        ("cancel" , "Cancel"),
    ])
    chief_complaint = fields.Text(string="Chief Complaint")

    # prescription_ids (O2M)


    
    