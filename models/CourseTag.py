from odoo import models, fields

class CourseTag(models.Model):
    _name = 'custom_module.course.tag'
    _description = 'Course Tags'

    name = fields.Char(string='Tag Name', required=True)
