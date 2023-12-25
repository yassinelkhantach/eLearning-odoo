from odoo import models, fields, api

class Lesson(models.Model):
    _name = 'e_courses.lesson'
    _description = 'Course Lessons'

    title = fields.Text(string='Title', required=True)
    objective = fields.Text(string='Objective')
    video_url = fields.Char(string='Video URL')
    duration = fields.Float(string='Duration (hours)')

    course_id = fields.Many2one('e_courses.course', string='Course', required=True)
    document_filename = fields.Char(string='Document Filename')
    
    def name_get(self):
        res = super(Lesson, self).name_get()
        return [(lesson.id, lesson.title) for lesson in self]

    @api.model
    def create(self, values):
        lesson = super(Lesson, self).create(values)
        return lesson
    
