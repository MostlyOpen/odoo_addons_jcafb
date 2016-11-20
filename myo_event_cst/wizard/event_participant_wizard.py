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

from __future__ import print_function

from openerp import api, fields, models

import logging

_logger = logging.getLogger(__name__)


class EventParticipantWizard(models.TransientModel):
    _name = 'myo.event.participant.wizard'

    event_ids = fields.Many2many('myo.event', string='Events')

    @api.multi
    def do_active_update(self):
        self.ensure_one()

        hr_department_model = self.env['hr.department']
        hr_employee_model = self.env['hr.employee']
        person_model = self.env['myo.person']
        event_employee_model = self.env['myo.event.employee']
        event_person_model = self.env['myo.event.person']

        for event_reg in self.event_ids:
            print()
            print('>>>>>', event_reg.name, event_reg.address_id.name)

            user_id = event_reg.address_id.user_id.id
            user_name = event_reg.address_id.user_id.name

            event_reg.user_id = user_id

            hr_department_search = hr_department_model.search([('name', '=', user_name), ])
            department_id = hr_department_search.id

            hr_employee_search = hr_employee_model.search([('department_id', '=', department_id), ])

            for employee_reg in hr_employee_search:
                print('>>>>>>>>>>', employee_reg.name.encode("utf-8"))

                event_employee_search = event_employee_model.search([
                    ('event_id', '=', event_reg.id),
                    ('employee_id', '=', employee_reg.id),
                ])
                print('>>>>>>>>>>>>>>>', event_employee_search.id)

                if event_employee_search.id is False:
                    values = {
                        'event_id': event_reg.id,
                        'employee_id': employee_reg.id,
                        # 'role': False
                    }
                    event_employee_model.create(values)

            person_search = person_model.search([
                ('address_id', '=', event_reg.address_id.id),
                ('state', '=', 'selected'),
            ])

            for person_reg in person_search:
                print('>>>>>>>>>>', person_reg.name.encode("utf-8"))

                event_person_search = event_person_model.search([
                    ('event_id', '=', event_reg.id),
                    ('person_id', '=', person_reg.id),
                ])
                print('>>>>>>>>>>>>>>>', event_person_search.id)

                if event_person_search.id is False:
                    values = {
                        'event_id': event_reg.id,
                        'person_id': person_reg.id,
                        # 'role': False
                    }
                    event_person_model.create(values)

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
    def do_populate_events(self):
        self.ensure_one()
        self.event_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
