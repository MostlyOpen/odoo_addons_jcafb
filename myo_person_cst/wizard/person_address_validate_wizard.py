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


class PersonAddressValidateWizard(models.TransientModel):
    _name = 'myo.person.address.validate.wizard'

    def _default_person_ids(self):
        return self._context.get('active_ids')
    person_ids = fields.Many2many(
        'myo.person',
        'myo_person_address_validate_wizard_rel',
        string='Persons',
        default=_default_person_ids)

    @api.multi
    def do_person_address_validate(self):
        self.ensure_one()

        person_address_model = self.env['myo.person.address']

        count = 0
        for person_reg in self.person_ids:
            # print '>>>>>', person_reg.code, person_reg.name

            person_address_search = person_address_model.search([
                ('person_id', '=', person_reg.id),
                ('address_id', '=', person_reg.address_id.id),
            ])
            try:
                if person_address_search.id is False:
                    count += 1
                    print '>>>>>>>>>>', person_reg.code, person_reg.name, 'Not Ok'
                    values = {
                        'person_id': person_reg.id,
                        'address_id': person_reg.address_id.id,
                        'sign_in_date': '2017-01-10',
                    }
                    person_address_model.create(values)
            except:
                pass

        print '>>>>> count: ', count

        return True
