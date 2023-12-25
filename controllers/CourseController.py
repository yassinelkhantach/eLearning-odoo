from odoo import http
from odoo.http import request

class WebsiteCourses(http.Controller):

    @http.route('/courses', type='http', auth='public', website=True)
    def courses(self, **kwargs):
        courses = request.env['e_courses.course'].search([])
        return http.request.render('e_courses.website_homepage', {"courses": courses})
    
    @http.route('/course/details', type='http', auth='public', website=True)
    def courseDetails(self, **kwargs):
        first_course = request.env['e_courses.course'].sudo().search([], limit=1)
        return http.request.render('e_courses.course_details', {'course':first_course})
    
 