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


class SurveyUserInputTranscribeWizard(models.TransientModel):
    _name = 'survey.user_input.transcribe.wizard'

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
        'myo_survey_user_input_transcribe_wizard_rel',
        string='Exames de Urina',
        default=_default_survey_user_input_ids)

    @api.multi
    def do_survey_user_input_transcribe(self):
        self.ensure_one()

        lab_test_result_model = self.env['myo.lab_test.result']

        for survey_user_input_reg in self.survey_user_input_ids:
            print '>>>>>', survey_user_input_reg.survey_id.title, survey_user_input_reg.linked_code

            survey_user_input_reg.linked_message = False

            if survey_user_input_reg.survey_id.title == '[QAN17]':

                codigo_exame = self.get_value('QAN17_01_04', survey_user_input_reg)

                lab_test_result_search = lab_test_result_model.search([
                    ('name', '=', codigo_exame),
                ])
                if lab_test_result_search.id is not False:

                    lab_test_result_search.survey_user_input_id = survey_user_input_reg.id
                    data_entrevista = self.get_value('QAN17_01_02', survey_user_input_reg)
                    lab_test_result_search.date_result = data_entrevista + ' 20:00:00'

                    for criterion_reg in lab_test_result_search.criterion_ids:

                        if criterion_reg.code == 'EAN-01-01':
                            criterion_reg.result = self.get_value('QAN17_03_01', survey_user_input_reg)
                        # if criterion_reg.code == 'EAN-01-02':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                        if criterion_reg.code == 'EAN-01-03':
                            criterion_reg.result = self.get_value('QAN17_03_03', survey_user_input_reg)
                        # if criterion_reg.code == 'EAN-01-04':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.?

                        # if criterion_reg.code == 'EAN-02-01':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                        # if criterion_reg.code == 'EAN-02-02':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                        if criterion_reg.code == 'EAN-02-03':
                            criterion_reg.result = self.get_value('QAN17_04_03', survey_user_input_reg)
                        # if criterion_reg.code == 'EAN-02-04':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                        if criterion_reg.code == 'EAN-02-05':
                            criterion_reg.result = self.get_value('QAN17_04_05', survey_user_input_reg)

                        # if criterion_reg.code == 'EAN-03-01':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.obs_anemia

            if survey_user_input_reg.survey_id.title == '[QDH17]':

                codigo_exame = self.get_value('QDH17_01_04', survey_user_input_reg)

                lab_test_result_search = lab_test_result_model.search([
                    ('name', '=', codigo_exame),
                ])
                if lab_test_result_search.id is not False:

                    lab_test_result_search.survey_user_input_id = survey_user_input_reg.id
                    data_entrevista = self.get_value('QDH17_01_02', survey_user_input_reg)
                    lab_test_result_search.date_result = data_entrevista + ' 20:00:00'

                    for criterion_reg in lab_test_result_search.criterion_ids:

                        if criterion_reg.code == 'EDH-01-01':
                            criterion_reg.result = self.get_value('QDH17_03_02', survey_user_input_reg)

                        if criterion_reg.code == 'EDH-02-01':
                            criterion_reg.result = self.get_value('QDH17_04_01', survey_user_input_reg)
                        if criterion_reg.code == 'EDH-02-02':
                            criterion_reg.result = self.get_value('QDH17_04_03', survey_user_input_reg)
                        if criterion_reg.code == 'EDH-02-03':
                            criterion_reg.result = self.get_value('QDH17_04_05', survey_user_input_reg)
                        if criterion_reg.code == 'EDH-02-04':
                            criterion_reg.result = self.get_value('QDH17_04_07', survey_user_input_reg)
                        # if criterion_reg.code == 'EDH-02-05':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                        if criterion_reg.code == 'EDH-02-06':
                            criterion_reg.result = self.get_value('QDH17_04_07', survey_user_input_reg)
                        if criterion_reg.code == 'EDH-02-07':
                            criterion_reg.result = self.get_value('QDH17_04_10', survey_user_input_reg)
                        # if criterion_reg.code == 'EDH-02-08':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.?

                        if criterion_reg.code == 'EDH-03-01':
                            criterion_reg.result = self.get_value('QDH17_05_01', survey_user_input_reg)
                        if criterion_reg.code == 'EDH-03-02':
                            criterion_reg.result = self.get_value('QDH17_05_03', survey_user_input_reg)
                        if criterion_reg.code == 'EDH-03-03':
                            criterion_reg.result = self.get_value('QDH17_05_05', survey_user_input_reg)
                        # if criterion_reg.code == 'EDH-03-04':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.obs_pressao_dhc

                        if criterion_reg.code == 'EDH-04-01':
                            criterion_reg.result = self.get_value('QDH17_06_01', survey_user_input_reg)
                        if criterion_reg.code == 'EDH-04-02':
                            criterion_reg.result = self.get_value('QDH17_06_03', survey_user_input_reg)
                        # if criterion_reg.code == 'EDH-04-03':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                        if criterion_reg.code == 'EDH-04-04':
                            criterion_reg.result = self.get_value('QDH17_06_04', survey_user_input_reg)
                        if criterion_reg.code == 'EDH-04-05':
                            criterion_reg.result = self.get_value('QDH17_06_06', survey_user_input_reg)
                        # if criterion_reg.code == 'EDH-04-06':
                        #     criterion_reg.result = lab_test_anemia_dhc_reg.obs_dhc

        return True
