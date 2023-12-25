from odoo import http
from odoo.http import request

class WebsiteCourses(http.Controller):

    @http.route('/courses', type='http', auth='public', website=True)
    def courses_controller(self, query=None, tag=None):
        if query:
            courses = request.env['e_courses.course'].search_courses(query)
        elif tag:
            courses = request.env['e_courses.course'].filter_courses_by_tags([tag])
        else:
            courses = request.env['e_courses.course'].search([])
        return http.request.render('e_courses.website_homepage', {'courses': courses})
