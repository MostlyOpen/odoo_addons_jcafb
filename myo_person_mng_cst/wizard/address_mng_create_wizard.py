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


class AddressMngCreateWizard(models.TransientModel):
    _name = 'myo.address.mng.create.wizard'

    person_mng_ids = fields.Many2many('myo.person.mng', string='Persons')

    @api.multi
    def do_create_address_mng(self):
        self.ensure_one()
        _logger.debug('Address Management create from Person Management %s',
                      self.person_mng_ids.ids)

        tag_model = self.env['myo.tag']
        tag_id_ZonaRural = tag_model.search([('name', '=', 'Zona Rural'), ])[0].id
        tag_id_ZonaUrbana = tag_model.search([('name', '=', 'Zona Urbana'), ])[0].id

        address_mng_model = self.env['myo.address.mng']

        rownum = 0
        duplicated = 0
        imported = 0
        not_imported = 0
        for person_mng_reg in self.person_mng_ids:
            rownum += 1

            if (person_mng_reg.street is not False) and \
               (person_mng_reg.street != '') and \
               (person_mng_reg.street != '-'):

                address_mng_search = address_mng_model.search([
                    ('street', '=', person_mng_reg.street),
                    ('number', '=', person_mng_reg.number),
                    ('street2', '=', person_mng_reg.street2),
                ])

                if address_mng_search.id is not False:
                    values = {
                        "address_mng_id": address_mng_search.id,
                    }
                    person_mng_reg.write(values)

                    duplicated += 1

                else:

                    name = person_mng_reg.street
                    if person_mng_reg.number is not False:
                        name = name + ', ' + person_mng_reg.number
                    if person_mng_reg.street2 is not False:
                        name = name + ' - ' + person_mng_reg.street2

                    tag_ids = []
                    for tag_id in person_mng_reg.tag_ids:
                        if tag_id_ZonaRural == tag_id.id:
                            tag_ids = tag_ids + [(4, tag_id_ZonaRural)]
                        if tag_id_ZonaUrbana == tag_id.id:
                            tag_ids = tag_ids + [(4, tag_id_ZonaUrbana)]

                    values = {
                        'batch_name': person_mng_reg.batch_name,
                        'name': name,
                        'code': False,
                        'zip': person_mng_reg.zip,
                        'street': person_mng_reg.street,
                        'number': person_mng_reg.number,
                        'street2': person_mng_reg.street2,
                        'district': person_mng_reg.district,
                        'country_id': person_mng_reg.country_id.id,
                        'state_id': person_mng_reg.state_id.id,
                        'l10n_br_city_id': person_mng_reg.l10n_br_city_id.id,
                        'phone': person_mng_reg.phone,
                        'mobile': person_mng_reg.mobile,
                        'tag_ids': tag_ids,
                    }
                    address_mng_reg_new = address_mng_model.create(values)

                    values = {
                        "address_mng_id": address_mng_reg_new.id,
                    }
                    person_mng_reg.write(values)

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
    def do_populate_persons(self):
        self.ensure_one()
        self.person_mng_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
