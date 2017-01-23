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
import xlrd

_logger = logging.getLogger(__name__)


class SurveyFileImportWizard(models.TransientModel):
    _name = 'myo.survey.file.import.wizard'

    def _default_survey_file_ids(self):
        return self._context.get('active_ids')
    survey_file_ids = fields.Many2many(
        'myo.survey.file',
        string='Survey Files',
        default=_default_survey_file_ids)

    dir_path = fields.Char(
        'Directory Path',
        required=True,
        help="Directory Path",
        default='/opt/openerp/mostlyopen_clvhealth_jcafb/survey_files/input'
    )

    @api.multi
    def do_survey_file_import(self):
        self.ensure_one()

        survey_question_model = self.env['survey.question']
        survey_labe_model = self.env['survey.label']
        survey_user_input_model = self.env['survey.user_input']
        survey_user_input_line_model = self.env['survey.user_input_line']

        for survey_file_reg in self.survey_file_ids:

            filepath = self.dir_path + '/' + survey_file_reg.name

            print '>>>>>', filepath

            book = xlrd.open_workbook(filepath)
            sheet = book.sheet_by_index(0)
            # survey_title = sheet.cell_value(0, 0)
            print '>>>>>', survey_file_reg.survey_id.description

            if survey_file_reg.state == 'validated':

                values = {
                    'survey_id': survey_file_reg.survey_id.id,
                    'state': 'done',
                }
                survey_user_input = survey_user_input_model.create(values)
                print '>>>>>', survey_user_input

                for i in range(sheet.nrows):

                    code_row = sheet.cell_value(i, 0)

                    if code_row == xlrd.empty_cell.value:
                        continue

                    if code_row == '[]':
                        code_cols = {}
                        for k in range(sheet.ncols):
                            code_col = sheet.cell_value(i, k)
                            if code_col != xlrd.empty_cell.value:
                                code_cols.update({k: code_col})

                    row_code = code_row.replace('[', '').replace(']', '')

                    for j in range(sheet.ncols):

                        if sheet.cell_value(i, j) == '.':

                            try:
                                value = sheet.cell_value(i, j + 1)
                            except:
                                value = xlrd.empty_cell.value

                            if value != xlrd.empty_cell.value:

                                question_code = row_code[:11]
                                survey_question_search = survey_question_model.search([
                                    ('code', '=', question_code),
                                ])
                                if survey_question_search.id is not False:
                                    question_type = survey_question_search.type
                                    question_matrix_subtype = False
                                    if question_type == 'matrix':
                                        question_matrix_subtype = survey_question_search.matrix_subtype

                                print '>>>>>>>>>> (', i, j + 1, ')', row_code, question_type, question_matrix_subtype
                                # print '>>>>>>>>>>>>>>>', value
                                # print '>>>>>>>>>>>>>>>', survey_question_search.survey_id.id, survey_question_search.id, survey_user_input.id

                                if survey_question_search.type == 'textbox':

                                    # print '>>>>>>>>>>>>>>>>>>>>', value
                                    values = {
                                        'survey_id': survey_question_search.survey_id.id,
                                        'question_id': survey_question_search.id,
                                        'user_input_id': survey_user_input.id,
                                        'answer_type': 'text',
                                        'value_text': value,
                                    }
                                    survey_user_input_line_model.create(values)

                                elif survey_question_search.type == 'simple_choice':

                                    if row_code != question_code:
                                        survey_label_code = row_code
                                        survey_label_search = survey_labe_model.search([
                                            ('code', '=', survey_label_code),
                                        ])
                                        if survey_label_search.id is not False:

                                            # print '>>>>>>>>>>>>>>>>>>>>', survey_label_search.value
                                            values = {
                                                'survey_id': survey_question_search.survey_id.id,
                                                'question_id': survey_question_search.id,
                                                'user_input_id': survey_user_input.id,
                                                'answer_type': 'suggestion',
                                                'value_suggested': survey_label_search.id,
                                                'quizz_mark': 0.0
                                            }
                                            survey_user_input_line_model.create(values)

                                    else:
                                        # print '>>>>>>>>>>>>>>>>>>>>xxxxxxxxxxxxxxxxx', value
                                        values = {
                                            'survey_id': survey_question_search.survey_id.id,
                                            'question_id': survey_question_search.id,
                                            'user_input_id': survey_user_input.id,
                                            'answer_type': 'text',
                                            'value_text': value,
                                            # 'quizz_mark': 0.0
                                        }
                                        survey_user_input_line_model.create(values)

                                elif survey_question_search.type == 'multiple_choice':

                                    if row_code != question_code:
                                        survey_label_code = row_code
                                        survey_label_search = survey_labe_model.search([
                                            ('code', '=', survey_label_code),
                                        ])
                                        if survey_label_search.id is not False:

                                            # print '>>>>>>>>>>>>>>>>>>>>', survey_label_search.value
                                            values = {
                                                'survey_id': survey_question_search.survey_id.id,
                                                'question_id': survey_question_search.id,
                                                'user_input_id': survey_user_input.id,
                                                'answer_type': 'suggestion',
                                                'value_suggested': survey_label_search.id,
                                                'quizz_mark': 0.0
                                            }
                                            survey_user_input_line_model.create(values)

                                    else:
                                        # print '>>>>>>>>>>>>>>>>>>>>', value
                                        values = {
                                            'survey_id': survey_question_search.survey_id.id,
                                            'question_id': survey_question_search.id,
                                            'user_input_id': survey_user_input.id,
                                            'answer_type': 'text',
                                            'value_text': value,
                                            # 'quizz_mark': 0.0
                                        }
                                        survey_user_input_line_model.create(values)

                                elif survey_question_search.type == 'matrix':

                                    if survey_question_search.matrix_subtype == 'simple':

                                        col_code = code_cols[j].replace('[', '').replace(']', '')

                                        # print '>>>>>>>>>>>>>>>>>>>>', row_code, col_code

                                        survey_label_row_search = survey_labe_model.search([
                                            ('code', '=', row_code),
                                        ])
                                        survey_label_col_search = survey_labe_model.search([
                                            ('code', '=', col_code),
                                        ])
                                        if survey_label_row_search.id is not False and\
                                           survey_label_col_search.id is not False:

                                            # print '>>>>>>>>>>>>>>>>>>>>', survey_label_col_search.value
                                            values = {
                                                'survey_id': survey_question_search.survey_id.id,
                                                'question_id': survey_question_search.id,
                                                'user_input_id': survey_user_input.id,
                                                'answer_type': 'suggestion',
                                                'value_suggested_row': survey_label_row_search.id,
                                                'value_suggested': survey_label_col_search.id,
                                                'quizz_mark': 0.0
                                            }
                                            survey_user_input_line_model.create(values)

                survey_user_input.linked_code = survey_file_reg.document_code
                survey_user_input.linked_state = 'linked'
                survey_file_reg.state = 'imported'
                survey_file_reg.document_id.survey_user_input_id = survey_user_input.id
                survey_file_reg.document_id.state = 'done'

        return True

    # @api.multi
    # def do_reopen_form(self):
    #     self.ensure_one()
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': self._name,  # this model
    #         'res_id': self.id,  # the current wizard record
    #         'view_type': 'form',
    #         'view_mode': 'form, tree',
    #         'target': 'new'}

    # @api.multi
    # def do_populate_marked_survey_files(self):
    #     self.ensure_one()
    #     self.survey_file_ids = self._context.get('active_ids')
    #     # reopen wizard form on same wizard record
    #     return self.do_reopen_form()
