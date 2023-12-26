from odoo import models, fields, api

class Rating(models.Model):
    _name = 'e_courses.rating'
    _description = 'Rating Courses'

    course_id = fields.Many2one('e_courses.course', string='Course', required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    value = fields.Float(string='Rating')

    @api.model
    def create(self, values):
        if 'value' in values:
            if not 1 <= values['value'] <= 5:
                raise self.env['exceptions'].ValidationError('Rating value must be between 1 and 5.')
        rating = super(Rating, self).create(values)
        return rating
