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

                EUR_02_01 = self.get_value('EUR-02-01', lab_test_result_reg)
                EUR_02_02 = self.get_value('EUR-02-02', lab_test_result_reg)
                EUR_02_03 = self.get_value('EUR-02-03', lab_test_result_reg)
                EUR_02_04 = self.get_value('EUR-02-04', lab_test_result_reg)
                EUR_02_05 = self.get_value('EUR-02-05', lab_test_result_reg)

                EUR_03_01 = self.get_value('EUR-03-01', lab_test_result_reg)
                EUR_03_02 = self.get_value('EUR-03-02', lab_test_result_reg)
                EUR_03_03 = self.get_value('EUR-03-03', lab_test_result_reg)
                EUR_03_04 = self.get_value('EUR-03-04', lab_test_result_reg)
                EUR_03_05 = self.get_value('EUR-03-05', lab_test_result_reg)
                EUR_03_06 = self.get_value('EUR-03-06', lab_test_result_reg)
                EUR_03_07 = self.get_value('EUR-03-07', lab_test_result_reg)
                EUR_03_08 = self.get_value('EUR-03-08', lab_test_result_reg)

                EUR_04_01 = self.get_value('EUR-04-01', lab_test_result_reg)
                EUR_04_02 = self.get_value('EUR-04-02', lab_test_result_reg)
                EUR_04_03 = self.get_value('EUR-04-03', lab_test_result_reg)
                EUR_04_04 = self.get_value('EUR-04-04', lab_test_result_reg)
                EUR_04_05 = self.get_value('EUR-04-05', lab_test_result_reg)
                EUR_04_06 = self.get_value('EUR-04-06', lab_test_result_reg)
                EUR_04_07 = self.get_value('EUR-04-07', lab_test_result_reg)
                EUR_04_08 = self.get_value('EUR-04-08', lab_test_result_reg)
                EUR_04_09 = self.get_value('EUR-04-09', lab_test_result_reg)
                EUR_04_10 = self.get_value('EUR-04-10', lab_test_result_reg)
                EUR_04_11 = self.get_value('EUR-04-11', lab_test_result_reg)
                EUR_04_12 = self.get_value('EUR-04-12', lab_test_result_reg)

                EUR_05_01 = self.get_value('EUR-05-01', lab_test_result_reg)

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

                    'EUR_02_01': EUR_02_01,
                    'EUR_02_02': EUR_02_02,
                    'EUR_02_03': EUR_02_03,
                    'EUR_02_04': EUR_02_04,
                    'EUR_02_05': EUR_02_05,

                    'EUR_03_01': EUR_03_01,
                    'EUR_03_02': EUR_03_02,
                    'EUR_03_03': EUR_03_03,
                    'EUR_03_04': EUR_03_04,
                    'EUR_03_05': EUR_03_05,
                    'EUR_03_06': EUR_03_06,
                    'EUR_03_07': EUR_03_07,
                    'EUR_03_08': EUR_03_08,

                    'EUR_04_01': EUR_04_01,
                    'EUR_04_02': EUR_04_02,
                    'EUR_04_03': EUR_04_03,
                    'EUR_04_04': EUR_04_04,
                    'EUR_04_05': EUR_04_05,
                    'EUR_04_06': EUR_04_06,
                    'EUR_04_07': EUR_04_07,
                    'EUR_04_08': EUR_04_08,
                    'EUR_04_09': EUR_04_09,
                    'EUR_04_10': EUR_04_10,
                    'EUR_04_11': EUR_04_11,
                    'EUR_04_12': EUR_04_12,

                    'EUR_05_01': EUR_05_01,
                }
                try:
                    lab_test_result_urina_model.create(values)
                except Exception as e:
                    print
                    print '>>>>>>>>>>', e
                    print '>>>>>>>>>>', lab_test_result_reg, lab_test_result_reg.name, person_reg.code
                    print
                    raise

        return True
