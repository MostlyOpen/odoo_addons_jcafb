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


class SurveyFileValidateWizard(models.TransientModel):
    _name = 'myo.survey.file.validate.wizard'

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
    def do_survey_file_validate(self):
        self.ensure_one()

        for survey_file_reg in self.survey_file_ids:

            filepath = self.dir_path + '/' + survey_file_reg.name

            print '>>>>>', filepath

            book = xlrd.open_workbook(filepath)
            sheet = book.sheet_by_index(0)
            survey_title = sheet.cell_value(0, 0)
            print '>>>>>>>>>>', '"' + survey_title + '"'

            if survey_file_reg.state == 'checked':

                # survey_model = self.env['survey.survey']
                survey_question_model = self.env['survey.question']
                # survey_label = self.env['survey.label']

                question_code = False
                question_type = False
                question_matrix_subtype = False
                matrix_row = False
                question_constr_mandatory = False
                question_comments_allowed = False
                response_count = 0

                prev_question_code = False
                prev_question_type = False
                prev_question_matrix_subtype = False
                prev_matrix_row = False
                prev_question_constr_mandatory = False
                # prev_question_comments_allowed = False
                # prev_response_count = 0

                begin_question = False
                end_question = False
                last_row = sheet.nrows - 1
                last_question_code = False

                print '>>>>>', last_row
                for i in range(sheet.nrows):

                    prev_question_code = question_code
                    prev_question_type = question_type
                    prev_question_matrix_subtype = question_matrix_subtype
                    prev_matrix_row = matrix_row
                    prev_question_constr_mandatory = question_constr_mandatory
                    # prev_question_comments_allowed = question_comments_allowed
                    # prev_response_count = response_count

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

                    if len(row_code) < 11:
                        continue
                    else:
                        question_code = row_code[:11]
                        survey_question_search = survey_question_model.search([
                            ('code', '=', question_code),
                        ])
                        if survey_question_search.id is not False:
                            matrix_row = False
                            question_type = survey_question_search.type
                            question_constr_mandatory = survey_question_search.constr_mandatory
                            if question_type == 'matrix':
                                question_matrix_subtype = survey_question_search.matrix_subtype
                                question_comments_allowed = False
                            else:
                                question_matrix_subtype = False
                                question_comments_allowed = survey_question_search.comments_allowed
                            if question_type == 'matrix':
                                if question_code != row_code:
                                    matrix_row = True
                                    question_code = row_code
                                    if question_code != last_question_code:
                                        if question_code is not False and last_question_code is not False:
                                            end_question = True
                                        begin_question = True
                                        last_question_code = question_code
                        if question_code != last_question_code:
                            if question_code is not False and last_question_code is not False:
                                end_question = True
                            begin_question = True
                            last_question_code = question_code

                    if end_question is True:

                        if prev_question_constr_mandatory is True:
                            if prev_question_type in ['textbox', 'datetime']:
                                if response_count != 1:
                                    if survey_file_reg.notes is False:
                                        survey_file_reg.notes = \
                                            'Erro: Questao ' + prev_question_code + ' sem resposta!'
                                    else:
                                        survey_file_reg.notes += \
                                            '\nErro: Questao ' + prev_question_code + ' sem resposta!'

                            if prev_question_type in ['simple_choice']:
                                if response_count == 0:
                                    if survey_file_reg.notes is False:
                                        survey_file_reg.notes = \
                                            'Erro: Questao ' + prev_question_code + ' sem resposta!'
                                    else:
                                        survey_file_reg.notes += \
                                            '\nErro: Questao ' + prev_question_code + ' sem resposta!'
                                if response_count > 1:
                                    if survey_file_reg.notes is False:
                                        survey_file_reg.notes = \
                                            'Erro: Questao ' + prev_question_code + ' com mais de uma resposta!'
                                    else:
                                        survey_file_reg.notes += \
                                            '\nErro: Questao ' + prev_question_code + ' com mais de uma resposta!'

                            if prev_question_type in ['multiple_choice']:
                                if response_count < 1:
                                    if survey_file_reg.notes is False:
                                        survey_file_reg.notes = \
                                            'Erro: Questao ' + prev_question_code + ' sem resposta!'
                                    else:
                                        survey_file_reg.notes += \
                                            '\nErro: Questao ' + prev_question_code + ' sem resposta!'

                            if prev_question_type in ['matrix'] and prev_question_matrix_subtype in ['simple']:
                                if prev_matrix_row is True:
                                    if response_count == 0:
                                        if survey_file_reg.notes is False:
                                            survey_file_reg.notes = \
                                                'Erro: Questao ' + prev_question_code + ' sem resposta!'
                                        else:
                                            survey_file_reg.notes += \
                                                '\nErro: Questao ' + prev_question_code + ' sem resposta!'
                                    if response_count > 1:
                                        if survey_file_reg.notes is False:
                                            survey_file_reg.notes = \
                                                'Erro: Questao ' + prev_question_code + ' com mais de uma resposta!'
                                        else:
                                            survey_file_reg.notes += \
                                                '\nErro: Questao ' + prev_question_code + ' com mais de uma resposta!'

                        print '---------->', response_count, matrix_row, prev_matrix_row
                        response_count = 0
                        end_question = False

                    if begin_question is True:
                        print '---------->', question_code, question_type, question_matrix_subtype, question_constr_mandatory, question_comments_allowed, matrix_row, prev_matrix_row
                        begin_question = False

                    print '>>>>>>>>>> (', i, ')', code_row, row_code, question_code, last_question_code

                    for j in range(sheet.ncols):

                        if sheet.cell_value(i, j) == '.':
                            try:
                                value = sheet.cell_value(i, j + 1)
                            except:
                                value = xlrd.empty_cell.value
                            if value != xlrd.empty_cell.value:
                                if question_type in ['multiple_choice', 'simple_choice']:
                                    if question_code != row_code:
                                        response_count += 1
                                else:
                                    response_count += 1

                    if i == last_row or \
                       (i == last_row - 1 and sheet.cell_value(i + 1, 0) == xlrd.empty_cell.value):
                        end_question = True

                    if end_question is True:

                        if question_constr_mandatory is True:
                            if question_type in ['textbox', 'datetime']:
                                if response_count != 1:
                                    if survey_file_reg.notes is False:
                                        survey_file_reg.notes = \
                                            'Erro: Questao ' + question_code + ' sem resposta!'
                                    else:
                                        survey_file_reg.notes += \
                                            '\nErro: Questao ' + question_code + ' sem resposta!'

                            if question_type in ['simple_choice']:
                                if response_count == 0:
                                    if survey_file_reg.notes is False:
                                        survey_file_reg.notes = \
                                            'Erro: Questao ' + question_code + ' sem resposta!'
                                    else:
                                        survey_file_reg.notes += \
                                            '\nErro: Questao ' + question_code + ' sem resposta!'
                                if response_count > 1:
                                    if survey_file_reg.notes is False:
                                        survey_file_reg.notes = \
                                            'Erro: Questao ' + question_code + ' com mais de uma resposta!'
                                    else:
                                        survey_file_reg.notes += \
                                            '\nErro: Questao ' + question_code + ' com mais de uma resposta!'

                            if question_type in ['multiple_choice']:
                                if response_count < 1:
                                    if survey_file_reg.notes is False:
                                        survey_file_reg.notes = \
                                            'Erro: Questao ' + question_code + ' sem resposta!'
                                    else:
                                        survey_file_reg.notes += \
                                            '\nErro: Questao ' + question_code + ' sem resposta!'

                            if question_type in ['matrix'] and question_matrix_subtype in ['simple']:
                                if matrix_row is True:
                                    if response_count == 0:
                                        if survey_file_reg.notes is False:
                                            survey_file_reg.notes = \
                                                'Erro: Questao ' + question_code + ' sem resposta!'
                                        else:
                                            survey_file_reg.notes += \
                                                '\nErro: Questao ' + question_code + ' sem resposta!'
                                    if response_count > 1:
                                        if survey_file_reg.notes is False:
                                            survey_file_reg.notes = \
                                                'Erro: Questao ' + question_code + ' com mais de uma resposta!'
                                        else:
                                            survey_file_reg.notes += \
                                                '\nErro: Questao ' + question_code + ' com mais de uma resposta!'

                        print '---------->', response_count, matrix_row, prev_matrix_row
                        response_count = 0
                        end_question = False

                if survey_file_reg.notes is False:
                    survey_file_reg.state = 'validated'
                else:
                    survey_file_reg.state = 'draft'

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
