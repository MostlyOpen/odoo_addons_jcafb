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


class LabTestPersonImportWizard(models.TransientModel):
    _name = 'myo.lab_test.person.import.wizard'

    # def _default_lab_test_person_ids(self):
    #     return self._context.get('active_ids')
    # lab_test_person_ids = fields.Many2many(
    #     'myo.lab_test.person',
    #     string='Lab Test Persons',
    #     default=_default_lab_test_person_ids)

    file_path = fields.Char(
        'File Path',
        required=True,
        help="File Path",
        default='/opt/openerp/mostlyopen_clvhealth_jcafb/lab_test/input/1a-TABELA PESSOAS (COMPLETA).xls'
    )

    @api.multi
    def do_lab_test_person_import(self):
        self.ensure_one()

        print '>>>>>', self.file_path

        lab_test_person_model = self.env['myo.lab_test.person']
        person_model = self.env['myo.person']

        book = xlrd.open_workbook(self.file_path)
        sheet = book.sheet_by_index(0)

        for i in range(sheet.nrows):

            if i == 0:

                name_cols = {}
                for k in range(sheet.ncols):
                    name_col = sheet.cell_value(i, k)
                    if name_col != xlrd.empty_cell.value:
                        name_cols.update({name_col: k})

                print '>>>>>', name_cols

                continue

            CODIGO_Access_PESSOAS = sheet.cell_value(i, name_cols['CODIGO_Access_PESSOAS'])
            Nome = sheet.cell_value(i, name_cols['Nome'])
            CodigoPessoa = sheet.cell_value(i, name_cols['CodigoPessoa'])

            # Parasito_recebido_por = sheet.cell_value(i, name_cols['Parasito recebido por'])

            print '>>>>>>>>>>', i, CODIGO_Access_PESSOAS, Nome, CodigoPessoa

            access_id = int(CODIGO_Access_PESSOAS)

            lab_test_person_search = lab_test_person_model.search([
                ('access_id', '=', access_id),
            ])
            if lab_test_person_search.id is not False:

                lab_test_person = lab_test_person_search

                lab_test_person_search.name = Nome
                lab_test_person_search.code = CodigoPessoa
                lab_test_person_search.person_id = False

            else:
                values = {
                    'access_id': access_id,
                    'name': Nome,
                    'code': CodigoPessoa,
                }
                lab_test_person = lab_test_person_model.create(values)

            person_search = person_model.search([
                ('code', '=', CodigoPessoa),
            ])
            if person_search.id is not False:
                lab_test_person.person_id = person_search.id

        return True
