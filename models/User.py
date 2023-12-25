from odoo import models, fields

class User(models.Model):
    _name = 'e_courses.user'
    _description = 'Users'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    birth_date = fields.Date(string='Birth Date')
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Password', required=True)
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    
    def name_get(self):
            res = super(User, self).name_get()
            return [(user.id, user.first_name+" "+user.last_name) for user in self]
