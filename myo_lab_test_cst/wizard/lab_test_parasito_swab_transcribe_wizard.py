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

        # lab_test_result_model = self.env['myo.lab_test.result']

        for lab_test_parasito_swab_reg in self.lab_test_parasito_swab_ids:
            print '>>>>>', lab_test_parasito_swab_reg.request_code_parasito, \
                  lab_test_parasito_swab_reg.request_code_swab

            if lab_test_parasito_swab_reg.request_code_parasito != 'n/d' and \
               lab_test_parasito_swab_reg.state == 'validated':

                if lab_test_parasito_swab_reg.request_id_parasito_swab.lab_test_type_id.name == \
                   u'JCAFB 2017 - Laboratório - Parasitologia':
                    pass

            if lab_test_parasito_swab_reg.request_code_swab != 'n/d' and \
               lab_test_parasito_swab_reg.state == 'validated':

                if lab_test_parasito_swab_reg.request_id_parasito_swab.lab_test_type_id.name == \
                   u'JCAFB 2017 - Laboratório - Pesquisa de Enterobius vermicularis':
                    pass

            if lab_test_parasito_swab_reg.notes is False:
                lab_test_parasito_swab_reg.state = 'transcribed'
            else:
                lab_test_parasito_swab_reg.state = 'draft'

        return True
