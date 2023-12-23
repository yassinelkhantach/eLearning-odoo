from odoo import models, fields, api

class Course(models.Model):
    _name = 'courses.course'
    _description = 'Courses'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    instructor_ids = fields.Many2many('res.partner', string='Instructors')
    price = fields.Float(string='Course Price')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in progress', 'Ongoing'),
        ('completed', 'Completed')],default='draft')

    tags = fields.Many2many('custom_module.course.tag', string='Tags')
    photo = fields.Binary(string='Photo')

    @api.model
    def create(self, values):
        course = super(Course, self).create(values)
        return course

    def start_course(self):
        self.write({'state': 'in progress'})

    def complete_course(self):
        self.write({'state': 'completed'})

class CourseTag(models.Model):
    _name = 'courses.course.tag'
    _description = 'Course Tags'

    name = fields.Char(string='Tag Name', required=True)
