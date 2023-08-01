{
    'name': 'odoo_training',
    "summary":"""Module to handle courses and sessions""",
    "description":"""Module to handle:
        - Courses
        - Sessions
        - Attendees
    """,
    'license':'OPL-1',
    'author': 'Miguel',
    'website':'www.odoo.com',
    'category': 'Custom Modules/Tech Training',
    'depends':  ['base'],
    'data':  [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'views/academy_menuitemx.xml',
        'views/course_views.xml',
        ],
    'demo':  [
        'demo/course_demo.xml',
        ],
    'application': True,
}