# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import fields, models


class DocumentEmployee(models.Model):
    _name = 'myo.document.employee'

    document_id = fields.Many2one('myo.document', string='Document',
                                  help='Document', required=False, ondelete='restrict')
    employee_id = fields.Many2one('hr.employee', string='Employee', ondelete='restrict')
    role_id = fields.Many2one('myo.document.role', 'Role', required=False)
    notes = fields.Text(string='Notes')
    active = fields.Boolean('Active',
                            help="If unchecked, it will allow you to hide the document employee without removing it.",
                            default=1)


class Document(models.Model):
    _inherit = 'myo.document'

    employee_ids = fields.One2many(
        'myo.document.employee',
        'document_id',
        'Employees'
    )


class Employee(models.Model):
    _inherit = 'hr.employee'

    document_employee_ids = fields.One2many(
        'myo.document.employee',
        'employee_id',
        'Document Employees'
    )
