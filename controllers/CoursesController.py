# controllers/main.py
from odoo import http
from odoo.http import request

class CoursesController(http.Controller):

    @http.route('/courses', auth='public', website=True)
    def courses(self, **kwargs):
        #courses = request.env['elearning.course'].search([])
        return request.render('courses.courses_template',{})
