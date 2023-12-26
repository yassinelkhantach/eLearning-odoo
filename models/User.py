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
    odoo_user_id = fields.Many2one('res.users', string='Odoo User')

    def name_get(self):
            res = super(User, self).name_get()
            return [(user.id, user.first_name+" "+user.last_name) for user in self]


    @api.model
    def create(self, values):
        # Call the create method of the superclass
        new_user = super(User, self).create(values)
        # Create the corresponding Odoo user
        new_user.create_odoo_user()
        return new_user

    def create_odoo_user(self):
        # Create a user in res.users
        user_values = {
            'name': self.first_name+" "+self.last_name,
            'login': self.email,
            'email': self.email,
            'password': self.password
        }
        odoo_user = self.env['res.users'].sudo().create(user_values)
        # Link the custom user with the corresponding res.users record
        self.write({'odoo_user_id': odoo_user.id})

        return odoo_user