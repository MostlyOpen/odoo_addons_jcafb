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

        # lab_test_result_model = self.env['myo.lab_test.result']

        for lab_test_anemia_dhc_reg in self.lab_test_anemia_dhc_ids:
            print '>>>>>', lab_test_anemia_dhc_reg.request_code_anemia, lab_test_anemia_dhc_reg.request_code_dhc

            if lab_test_anemia_dhc_reg.request_code_anemia != 'n/d' and \
               lab_test_anemia_dhc_reg.state == 'validated':

                if lab_test_anemia_dhc_reg.request_id_anemia_dhc.lab_test_type_id.name == \
                   u'JCAFB 2017 - Exames para detecção de Anemia':
                    pass

            if lab_test_anemia_dhc_reg.request_code_dhc != 'n/d' and \
               lab_test_anemia_dhc_reg.state == 'validated':

                if lab_test_anemia_dhc_reg.request_id_anemia_dhc.lab_test_type_id.name == \
                   u'JCAFB 2017 - Exames - Diabetes, Hipertensão Arterial e Hipercolesterolemia':
                    pass

            if lab_test_anemia_dhc_reg.notes is False:
                lab_test_anemia_dhc_reg.state = 'transcribed'
            else:
                lab_test_anemia_dhc_reg.state = 'draft'

        return True
