# -*- coding: utf-8 -*-
##############################################################################
#
#    NCTR, Nile Center for Technology Research
#    Copyright (C) 2022-2023 NCTR (<http://www.nctr.sd>).
#
##############################################################################

import time
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class EmployeeHrRepot(models.AbstractModel):
    _name = 'report.hr_reports.hr_report_template_view'

    def get_employee_loans_report_data(self, data):
        emp_dic = []
        domain = []
        header = []
        # print("data['group']>>>>>>>>>",data['group'])
        department_ids = data['department']
        degree_id = data['degree']
        company_ids = data['company']
        job_ids = data['job']
        employee_state = data['state']
        collect_by = data['group']
        report_type = data['type']
        # print ('/////////z/////////', department_ids)

        recordset = self.env['hr.department'].search([('id', 'in', department_ids)]) 
        job_recordset = self.env['hr.job'].search([('id', 'in', job_ids)]) 
        company_recordset = self.env['res.company'].search([('id', 'in', company_ids)])
        degree_recordset = self.env['hr.payroll.structure'].search([('id', 'in', degree_id)]) 

        x = False
        if department_ids :
            domain += [('department_id', 'in', department_ids)]
            w = recordset
            x = department_ids
            y = lambda l: l.department_id.id == rec
            z = 'department'


        if job_ids :
            domain += [('job_id', 'in', job_ids)]
            # w = job_recordset
            # x = job_ids
            # y = lambda l: l.job_id.id == rec
            # z = 'job'

        if degree_id :
            domain += [('struct_id', 'in', degree_id)]
            w = degree_recordset
            x = degree_id
            y = lambda l: l.struct_id.id == rec
            z = 'degree'

        if company_ids :
            domain += [('company_id', 'in', company_ids)]
            w = company_recordset
            x = company_ids
            y = lambda l: l.company_id.id == rec
            z = 'company'

        if employee_state :
            domain += [('state', '=', employee_state)]
    

        employee = self.env['hr.employee'].search(domain)
        # debit_rec = sum(self.move_line_ids.filtered(lambda x: x.move_id.date >= begin_day).mapped('debit'))
        # child_reports = child_reports.filtered(lambda l: l.detail_number).sorted(key=lambda l: l.detail_number)
        
        print ('xxxxxxxxxxxxxxxxxxxx', x)
        x == collect_by 
        if report_type == 'detailed':
            if x != False  :
                for rec in x :
                    name = w.browse(rec).name
                    dep_emp = employee.filtered(y)
                    # print ('xxxxxxxxxxxxxxxxxxxx', emp_dic)
                    emps = []
                    if dep_emp  :
                        for type in dep_emp :
                            emp_data = {
                                'name': type.name,
                                'number': type.emp_code,
                                'birthday': type.birthday,
                                'department': type.department_id.name,
                                'job': type.job_id.name,
                                'degree': type.struct_id.name,
                                'start': type.start_date,
                                'certificate_level': type.certificate,
                                'company': type.company_id.name,

                            }

                            emps.append(emp_data)
                        emp_dic.append({
                            'type' : name, 'employees': emps,
                        })
                            
            else : 
                    emps = []
                    for type in employee :
                        emp_data = {
                            'name': type.name,
                            'number': type.emp_code,
                            'birthday': type.birthday,
                            'department': type.department_id.name,
                            'job': type.job_id.name,
                            'degree': type.struct_id.name,
                            'start': type.start_date,
                            'certificate_level': type.certificate,
                            'company': type.company_id.name,

                        }

                        emp_dic.append(emp_data)
                    # emp_dic.append({
                    #     'employees': emps
                    # })
        elif report_type == 'synthesis':
            # emp_dic.append({
            #     'header': "synthesis",
            #     # 'count': "",
            # })

            for rec in x :
                name = w.browse(rec).name
                dep_emp = employee.filtered(y)
                emp_count = len(dep_emp)

                emp_dic.append({
                    'type' : name,
                    'count': emp_count,
                    # 'count': "",
                })

        # header.append({
        #     'header': "synthesis",
        #     # 'count': "",
        # })

            # print ("ggggggggggggggggggggg", emp_dic)


        print ('/.........,,,,,,,,,,,/////', emp_dic)
        # print ('/.........,,,,,,,,,,,/////', emps)
        return  emp_dic
        
        # for type in employee:
        #     emp_data = {
        #         'name': type.name,
        #         'number': type.emp_code,
        #         'birthday': type.birthday,
        #         'department': type.department_id.name,
        #         'job': type.job_id.name,
        #         'degree': type.struct_id.name,
        #         'start': type.start_date,
        #         'certificate_level': type.certificate,
        #         'company': type.company_id.name,

        #     }
        #     if collect_by == 'job' :
        #         emp_data.update({
        #         'group_by': type.job_id.id
        #     })
        #     elif collect_by == 'department' :
        #         emp_data.update({
        #         'group_by': type.department_id.id
        #     })
        #     elif collect_by == 'company' :
        #         emp_data.update({
        #         'group_by': type.company_id.id
        #     })
        #     elif collect_by == 'degree' :
        #         emp_data.update({
        #         'group_by': type.struct_id.id
        #     })
        #     elif collect_by == 'certificate' :
        #         emp_data.update({
        #         'group_by': type.certificate
        #     })
        #     # elif collect_by == 'company' :
        #     #     emp_data.tytypetypepe({
        #     #     'group_by': type.company_id.id
        #     # })
        #     docargs.append(emp_data)
            
    
        # print('11111111111111111111',docargs)

        # return docargs

    @api.model
    def _get_report_values(self, docids, data=None):
        docargs = self.get_employee_loans_report_data(data)
        print('22222222222222222',data)
        return {
            'doc_ids': self.ids,
            'doc_model': 'hr.employee',
            'emp_dic': docargs,
            'data' : data
            
            
        }


