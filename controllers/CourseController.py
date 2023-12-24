from odoo import http
from odoo.http import request

class WebsiteCourses(http.Controller):

    @http.route('/courses', type='http', auth='public', website=True)
    def courses(self, **kwargs):
        courses = request.env['e_courses.course'].search([])
        return http.request.render('e_courses.website_homepage', {"courses": courses})