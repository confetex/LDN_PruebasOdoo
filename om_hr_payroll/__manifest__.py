# -*- coding:utf-8 -*-

{
    'name': 'Odoo 14 HR Payroll',
    'category': 'Generic Modules/Human Resources',
    'version': '14.08',
    'sequence': 1,
    'author': 'IT Admin',
    'summary': 'Payroll For Odoo 14 Community Edition',
    'description': "Odoo 14 Payroll, Payroll Odoo 15, Odoo Community Payroll",
    'website': 'https://odoo.itadmin.com.mx',
    'license': 'LGPL-3',
    'depends': [
        'mail',
        'hr_contract',
        'hr_holidays',
    ],
    'data': [
        'security/hr_payroll_security.xml',
        'security/ir.model.access.csv',
        'data/hr_payroll_sequence.xml',
        'data/hr_payroll_category.xml',
        'data/hr_payroll_data.xml',
        'wizard/hr_payroll_payslips_by_employees_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_salary_rule_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_employee_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'application': True,
}
