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


class LabTestAnemiaDHCImportWizard(models.TransientModel):
    _name = 'myo.lab_test.anemia_dhc.import.wizard'

    file_path = fields.Char(
        'File Path',
        required=True,
        help="File Path",
        default='/opt/openerp/mostlyopen_clvhealth_jcafb/lab_test/input/4-TABELA ANEMIA - DHC 2017.xls'
    )

    @api.multi
    def do_lab_test_anemia_dhc_import(self):
        self.ensure_one()

        print '>>>>>', self.file_path

        lab_test_anemia_dhc_model = self.env['myo.lab_test.anemia_dhc']
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

            Codigo_Exame2017 = sheet.cell_value(i, name_cols[u'Código Exame2017'])
            Farmaceutico_DHC2017 = sheet.cell_value(i, name_cols[u'Farmacêutico DHC2017'])
            Data_DHC2017 = False
            date = sheet.cell_value(i, name_cols[u'Data DHC2017'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                Data_DHC2017 = date
            Peso_DHC2017 = sheet.cell_value(i, name_cols[u'Peso DHC2017'])
            if Peso_DHC2017 == '---':
                Peso_DHC2017 = xlrd.empty_cell.value
            Altura_DHC2017 = sheet.cell_value(i, name_cols[u'Altura DHC2017'])
            if Altura_DHC2017 == '---':
                Altura_DHC2017 = xlrd.empty_cell.value
            Circ_Abd_DHC2017 = sheet.cell_value(i, name_cols[u'Circ Abd DHC2017'])
            if Circ_Abd_DHC2017 == '---':
                Circ_Abd_DHC2017 = xlrd.empty_cell.value
            Pressao_sistolica2017 = sheet.cell_value(i, name_cols[u'Pressão sistólica2017'])
            Pressao_diastolica2017 = sheet.cell_value(i, name_cols[u'Pressão diastólica2017'])
            Obs_pressao2017 = sheet.cell_value(i, name_cols[u'Obs pressão2017'])
            Result_glc2017 = sheet.cell_value(i, name_cols[u'Result glc2017'])
            Obs_glc2017 = sheet.cell_value(i, name_cols[u'Obs glc2017'])
            Valor_colest2017 = sheet.cell_value(i, name_cols[u'Valor colest2017'])
            if Valor_colest2017 == '---':
                Valor_colest2017 = xlrd.empty_cell.value
            Obs_colest2017 = sheet.cell_value(i, name_cols[u'Obs colest2017'])
            OBS_DHC2017 = sheet.cell_value(i, name_cols[u'OBS DHC2017'])

            Codigo_Ex_ANEMIA2017 = sheet.cell_value(i, name_cols[u'Código Ex ANEMIA2017'])
            Farmaceutico_ANEMIA2017 = sheet.cell_value(i, name_cols[u'Farmacêutico ANEMIA2017'])
            Data_Anemia2017 = False
            date = sheet.cell_value(i, name_cols[u'Data Anemia2017'])
            if date != xlrd.empty_cell.value and date != 0:
                # print '>>>>>>>>>>', date, xlrd.xldate_as_tuple(date, book.datemode)
                date = datetime.datetime(*xlrd.xldate_as_tuple(date, book.datemode)).strftime('%Y-%m-%d')
                Data_Anemia2017 = date
            PesoHb2017 = sheet.cell_value(i, name_cols[u'PesoHb2017'])
            if PesoHb2017 == '---':
                PesoHb2017 = xlrd.empty_cell.value
            AlturaHb2017 = sheet.cell_value(i, name_cols[u'AlturaHb2017'])
            if AlturaHb2017 == '---':
                AlturaHb2017 = xlrd.empty_cell.value
            Resultado_Hb2017 = sheet.cell_value(i, name_cols[u'Resultado Hb2017'])
            Obs_Hb2017 = sheet.cell_value(i, name_cols[u'Obs Hb2017'])
            Obs2_Hb2017 = sheet.cell_value(i, name_cols[u'Obs2 Hb2017'])

            # print '>>>>>>>>>>', i, CODIGO_Access_PESSOAS

            try:
                access_id = int(CODIGO_Access_PESSOAS)
            except:
                access_id = False

            lab_test_anemia_dhc_search = lab_test_anemia_dhc_model.search([
                ('access_id', '=', access_id),
            ])
            if lab_test_anemia_dhc_search.id is not False:

                lab_test_anemia_dhc = lab_test_anemia_dhc_search

                lab_test_anemia_dhc_search.request_code_anemia = Codigo_Ex_ANEMIA2017
                lab_test_anemia_dhc_search.request_id_anemia = False
                lab_test_anemia_dhc_search.farmaceutico_anemia = Farmaceutico_ANEMIA2017
                lab_test_anemia_dhc_search.date_anemia = Data_Anemia2017
                lab_test_anemia_dhc_search.peso_anemia = PesoHb2017
                lab_test_anemia_dhc_search.altura_anemia = AlturaHb2017
                lab_test_anemia_dhc_search.hemoglobina_anemia = Resultado_Hb2017
                lab_test_anemia_dhc_search.obs_anemia = Obs_Hb2017
                lab_test_anemia_dhc_search.obs2_anemia = Obs2_Hb2017

                lab_test_anemia_dhc_search.request_code_dhc = Codigo_Exame2017
                lab_test_anemia_dhc_search.request_id_dhc = False
                lab_test_anemia_dhc_search.farmaceutico_dhc = Farmaceutico_DHC2017
                lab_test_anemia_dhc_search.date_dhc = Data_DHC2017
                lab_test_anemia_dhc_search.peso_dhc = Peso_DHC2017
                lab_test_anemia_dhc_search.altura_dhc = Altura_DHC2017
                lab_test_anemia_dhc_search.circ_abdm_dhc = Circ_Abd_DHC2017
                lab_test_anemia_dhc_search.pressao_sist_dhc = Pressao_sistolica2017
                lab_test_anemia_dhc_search.pressao_diast_dhc = Pressao_diastolica2017
                lab_test_anemia_dhc_search.obs_pressao_dhc = Obs_pressao2017
                lab_test_anemia_dhc_search.glicemia_dhc = Result_glc2017
                lab_test_anemia_dhc_search.obs_glicemia_dhc = Obs_glc2017
                lab_test_anemia_dhc_search.colesterol_dhc = Valor_colest2017
                lab_test_anemia_dhc_search.obs_colesterol_dhc = Obs_colest2017
                lab_test_anemia_dhc_search.obs_dhc = OBS_DHC2017

            else:

                values = {
                    'access_id': access_id,

                    'request_code_anemia': Codigo_Ex_ANEMIA2017,
                    'farmaceutico_anemia': Farmaceutico_ANEMIA2017,
                    'date_anemia': Data_Anemia2017,
                    'peso_anemia': PesoHb2017,
                    'altura_anemia': AlturaHb2017,
                    'hemoglobina_anemia': Resultado_Hb2017,
                    'obs_anemia': Obs_Hb2017,
                    'obs2_anemia': Obs2_Hb2017,

                    'request_code_dhc': Codigo_Exame2017,
                    'farmaceutico_dhc': Farmaceutico_DHC2017,
                    'date_dhc': Data_DHC2017,
                    'peso_dhc': Peso_DHC2017,
                    'altura_dhc': Altura_DHC2017,
                    'circ_abdm_dhc': Circ_Abd_DHC2017,
                    'pressao_sist_dhc': Pressao_sistolica2017,
                    'pressao_diast_dhc': Pressao_diastolica2017,
                    'obs_pressao_dhc': Obs_pressao2017,
                    'glicemia_dhc': Result_glc2017,
                    'obs_glicemia_dhc': Obs_glc2017,
                    'colesterol_dhc': Valor_colest2017,
                    'obs_colesterol_dhc': Obs_colest2017,
                    'obs_dhc': OBS_DHC2017,
                }
                lab_test_anemia_dhc = lab_test_anemia_dhc_model.create(values)

            lab_test_person_search = lab_test_person_model.search([
                ('access_id', '=', access_id),
            ])
            if lab_test_person_search.id is not False:
                lab_test_anemia_dhc.lab_test_person_id = lab_test_person_search.id

            lab_test_request_search = lab_test_request_model.search([
                ('name', '=', Codigo_Ex_ANEMIA2017),
            ])
            if lab_test_request_search.id is not False:
                lab_test_anemia_dhc.request_id_anemia = lab_test_request_search.id

            lab_test_request_search = lab_test_request_model.search([
                ('name', '=', Codigo_Exame2017),
            ])
            if lab_test_request_search.id is not False:
                lab_test_anemia_dhc.request_id_dhc = lab_test_request_search.id

        return True
