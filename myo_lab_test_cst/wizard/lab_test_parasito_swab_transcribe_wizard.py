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


class LabTestParasitoSWABTranscribeWizard(models.TransientModel):
    _name = 'myo.lab_test.parasito_swab.transcribe.wizard'

    def _default_lab_test_parasito_swab_ids(self):
        return self._context.get('active_ids')
    lab_test_parasito_swab_ids = fields.Many2many(
        'myo.lab_test.parasito_swab',
        'myo_lab_test_parasito_swab_transcribe_wizard_rel',
        string='Exames de Parasito SWAB',
        default=_default_lab_test_parasito_swab_ids)

    @api.multi
    def do_lab_test_parasito_swab_transcribe(self):
        self.ensure_one()

        lab_test_result_model = self.env['myo.lab_test.result']

        for lab_test_parasito_swab_reg in self.lab_test_parasito_swab_ids:
            print '>>>>>', lab_test_parasito_swab_reg.request_code_parasito, \
                  lab_test_parasito_swab_reg.request_code_swab

            if lab_test_parasito_swab_reg.request_code_parasito != 'n/d' and \
               lab_test_parasito_swab_reg.state == 'validated':

                if lab_test_parasito_swab_reg.request_id_parasito.lab_test_type_id.name == \
                   u'JCAFB 2017 - Laboratório - Parasitologia':

                    lab_test_result_search = lab_test_result_model.search([
                        ('name', '=', lab_test_parasito_swab_reg.request_code_parasito),
                    ])
                    if lab_test_result_search.id is not False:

                        lab_test_result_search.professional_id = lab_test_parasito_swab_reg.professional_id

                        for criterion_reg in lab_test_result_search.criterion_ids:

                            if criterion_reg.code == 'ECP-01-01':
                                criterion_reg.result = lab_test_parasito_swab_reg.entrada_parasito
                            if criterion_reg.code == 'ECP-01-02':
                                criterion_reg.result = lab_test_parasito_swab_reg.saida_parasito
                            if criterion_reg.code == 'ECP-01-03':
                                criterion_reg.result = lab_test_parasito_swab_reg.resultado_parasito
                            # if criterion_reg.code == 'ECP-01-04':
                            #     criterion_reg.result = lab_test_parasito_swab_reg.?
                            if criterion_reg.code == 'ECP-01-05':
                                criterion_reg.result = lab_test_parasito_swab_reg.metodos_parasito

                            if criterion_reg.code == 'ECP-02-01':
                                criterion_reg.result = lab_test_parasito_swab_reg.result_parasito_ritchie
                            if criterion_reg.code == 'ECP-02-02':
                                criterion_reg.result = lab_test_parasito_swab_reg.examinador_ritchie

                            if criterion_reg.code == 'ECP-03-01':
                                criterion_reg.result = lab_test_parasito_swab_reg.result_parasito_hoffmann
                            if criterion_reg.code == 'ECP-03-02':
                                criterion_reg.result = lab_test_parasito_swab_reg.examinador_hoffmann

                        if lab_test_parasito_swab_reg.notes is False:
                            lab_test_result_search.state = 'transcribed'

            if lab_test_parasito_swab_reg.request_code_swab != 'n/d' and \
               lab_test_parasito_swab_reg.state == 'validated':

                if lab_test_parasito_swab_reg.request_id_swab.lab_test_type_id.name == \
                   u'JCAFB 2017 - Laboratório - Pesquisa de Enterobius vermicularis':
                    pass

                    lab_test_result_search = lab_test_result_model.search([
                        ('name', '=', lab_test_parasito_swab_reg.request_code_swab),
                    ])
                    if lab_test_result_search.id is not False:

                        lab_test_result_search.professional_id = lab_test_parasito_swab_reg.professional_id

                        for criterion_reg in lab_test_result_search.criterion_ids:

                            if criterion_reg.code == 'EEV-01-01':
                                criterion_reg.result = lab_test_parasito_swab_reg.entrada_swab
                            if criterion_reg.code == 'EEV-01-02':
                                criterion_reg.result = lab_test_parasito_swab_reg.saida_swab
                            if criterion_reg.code == 'EEV-01-03':
                                criterion_reg.result = lab_test_parasito_swab_reg.result_swab
                            if criterion_reg.code == 'EEV-01-04':
                                criterion_reg.result = lab_test_parasito_swab_reg.examinador_swab
                            if criterion_reg.code == 'EEV-01-05':
                                criterion_reg.result = lab_test_parasito_swab_reg.metodo_swab
                            # if criterion_reg.code == 'EEV-01-06':
                            #     criterion_reg.result = lab_test_parasito_swab_reg.?

                        if lab_test_parasito_swab_reg.notes is False:
                            lab_test_result_search.state = 'transcribed'

            if lab_test_parasito_swab_reg.notes is False:
                lab_test_parasito_swab_reg.state = 'transcribed'
            else:
                lab_test_parasito_swab_reg.state = 'draft'

        return True
