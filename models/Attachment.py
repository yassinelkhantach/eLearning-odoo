from odoo import models, fields, api

class Attachment(models.Model):
    _name = 'e_courses.attachment'
    _description = 'Lesson Attachments'

    file = fields.Binary(string='File')
    lesson_id = fields.Many2one('e_courses.lesson', string='Lesson', required=True)

    @api.model
    def create(self, values):
        attachment = super(Attachment, self).create(values)
        return attachment
