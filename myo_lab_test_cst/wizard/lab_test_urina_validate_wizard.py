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


class LabTestUrinaValidateWizard(models.TransientModel):
    _name = 'myo.lab_test.urina.validate.wizard'

    def _default_lab_test_urina_ids(self):
        return self._context.get('active_ids')
    lab_test_urina_ids = fields.Many2many(
        'myo.lab_test.urina',
        'myo_lab_test_urina_validate_wizard_rel',
        string='Exames de Urina',
        default=_default_lab_test_urina_ids)

    @api.multi
    def do_lab_test_urina_validate(self):
        self.ensure_one()

        lab_test_result_model = self.env['myo.lab_test.result']

        for lab_test_urina_reg in self.lab_test_urina_ids:
            print '>>>>>', lab_test_urina_reg.request_code_urina

            lab_test_result_data = {}
            test_cases = []

            if lab_test_urina_reg.request_code_urina != 'n/d' and \
               lab_test_urina_reg.state == 'checked':

                if lab_test_urina_reg.request_id_urina.lab_test_type_id.name != \
                   u'JCAFB 2017 - Laboratório - Urinálise':
                    if lab_test_urina_reg.notes is False:
                        lab_test_urina_reg.notes = u'Erro: Tipo de Exame da Requisição (Urina) inválido!'
                    else:
                        lab_test_urina_reg.notes += u'\nErro: Tipo de Exame da Requisição (Urina) inválido!'
                else:

                    lab_test_result_search = lab_test_result_model.search([
                        ('name', '=', lab_test_urina_reg.request_code_urina),
                    ])
                    if lab_test_result_search.id is False:

                        if lab_test_urina_reg.request_id_urina.state == 'draft':

                            lab_test_result_data['name'] = lab_test_urina_reg.request_id_urina.name
                            lab_test_result_data['lab_test_type_id'] = \
                                lab_test_urina_reg.request_id_urina.lab_test_type_id.id
                            lab_test_type = lab_test_urina_reg.request_id_urina.lab_test_type_id
                            lab_test_result_data['patient_id'] = lab_test_urina_reg.request_id_urina.patient_id.id
                            for criterion in lab_test_type.criterion_ids:
                                test_cases.append((0, 0, {'code': criterion.code,
                                                          'name': criterion.name,
                                                          'sequence': criterion.sequence,
                                                          'normal_range': criterion.normal_range,
                                                          'unit_id': criterion.unit_id.id,
                                                          }))
                            lab_test_result_data['criterion_ids'] = test_cases
                            lab_test_result_id = lab_test_result_model.create(lab_test_result_data)
                            lab_test_result_id.state = 'started'
                            lab_test_urina_reg.request_id_urina.state = 'tested'
                            lab_test_urina_reg.request_id_urina.lab_test_result_id = lab_test_result_id
                            lab_test_urina_reg.result_id_urina = lab_test_result_id
                    else:
                        pass

            if lab_test_urina_reg.notes is False:
                lab_test_urina_reg.state = 'validated'
            else:
                lab_test_urina_reg.state = 'draft'

        return True
