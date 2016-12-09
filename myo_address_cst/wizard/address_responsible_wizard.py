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


class AddressResponsibleWizard(models.TransientModel):
    _name = 'myo.address.responsible.wizard'

    address_ids = fields.Many2many('myo.address', string='Addresses')
    user_id = fields.Many2one('res.users', 'Address Responsible')

    @api.multi
    def do_update(self):
        self.ensure_one()

        # address_model = self.env['myo.address']
        # person_model = self.env['myo.person']

        for address_reg in self.address_ids:

            address_reg.user_id = self.user_id

            for person_reg in address_reg.person_ids:
                if person_reg.state == 'selected':
                    person_reg.user_id = self.user_id

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
