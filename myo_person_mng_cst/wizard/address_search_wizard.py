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


class AddressSearchWizard(models.TransientModel):
    _name = 'myo.address.search.wizard'

    person_mng_ids = fields.Many2many('myo.person.mng', string='Persons')

    @api.multi
    def do_search_address(self):
        self.ensure_one()
        _logger.debug('Address search from Address %s',
                      self.person_mng_ids.ids)

        address_model = self.env['myo.address']

        rownum = 0
        found = 0
        not_found = 0
        for person_mng_reg in self.person_mng_ids:
            rownum += 1

            if (person_mng_reg.street is not False) and \
               (person_mng_reg.street != '') and \
               (person_mng_reg.street != '-'):

                address_search = address_model.search([
                    ('street', '=', person_mng_reg.street),
                    ('number', '=', person_mng_reg.number),
                    ('street2', '=', person_mng_reg.street2),
                ])

                if address_search.id is not False:
                    values = {
                        "address_id": address_search.id,
                    }
                    person_mng_reg.write(values)

                    found += 1

                else:

                    not_found += 1

        print()
        print('--> rownum: ', rownum)
        print('--> found: ', found)
        print('--> not_found: ', not_found)
        print()

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
    def do_populate_persons(self):
        self.ensure_one()
        self.person_mng_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
