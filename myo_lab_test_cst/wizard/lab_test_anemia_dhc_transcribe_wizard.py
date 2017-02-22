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


class LabTestAnemiaDHCTranscribeWizard(models.TransientModel):
    _name = 'myo.lab_test.anemia_dhc.transcribe.wizard'

    def _default_lab_test_anemia_dhc_ids(self):
        return self._context.get('active_ids')
    lab_test_anemia_dhc_ids = fields.Many2many(
        'myo.lab_test.anemia_dhc',
        'myo_lab_test_anemia_dhc_transcribe_wizard_rel',
        string='Exames de Anemia DHC',
        default=_default_lab_test_anemia_dhc_ids)

    @api.multi
    def do_lab_test_anemia_dhc_transcribe(self):
        self.ensure_one()

        lab_test_result_model = self.env['myo.lab_test.result']

        for lab_test_anemia_dhc_reg in self.lab_test_anemia_dhc_ids:
            print '>>>>>', lab_test_anemia_dhc_reg.request_code_anemia, lab_test_anemia_dhc_reg.request_code_dhc

            if lab_test_anemia_dhc_reg.request_code_anemia != 'n/d' and \
               lab_test_anemia_dhc_reg.state == 'validated':

                if lab_test_anemia_dhc_reg.request_id_anemia.lab_test_type_id.name == \
                   u'JCAFB 2017 - Exames para detecção de Anemia':

                    lab_test_result_search = lab_test_result_model.search([
                        ('name', '=', lab_test_anemia_dhc_reg.request_code_anemia),
                    ])
                    if lab_test_result_search.id is not False:

                        lab_test_result_search.professional_id = lab_test_anemia_dhc_reg.professional_id_anemia
                        if lab_test_anemia_dhc_reg.date_anemia is not False:
                            lab_test_result_search.date_result = lab_test_anemia_dhc_reg.date_anemia + ' 20:00:00'

                        for criterion_reg in lab_test_result_search.criterion_ids:

                            if criterion_reg.code == 'EAN-01-01':
                                criterion_reg.result = lab_test_anemia_dhc_reg.peso_anemia
                            # if criterion_reg.code == 'EAN-01-02':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            if criterion_reg.code == 'EAN-01-03':
                                criterion_reg.result = lab_test_anemia_dhc_reg.altura_anemia
                            # if criterion_reg.code == 'EAN-01-04':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?

                            # if criterion_reg.code == 'EAN-02-01':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            # if criterion_reg.code == 'EAN-02-02':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            if criterion_reg.code == 'EAN-02-03':
                                criterion_reg.result = lab_test_anemia_dhc_reg.hemoglobina_anemia
                            # if criterion_reg.code == 'EAN-02-04':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            # if criterion_reg.code == 'EAN-02-05':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?

                            if criterion_reg.code == 'EAN-03-01':
                                criterion_reg.result = lab_test_anemia_dhc_reg.obs_anemia

                        # if lab_test_anemia_dhc_reg.notes is False:
                        #     lab_test_result_search.state = 'transcribed'

            if lab_test_anemia_dhc_reg.request_code_dhc != 'n/d' and \
               lab_test_anemia_dhc_reg.state == 'validated':

                if lab_test_anemia_dhc_reg.request_id_dhc.lab_test_type_id.name == \
                   u'JCAFB 2017 - Exames - Diabetes, Hipertensão Arterial e Hipercolesterolemia':

                    lab_test_result_search = lab_test_result_model.search([
                        ('name', '=', lab_test_anemia_dhc_reg.request_code_dhc),
                    ])
                    if lab_test_result_search.id is not False:

                        lab_test_result_search.professional_id = lab_test_anemia_dhc_reg.professional_id_dhc
                        if lab_test_anemia_dhc_reg.date_dhc is not False:
                            lab_test_result_search.date_result = lab_test_anemia_dhc_reg.date_dhc + ' 20:00:00'

                        for criterion_reg in lab_test_result_search.criterion_ids:

                            # if criterion_reg.code == 'EDH-01-01':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?

                            if criterion_reg.code == 'EDH-02-01':
                                criterion_reg.result = lab_test_anemia_dhc_reg.peso_dhc
                            if criterion_reg.code == 'EDH-02-02':
                                criterion_reg.result = lab_test_anemia_dhc_reg.altura_dhc
                            # if criterion_reg.code == 'EDH-02-03':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            # if criterion_reg.code == 'EDH-02-04':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            # if criterion_reg.code == 'EDH-02-05':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            if criterion_reg.code == 'EDH-02-06':
                                criterion_reg.result = lab_test_anemia_dhc_reg.circ_abdm_dhc
                            # if criterion_reg.code == 'EDH-02-07':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            # if criterion_reg.code == 'EDH-02-08':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?

                            if criterion_reg.code == 'EDH-03-01':
                                criterion_reg.result = lab_test_anemia_dhc_reg.pressao_sist_dhc + 'x' + \
                                    lab_test_anemia_dhc_reg.pressao_diast_dhc
                            # if criterion_reg.code == 'EDH-03-02':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            # if criterion_reg.code == 'EDH-03-03':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            if criterion_reg.code == 'EDH-03-04':
                                criterion_reg.result = lab_test_anemia_dhc_reg.obs_pressao_dhc

                            if criterion_reg.code == 'EDH-04-01':
                                criterion_reg.result = lab_test_anemia_dhc_reg.glicemia_dhc
                            # if criterion_reg.code == 'EDH-04-02':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            # if criterion_reg.code == 'EDH-04-03':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            if criterion_reg.code == 'EDH-04-04':
                                criterion_reg.result = lab_test_anemia_dhc_reg.colesterol_dhc
                            # if criterion_reg.code == 'EDH-04-05':
                            #     criterion_reg.result = lab_test_anemia_dhc_reg.?
                            if criterion_reg.code == 'EDH-04-06':
                                criterion_reg.result = lab_test_anemia_dhc_reg.obs_dhc

                        # if lab_test_anemia_dhc_reg.notes is False:
                        #     lab_test_result_search.state = 'transcribed'

            if lab_test_anemia_dhc_reg.notes is False:
                lab_test_anemia_dhc_reg.state = 'transcribed'
            else:
                lab_test_anemia_dhc_reg.state = 'draft'

        return True
