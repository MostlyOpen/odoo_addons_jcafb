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


class SurveyQSC17RefreshWizard(models.TransientModel):
    _name = 'myo.survey.qsc17.refresh.wizard'

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
        default='[QSC17]'
    )

    @api.multi
    def do_survey_qsc17_refresh(self):
        self.ensure_one()

        survey_qsc17_model = self.env['myo.survey.qsc17']
        survey_user_input_model = self.env['survey.user_input']
        document_model = self.env['myo.document']

        # survey_user_input_line_model = self.env['survey.user_input_line']
        # survey_question_model = self.env['survey.question']

        survey_qsc17_search = survey_qsc17_model.search([])
        survey_qsc17_search.unlink()

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

                        QSC17_03_01 = self.get_value('QSC17_03_01', survey_user_input_reg)
                        QSC17_06_01 = self.get_value('QSC17_06_01', survey_user_input_reg)

                        print '>>>>>>>>>>', survey_user_input_reg, document_search.code, person_reg.code

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

                            'QSC17_03_01': QSC17_03_01,
                            'QSC17_06_01': QSC17_06_01,
                        }
                        try:
                            survey_qsc17_model.create(values)
                        except Exception as e:
                            print
                            print '>>>>>>>>>>', e
                            print '>>>>>>>>>>', survey_user_input_reg, document_search.code, person_reg.code
                            print
                            raise

        return True
