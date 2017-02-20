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


class LabTestUrinamportWizard(models.TransientModel):
    _name = 'myo.lab_test.urina.import.wizard'

    file_path = fields.Char(
        'File Path',
        required=True,
        help="File Path",
        default='/opt/openerp/mostlyopen_clvhealth_jcafb/lab_test/input/3-TABELA URINA TIPO I 2017.xls'
    )

    @api.multi
    def do_lab_test_urina_import(self):
        self.ensure_one()

        print '>>>>>', self.file_path

        lab_test_urina_model = self.env['myo.lab_test.urina']
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

            Cod_Bco_Carlos2017 = sheet.cell_value(i, name_cols[u'Cod_Bco_Carlos2017'])
            Farmaceutico_Responsavel2017 = sheet.cell_value(i, name_cols[u'Farmacêutico(a) Responsável2017:'])
            DataExame2017 = False
            date = sheet.cell_value(i, name_cols[u'DataExame2017'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                DataExame2017 = date

            Vol2017 = sheet.cell_value(i, name_cols[u'Vol2017'])
            Den2017 = sheet.cell_value(i, name_cols[u'Den2017'])
            Aspecto2017 = sheet.cell_value(i, name_cols[u'Aspecto2017'])
            Cor2017 = sheet.cell_value(i, name_cols[u'Cor2017'])
            Odor2017 = sheet.cell_value(i, name_cols[u'Odor2017'])
            pH2017 = sheet.cell_value(i, name_cols[u'pH2017'])
            Prot2017 = sheet.cell_value(i, name_cols[u'Prot2017'])
            Glc2017 = sheet.cell_value(i, name_cols[u'Glc2017'])
            Cet2017 = sheet.cell_value(i, name_cols[u'Cet2017'])
            Bili2017 = sheet.cell_value(i, name_cols[u'Bili2017'])
            Sg2017 = sheet.cell_value(i, name_cols[u'Sg2017'])
            Uro2017 = sheet.cell_value(i, name_cols[u'Uro2017'])
            Nitrito2017 = sheet.cell_value(i, name_cols[u'Nitrito2017'])
            Cels2017 = sheet.cell_value(i, name_cols[u'Cels2017'])
            Muco2017 = sheet.cell_value(i, name_cols[u'Muco2017'])
            Cristais2017 = sheet.cell_value(i, name_cols[u'Cristais2017'])
            Leuco2017 = sheet.cell_value(i, name_cols[u'Leuco2017'])
            Hmcs2017 = sheet.cell_value(i, name_cols[u'Hmcs2017'])
            Cilindros2017 = sheet.cell_value(i, name_cols[u'Cilindros2017'])
            Hialinos2017 = sheet.cell_value(i, name_cols[u'Hialinos2017'])
            Granulosos2017 = sheet.cell_value(i, name_cols[u'Granulosos2017'])
            Leucocitarios2017 = sheet.cell_value(i, name_cols[u'Leucocitarios2017'])
            Hematicos2017 = sheet.cell_value(i, name_cols[u'Hematicos2017'])
            Cereos2017 = sheet.cell_value(i, name_cols[u'Cereos2017'])
            Outros2017 = sheet.cell_value(i, name_cols[u'Outros2017'])
            Obs2017 = sheet.cell_value(i, name_cols[u'Obs2017'])
            Obs_int2017 = sheet.cell_value(i, name_cols[u'Obs_int2017'])
            Laudo_emitido_em2017 = False
            date = sheet.cell_value(i, name_cols[u'Laudo_emitido_em2017'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                Laudo_emitido_em2017 = date
            Examinador2017 = sheet.cell_value(i, name_cols[u'Examinador2017'])
            STATUS_URINA = sheet.cell_value(i, name_cols[u'STATUS URINA'])

            # # print '>>>>>>>>>>', i, CODIGO_Access_PESSOAS

            try:
                access_id = int(CODIGO_Access_PESSOAS)
            except:
                access_id = False

            lab_test_urina_search = lab_test_urina_model.search([
                ('access_id', '=', access_id),
            ])
            if lab_test_urina_search.id is not False:

                lab_test_urina = lab_test_urina_search

                lab_test_urina_search.request_code_urina = Cod_Bco_Carlos2017

                lab_test_urina_search.request_id_urina = False
                lab_test_urina_search.farmaceutico_resp = Farmaceutico_Responsavel2017
                lab_test_urina_search.date_urina = DataExame2017

                lab_test_urina_search.volume = Vol2017
                lab_test_urina_search.densidade = Den2017
                lab_test_urina_search.aspecto = Aspecto2017
                lab_test_urina_search.cor = Cor2017
                lab_test_urina_search.odor = Odor2017
                lab_test_urina_search.ph = pH2017
                lab_test_urina_search.proteinas = Prot2017
                lab_test_urina_search.glicose = Glc2017
                lab_test_urina_search.cetona = Cet2017
                lab_test_urina_search.pig_biliares = Bili2017
                lab_test_urina_search.sangue = Sg2017
                lab_test_urina_search.urobilinogenio = Uro2017
                lab_test_urina_search.nitrito = Nitrito2017
                lab_test_urina_search.cels_epit = Cels2017
                lab_test_urina_search.muco = Muco2017
                lab_test_urina_search.cristais = Cristais2017
                lab_test_urina_search.leucocitos = Leuco2017
                lab_test_urina_search.hemacias = Hmcs2017
                lab_test_urina_search.cilindros = Cilindros2017
                lab_test_urina_search.hialinos = Hialinos2017
                lab_test_urina_search.ganulosos = Granulosos2017
                lab_test_urina_search.leucocitarios = Leucocitarios2017
                lab_test_urina_search.hematicos = Hematicos2017
                lab_test_urina_search.cereos = Cereos2017
                lab_test_urina_search.outros_tipos = Outros2017
                lab_test_urina_search.obs = Obs2017
                lab_test_urina_search.obs_int = Obs_int2017
                lab_test_urina_search.date_laudo = Laudo_emitido_em2017
                lab_test_urina_search.examinador = Examinador2017
                lab_test_urina_search.status_urina = STATUS_URINA

            else:

                values = {
                    'access_id': access_id,

                    'request_code_urina': Cod_Bco_Carlos2017,
                    'farmaceutico_resp': Farmaceutico_Responsavel2017,
                    'date_urina': DataExame2017,

                    'volume': Vol2017,
                    'densidade': Den2017,
                    'aspecto': Aspecto2017,
                    'cor': Cor2017,
                    'odor': Odor2017,
                    'ph': pH2017,
                    'proteinas': Prot2017,
                    'glicose': Glc2017,
                    'cetona': Cet2017,
                    'pig_biliares': Bili2017,
                    # 'sangue': DataExame2017,
                    'sangue': Sg2017,
                    # 'date_urina': Sg2017,
                    'urobilinogenio': Uro2017,
                    'nitrito': Nitrito2017,
                    'cels_epit': Cels2017,
                    'muco': Muco2017,
                    'cristais': Cristais2017,
                    'leucocitos': Leuco2017,
                    'hemacias': Hmcs2017,
                    'cilindros': Cilindros2017,
                    'hialinos': Hialinos2017,
                    'ganulosos': Granulosos2017,
                    'leucocitarios': Leucocitarios2017,
                    'hematicos': Hematicos2017,
                    'cereos': Cereos2017,
                    'outros_tipos': Outros2017,
                    'obs': Obs2017,
                    'obs_int': Obs_int2017,
                    'date_laudo': Laudo_emitido_em2017,
                    'examinador': Examinador2017,
                    'status_urina': STATUS_URINA,
                }
                lab_test_urina = lab_test_urina_model.create(values)

            lab_test_person_search = lab_test_person_model.search([
                ('access_id', '=', access_id),
            ])
            if lab_test_person_search.id is not False:
                lab_test_urina.lab_test_person_id = lab_test_person_search.id

            lab_test_request_search = lab_test_request_model.search([
                ('name', '=', Cod_Bco_Carlos2017),
            ])
            if lab_test_request_search.id is not False:
                lab_test_urina.request_id_urina = lab_test_request_search.id

        return True
