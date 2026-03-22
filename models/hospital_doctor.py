
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class hospital_doctor(models.Model): 
    _name = "hospital.doctor"
    _inherit = ["hr.employee", "mail.thread", "mail.activity.mixin"]
    _description = "hospital doctor" 


    category_ids = fields.Many2many(
        "hr.employee.category", 
        'hospital_doctor_category_rel',
        "doctor_id",
        'category_id' , 
        string='Categories'
    )

    ref = fields.Char(default="New")
    active = fields.Boolean(default=True)
    name = fields.Char(string="Doctor Name")
    user_id = fields.Many2one("res.users" ,"user")
    specialty_id = fields.Many2one("hospital.specialty", required=True)

    consultation_fee = fields.Float(default=5.00)
    license_no = fields.Char(string="License No" , required=True)

    availability_ids = fields.One2many("hospital.doctor.availbalilty" 
    , "doctor_id" , 
    string="Availability"
    )
    appointment_ids = fields.One2many("hospital.appointment" ,"doctor_id" )

    _sql_constraints = [
        ('unique_user_id', 'unique(user_id)', 'This user is already linked to another doctor. Each doctor must have a unique user!')
    ]

    @api.onchange('user_id')
    def _onchange_user_id(self):
        """Automatically set the doctor's name based on the chosen user."""
        if self.user_id and not self.name:
            self.name = self.user_id.name

    @api.constrains('consultation_fee')
    def _check_consultation_fee(self):
        """Ensure the consultation fee is not negative."""
        for rec in self:
            if rec.consultation_fee < 0.0:
                raise ValidationError("Consultation fee cannot be lower than zero!")
    