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

# import logging

# _logger = logging.getLogger(__name__)

import os
import datetime
import xlrd


def modification_date(filepath):
    t = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(t)


def ir_model_data_get_instance(ir_model_data, code):

    code = code.replace('[', '')
    code = code.replace(']', '')
    ir_model_data_browse = ir_model_data.browse([('name', '=', code), ])

    if ir_model_data_browse.name != []:
        instance = ir_model_data_browse.name[0], ir_model_data_browse.model[0], ir_model_data_browse.res_id[0]
        return instance
    else:
        instance = False, False, False
        return instance


class SurveyFileRefreshWizard(models.TransientModel):
    _name = 'myo.survey.file.refresh.wizard'

    dir_path = fields.Char(
        'Directory Path',
        required=True,
        help="Directory Path",
        default='/opt/openerp/mostlyopen_clvhealth_jcafb/survey_files/input'
    )

    @api.multi
    def do_survey_file_refresh(self):
        self.ensure_one()

        ir_model_data = self.env['ir.model.data']
        survey_file_model = self.env['myo.survey.file']
        survey_model = self.env['survey.survey']
        survey_question = self.env['survey.question']
        survey_label = self.env['survey.label']

        listdir = os.listdir(self.dir_path)
        for file in listdir:
            print '>>>>>', file

            filepath = self.dir_path + '/' + file

            book = xlrd.open_workbook(filepath)
            sheet = book.sheet_by_index(0)
            survey_title = sheet.cell_value(0, 0)
            # print '>>>>>>>>>>', '"' + survey_title + '"'

            survey_browse = survey_model.search([
                ('title', '=', survey_title),
            ])

            survey_file_search = survey_file_model.search([
                ('name', '=', file),
            ])
            if survey_file_search.id is False:

                values = {
                    'name': file,
                    'survey_title': survey_title,
                    'date_survey_file': modification_date(filepath),
                }
                new_survey_file = survey_file_model.create(values)

                survey_file = new_survey_file

                if survey_browse.id is not False:
                    survey_file.survey_id = survey_browse.id

            else:

                survey_file = survey_file_search

                survey_file.date_survey_file = modification_date(filepath)
                survey_file.survey_title = survey_title

                if survey_browse.id is not False:
                    survey_file.survey_id = survey_browse.id

            for i in range(sheet.nrows):

                # row = sheet.row_values(i)
                code_row = sheet.cell_value(i, 0)

                if code_row == '[]':
                    code_cols = {}
                    for k in range(sheet.ncols):
                        code_col = sheet.cell_value(i, k)
                        if code_col != xlrd.empty_cell.value:
                            code_cols.update({k: code_col})

                for j in range(sheet.ncols):

                    if sheet.cell_value(i, j) != xlrd.empty_cell.value:

                        # if sheet.cell_value(i, j) == 'free_text':
                        #     question_type = 'free_text'
                        # if sheet.cell_value(i, j) == 'textbox':
                        #     question_type = 'textbox'
                        # if sheet.cell_value(i, j) == 'datetime':
                        #     question_type = 'datetime'
                        # if sheet.cell_value(i, j) == 'simple_choice':
                        #     question_type = 'simple_choice'
                        # if sheet.cell_value(i, j) == 'multiple_choice':
                        #     question_type = 'multiple_choice'
                        # if sheet.cell_value(i, j) == 'matrix_simple':
                        #     question_type = 'matrix_simple'

                        if sheet.cell_value(i, j) == '.':
                            try:
                                value = sheet.cell_value(i, j + 1)
                            except:
                                value = xlrd.empty_cell.value
                            if value != xlrd.empty_cell.value:
                                print '>>>>>>>>>> (', i, j + 1, ')', value, code_row

                                if survey_title == '[QAN17]' and code_row == '[QAN17_01_01]' or \
                                   survey_title == '[QDH17]' and code_row == '[QDH17_01_01]' or \
                                   survey_title == '[QMD17]' and code_row == '[QMD17_01_01]' or \
                                   survey_title == '[QSC17]' and code_row == '[QSC17_01_01]' or \
                                   survey_title == '[QSF17]' and code_row == '[QSF17_01_01]' or \
                                   survey_title == '[QSI17]' and code_row == '[QSI17_01_01]' or \
                                   survey_title == '[TCP17]' and code_row == '[TCP17_01_01]' or \
                                   survey_title == '[TCR17]' and code_row == '[TCR17_01_01]' or \
                                   survey_title == '[TID17]' and code_row == '[TID17_01_01]':
                                    document_code = value

                                # if question_type == 'textbox':
                                #     # print '>>>>>>>>>>>>>>>', code_row
                                #     instance_row = ir_model_data_get_instance(ir_model_data, code_row)
                                #     # print('------>', instance_row)
                                #     if instance_row[1] == 'survey.question':
                                #         survey_question_browse = survey_question.browse([
                                #             ('id', '=', instance_row[2]),
                                #         ])

                                #         print('------>(textbox)', survey_question_browse[0].question.encode('utf-8'))

                                # if question_type == 'simple_choice':
                                #     # print '>>>>>>>>>>>>>>>', code_row
                                #     instance_row = ir_model_data_get_instance(ir_model_data, code_row)
                                #     # print('------>', instance_row)
                                #     if instance_row[1] == 'survey.question':
                                #         survey_question_browse = survey_question.browse([
                                #             ('id', '=', instance_row[2]),
                                #         ])

                                #         print(
                                #             '------>(simple_choice_question)',
                                #             survey_question_browse[0].question.encode('utf-8')
                                #         )
                                #         print(
                                #             '------>(simple_choice_comment)',
                                #             survey_question_browse[0].comments_message.encode('utf-8')
                                #         )
                                #     if instance_row[1] == 'survey.label':
                                #         survey_label_browse = survey_label.browse([
                                #             ('id', '=', instance_row[2]),
                                #         ])

                                #         print(
                                #             '------>(simple_choice_question)',
                                #             survey_label_browse[0].question_id.question.encode('utf-8')
                                #         )
                                #         print(
                                #             '------>(simple_choice_answer)',
                                #             survey_label_browse[0].value.encode('utf-8')
                                #         )

                                # if question_type == 'multiple_choice':
                                #     # print '>>>>>>>>>>>>>>>', code_row
                                #     instance_row = ir_model_data_get_instance(ir_model_data, code_row)
                                #     # print('------>', instance_row)
                                #     if instance_row[1] == 'survey.question':
                                #         survey_question_browse = survey_question.browse([
                                #             ('id', '=', instance_row[2]),
                                #         ])

                                #         print(
                                #             '------>((multiple_choice_question)',
                                #             survey_question_browse[0].question.encode('utf-8')
                                #         )
                                #         print(
                                #             '------>((multiple_choice_comment)',
                                #             survey_question_browse[0].comments_message.encode('utf-8')
                                #         )
                                #     if instance_row[1] == 'survey.label':
                                #         survey_label_browse = survey_label.browse([
                                #             ('id', '=', instance_row[2]),
                                #         ])

                                #         print(
                                #             '------>(simple_choice_question)',
                                #             survey_label_browse[0].question_id.question.encode('utf-8')
                                #         )
                                #         print(
                                #             '------>(simple_choice_answer)',
                                #             survey_label_browse[0].value.encode('utf-8')
                                #         )

                                # if question_type == 'matrix_simple':
                                #     code_col = code_cols[j]
                                #     # print '>>>>>>>>>>>>>>>', code_row, code_col
                                #     instance_row = ir_model_data_get_instance(ir_model_data, code_row)
                                #     # print('------>', instance_row)
                                #     instance_col = ir_model_data_get_instance(ir_model_data, code_col)
                                #     # print('------>', instance_col)
                                #     if instance_row[1] == 'survey.label':
                                #         survey_label_browse = survey_label.browse([
                                #             ('id', '=', instance_row[2]),
                                #         ])

                                #         print(
                                #             '------>(matrix_simple_row)',
                                #             survey_label_browse[0].value.encode('utf-8')
                                #         )
                                #     if instance_col[1] == 'survey.label':
                                #         survey_label_browse = survey_label.browse([
                                #             ('id', '=', instance_col[2]),
                                #         ])

                                #         print(
                                #             '------>(matrix_simple_col)',
                                #             survey_label_browse[0].value.encode('utf-8')
                                #         )

                            survey_file.document_code = document_code

        return True
