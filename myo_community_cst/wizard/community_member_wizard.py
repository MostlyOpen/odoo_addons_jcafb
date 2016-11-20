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


class CommunityMemberWizard(models.TransientModel):
    _name = 'myo.community.member.wizard'

    community_ids = fields.Many2many('myo.community', string='Communities')

    @api.multi
    def do_active_update(self):
        self.ensure_one()

        hr_department_model = self.env['hr.department']
        hr_employee_model = self.env['hr.employee']
        res_users_model = self.env['res.users']
        address_model = self.env['myo.address']
        person_model = self.env['myo.person']
        community_employee_model = self.env['myo.community.employee']
        community_address_model = self.env['myo.community.address']
        community_person_model = self.env['myo.community.person']

        for community_reg in self.community_ids:
            print()
            print('>>>>>', community_reg.name)

            hr_department_search = hr_department_model.search([('name', '=', community_reg.name), ])
            department_id = hr_department_search.id

            hr_employee_search = hr_employee_model.search([('department_id', '=', department_id), ])

            for employee_reg in hr_employee_search:
                print('>>>>>>>>>>', employee_reg.name.encode("utf-8"))

                community_employee_search = community_employee_model.search([
                    ('community_id', '=', community_reg.id),
                    ('employee_id', '=', employee_reg.id),
                ])
                print('>>>>>>>>>>>>>>>', community_employee_search.id)

                if community_employee_search.id is False:
                    values = {
                        'community_id': community_reg.id,
                        'employee_id': employee_reg.id,
                        # 'role': False
                    }
                    community_employee_model.create(values)

            res_users_search = res_users_model.search([('name', '=', community_reg.name), ])
            user_id = res_users_search.id

            address_search = address_model.search([('user_id', '=', user_id), ])

            for address_reg in address_search:
                print('>>>>>>>>>>', address_reg.name.encode("utf-8"))

                community_address_search = community_address_model.search([
                    ('community_id', '=', community_reg.id),
                    ('address_id', '=', address_reg.id),
                ])
                print('>>>>>>>>>>>>>>>', community_address_search.id)

                if community_address_search.id is False:
                    values = {
                        'community_id': community_reg.id,
                        'address_id': address_reg.id,
                        # 'role': False
                    }
                    community_address_model.create(values)

            person_search = person_model.search([('user_id', '=', user_id), ])

            for person_reg in person_search:
                print('>>>>>>>>>>', person_reg.name.encode("utf-8"))

                community_person_search = community_person_model.search([
                    ('community_id', '=', community_reg.id),
                    ('person_id', '=', person_reg.id),
                ])
                print('>>>>>>>>>>>>>>>', community_person_search.id)

                if community_person_search.id is False:
                    values = {
                        'community_id': community_reg.id,
                        'person_id': person_reg.id,
                        # 'role': False
                    }
                    community_person_model.create(values)

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
    def do_populate_communities(self):
        self.ensure_one()
        self.community_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
