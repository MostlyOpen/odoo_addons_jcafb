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
import datetime

_logger = logging.getLogger(__name__)


class LabTestParasitoSWABImportWizard(models.TransientModel):
    _name = 'myo.lab_test.parasito_swab.import.wizard'

    file_path = fields.Char(
        'File Path',
        required=True,
        help="File Path",
        default='/opt/openerp/mostlyopen_clvhealth_jcafb/lab_test/input/2-TABELA PARASITOLOGIA  2017.xls'
    )

    @api.multi
    def do_lab_test_parasito_swab_import(self):
        self.ensure_one()

        print '>>>>>', self.file_path

        lab_test_parasito_swab_model = self.env['myo.lab_test.parasito_swab']
        lab_test_person_model = self.env['myo.lab_test.person']
        lab_test_request_model = self.env['myo.lab_test.request']

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

            CODIGO_EXAME_PARASITO2017 = sheet.cell_value(i, name_cols[u'CODIGO_EXAME_PARASITO2017'])
            Farmaceutico_Responsavel_2017 = sheet.cell_value(i, name_cols[u'Farmacêutico(a) Responsável:2017'])
            DATA_DO_Parasito2017 = False
            date = sheet.cell_value(i, name_cols[u'DATA DO Parasito2017'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                DATA_DO_Parasito2017 = date

            Resultado_Parasito2017 = sheet.cell_value(i, name_cols[u'Resultado Parasito2017'])
            METODOS_Parasito2017 = sheet.cell_value(i, name_cols[u'MÉTODO(S) Parasito2017'])
            Entrada_Parasito2017 = False
            date = sheet.cell_value(i, name_cols[u'Entrada Parasito2017'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                Entrada_Parasito2017 = date
            Saida_Parasito2017 = False
            date = sheet.cell_value(i, name_cols[u'Saída Parasito2017'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                Saida_Parasito2017 = date
            Laudo_so_parasito2017 = False
            date = sheet.cell_value(i, name_cols[u'Laudo só parasito2017:'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                Laudo_so_parasito2017 = date
            ResultadoPARAASITO2017 = sheet.cell_value(i, name_cols[u'ResultadoPARAASITO2017:'])
            Resultado_liberado_1a = sheet.cell_value(i, name_cols[u'Resultado liberado 1a'])
            Resultado_liberado_1b = sheet.cell_value(i, name_cols[u'Resultado liberado 1b'])
            Resultado_liberado_1c = sheet.cell_value(i, name_cols[u'Resultado liberado 1c'])
            Resultado_liberado_1d = sheet.cell_value(i, name_cols[u'Resultado liberado 1d'])
            Resultado_liberado_1e = sheet.cell_value(i, name_cols[u'Resultado liberado 1e'])
            Resultado_liberado_1f = sheet.cell_value(i, name_cols[u'Resultado liberado 1f'])
            Resultado_liberado_2a = sheet.cell_value(i, name_cols[u'Resultado liberado 2a'])
            Resultado_liberado_2b = sheet.cell_value(i, name_cols[u'Resultado liberado 2b'])
            Resultado_liberado_2c = sheet.cell_value(i, name_cols[u'Resultado liberado 2c'])
            Resultado_liberado_2d = sheet.cell_value(i, name_cols[u'Resultado liberado 2d'])
            Resultado_liberado_2e = sheet.cell_value(i, name_cols[u'Resultado liberado 2e'])
            Resultado_liberado_2f = sheet.cell_value(i, name_cols[u'Resultado liberado 2f'])
            obs_interno_parasito_2017 = sheet.cell_value(i, name_cols[u'obs interno parasito 2017'])
            Laudo_parasito_swab2017 = False
            date = sheet.cell_value(i, name_cols[u'Laudo parasito+swab2017:'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                Laudo_parasito_swab2017 = date
            REALIZADOS2017 = sheet.cell_value(i, name_cols[u'REALIZADOS2017'])
            SE_AMBOS2017 = sheet.cell_value(i, name_cols[u'SE AMBOS2017'])
            Resultado_Parasito_Ritchie2017 = sheet.cell_value(i, name_cols[u'Resultado Parasito Ritchie2017'])
            Examinador_Ritchie2017 = sheet.cell_value(i, name_cols[u'Examinador Ritchie2017'])
            Resultado_Parasito_Hoffmann2017 = sheet.cell_value(i, name_cols[u'Resultado Parasito Hoffmann2017'])
            Examinador_Hoffmann2017 = sheet.cell_value(i, name_cols[u'Examinador Hoffmann2017'])
            STATUS_PARASITO = sheet.cell_value(i, name_cols[u'STATUS PARASITO'])

            CODIGO_EXAME_SWAB2017 = sheet.cell_value(i, name_cols[u'CODIGO_EXAME_SWAB2017'])
            DATA_DO_Swab2017 = False
            date = sheet.cell_value(i, name_cols[u'DATA DO Swab2017'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                DATA_DO_Swab2017 = date

            Entrada_Swab2017 = False
            date = sheet.cell_value(i, name_cols[u'Entrada Swab2017'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                Entrada_Swab2017 = date
            Saida_Swab2017 = False
            date = sheet.cell_value(i, name_cols[u'Saída Swab2017'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                Saida_Swab2017 = date
            METODO_Swab2017 = sheet.cell_value(i, name_cols[u'MÉTODO Swab2017'])
            Resultado_swab2017 = sheet.cell_value(i, name_cols[u'Resultado swab2017'])
            Laudo_so_swab2017 = False
            date = sheet.cell_value(i, name_cols[u'Laudo só swab2017:'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                Laudo_so_swab2017 = date
            Examinador_Swab2017 = sheet.cell_value(i, name_cols[u'Examinador Swab2017'])
            STATUS_SWAB = sheet.cell_value(i, name_cols[u'STATUS SWAB'])

            # # print '>>>>>>>>>>', i, CODIGO_Access_PESSOAS

            try:
                access_id = int(CODIGO_Access_PESSOAS)
            except:
                access_id = False

            lab_test_parasito_swab_search = lab_test_parasito_swab_model.search([
                ('access_id', '=', access_id),
            ])
            if lab_test_parasito_swab_search.id is not False:

                lab_test_parasito_swab = lab_test_parasito_swab_search

                lab_test_parasito_swab_search.request_code_swab = CODIGO_EXAME_SWAB2017
                lab_test_parasito_swab_search.request_id_swab = False
                lab_test_parasito_swab_search.date_swab = DATA_DO_Swab2017
                lab_test_parasito_swab_search.entrada_swab = Entrada_Swab2017
                lab_test_parasito_swab_search.saida_swab = Saida_Swab2017
                lab_test_parasito_swab_search.metodo_swab = METODO_Swab2017
                lab_test_parasito_swab_search.result_swab = Resultado_swab2017
                lab_test_parasito_swab_search.laudo_so_swab = Laudo_so_swab2017
                lab_test_parasito_swab_search.examinador_swab = Examinador_Swab2017
                lab_test_parasito_swab_search.status_swab = STATUS_SWAB

                lab_test_parasito_swab_search.request_code_parasito = CODIGO_EXAME_PARASITO2017
                lab_test_parasito_swab_search.request_id_parasito = False
                lab_test_parasito_swab_search.date_parasito = DATA_DO_Parasito2017
                lab_test_parasito_swab_search.resultado_parasito = Resultado_Parasito2017
                lab_test_parasito_swab_search.metodos_parasito = METODOS_Parasito2017
                lab_test_parasito_swab_search.entrada_parasito = Entrada_Parasito2017
                lab_test_parasito_swab_search.saida_parasito = Saida_Parasito2017
                lab_test_parasito_swab_search.laudo_so_parasito = Laudo_so_parasito2017
                lab_test_parasito_swab_search.resultado_parasito_2 = ResultadoPARAASITO2017
                lab_test_parasito_swab_search.result_liberado_1a = Resultado_liberado_1a
                lab_test_parasito_swab_search.result_liberado_1b = Resultado_liberado_1b
                lab_test_parasito_swab_search.result_liberado_1c = Resultado_liberado_1c
                lab_test_parasito_swab_search.result_liberado_1d = Resultado_liberado_1d
                lab_test_parasito_swab_search.result_liberado_1e = Resultado_liberado_1e
                lab_test_parasito_swab_search.result_liberado_1f = Resultado_liberado_1f
                lab_test_parasito_swab_search.result_liberado_2a = Resultado_liberado_2a
                lab_test_parasito_swab_search.result_liberado_2b = Resultado_liberado_2b
                lab_test_parasito_swab_search.result_liberado_2c = Resultado_liberado_2c
                lab_test_parasito_swab_search.result_liberado_2d = Resultado_liberado_2d
                lab_test_parasito_swab_search.result_liberado_2e = Resultado_liberado_2e
                lab_test_parasito_swab_search.result_liberado_2f = Resultado_liberado_2f
                lab_test_parasito_swab_search.obs_interno_parasito = obs_interno_parasito_2017
                lab_test_parasito_swab_search.laudo_parasito_swab = Laudo_parasito_swab2017
                lab_test_parasito_swab_search.realizados = REALIZADOS2017
                lab_test_parasito_swab_search.se_ambos = SE_AMBOS2017
                lab_test_parasito_swab_search.result_parasito_ritchie = Resultado_Parasito_Ritchie2017
                lab_test_parasito_swab_search.examinador_ritchie = Examinador_Ritchie2017
                lab_test_parasito_swab_search.result_parasito_hoffmann = Resultado_Parasito_Hoffmann2017
                lab_test_parasito_swab_search.examinador_hoffmann = Examinador_Hoffmann2017
                lab_test_parasito_swab_search.status_parasito = STATUS_PARASITO

                lab_test_parasito_swab_search.farmaceutico_respons = Farmaceutico_Responsavel_2017

            else:

                values = {
                    'access_id': access_id,

                    'request_code_swab': CODIGO_EXAME_SWAB2017,
                    'date_swab': DATA_DO_Swab2017,
                    'entrada_swab': Entrada_Swab2017,
                    'saida_swab': Saida_Swab2017,
                    'metodo_swab': METODO_Swab2017,
                    'result_swab': Resultado_swab2017,
                    'laudo_so_swab': Laudo_so_swab2017,
                    'examinador_swab': Examinador_Swab2017,
                    'status_swab': STATUS_SWAB,

                    'request_code_parasito': CODIGO_EXAME_PARASITO2017,
                    'date_parasito': DATA_DO_Parasito2017,
                    'resultado_parasito': Resultado_Parasito2017,
                    'metodos_parasito': METODOS_Parasito2017,
                    'entrada_parasito': Entrada_Parasito2017,
                    'saida_parasito': Saida_Parasito2017,
                    'laudo_so_parasito': Laudo_so_parasito2017,
                    'resultado_parasito_2': ResultadoPARAASITO2017,
                    'result_liberado_1a': Resultado_liberado_1a,
                    'result_liberado_1b': Resultado_liberado_1b,
                    'result_liberado_1c': Resultado_liberado_1c,
                    'result_liberado_1d': Resultado_liberado_1d,
                    'result_liberado_1e': Resultado_liberado_1e,
                    'result_liberado_1f': Resultado_liberado_1f,
                    'result_liberado_2a': Resultado_liberado_2a,
                    'result_liberado_2b': Resultado_liberado_2b,
                    'result_liberado_2c': Resultado_liberado_2c,
                    'result_liberado_2d': Resultado_liberado_2d,
                    'result_liberado_2e': Resultado_liberado_2e,
                    'result_liberado_2f': Resultado_liberado_2f,
                    'obs_interno_parasito': obs_interno_parasito_2017,
                    'laudo_parasito_swab': Laudo_parasito_swab2017,
                    'realizados': REALIZADOS2017,
                    'se_ambos': SE_AMBOS2017,
                    'result_parasito_ritchie': Resultado_Parasito_Ritchie2017,
                    'examinador_ritchie': Examinador_Ritchie2017,
                    'result_parasito_hoffmann': Resultado_Parasito_Hoffmann2017,
                    'examinador_hoffmann': Examinador_Hoffmann2017,
                    'status_parasito': STATUS_PARASITO,

                    'farmaceutico_respons': Farmaceutico_Responsavel_2017,
                }
                lab_test_parasito_swab = lab_test_parasito_swab_model.create(values)

            lab_test_person_search = lab_test_person_model.search([
                ('access_id', '=', access_id),
            ])
            if lab_test_person_search.id is not False:
                lab_test_parasito_swab.lab_test_person_id = lab_test_person_search.id

            lab_test_request_search = lab_test_request_model.search([
                ('name', '=', CODIGO_EXAME_SWAB2017),
            ])
            if lab_test_request_search.id is not False:
                lab_test_parasito_swab.request_id_swab = lab_test_request_search.id

            lab_test_request_search = lab_test_request_model.search([
                ('name', '=', CODIGO_EXAME_PARASITO2017),
            ])
            if lab_test_request_search.id is not False:
                lab_test_parasito_swab.request_id_parasito = lab_test_request_search.id

        return True
