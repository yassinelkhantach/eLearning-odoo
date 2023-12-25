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
    
    lessons = fields.One2many('e_courses.lesson', 'course_id', string='Lessons')
    ratings = fields.One2many('e_courses.rating', 'course_id', string='Ratings')

    average_rating = fields.Float(string='Average Rating', compute='compute_average_rating', store=True)
    number_of_ratings = fields.Integer(string='Number of Ratings', compute='compute_number_of_ratings', store=True)

    @api.depends('ratings', 'ratings.value')
    def compute_average_rating(self):
        for course in self:
            ratings = course.ratings.mapped('value')
            course.average_rating = sum(ratings) / len(ratings) if ratings else 0.0
    
    
    @api.depends('ratings')
    def compute_number_of_ratings(self):
        for course in self:
            course.number_of_ratings = len(course.ratings)


    def name_get(self):
        res = super(Course, self).name_get()
        return [(course.id, course.title) for course in self]

    @api.model
    def create(self, values):
        course = super(Course, self).create(values)
        return course
    
    @api.model
    def get_average_rating(self, course_id):
        course = self.browse(course_id)
        return course.average_rating

    @api.model
    def get_number_of_ratings(self, course_id):
        course = self.browse(course_id)
        return course.number_of_ratings
    
    @api.model
    def get_rating_percentage(self, value):
        if not (1 <= value <= 5):
            raise ValueError('Rating value must be between 1 and 5.')

        total_ratings = len(self.ratings)
        if total_ratings == 0:
            return 0.0

        specific_value_count = len(self.ratings.filtered(lambda r: r.value == value))
        percentage = (specific_value_count / total_ratings) * 100
        return round(percentage, 2)
    

    def get_instructor_names(self):
        return ', '.join(self.instructor_ids.mapped('name'))