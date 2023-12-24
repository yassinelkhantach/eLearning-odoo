from odoo import models, fields, api

class Course(models.Model):
    _name = 'e_courses.course'
    _description = 'Courses'

    # Fields for Course model
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    price = fields.Float(string='Course Price')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in progress', 'Ongoing'),
        ('completed', 'Completed')], default='draft')

    # Many-to-many relationship with CourseTag model
    tags = fields.Many2many('e_courses.course.tag', string='Tags')

    # Binary field for storing course photo
    photo = fields.Binary(string='Photo')

    # Override create method to add custom logic
    @api.model
    def create(self, values):
        course = super(Course, self).create(values)
        return course

    # Custom method to transition course to 'in progress' state
    def start_course(self):
        self.write({'state': 'in progress'})

    # Custom method to transition course to 'completed' state
    def complete_course(self):
        self.write({'state': 'completed'})

class CourseTag(models.Model):
    _name = 'e_courses.course.tag'
    _description = 'Course Tags'

    # Field for CourseTag model
    name = fields.Char(string='Tag Name', required=True)
