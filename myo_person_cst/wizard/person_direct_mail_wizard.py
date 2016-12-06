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


class PersonDirectMailWizard(models.TransientModel):
    _name = 'myo.person.direct_mail.wizard'

    person_ids = fields.Many2many('myo.person', string='Persons')

    @api.multi
    def do_active_update(self):
        self.ensure_one()

        person_direct_mail_model = self.env['myo.person.direct_mail']

        for person_reg in self.person_ids:

            name = person_reg.name
            code = person_reg.code
            birthday = person_reg.birthday
            age = person_reg.age
            estimated_age = person_reg.estimated_age
            date_reference = person_reg.date_reference
            age_reference = person_reg.age_reference
            gender = person_reg.gender
            categories = ''
            for category in person_reg.category_ids:
                if categories == '':
                    categories = category.name
                else:
                    categories += ';' + category.name
            state = person_reg.state
            responsible_name = person_reg.responsible_id.name
            responsible_code = person_reg.responsible_id.code

            address_name = person_reg.address_id.name
            address_code = person_reg.address_id.code
            address_categories = ''
            for category in person_reg.address_id.category_ids:
                if address_categories == '':
                    address_categories = category.name
                else:
                    address_categories += ';' + category.name
            street = person_reg.address_id.street
            number = person_reg.address_id.number
            street2 = person_reg.address_id.street2
            district = person_reg.address_id.district
            l10n_br_city = person_reg.address_id.l10n_br_city_id.name
            country_state = person_reg.address_id.state_id.name
            country = person_reg.address_id.country_id.name
            zip_code = person_reg.address_id.zip
            email = person_reg.address_id.email
            phone = person_reg.address_id.phone
            mobile = person_reg.address_id.mobile

            values = {
                'name': name,
                'code': code,
                'birthday': birthday,
                'age': age,
                'estimated_age': estimated_age,
                'date_reference': date_reference,
                'age_reference': age_reference,
                'gender': gender,
                'categories': categories,
                'state': state,
                'responsible_name': responsible_name,
                'responsible_code': responsible_code,
                'address_name': address_name,
                'address_code': address_code,
                'address_categories': address_categories,
                'street': street,
                'number': number,
                'street2': street2,
                'district': district,
                'l10n_br_city': l10n_br_city,
                'country_state': country_state,
                'country': country,
                'zip_code': zip_code,
                'email': email,
                'phone': phone,
                'mobile': mobile,
            }
            person_direct_mail_model.create(values)

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

    @api.multi
    def do_populate_selected_persons(self):
        self.ensure_one()
        Person = self.env['myo.person']
        all_selected_persons = Person.search([('state', '=', 'selected'), ])
        self.person_ids = all_selected_persons
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
