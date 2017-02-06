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
import shutil
import xlrd
import xlutils.copy

_logger = logging.getLogger(__name__)


def _get_sheet(wb, name):
    """Return the worksheet called `name`
    """
    try:
        idx = wb._Workbook__worksheet_idx_from_name[name.lower()]
        return wb._Workbook__worksheets[idx]
    except KeyError:
        print "sheet name %s not found" % repr(name)


def _getOutCell(outSheet, rowIndex, colIndex):
    """ HACK: Extract the internal xlwt cell representation.
    """
    row = outSheet._Worksheet__rows.get(rowIndex)
    if not row:
        return None

    cell = row._Row__cells.get(colIndex)
    return cell


class DocumentCreateXlsTID17Wizard(models.TransientModel):
    _name = 'myo.document.create_xls_tid17.wizard'

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

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        'myo.document',
        string='Survey Files',
        default=_default_document_ids)

    dir_path = fields.Char(
        'Directory Path',
        required=True,
        help="Directory Path",
        default='/opt/openerp/mostlyopen_clvhealth_jcafb/survey_files/input'
    )
    reference_file_path = fields.Char(
        'Reference File Path',
        required=True,
        help="Arquive Directory Path",
        default='/opt/openerp/mostlyopen_clvhealth_jcafb/data/TID17/survey_jcafb_TID17.xls'
    )

    @api.multi
    def do_document_create_xls_tid17(self):
        self.ensure_one()

        person_model = self.env['myo.person']

        for document_reg in self.document_ids:

            if document_reg.survey_id.title == '[TID17]' and document_reg.state == 'draft':

                for document_person in document_reg.person_ids:

                    person_search = person_model.search([
                        ('code', '=', document_person.person_id.code),
                    ])

                    for document_person_2 in person_search.document_person_ids:

                        if document_person_2.document_id.survey_id.title == '[QAN17]' and \
                           document_person_2.document_id.state == 'done':

                            filepath = self.dir_path + '/TID17_' + document_person.document_id.code + '.xls'

                            print '>>>>>', filepath

                            shutil.copyfile(self.reference_file_path, filepath)

                            book = xlrd.open_workbook(filepath, formatting_info=True)
                            book = xlutils.copy.copy(book)
                            sheet = _get_sheet(book, 'TID17')

                            previousCell = _getOutCell(sheet, 10, 5)
                            sheet.write(10, 5, document_person.document_id.code)
                            newCell = _getOutCell(sheet, 10, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            QAN17_01_02 = self.get_value(
                                'QAN17_01_02',
                                document_person_2.document_id.survey_user_input_id)
                            previousCell = _getOutCell(sheet, 15, 5)
                            # sheet.write(15, 5, survey_user_input_line_search.value_text)
                            sheet.write(15, 5, str(QAN17_01_02))
                            newCell = _getOutCell(sheet, 15, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            previousCell = _getOutCell(sheet, 20, 5)
                            sheet.write(20, 5, '910.014-80')
                            newCell = _getOutCell(sheet, 20, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            previousCell = _getOutCell(sheet, 25, 5)
                            sheet.write(25, 5, 'n/d')
                            newCell = _getOutCell(sheet, 25, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            previousCell = _getOutCell(sheet, 33, 5)
                            sheet.write(33, 5, document_person_2.person_id.name)
                            newCell = _getOutCell(sheet, 33, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            previousCell = _getOutCell(sheet, 38, 5)
                            sheet.write(38, 5, document_person_2.person_id.code)
                            newCell = _getOutCell(sheet, 38, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            QAN17_02_06 = self.get_value('QAN17_02_06', document_reg.survey_user_input_id)
                            if QAN17_02_06 == 'b) Paciente':
                                row = 53
                            else:
                                row = 54
                            previousCell = _getOutCell(sheet, row, 5)
                            sheet.write(row, 5, 'X')
                            newCell = _getOutCell(sheet, row, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            previousCell = _getOutCell(sheet, 63, 5)
                            sheet.write(63, 5, 'X')
                            newCell = _getOutCell(sheet, 63, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            previousCell = _getOutCell(sheet, 69, 5)
                            sheet.write(69, 5, 'X')
                            newCell = _getOutCell(sheet, 69, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            previousCell = _getOutCell(sheet, 75, 5)
                            sheet.write(75, 5, 'X')
                            newCell = _getOutCell(sheet, 75, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            previousCell = _getOutCell(sheet, 80, 5)
                            sheet.write(80, 5, 'X')
                            newCell = _getOutCell(sheet, 80, 5)
                            newCell.xf_idx = previousCell.xf_idx

                            book.save(filepath)

        return True
