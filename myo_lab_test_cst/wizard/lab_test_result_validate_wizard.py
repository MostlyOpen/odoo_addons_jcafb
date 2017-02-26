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


class DocumentValidateWizard(models.TransientModel):
    _name = 'myo.lab_test.result.validate.wizard'

    def _default_lab_test_result_ids(self):
        return self._context.get('active_ids')
    lab_test_result_ids = fields.Many2many(
        'myo.lab_test.result',
        'myo_lab_test_result_validate_wizard_rel',
        string='Lab Test Results',
        default=_default_lab_test_result_ids)

    @api.multi
    def do_lab_test_result_validate(self):
        self.ensure_one()

        for lab_test_result_reg in self.lab_test_result_ids:
            print '>>>>>', lab_test_result_reg.name

            lab_test_result_reg.base_document_id = False
            lab_test_result_reg.base_survey_user_input_id = False

            if lab_test_result_reg.lab_test_type_id.name == \
               u'JCAFB 2017 - Exames para detecção de Anemia':

                for document_person in lab_test_result_reg.patient_id.document_person_ids:
                    if document_person.document_id.survey_id.title == '[TID17]' or \
                       document_person.document_id.survey_id.title == '[TCR17]':
                        lab_test_result_reg.base_document_id = document_person.document_id.id
                        if document_person.document_id.survey_user_input_id.id is not False:
                            lab_test_result_reg.base_survey_user_input_id = \
                                document_person.document_id.survey_user_input_id.id

            if lab_test_result_reg.lab_test_type_id.name == \
               u'JCAFB 2017 - Exames - Diabetes, Hipertensão Arterial e Hipercolesterolemia':

                for document_person in lab_test_result_reg.patient_id.document_person_ids:
                    if document_person.document_id.survey_id.title == '[TCP17]':
                        lab_test_result_reg.base_document_id = document_person.document_id.id
                        if document_person.document_id.survey_user_input_id.id is not False:
                            lab_test_result_reg.base_survey_user_input_id = \
                                document_person.document_id.survey_user_input_id.id

            if lab_test_result_reg.lab_test_type_id.name == \
               u'JCAFB 2017 - Laboratório - Urinálise':

                for document_person in lab_test_result_reg.patient_id.document_person_ids:
                    if document_person.document_id.survey_id.title == '[TID17]':
                        lab_test_result_reg.base_document_id = document_person.document_id.id
                        if document_person.document_id.survey_user_input_id.id is not False:
                            lab_test_result_reg.base_survey_user_input_id = \
                                document_person.document_id.survey_user_input_id.id

            if lab_test_result_reg.lab_test_type_id.name == \
               u'JCAFB 2017 - Laboratório - Parasitologia':

                for document_person in lab_test_result_reg.patient_id.document_person_ids:
                    if document_person.document_id.survey_id.title == '[TID17]' or \
                       document_person.document_id.survey_id.title == '[TCR17]':
                        lab_test_result_reg.base_document_id = document_person.document_id.id
                        if document_person.document_id.survey_user_input_id.id is not False:
                            lab_test_result_reg.base_survey_user_input_id = \
                                document_person.document_id.survey_user_input_id.id

            if lab_test_result_reg.lab_test_type_id.name == \
               u'JCAFB 2017 - Laboratório - Pesquisa de Enterobius vermicularis':

                for document_person in lab_test_result_reg.patient_id.document_person_ids:
                    if document_person.document_id.survey_id.title == '[TCR17]':
                        lab_test_result_reg.base_document_id = document_person.document_id.id
                        if document_person.document_id.survey_user_input_id.id is not False:
                            lab_test_result_reg.base_survey_user_input_id = \
                                document_person.document_id.survey_user_input_id.id

        return True
