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
    'depends':  ['sale','website'],
    'data':  [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'data/session_data.xml',
        'views/academy_menuitemx.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sales_views_inherit.xml',
        'views/product_view_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'report/session_report_templates.xml',
        'views/academy_web_templates.xml',
        ],
    'demo':  [
        'demo/course_demo.xml',
        ],
    'application': True,
}