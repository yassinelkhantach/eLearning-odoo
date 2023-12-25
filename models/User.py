from odoo import models, fields, api

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

    @api.model
    def create_new_user(self):
        # Create a new user
        new_user = self.env['res.users'].create({
            'name': self.first_name+" "+self.last_name,  # Full name of the user
            'login': self.email,  # Login username
            'email': self.email,  # Email address
            'password': self.password,  # Set a secure password
            # Add other fields as needed
        })

        # Return or use the new user data as needed
        return {
            'user_id': new_user.id,
            'user_name': new_user.name,
            'user_email': new_user.email,
        }