# -*- coding: utf-8 -*-
{
    'name': "Real State",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        ## Security
        'security/ir.model.access.csv',
        
        ## Views
        'views/o_properties_views.xml',
        'views/o_property_type_views.xml',
        'views/o_property_tag_views.xml',
        'views/o_property_offer_views.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

