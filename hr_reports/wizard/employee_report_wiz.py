# -*- coding: utf-8 -*-
##############################################################################
#
#    NCTR, Nile Center for Technology Research
#    Copyright (C) 2022-2023 NCTR (<http://www.nctr.sd>).
#
##############################################################################

# from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, exceptions, _
from datetime import datetime
import calendar


class EmployeeReportWiz(models.TransientModel):
    _name = 'employee.report.wiz'


    company_ids = fields.Many2one('res.company', string='Unit')
    collect_by = fields.Selection([
        ('degree', 'Degree'),
        ('job', 'Job'),
        ('department', 'Department'),
        ('company', 'Company'),
        ('certificate', 'Certificate'),
        ('all', 'All Employees'),
    ], string='Group By')
   
    report_type = fields.Selection([
        ('synthesis', 'Synthesis'),
        ('detailed', 'Detailed'),
    ], string='Report Type' )

    employee_state = fields.Selection([
        ('draft', 'Draft'),
        ('experiment', 'Experiment'),
        ('approved', 'Approved'),
        ('refuse', 'refuse')
    ], string='Employee State')

    degree_id = fields.Many2many(
        'hr.payroll.structure',
        string='Degree',
    )

    job_ids = fields.Many2many(
        'hr.job',
        string='Job',
    )

    company_id = fields.Many2many(
        'res.company',
        string='Company',
    )

    department_ids = fields.Many2many(
        'hr.department',
        string='Department',
    )

    def print_report(self):
        """
        Call Abstract Model To Generate Report and pass the data
        :return:report
        """
        datas = {
            'ids': [],
            'model': 'hr.employee',
            'service': self.employee_state,
            'job': self.job_ids.ids,
            'department': self.department_ids.ids,
            'degree': self.degree_id.ids,
            'company': self.company_id.ids,
            'state': self.employee_state,
            'group': self.collect_by,
            'type': self.report_type,
            # 'grade': self.degr_ids.mapped('id'),

        }
        return self.env.ref('hr_reports.employee_report_action').report_action(self, data=datas)