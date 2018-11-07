# -*- coding: utf-8 -*-
{
    'name': "Bệnh Nhân",

    'summary': """
        Tạo danh sách bệnh nhân
        Thêm Xóa Sửa DS Bệnh nhân""",

    'description': """
        Quản lý danh sách Bệnh nhân
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
        'views/patient.xml',
        'views/menu.xml'
            ],
    # only loaded in demonstration mode
    #'demo': [
     #   'demo/demo.xml',
   # ],
}