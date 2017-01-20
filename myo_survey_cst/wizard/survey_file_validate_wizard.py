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

            # survey_model = self.env['survey.survey']
            survey_question_model = self.env['survey.question']
            # survey_label = self.env['survey.label']

            question_code = False
            question_question = False
            question_type = False
            question_matrix_subtype = False
            question_constr_mandatory = False

            response_count = 0

            last_row = sheet.nrows - 1
            last_question_code = False

            print '>>>>>', last_row
            for i in range(sheet.nrows):

                code_row = sheet.cell_value(i, 0)

                if code_row == '[]':
                    code_cols = {}
                    for k in range(sheet.ncols):
                        code_col = sheet.cell_value(i, k)
                        if code_col != xlrd.empty_cell.value:
                            code_cols.update({k: code_col})

                row_code = code_row.replace('[', '').replace(']', '')
                if len(row_code) < 11:
                    question_code = False
                    last_question_code = False
                else:
                    question_code = row_code[:11]
                    if question_code != last_question_code:
                        last_question_code = question_code
                print '>>>>>>>>>> (', i, ')', code_row, row_code, question_code, last_question_code

                # if i == last_row:
                #     print '>>>>>>>>>>'

                for j in range(sheet.ncols):
                    pass

                    # if sheet.cell_value(i, j) != xlrd.empty_cell.value:

                    #     # if sheet.cell_value(i, j) == 'free_text':
                    #     #     question_type = 'free_text'
                    #     # if sheet.cell_value(i, j) == 'textbox':
                    #     #     response_count = 0
                    #     #     question_code = code_row.replace('[', '').replace(']', '')
                    #     #     question_type = 'textbox'
                    #     #     survey_question_search = survey_question_model.search([
                    #     #         ('code', '=', question_code),
                    #     #     ])
                    #     #     if survey_question_search.id is not False:
                    #     #         question_question = survey_question_search.question
                    #     #         question_constr_mandatory = survey_question_search.constr_mandatory
                    #     # if sheet.cell_value(i, j) == 'datetime':
                    #     #     question_type = 'datetime'
                    #     # if sheet.cell_value(i, j) == 'simple_choice':
                    #     #     question_type = 'simple_choice'
                    #     # if sheet.cell_value(i, j) == 'multiple_choice':
                    #     #     question_type = 'multiple_choice'
                    #     # if sheet.cell_value(i, j) == 'matrix_simple':
                    #     #     question_type = 'matrix_simple'

                    #     # # if question_type is not False:
                    #     # #     print '>>>>>>>>>> (', i, j + 1, ')', question_question, question_type, question_constr_mandatory, code_row

                    #     # if sheet.cell_value(i, j) == '.':
                    #     #     try:
                    #     #         value = sheet.cell_value(i, j + 1)
                    #     #     except:
                    #     #         value = xlrd.empty_cell.value
                    #     #     if value != xlrd.empty_cell.value:
                    #     #         response_count += 1
                    #     #         # print '>>>>>>>>>> (', i, j + 1, ')', value, code_row
                    #     #     print '>>>>>>>>>>>>>>> (', i, j + 1, ')', value, code_row, response_count

                    #     question_type_list = [
                    #         'free_text',
                    #         'textbox',
                    #         'datetime',
                    #         'simple_choice',
                    #         'multiple_choice',
                    #         'matrix_simple',
                    #     ]
                    #     if sheet.cell_value(i, j) in question_type_list:
                    #         question_code = code_row.replace('[', '').replace(']', '')[:11]
                    #         survey_question_search = survey_question_model.search([
                    #             ('code', '=', question_code),
                    #         ])
                    #         if survey_question_search.id is not False:
                    #             question_question = survey_question_search.question
                    #             question_type = survey_question_search.type
                    #             question_constr_mandatory = survey_question_search.constr_mandatory
                    #             print '>>>>>>>>>>>>>>>', ' (', i, j + 1, ')', question_code
                    #             print '>>>>>>>>>>>>>>>>>>>>', question_question
                    #             print '>>>>>>>>>>>>>>>>>>>>', question_type, question_constr_mandatory
                    #             if question_type == 'matrix':
                    #                 question_matrix_subtype = survey_question_search.matrix_subtype
                    #                 print '>>>>>>>>>>>>>>>>>>>>', question_matrix_subtype


                    #     # if sheet.cell_value(i, j) == '.':
                    #     #     question_code = code_row.replace('[', '').replace(']', '')[:11]
                    #     #     survey_question_search = survey_question_model.search([
                    #     #         ('code', '=', question_code),
                    #     #     ])
                    #     #     if survey_question_search.id is not False:
                    #     #         question_question = survey_question_search.question
                    #     #         question_type = survey_question_search.type
                    #     #         question_constr_mandatory = survey_question_search.constr_mandatory
                    #     #     try:
                    #     #         value = sheet.cell_value(i, j + 1)
                    #     #         response_count += 1
                    #     #     except:
                    #     #         value = xlrd.empty_cell.value
                    #     #     print '>>>>>>>>>>>>>>>', ' (', i, j + 1, ')', question_code
                    #     #     print '>>>>>>>>>>>>>>>>>>>>', question_question
                    #     #     print '>>>>>>>>>>>>>>>>>>>>', question_type, question_constr_mandatory
                    #     #     print '>>>>>>>>>>>>>>>>>>>>', response_count, value

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
