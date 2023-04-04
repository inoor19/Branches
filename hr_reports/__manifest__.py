# -*- coding: utf-8 -*-
##############################################################################
#
#    NCTR, Nile Center for Technology Research
#    Copyright (C) 2022-2023 NCTR (<http://www.nctr.sd>).
#
##############################################################################

{
    "name": "Employee Reports",
    "version": "1.0",
    "category": "Human Resources",
    "sequence": 2,
    "description": """ 
    Manage Employee Reports
    """,
    "author": "NCTR",
    "website": "http://www.nctr.sd",
    "depends": [
                'hr_custom',
                'hr_payroll',
                'base_custom',
                ],
    "data": [

        "wizard/employee_report_wiz_view.xml",
        "report/hr_report_template.xml",
    
    ],
    'license': 'LGPL-3',
    'application': True,
}
