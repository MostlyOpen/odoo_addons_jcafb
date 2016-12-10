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


class AddressEventWizard(models.TransientModel):
    _name = 'myo.address.event.wizard'

    address_ids = fields.Many2many('myo.address', string='Addresses')
    name = fields.Char(string='Event Title')
    description = fields.Html(string='Description')
    planned_hours = fields.Float(
        string='Planned Hours',
        help='Estimated time (in hours) to do the event.'
    )
    date_foreseen = fields.Datetime(string='Foreseen Date', index=True, copy=False)
    date_deadline = fields.Date(string='Deadline', index=True, copy=False)

    @api.multi
    def do_update(self):
        self.ensure_one()

        event_model = self.env['myo.event']

        for address_reg in self.address_ids:
            name = self.name
            description = self.description
            planned_hours = self.planned_hours
            date_foreseen = self.date_foreseen
            date_deadline = self.date_deadline
            address_id = address_reg.id
            user_id = False
            if address_reg.user_id is not False:
                user_id = address_reg.user_id.id
            values = {
                'name': name,
                'description': description,
                'planned_hours': planned_hours,
                'date_foreseen': date_foreseen,
                'date_deadline': date_deadline,
                'address_id': address_id,
                'user_id': user_id,
            }
            event_model.create(values)

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
    def do_populate_marked_addresses(self):
        self.ensure_one()
        self.address_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
