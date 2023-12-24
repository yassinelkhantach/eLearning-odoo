from odoo import models, fields, api

class Course(models.Model):
    _name = 'e_learning.course'
    _description = 'Courses'

    title = fields.Char(string='Title', required=True)
    description = fields.Char(string='Description')
    price = fields.Float(string='Course Price')
    photo = fields.Char(string='Photo')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    duration_hours = fields.Float(string='Duration (hours)')
    enrollment_deadline = fields.Date(string='Enrollment Deadline')
    instructor_ids = fields.Many2many('res.partner', string='Instructors')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    tags = fields.Many2many('custom_module.course.tag', string='Tags')
    

    @api.model
    def create(self, values):
        course = super(Course, self).create(values)
        return course
    