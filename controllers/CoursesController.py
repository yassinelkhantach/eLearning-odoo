# Import necessary modules from Odoo
from odoo import http
from odoo.http import request

# Define a controller class for handling courses-related HTTP requests
class CoursesController(http.Controller):

    # Define a route for the URL path '/courses'
    @http.route('/courses', auth='public', website=True)
    def courses(self, **kwargs):
        # Fetch all records from the 'e_courses.course' model
        courses = request.env['e_courses.course'].search([])

        # Render the 'e_courses.courses_template' template, passing the fetched courses for display
        return request.render('e_courses.courses_template', {"courses": courses})
