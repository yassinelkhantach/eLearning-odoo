{
    'name': "E-Courses Module",

    'summary': """Revolutionize Online Learning""",

    'description': """
        The E-Courses module is a dynamic platform designed for modern online learning. Key features include:
            - Course Management: Create, update, and organize courses, lessons, and attachments.
            - Attendees Registration: Facilitate easy registration for online course.

        Explore a user-friendly interface that empowers educators and provides an engaging learning experience for students.

        Developed by DARDOURI Chaimae, EL KHANTACH Yassine, and BERHI Othmane.
    """,

    'author': "DARDOURI Chaimae, EL KHANTACH Yassine, BERHI Othmane",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
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
        'views/course_details.xml',
        'views/Rating_view.xml',
        'views/explore_courses.xml'
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
                            '/e_courses/static/lib/pdfslidesviewer/PDFSlidesViewer.js'
            ]
        }
}