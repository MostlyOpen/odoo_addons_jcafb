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


class AddressSummaryWizard(models.TransientModel):
    _name = 'myo.address.summary.wizard'

    address_ids = fields.Many2many('myo.address', string='Addresses')
    category_id = fields.Many2one('myo.summary.category', string='Category')

    @api.multi
    def do_address_update(self):
        self.ensure_one()

        summary_model = self.env['myo.summary']

        for address_reg in self.address_ids:
            name = address_reg.name
            if address_reg.user_id is not False:
                user_id = address_reg.user_id.id
            address_id = address_reg.id
            values = {
                'name': name,
                'user_id': user_id,
                'address_id': address_id,
                'is_address_summary': True,
            }
            new_summary = summary_model.create(values)

            print '>>>>>>>>>>>', self.category_id.id
            if self.category_id.id is not False:

                values = {
                    'category_ids': [(4, self.category_id.id)],
                }
                new_summary.write(values)

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
