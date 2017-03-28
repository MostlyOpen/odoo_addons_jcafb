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


class LabTestResultUrinaRefreshWizard(models.TransientModel):
    _name = 'myo.lab_test.result.urina.refresh.wizard'

    def get_value(self, criterion_code, lab_test_result_reg):

        lab_test_criterion_model = self.env['myo.lab_test.criterion']

        lab_test_criterio_search = lab_test_criterion_model.search([
            ('lab_test_result_id', '=', lab_test_result_reg.id),
            ('code', '=', criterion_code),
        ])

        value = lab_test_criterio_search.result

        return value

    lab_test_type = fields.Char(
        'Lab Test Type',
        required=True,
        default=u'JCAFB 2017 - Laboratório - Urinálise'
    )

    @api.multi
    def do_lab_test_result_urina_refresh(self):
        self.ensure_one()

        lab_test_result_urina_model = self.env['myo.lab_test.result.urina']
        lab_test_result_model = self.env['myo.lab_test.result']

        lab_test_result_urina_search = lab_test_result_urina_model.search([])
        lab_test_result_urina_search.unlink()

        lab_test_result_search = lab_test_result_model.search([])

        for lab_test_result_reg in lab_test_result_search:

            if lab_test_result_reg.lab_test_type_id.name == self.lab_test_type:

                person_reg = lab_test_result_reg.patient_id

                age = False
                if person_reg.birthday is not False:
                    age = person_reg.age_reference
                else:
                    age = person_reg.estimated_age

                EUR_03_01 = self.get_value('EUR-03-01', lab_test_result_reg)

                print '>>>>>>>>>>', lab_test_result_reg, lab_test_result_reg.name, person_reg.code

                values = {
                    'person_code': person_reg.code,
                    'address_code': person_reg.address_id.code,
                    'lab_test_code': lab_test_result_reg.name,
                    'lab_test_type': self.lab_test_type,

                    'gender': person_reg.gender,
                    'age': age,
                    'person_category': person_reg.category_names,
                    'person_status': person_reg.state,
                    'address_city': person_reg.address_id.l10n_br_city_id.name,
                    'address_category': person_reg.address_id.category_names,
                    'address_ditrict': person_reg.address_id.district,

                    'EUR_03_01': EUR_03_01,
                }
                lab_test_result_urina_model.create(values)

        return True
