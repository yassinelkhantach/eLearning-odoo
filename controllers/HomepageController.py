from odoo import http
from odoo.http import request

class HomepageController(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def render_homepage(self, **kw):
        courses = request.env['e_courses.attachment'].search([])
        return http.request.render('e_courses.website_homepage', {"courses": courses})
