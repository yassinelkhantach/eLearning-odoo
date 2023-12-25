from odoo import http
from odoo.http import request, Response
import json


class WebsiteCourses(http.Controller):

    @http.route('/courses', type='http', auth='public', website=True)
    def courses(self, **kwargs):
        courses = request.env['e_courses.course'].search([])
        return http.request.render('e_courses.website_homepage', {"courses": courses})
    
    @http.route('/course/details', type='http', auth='user', website=True)
    def courseDetails(self, **kwargs):
        user =  request.env.user
        first_course = request.env['e_courses.course'].sudo().search([], limit=1)
        return http.request.render('e_courses.course_details', {'course':first_course,'user':user})
    

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