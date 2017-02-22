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


class LabTestUrinaTranscribeWizard(models.TransientModel):
    _name = 'myo.lab_test.urina.transcribe.wizard'

    def _default_lab_test_urina_ids(self):
        return self._context.get('active_ids')
    lab_test_urina_ids = fields.Many2many(
        'myo.lab_test.urina',
        'myo_lab_test_urina_transcribe_wizard_rel',
        string='Exames de Urina',
        default=_default_lab_test_urina_ids)

    @api.multi
    def do_lab_test_urina_transcribe(self):
        self.ensure_one()

        lab_test_result_model = self.env['myo.lab_test.result']

        for lab_test_urina_reg in self.lab_test_urina_ids:
            print '>>>>>', lab_test_urina_reg.request_code_urina

            if lab_test_urina_reg.request_code_urina != 'n/d' and \
               lab_test_urina_reg.state == 'validated':

                if lab_test_urina_reg.request_id_urina.lab_test_type_id.name == \
                   u'JCAFB 2017 - Laboratório - Urinálise':

                    lab_test_result_search = lab_test_result_model.search([
                        ('name', '=', lab_test_urina_reg.request_code_urina),
                    ])
                    if lab_test_result_search.id is not False:

                        lab_test_result_search.professional_id = lab_test_urina_reg.professional_id
                        if lab_test_urina_reg.date_urina is not False:
                            lab_test_result_search.date_result = lab_test_urina_reg.date_urina + ' 20:00:00'

                        for criterion_reg in lab_test_result_search.criterion_ids:

                            if criterion_reg.code == 'EUR-01-01':
                                criterion_reg.result = lab_test_urina_reg.date_urina
                            if criterion_reg.code == 'EUR-01-02':
                                criterion_reg.result = lab_test_urina_reg.date_laudo
                            if criterion_reg.code == 'EUR-01-03':
                                criterion_reg.result = lab_test_urina_reg.examinador

                            if criterion_reg.code == 'EUR-02-01':
                                criterion_reg.result = lab_test_urina_reg.volume
                            if criterion_reg.code == 'EUR-02-02':
                                criterion_reg.result = lab_test_urina_reg.densidade
                            if criterion_reg.code == 'EUR-02-03':
                                criterion_reg.result = lab_test_urina_reg.aspecto
                            if criterion_reg.code == 'EUR-02-04':
                                criterion_reg.result = lab_test_urina_reg.cor
                            if criterion_reg.code == 'EUR-02-05':
                                criterion_reg.result = lab_test_urina_reg.odor

                            if criterion_reg.code == 'EUR-03-01':
                                criterion_reg.result = lab_test_urina_reg.ph
                            if criterion_reg.code == 'EUR-03-02':
                                criterion_reg.result = lab_test_urina_reg.proteinas
                            if criterion_reg.code == 'EUR-03-03':
                                criterion_reg.result = lab_test_urina_reg.glicose
                            if criterion_reg.code == 'EUR-03-04':
                                criterion_reg.result = lab_test_urina_reg.cetona
                            if criterion_reg.code == 'EUR-03-05':
                                criterion_reg.result = lab_test_urina_reg.pig_biliares
                            if criterion_reg.code == 'EUR-03-06':
                                criterion_reg.result = lab_test_urina_reg.sangue
                            if criterion_reg.code == 'EUR-03-07':
                                criterion_reg.result = lab_test_urina_reg.urobilinogenio
                            if criterion_reg.code == 'EUR-03-08':
                                criterion_reg.result = lab_test_urina_reg.nitrito

                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.cels_epit
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.muco
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.cristais
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.leucocitos
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.hemacias
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.cilindros
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.hialinos
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.ganulosos
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.leucocitarios
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.hematicos
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.cereos
                            if criterion_reg.code == 'EUR-04-01':
                                criterion_reg.result = lab_test_urina_reg.outros_tipos

                            if criterion_reg.code == 'EUR-05-01':
                                criterion_reg.result = lab_test_urina_reg.obs

            if lab_test_urina_reg.notes is False:
                lab_test_urina_reg.state = 'transcribed'
                lab_test_result_search.state = 'transcribed'
            else:
                lab_test_urina_reg.state = 'draft'

        return True
