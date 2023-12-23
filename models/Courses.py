from odoo import models, fields, api

class Course(models.Model):
    _name = 'e_learning.course'
    _description = 'Courses'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Course Price')
    duration_hours = fields.Float(string='Duration (hours)')
    tags = fields.Many2many('custom_module.course.tag', string='Tags')
    photo = fields.Binary(string='Photo')

    @api.model
    def create(self, values):
        course = super(Course, self).create(values)
        return course
    
class CourseTag(models.Model):
    _name = 'custom_module.course.tag'
    _description = 'Course Tags'

    name = fields.Char(string='Tag Name', required=True)
