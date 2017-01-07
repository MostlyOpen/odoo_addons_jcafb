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

from openerp import api, fields, models

import logging

_logger = logging.getLogger(__name__)


class LabTestRequestDirectMailWizard(models.TransientModel):
    _name = 'myo.lab_test.request.direct_mail.wizard'

    def _default_lab_test_request_ids(self):
        return self._context.get('active_ids')
    lab_test_request_ids = fields.Many2many(
        'myo.lab_test.request',
        'myo_lab_test_request_direct_mail_wizard_rel',
        'lab_test_request_direct_mail_id',
        'lab_test_request_id',
        'Lab Test Requests',
        default=_default_lab_test_request_ids
    )

    @api.multi
    def do_delete_all(self):
        self.ensure_one()

        lab_test_request_direct_mail_model = self.env['myo.lab_test.request.direct_mail']

        all_lab_test_request_direct_mail = lab_test_request_direct_mail_model.search([])
        all_lab_test_request_direct_mail.unlink()

        return self.do_reopen_form()

    @api.multi
    def do_update(self):
        self.ensure_one()

        lab_test_request_direct_mail_model = self.env['myo.lab_test.request.direct_mail']

        for lab_test_request_reg in self.lab_test_request_ids:

            name = lab_test_request_reg.name
            lab_test_type = lab_test_request_reg.lab_test_type_id.name
            person_responsible = lab_test_request_reg.patient_id.user_id.name
            person_name = lab_test_request_reg.patient_id.name
            person_initials = ''
            for word in person_name.split():
                person_initials += word[0]
            person_code = lab_test_request_reg.patient_id.code
            person_categories = ''
            for category in lab_test_request_reg.patient_id.category_ids:
                if person_categories == '':
                    person_categories = category.name
                else:
                    person_categories += ';' + category.name
            person_reference_age = lab_test_request_reg.patient_id.age_reference

            values = {
                'name': name,
                'lab_test_type': lab_test_type,
                'person_responsible': person_responsible,
                'person_name': person_name,
                'person_initials': person_initials,
                'person_code': person_code,
                'person_categories': person_categories,
                'person_reference_age': person_reference_age,
            }
            lab_test_request_direct_mail_model.create(values)

        return True

    @api.multi
    def do_reopen_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,  # this model
            'res_id': self.id,  # the current wizard record
            'view_type': 'form',
            'view_mode': 'form, tree',
            'target': 'new'}

    # @api.multi
    # def do_populate_marked_lab_test_requests(self):
    #     self.ensure_one()
    #     self.lab_test_request_ids = self._context.get('active_ids')
    #     # reopen wizard form on same wizard record
    #     return self.do_reopen_form()

    # @api.multi
    # def do_populate_selected_lab_test_requests(self):
    #     self.ensure_one()
    #     LabTestRequest = self.env['myo.lab_test.request']
    #     all_selected_lab_test_requests = LabTestRequest.search([('state', '=', 'selected'), ])
    #     self.lab_test_request_ids = all_selected_lab_test_requests
    #     # reopen wizard form on same wizard record
    #     return self.do_reopen_form()
