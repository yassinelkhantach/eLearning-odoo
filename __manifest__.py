{
    'name': "e-learning",

    'summary': """Manage trainings""",

    'description': """
        e-learning module for managing trainings:
            - training courses
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
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/Courses_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}