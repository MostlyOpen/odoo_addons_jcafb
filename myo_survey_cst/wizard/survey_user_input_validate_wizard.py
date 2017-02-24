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


class SurveyUserInputValidateWizard(models.TransientModel):
    _name = 'survey.user_input.validate.wizard'

    def get_value(self, question_code, survey_user_input_reg):

        survey_question_model = self.env['survey.question']
        survey_user_input_line_model = self.env['survey.user_input_line']

        survey_question_search = survey_question_model.search([
            ('code', '=', question_code),
        ])
        survey_user_input_line_search = survey_user_input_line_model.search([
            ('user_input_id', '=', survey_user_input_reg.id),
            ('question_id', '=', survey_question_search.id),
        ])
        if survey_question_search.type == 'textbox':
            value = survey_user_input_line_search.value_text

        if survey_question_search.type == 'simple_choice':
            value = ''
            for survey_user_input_line_reg in survey_user_input_line_search:
                if value == '':
                    value = survey_user_input_line_reg.value_suggested.value
                else:
                    if survey_user_input_line_reg.value_suggested.value is not False:
                        value = value + '; ' + survey_user_input_line_reg.value_suggested.value

        if survey_question_search.type == 'multiple_choice':
            value = ''
            for survey_user_input_line_reg in survey_user_input_line_search:
                if value == '':
                    value = survey_user_input_line_reg.value_suggested.value
                else:
                    if survey_user_input_line_reg.value_suggested.value is not False:
                        value = value + '; ' + survey_user_input_line_reg.value_suggested.value

        return value

    def _default_survey_user_input_ids(self):
        return self._context.get('active_ids')
    survey_user_input_ids = fields.Many2many(
        'survey.user_input',
        'myo_survey_user_input_validate_wizard_rel',
        string='Exames de Urina',
        default=_default_survey_user_input_ids)

    @api.multi
    def do_survey_user_input_validate(self):
        self.ensure_one()

        lab_test_request_model = self.env['myo.lab_test.request']
        lab_test_result_model = self.env['myo.lab_test.result']

        for survey_user_input_reg in self.survey_user_input_ids:
            print '>>>>>', survey_user_input_reg.survey_id.title, survey_user_input_reg.linked_code

            survey_user_input_reg.linked_message = False

            if survey_user_input_reg.survey_id.title == '[QAN17]':

                codigo_exame = self.get_value('QAN17_01_04', survey_user_input_reg)

                lab_test_request_search = lab_test_request_model.search([
                    ('name', '=', codigo_exame),
                ])
                if lab_test_request_search.id is False:
                    if survey_user_input_reg.linked_message is False:
                        survey_user_input_reg.linked_message = \
                            u'Erro: Codigo da requisição do Exame (Anemia) inválido!'
                    else:
                        survey_user_input_reg.linked_message += \
                            u'\nErro: Codigo da requisição do Exame (Anemia) inválido!'
                else:
                    lab_test_request_search.survey_user_input_id = survey_user_input_reg.id
                    if lab_test_request_search.lab_test_type_id.name != \
                       u'JCAFB 2017 - Exames para detecção de Anemia':
                        if survey_user_input_reg.linked_message is False:
                            survey_user_input_reg.linked_message = \
                                u'Erro: Tipo de Exame da Requisição (Anemia) inválido!'
                        else:
                            survey_user_input_reg.linked_message += \
                                u'\nErro: Tipo de Exame da Requisição (Anemia) inválido!'

                lab_test_result_search = lab_test_result_model.search([
                    ('name', '=', codigo_exame),
                ])
                if lab_test_result_search.id is False:
                    if survey_user_input_reg.linked_message is False:
                        survey_user_input_reg.linked_message = \
                            u'Erro: Codigo do Exame (Anemia) inválido!'
                    else:
                        survey_user_input_reg.linked_message += \
                            u'\nErro: Codigo do Exame (Anemia) inválido!'
                else:
                    lab_test_result_search.survey_user_input_id = survey_user_input_reg.id

            if survey_user_input_reg.survey_id.title == '[QDH17]':

                codigo_exame = self.get_value('QDH17_01_04', survey_user_input_reg)

                lab_test_request_search = lab_test_request_model.search([
                    ('name', '=', codigo_exame),
                ])
                if lab_test_request_search.id is False:
                    if survey_user_input_reg.linked_message is False:
                        survey_user_input_reg.linked_message = \
                            u'Erro: Codigo da requisição do Exame (DHC) inválido!'
                    else:
                        survey_user_input_reg.linked_message += \
                            u'\nErro: Codigo da requisição do Exame (DHC) inválido!'
                else:
                    lab_test_request_search.survey_user_input_id = survey_user_input_reg.id
                    if lab_test_request_search.lab_test_type_id.name != \
                       u'JCAFB 2017 - Exames - Diabetes, Hipertensão Arterial e Hipercolesterolemia':
                        if survey_user_input_reg.linked_message is False:
                            survey_user_input_reg.linked_message = \
                                u'Erro: Tipo de Exame da Requisição (DHC) inválido!'
                        else:
                            survey_user_input_reg.linked_message += \
                                u'\nErro: Tipo de Exame da Requisição (DHC) inválido!'

                lab_test_result_search = lab_test_result_model.search([
                    ('name', '=', codigo_exame),
                ])
                if lab_test_result_search.id is False:
                    if survey_user_input_reg.linked_message is False:
                        survey_user_input_reg.linked_message = \
                            u'Erro: Codigo do Exame (DHC) inválido!'
                    else:
                        survey_user_input_reg.linked_message += \
                            u'\nErro: Codigo do Exame (DHC) inválido!'
                else:
                    lab_test_result_search.survey_user_input_id = survey_user_input_reg.id

        return True
