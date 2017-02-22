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


class LabTestUrinaCheckWizard(models.TransientModel):
    _name = 'myo.lab_test.urina.check.wizard'

    def _default_lab_test_urina_ids(self):
        return self._context.get('active_ids')
    lab_test_urina_ids = fields.Many2many(
        'myo.lab_test.urina',
        'myo_lab_test_urina_check_wizard_rel',
        string='Survey Files',
        default=_default_lab_test_urina_ids)

    @api.multi
    def do_lab_test_urina_check(self):
        self.ensure_one()

        lab_test_request_model = self.env['myo.lab_test.request']
        lab_test_urina_model = self.env['myo.lab_test.urina']
        professional_model = self.env['myo.professional']

        for lab_test_urina_reg in self.lab_test_urina_ids:
            print '>>>>>', lab_test_urina_reg.request_code_urina

            lab_test_urina_reg.notes = False

            if lab_test_urina_reg.request_code_urina != 'n/d':

                lab_test_request_search = lab_test_request_model.search([
                    ('name', '=', lab_test_urina_reg.request_code_urina),
                ])
                if lab_test_request_search.id is False:
                    if lab_test_urina_reg.notes is False:
                        lab_test_urina_reg.notes = u'Erro: Codigo da Requisição (Urina) inválido!'
                    else:
                        lab_test_urina_reg.notes += u'\nErro: Codigo da Requisição (Urina) inválido!'
                else:
                    if lab_test_urina_reg.request_id_urina.lab_test_type_id.name != \
                       u'JCAFB 2017 - Laboratório - Urinálise':
                        if lab_test_urina_reg.notes is False:
                            lab_test_urina_reg.notes = u'Erro: Tipo de Exame da Requisição (Urina) inválido!'
                        else:
                            lab_test_urina_reg.notes += u'\nErro: Tipo de Exame da Requisição (Urina) inválido!'
                    if lab_test_urina_reg.request_id_urina.patient_id.name != \
                       lab_test_urina_reg.lab_test_person_id.name:
                        if lab_test_urina_reg.notes is False:
                            lab_test_urina_reg.notes = u'Erro: Pessoa da Requisição (Urina) inválida!'
                        else:
                            lab_test_urina_reg.notes += u'\nErro: Pessoa da Requisição (Urina) inválida!'

                    lab_test_urina_search = lab_test_urina_model.search([
                        ('request_code_urina', '=', lab_test_urina_reg.request_code_urina),
                    ])
                    if len(lab_test_urina_search) > 1:
                        if lab_test_urina_reg.notes is False:
                            lab_test_urina_reg.notes = u'Erro: Codigo da Requisição (Urina) Duplicado!'
                        else:
                            lab_test_urina_reg.notes += u'\nErro: Codigo da Requisição (Urina) Duplicado!'

                if lab_test_urina_reg.farmaceutico_resp != 'Alice Herminia Serpentino - CRF (SP): 7.891' and \
                   lab_test_urina_reg.farmaceutico_resp != 'Valdir Azevedo dos Santos - CRF (SP): 26.169':
                    if lab_test_urina_reg.notes is False:
                        lab_test_urina_reg.notes = u'Erro: Farmacẽutico Responsável inválido!'
                    else:
                        lab_test_urina_reg.notes += u'\nErro: Farmacẽutico Responsável inválido!'
                else:
                    if lab_test_urina_reg.farmaceutico_resp == 'Alice Herminia Serpentino - CRF (SP): 7.891':
                        professional_search = professional_model.search([
                            ('name', '=', 'Alice Herminia Serpentino'),
                        ])
                        if professional_search.id is not False:
                            lab_test_urina_reg.professional_id = professional_search.id
                    if lab_test_urina_reg.farmaceutico_resp == 'Valdir Azevedo dos Santos - CRF (SP): 26.169':
                        professional_search = professional_model.search([
                            ('name', '=', 'Valdir Azevedo dos Santos'),
                        ])
                        if professional_search.id is not False:
                            lab_test_urina_reg.professional_id = professional_search.id

                # if lab_test_urina_reg.date_urina is False:
                #     if lab_test_urina_reg.notes is False:
                #         lab_test_urina_reg.notes = u'Erro: Data do Exame não definida!'
                #     else:
                #         lab_test_urina_reg.notes += u'\nErro: Data do Exame não definida!'

            if lab_test_urina_reg.notes is False:
                lab_test_urina_reg.state = 'checked'
            else:
                lab_test_urina_reg.state = 'draft'

        return True
