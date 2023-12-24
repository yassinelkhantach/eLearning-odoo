from odoo import models, fields

class CourseTag(models.Model):
    _name = 'e_courses.course.tag'
    _description = 'Course Tags'

    name = fields.Char(string='Tag Name', required=True)
