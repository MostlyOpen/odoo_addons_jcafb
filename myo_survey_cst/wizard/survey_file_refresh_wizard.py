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

        # ir_model_data = self.env['ir.model.data']
        survey_file_model = self.env['myo.survey.file']
        survey_model = self.env['survey.survey']
        # survey_question = self.env['survey.question']
        # survey_label = self.env['survey.label']
        document_model = self.env['myo.document']

        listdir = os.listdir(self.dir_path)
        for file in listdir:
            print '>>>>>', file

            filepath = self.dir_path + '/' + file

            book = xlrd.open_workbook(filepath)
            sheet = book.sheet_by_index(0)
            survey_title = sheet.cell_value(0, 0)
            # print '>>>>>>>>>>', '"' + survey_title + '"'

            survey_file_search = survey_file_model.search([
                ('name', '=', file),
            ])
            if survey_file_search.id is False:
                values = {
                    'name': file,
                    'survey_title': survey_title,
                    'date_survey_file': modification_date(filepath),
                }
                survey_file = survey_file_model.create(values)
            else:
                survey_file = survey_file_search

                if survey_file.state != 'imported':
                    survey_file.date_survey_file = modification_date(filepath)
                    survey_file.survey_title = survey_title

            if survey_file.state != 'imported':
                document_code = False

                survey_file.notes = False
                survey_file.survey_id = False
                survey_file.document_code = False

                if survey_file.survey_title.replace('[', '').replace(']', '') != file[:5]:
                    survey_file.notes = 'Erro: Nome do arquivo inválido!'
                else:
                    survey_file.notes = False

                survey_browse = survey_model.search([
                    ('title', '=', survey_title),
                ])
                if survey_browse.id is not False:
                    survey_file.survey_id = survey_browse.id

                for i in range(sheet.nrows):

                    code_row = sheet.cell_value(i, 0)

                    if code_row == '[]':
                        code_cols = {}
                        for k in range(sheet.ncols):
                            code_col = sheet.cell_value(i, k)
                            if code_col != xlrd.empty_cell.value:
                                code_cols.update({k: code_col})

                    for j in range(sheet.ncols):

                        if sheet.cell_value(i, j) != xlrd.empty_cell.value:

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

                survey_file.document_code = document_code
                if survey_file.document_code is False:
                    if survey_file.notes is False:
                        survey_file.notes = 'Erro: Código do Documento inválido!'
                    else:
                        survey_file.notes += '\nErro: Código do Documento inválido!'
                else:
                    if survey_file.document_code != file[6:16]:
                        if survey_file.notes is False:
                            survey_file.notes = 'Erro: Nome do arquivo inválido!'
                        else:
                            survey_file.notes += '\nErro: Nome do arquivo inválido!'

                    document_search = document_model.search([
                        ('code', '=', survey_file.document_code),
                    ])
                    if document_search.id is False:
                        if survey_file.notes is False:
                            survey_file.notes = 'Erro: Código do Documento inválido!'
                        else:
                            survey_file.notes += '\nErro: Codigo do Documento invalido!'
                    else:
                        survey_file.document_id = document_search.id
                        survey_file.user_id = document_search.user_id.id

                        if survey_file.notes is False:
                            survey_file.document_id.state = 'waiting'

                if survey_file.notes is False:
                    survey_file.state = 'checked'
                else:
                    survey_file.state = 'draft'

        return True
