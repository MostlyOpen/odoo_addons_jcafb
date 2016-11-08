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


class AddressCreateWizard(models.TransientModel):
    _name = 'myo.address.create.wizard'

    address_mng_ids = fields.Many2many('myo.address.mng', string='Adresses')

    @api.multi
    def do_create_address(self):
        self.ensure_one()
        _logger.debug('Address create from Address Management %s',
                      self.address_mng_ids.ids)

        address_model = self.env['myo.address']

        rownum = 0
        duplicated = 0
        imported = 0
        not_imported = 0
        for address_mng_reg in self.address_mng_ids:
            rownum += 1

            if (address_mng_reg.street is not False) and \
               (address_mng_reg.street != '') and \
               (address_mng_reg.street != '-'):

                address_search = address_model.search([
                    ('street', '=', address_mng_reg.street),
                    ('number', '=', address_mng_reg.number),
                    ('street2', '=', address_mng_reg.street2),
                ])

                if address_search.id is not False:
                    values = {
                        "address_mng_id": address_search.id,
                        "code": address_search.code,
                        "state": 'done',
                    }
                    address_mng_reg.write(values)

                    duplicated += 1

                else:

                    tag_ids = []
                    for tag_id in address_mng_reg.tag_ids:
                        tag_ids = tag_ids + [(4, tag_id.id)]

                    print('>>>>>', tag_ids)
                    values = {
                        'name': address_mng_reg.name,
                        # 'code': '/',
                        'zip': address_mng_reg.zip,
                        'street': address_mng_reg.street,
                        'number': address_mng_reg.number,
                        'street2': address_mng_reg.street2,
                        'district': address_mng_reg.district,
                        'country_id': address_mng_reg.country_id.id,
                        'state_id': address_mng_reg.state_id.id,
                        'l10n_br_city_id': address_mng_reg.l10n_br_city_id.id,
                        'phone': address_mng_reg.phone,
                        'mobile': address_mng_reg.mobile,
                        'tag_ids': tag_ids,
                    }
                    address_reg_new = address_model.create(values)

                    values = {
                        "address_id": address_reg_new.id,
                        "code": address_reg_new.code,
                        "state": 'done',
                    }
                    address_mng_reg.write(values)

                    imported += 1

            else:
                not_imported += 1

        print()
        print('--> rownum: ', rownum)
        print('--> duplicated: ', duplicated)
        print('--> imported: ', imported)
        print('--> not_imported: ', not_imported)
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
    def do_populate_addresses(self):
        self.ensure_one()
        self.address_mng_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
