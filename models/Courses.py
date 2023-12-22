from odoo import models, fields, api

class Course(models.Model):
    _name = 'e_learning.course'
    _description = 'Courses'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    instructor_ids = fields.Many2many('res.partner', string='Instructors')
    price = fields.Float(string='Course Price')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed')],
        string='State', default='draft')

    tags = fields.Many2many('custom_module.course.tag', string='Tags')
    photo = fields.Binary(string='Photo')

    @api.model
    def create(self, values):
        course = super(Course, self).create(values)
        return course

    def start_course(self):
        self.write({'state': 'ongoing'})

    def complete_course(self):
        self.write({'state': 'completed'})

class CourseTag(models.Model):
    _name = 'custom_module.course.tag'
    _description = 'Course Tags'

    name = fields.Char(string='Tag Name', required=True)
