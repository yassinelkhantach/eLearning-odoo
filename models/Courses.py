from odoo import models, fields, api

class Course(models.Model):
    _name = 'e_courses.course'
    _description = 'Courses'

    title = fields.Char(string='Title', required=True)
    description = fields.Char(string='Description')
    price = fields.Float(string='Course Price')
    photo = fields.Char(string='Photo')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    duration_hours = fields.Float(string='Duration (hours)')
    enrollment_deadline = fields.Date(string='Enrollment Deadline')
    instructor_ids = fields.Many2many('res.partner', string='Instructors')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    tags = fields.Many2many('e_courses.course.tag', string='Tags')
    
    ratings = fields.One2many('e_courses.rating', 'course_id', string='Ratings')

    average_rating = fields.Float(string='Average Rating', compute='compute_average_rating', store=True)

    @api.depends('ratings', 'ratings.value')
    def compute_average_rating(self):
        for course in self:
            ratings = course.ratings.mapped('value')
            course.average_rating = sum(ratings) / len(ratings) if ratings else 0.0
    
    def name_get(self):
        res = super(Course, self).name_get()
        return [(course.id, course.title) for course in self]

    @api.model
    def create(self, values):
        course = super(Course, self).create(values)
        return course
    
    def get_instructor_names(self):
        return ', '.join(self.instructor_ids.mapped('name'))