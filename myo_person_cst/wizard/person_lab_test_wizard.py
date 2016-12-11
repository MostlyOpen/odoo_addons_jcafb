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


class PersonLabTestWizard(models.TransientModel):
    _name = 'myo.person.lab_test.wizard'

    person_ids = fields.Many2many('myo.person', string='Persons')
    lab_test_type_ids = fields.Many2many('myo.lab_test.type', string='Lab Test Types')

    @api.multi
    def do_active_update(self):
        self.ensure_one()
        _logger.debug('Lab Test update on Persons %s',
                      self.person_ids.ids)

        lab_test_patient_model = self.env['myo.lab_test.request']

        for person in self.person_ids:
            for lab_test_type in self.lab_test_type_ids:
                values = {
                    'lab_test_type_id': lab_test_type.id,
                    'patient_id': person.id,
                }
                lab_test_patient_model.create(values)

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

    @api.multi
    def do_populate_marked_persons(self):
        self.ensure_one()
        self.person_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
