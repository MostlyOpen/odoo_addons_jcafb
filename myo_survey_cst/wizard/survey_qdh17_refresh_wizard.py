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


class SurveyQDH17RefreshWizard(models.TransientModel):
    _name = 'myo.survey.qdh17.refresh.wizard'

    def get_value(self, question_code, survey_user_input_reg):

        survey_question_model = self.env['survey.question']
        survey_label_model = self.env['survey.label']
        survey_user_input_line_model = self.env['survey.user_input_line']

        survey_question_search = survey_question_model.search([
            ('code', '=', question_code[:11]),
        ])
        if question_code[:11] == question_code:
            survey_user_input_line_search = survey_user_input_line_model.search([
                ('user_input_id', '=', survey_user_input_reg.id),
                ('question_id', '=', survey_question_search.id),
            ])
        else:
            survey_label_search = survey_label_model.search([
                ('code', '=', question_code),
            ])
            survey_user_input_line_search = survey_user_input_line_model.search([
                ('user_input_id', '=', survey_user_input_reg.id),
                ('question_id', '=', survey_question_search.id),
                ('value_suggested_row', '=', survey_label_search.id),
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
                    # else:
                    #     value = value + '; False'
            # value = survey_user_input_line_search.value_suggested.value

        if survey_question_search.type == 'multiple_choice':
            value = ''
            for survey_user_input_line_reg in survey_user_input_line_search:
                if value == '':
                    value = survey_user_input_line_reg.value_suggested.value
                else:
                    if survey_user_input_line_reg.value_suggested.value is not False:
                        value = value + '; ' + survey_user_input_line_reg.value_suggested.value
                    # else:
                    #     value = value + '; False'

        if survey_question_search.type == 'matrix':
            value = ''
            for survey_user_input_line_reg in survey_user_input_line_search:
                if value == '':
                    value = survey_user_input_line_reg.value_suggested.value
                else:
                    if survey_user_input_line_reg.value_suggested.value is not False:
                        value = value + '; ' + survey_user_input_line_reg.value_suggested.value

        return value

    survey_title = fields.Char(
        'Survey Title',
        required=True,
        default='[QDH17]'
    )

    @api.multi
    def do_survey_qdh17_refresh(self):
        self.ensure_one()

        survey_qdh17_model = self.env['myo.survey.qdh17']
        survey_user_input_model = self.env['survey.user_input']
        document_model = self.env['myo.document']

        # survey_user_input_line_model = self.env['survey.user_input_line']
        # survey_question_model = self.env['survey.question']

        survey_qdh17_search = survey_qdh17_model.search([])
        survey_qdh17_search.unlink()

        survey_user_input_search = survey_user_input_model.search([])

        for survey_user_input_reg in survey_user_input_search:

            document_search = document_model.search([
                ('code', '=', survey_user_input_reg.linked_code),
            ])
            if document_search.id is not False:

                if document_search.survey_id.title == self.survey_title:

                    for person_reg in document_search.person_ids.person_id:

                        age = False
                        if person_reg.birthday is not False:
                            age = person_reg.age_reference
                        else:
                            age = person_reg.estimated_age

                        QDH17_03_01 = self.get_value('QDH17_03_01', survey_user_input_reg)

                        QDH17_03_02 = self.get_value('QDH17_03_02', survey_user_input_reg)

                        QDH17_04_07 = self.get_value('QDH17_04_07', survey_user_input_reg)

                        QDH17_04_08 = self.get_value('QDH17_04_08', survey_user_input_reg)

                        QDH17_04_10 = self.get_value('QDH17_04_10', survey_user_input_reg)

                        QDH17_05_05 = self.get_value('QDH17_05_05', survey_user_input_reg)

                        QDH17_06_03 = self.get_value('QDH17_06_03', survey_user_input_reg)

                        QDH17_06_06 = self.get_value('QDH17_06_06', survey_user_input_reg)

                        QDH17_07_01 = self.get_value('QDH17_07_01', survey_user_input_reg)

                        QDH17_07_02 = self.get_value('QDH17_07_02', survey_user_input_reg)

                        QDH17_07_03 = self.get_value('QDH17_07_03', survey_user_input_reg)

                        QDH17_07_04 = self.get_value('QDH17_07_04', survey_user_input_reg)

                        QDH17_07_05 = self.get_value('QDH17_07_05', survey_user_input_reg)

                        QDH17_07_06 = self.get_value('QDH17_07_06', survey_user_input_reg)

                        QDH17_07_07 = self.get_value('QDH17_07_07', survey_user_input_reg)

                        QDH17_07_08 = self.get_value('QDH17_07_08', survey_user_input_reg)

                        QDH17_09_01 = self.get_value('QDH17_09_01', survey_user_input_reg)

                        QDH17_09_02 = self.get_value('QDH17_09_02', survey_user_input_reg)

                        QDH17_09_03 = self.get_value('QDH17_09_03', survey_user_input_reg)

                        QDH17_09_04 = self.get_value('QDH17_09_04', survey_user_input_reg)

                        QDH17_09_05 = self.get_value('QDH17_09_05', survey_user_input_reg)

                        QDH17_09_06 = self.get_value('QDH17_09_06', survey_user_input_reg)

                        QDH17_10_01 = self.get_value('QDH17_10_01', survey_user_input_reg)

                        QDH17_10_04_06 = self.get_value('QDH17_10_04_06', survey_user_input_reg)

                        values = {
                            'person_code': person_reg.code,
                            'address_code': person_reg.address_id.code,
                            'document_code': document_search.code,
                            'survey_title': self.survey_title,

                            'gender': person_reg.gender,
                            'age': age,
                            'person_category': person_reg.category_names,
                            'person_status': person_reg.state,
                            'address_city': person_reg.address_id.l10n_br_city_id.name,
                            'address_category': person_reg.address_id.category_names,
                            'address_ditrict': person_reg.address_id.district,

                            'QDH17_03_01': QDH17_03_01,
                            'QDH17_03_02': QDH17_03_02,
                            'QDH17_04_07': QDH17_04_07,
                            'QDH17_04_08': QDH17_04_08,
                            'QDH17_04_10': QDH17_04_10,
                            'QDH17_05_05': QDH17_05_05,
                            'QDH17_06_03': QDH17_06_03,
                            'QDH17_06_06': QDH17_06_06,
                            'QDH17_07_01': QDH17_07_01,
                            'QDH17_07_01': QDH17_07_01,
                            'QDH17_07_02': QDH17_07_02,
                            'QDH17_07_03': QDH17_07_03,
                            'QDH17_07_04': QDH17_07_04,
                            'QDH17_07_05': QDH17_07_05,
                            'QDH17_07_06': QDH17_07_06,
                            'QDH17_07_07': QDH17_07_07,
                            'QDH17_07_08': QDH17_07_08,
                            'QDH17_09_01': QDH17_09_01,
                            'QDH17_09_02': QDH17_09_02,
                            'QDH17_09_03': QDH17_09_03,
                            'QDH17_09_04': QDH17_09_04,
                            'QDH17_09_05': QDH17_09_05,
                            'QDH17_09_06': QDH17_09_06,
                            'QDH17_10_01': QDH17_10_01,
                            'QDH17_10_04_06': QDH17_10_04_06,
                        }
                        survey_qdh17_model.create(values)

        return True
