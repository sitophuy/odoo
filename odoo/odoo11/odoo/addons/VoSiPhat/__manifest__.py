# -*- coding: utf-8 -*-
{
    'name': "Senmailbackup",
    'summary': """
        Module này do Võ Sĩ Phát viết, vui lòng không sửa khi chưa hỏi ý k""",
    'description': """
        Module gửi email
    """,
    'author': "Võ Sĩ Phát",
    'website': "http://www.tsiphat.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'views/mymenu.xml',
    ],
    'application': True,
}