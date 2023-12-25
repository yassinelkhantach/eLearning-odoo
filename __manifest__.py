{
    'name': "e_courses",

    'summary': """Manage trainings""",

    'description': """
        e-courses module for managing trainings:
            - training courses : courses -> lessons -> attachments
            - training sessions
            - attendees registration
    """,

    'author': "DARDOURI Chaimae, EL KHANTACH Yassine, BERHI Othmane",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',"web","website"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/Courses_view.xml',
        'views/Users_view.xml',
        'views/Lessons_view.xml',
        'views/Attachments_view.xml',
        'views/home.xml',
        'views/Rating_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'assets': {
            'web.assets_frontend': [
                            'https://code.jquery.com/jquery-3.5.1.slim.min.js',
                            'https://cdn.jsdelivr.net/npm/@popperjs/core@2.0.8/dist/umd/popper.min.js',
                            'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js'
            ]
        }
}