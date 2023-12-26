from odoo import http
from odoo.http import request, Response
import json


class WebsiteCourses(http.Controller):

    @http.route('/courses', type='http', auth='public', website=True)
    def courses(self, **kwargs):
        courses = request.env['e_courses.course'].search([])
        return http.request.render('e_courses.website_homepage', {"courses": courses})
    
    @http.route('/course/<int:course_id>/details', type='http', auth='user', website=True)
    def courseDetails(self, course_id, **kwargs):
        user = request.env.user
        course = request.env['e_courses.course'].sudo().browse(course_id)
        return http.request.render('e_courses.course_details', {'course': course, 'user': user})


    @http.route('/course/<int:course_id>/rate', type='http', auth="public", website=True, csrf=False)
    def rate_course(self, course_id, value, **kwargs):
        try:
            # Get or create the course and user records
            course = request.env['e_courses.course'].browse(course_id)
            
            # Create a new rating record
            request.env['e_courses.rating'].create({
                'course_id': course.id,
                'user_id': request.env.user.id,
                'value': float(value),
            })

            # Return success response
            return Response(json.dumps({'result': 'success'}), content_type='application/json', status=200)
        except Exception as e:
            # Return failure response
            return Response(json.dumps({'result': 'failed', 'error': str(e)}), content_type='application/json', status=500)
 

    @http.route('/course/<int:course_id>/user_rating', type='http', auth="public", website=True, csrf=False)
    def get_user_rating(self, course_id, **kwargs):
        try:
            user_id = request.env.user.id if request.env.user else False

            if user_id:
                ratings = request.env['e_courses.rating'].sudo().search([
                    ('course_id', '=', course_id),
                    ('user_id', '=', user_id),
                ])
                
                user_rating = ratings[0].value if ratings else 0

                # Calculate the average rating
                all_ratings = request.env['e_courses.rating'].sudo().search([('course_id', '=', course_id)])
                average_rating = sum(all_ratings.mapped('value')) / len(all_ratings) if all_ratings else 0

                response_data = {
                    'result': 'success',
                    'user_rating': user_rating,
                    'average_rating': average_rating,
                }

                return Response(json.dumps(response_data), content_type='application/json')
            else:
                return Response(json.dumps({'result': 'error', 'message': 'User not authenticated'}), content_type='application/json')
        except Exception as e:
            return Response(json.dumps({'result': 'error', 'message': str(e)}), content_type='application/json')
        
    def _get_user_name(self, cr, uid, *args):
        user_obj = self.pool.get('res.users')
        user_value = user_obj.browse(cr, uid, uid)
        return user_value.login or False
    
    def courses_controller(self, query=None, tag=None):
        if query:
            courses = request.env['e_courses.course'].search_courses(query)
        elif tag:
            courses = request.env['e_courses.course'].filter_courses_by_tags([tag])
        else:
            courses = request.env['e_courses.course'].search([])
        tags= request.env['e_courses.course.tag'].search([])
        return http.request.render('e_courses.website_explore_courses', {'courses': courses,'tags':tags})
    
    @http.route('/course/<int:course_id>/enroll', type='http', auth='user', website=True, csrf=False)
    def enroll_course(self, course_id, **kwargs):
        # Get the current user
        user = request.env.user

        # Get the course based on the provided course_id
        course = request.env['e_courses.course'].sudo().browse(course_id)

        # Check if the user is already enrolled in the course
        is_enrolled = request.env['e_courses.enroll_course'].sudo().search([
            ('course_id', '=', course.id),
            ('user_id', '=', user.id),
        ])
        if not is_enrolled:
            # Enroll the user in the course
            request.env['e_courses.enroll_course'].sudo().create({
                'course_id': course.id,
                'user_id': user.id,
            })

            # Return success response
            success_response = {'result': 'success', 'message': 'Enrollment successful','enrolled': True}
            return Response(json.dumps(success_response), content_type='application/json')
        else:
            # The user is already enrolled, return failure response
            failure_response = {'result': 'failure', 'message': 'User is already enrolled in this course','enrolled': True}
            return Response(json.dumps(failure_response), content_type='application/json')

    
    @http.route('/course/<int:course_id>/enrollment_status', type='http', auth='user', website=True, csrf=False)
    def check_enrollment_status(self, course_id, **kwargs):
        try:
            # Get the current user
            user = http.request.env.user

            # Get the course based on the provided course_id
            course = http.request.env['e_courses.course'].sudo().browse(course_id)

            # Check if the user is enrolled in the course
            is_enrolled = http.request.env['e_courses.enroll_course'].sudo().search([
                ('course_id', '=', course.id),
                ('user_id', '=', user.id),
            ])

            # Return enrollment status
            response_data = {'enrolled': bool(is_enrolled)}
            return Response(json.dumps(response_data), content_type='application/json')

        except Exception as e:
            # Handle any exceptions
            error_response = {'error': str(e)}
            return Response(json.dumps(error_response), content_type='application/json')
