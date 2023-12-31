from odoo import models, fields, api

class EnrollCourse(models.Model):
    _name = 'e_courses.enroll_course'
    _description = 'Enrolled Courses'

    course_id = fields.Many2one('e_courses.course', string='Course', required=True)
    user_id = fields.Many2one('e_courses.user', string='User', required=True)
    created_at = fields.Datetime(string='Enrollment Date', default=fields.Datetime.now)

    @api.model
    def create(self, values):
        enrollment = super(EnrollCourse, self).create(values)
        return enrollment
