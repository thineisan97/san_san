from datetime import datetime
from odoo import models,fields,api

class ImprovementSuggestion(models.Model):
    _name = 'improvement.suggestion'

    name = fields.Char(string='Doc No', required=True, copy=False,default=lambda self: ('New'))
    issue_date = fields.Date(string='Issue Date:[Date]',default=datetime.today())

    def get_emp_id(self):
        emp_id = self.env['hr.employee'].search([('user_id', '=', uid)])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ', '=', uid)])
        print("********************************",emp_id)
        return emp_id

    proposed_id = fields.Many2one("hr.employee",string='Proposed By')
    proposed_email = fields.Char(string='Proposed By Email',related='proposed_id.work_email')
    job_title = fields.Char(string='Designation',related='proposed_id.job_title')
    div_bu_br = fields.Char(string='Division/Bu/Branch Name')
    dept_name = fields.Char(string='Department Name',related='proposed_id.department_id.name')
    facilitor_id = fields.Many2one('hr.employee',string='Facilitated By')
    facilitor_email = fields.Char(string='Facilitated By Email',related='facilitor_id.work_email')
    dh_id= fields.Many2one('hr.employee',string='Department Head Name')
    dh_email = fields.Char(string='Department Head Email',related='dh_id.work_email')
    improvement_theme = fields.Text('IMPROVEMENT THEME')
    cur_con_analyze = fields.Text('CURRENT CONDITION ANALYZE')
    improvement_suggestion = fields.Text('IMPROVEMENT SUGGESTION')
    safety_healthy = fields.Boolean(string='Safety/Healthy')
    quality = fields.Boolean(string='Quality (next process/customer satisfaction)')
    cost_budget = fields.Boolean(string='Cost/Budget')
    delivery = fields.Boolean(string='Delivery (next process/customer send on time)')
    morality = fields.Boolean(string='Morality/Good Habit')
    man_people = fields.Boolean(string='Man/People')
    machine = fields.Boolean(string='Machine/Equipment/Tools')
    method = fields.Boolean(string='Method/Process(SOP)')
    material = fields.Boolean(string='Material/Parts')
    environment = fields.Boolean(string='Environment')
    information = fields.Boolean(string='Information')
    sort = fields.Boolean(string='Sort (Separating needed & unneeded)')
    set_in_order = fields.Boolean(string='Set in Order (Keep well & easy to retrieval)')
    shine = fields.Boolean(string='Shine (Neat & Clean)')
    standardize = fields.Boolean(string='Standardize (Standard for 3S above)')
    sustain = fields.Boolean(string='Sustain (Do it & maintain with discipline)')
    improvement_scope = fields.Selection([
        ('individual', 'Individual Improvement'),
        ('departmental','Departmental Improvement'),
        ('whole_umg','The Whole UMG Improvement'),
        ('other','Other Improvement')
    ], string='Improvement Scope')
    before = fields.Image(string='Before Improvement')
    after = fields.Image(string='After Improvement')   
    deliverables = fields.Text(string='DELIVERABLES')
    next_improve_plan = fields.Text(string='NEXT IMPROVEMENT PLAN')
    create_id = fields.Many2one('res.users',string='Created By:',default=lambda self:self.env.user)
    create_date = fields.Datetime('Create Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('add', 'Add'),
        ('approve', 'Approve'),
        ('close', 'Close')
    ], string='State',default="draft")

    def add(self):
        for rec in self:
            rec.state = 'add'
    
    def approve(self):
        for rec in self:
            rec.state = 'approve'

    def close(self):
        for rec in self:
            rec.state = 'close'

    def draft(self):
        for rec in self:
            rec.state = 'draft'

    @api.model
    def create(self,values):
        if not values.get('name', False) or values['name'] == ('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('improvement.suggestion') or 'New'
        res = super(ImprovementSuggestion, self).create(values)
        return res
    