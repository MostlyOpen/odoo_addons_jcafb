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


class LabTestParasitoSwabCheckWizard(models.TransientModel):
    _name = 'myo.lab_test.parasito_swab.check.wizard'

    def _default_lab_test_parasito_swab_ids(self):
        return self._context.get('active_ids')
    lab_test_parasito_swab_ids = fields.Many2many(
        'myo.lab_test.parasito_swab',
        'myo_lab_test_parasito_swab_check_wizard_rel',
        string='Survey Files',
        default=_default_lab_test_parasito_swab_ids)

    @api.multi
    def do_lab_test_parasito_swab_check(self):
        self.ensure_one()

        lab_test_request_model = self.env['myo.lab_test.request']
        lab_test_parasito_swab_model = self.env['myo.lab_test.parasito_swab']
        professional_model = self.env['myo.professional']

        for lab_test_parasito_swab_reg in self.lab_test_parasito_swab_ids:
            print '>>>>>', \
                  lab_test_parasito_swab_reg.request_code_parasito, lab_test_parasito_swab_reg.request_code_swab

            lab_test_parasito_swab_reg.notes = False

            if lab_test_parasito_swab_reg.request_code_parasito == 'n/d' and \
               lab_test_parasito_swab_reg.request_code_swab == 'n/d':

                if lab_test_parasito_swab_reg.notes is False:
                    lab_test_parasito_swab_reg.notes = u'Erro: Nenhum resultado de exame definido!'
                else:
                    lab_test_parasito_swab_reg.notes += u'\nErro: Nenhum resultado de exame definido'

            if lab_test_parasito_swab_reg.request_code_parasito != 'n/d':

                lab_test_request_search = lab_test_request_model.search([
                    ('name', '=', lab_test_parasito_swab_reg.request_code_parasito),
                ])
                if lab_test_request_search.id is False:
                    if lab_test_parasito_swab_reg.notes is False:
                        lab_test_parasito_swab_reg.notes = u'Erro: Codigo da Requisição (Parasito) inválido!'
                    else:
                        lab_test_parasito_swab_reg.notes += u'\nErro: Codigo da Requisição (Parasito) inválido!'
                else:
                    if lab_test_parasito_swab_reg.request_id_parasito.lab_test_type_id.name != \
                       u'JCAFB 2017 - Laboratório - Parasitologia (Criança)' and \
                       lab_test_parasito_swab_reg.request_id_parasito.lab_test_type_id.name != \
                       u'JCAFB 2017 - Laboratório - Parasitologia (Idoso)' and \
                       lab_test_parasito_swab_reg.request_id_parasito.lab_test_type_id.name != \
                       u'JCAFB 2017 - Laboratório - Parasitologia':
                        if lab_test_parasito_swab_reg.notes is False:
                            lab_test_parasito_swab_reg.notes = \
                                u'Erro: Tipo de Exame da Requisição (Parasito) inválido!'
                        else:
                            lab_test_parasito_swab_reg.notes += \
                                u'\nErro: Tipo de Exame da Requisição (Parasito) inválido!'
                    if lab_test_parasito_swab_reg.request_id_parasito.patient_id.name != \
                       lab_test_parasito_swab_reg.lab_test_person_id.name:
                        if lab_test_parasito_swab_reg.notes is False:
                            lab_test_parasito_swab_reg.notes = u'Erro: Pessoa da Requisição (Parasito) inválida!'
                        else:
                            lab_test_parasito_swab_reg.notes += u'\nErro: Pessoa da Requisição (Parasito) inválida!'

                    lab_test_parasito_swab_search = lab_test_parasito_swab_model.search([
                        ('request_code_parasito', '=', lab_test_parasito_swab_reg.request_code_parasito),
                    ])
                    if len(lab_test_parasito_swab_search) > 1:
                        if lab_test_parasito_swab_reg.notes is False:
                            lab_test_parasito_swab_reg.notes = u'Erro: Codigo da Requisição (Parasito) Duplicado!'
                        else:
                            lab_test_parasito_swab_reg.notes += u'\nErro: Codigo da Requisição (Parasito) Duplicado!'

                if lab_test_parasito_swab_reg.farmaceutico_respons != 'Alice Herminia Serpentino - CRF (SP): 7.891' \
                   and \
                   lab_test_parasito_swab_reg.farmaceutico_respons != 'Valdir Azevedo dos Santos - CRF (SP): 26.169':
                    if lab_test_parasito_swab_reg.notes is False:
                        lab_test_parasito_swab_reg.notes = u'Erro: Farmacẽutico Responsável inválido!'
                    else:
                        lab_test_parasito_swab_reg.notes += u'\nErro: Farmacẽutico Responsável inválido!'
                else:
                    if lab_test_parasito_swab_reg.farmaceutico_respons == \
                       'Alice Herminia Serpentino - CRF (SP): 7.891':
                        professional_search = professional_model.search([
                            ('name', '=', 'Alice Herminia Serpentino'),
                        ])
                        if professional_search.id is not False:
                            lab_test_parasito_swab_reg.professional_id = professional_search.id
                    if lab_test_parasito_swab_reg.farmaceutico_respons == \
                       'Valdir Azevedo dos Santos - CRF (SP): 26.169':
                        professional_search = professional_model.search([
                            ('name', '=', 'Valdir Azevedo dos Santos'),
                        ])
                        if professional_search.id is not False:
                            lab_test_parasito_swab_reg.professional_id = professional_search.id

            if lab_test_parasito_swab_reg.request_code_swab != 'n/d':

                lab_test_request_search = lab_test_request_model.search([
                    ('name', '=', lab_test_parasito_swab_reg.request_code_swab),
                ])
                if lab_test_request_search.id is False:
                    if lab_test_parasito_swab_reg.notes is False:
                        lab_test_parasito_swab_reg.notes = u'Erro: Codigo da Requisição (SWAB) inválido!'
                    else:
                        lab_test_parasito_swab_reg.notes += u'\nErro: Codigo da Requisição (SWAB) inválido!'
                else:
                    if lab_test_parasito_swab_reg.request_id_swab.lab_test_type_id.name != \
                       u'JCAFB 2017 - Laboratório - Pesquisa de Enterobius vermicularis':
                        if lab_test_parasito_swab_reg.notes is False:
                            lab_test_parasito_swab_reg.notes = u'Erro: Tipo de Exame da Requisição (SWAB) inválido!'
                        else:
                            lab_test_parasito_swab_reg.notes += u'\nErro: Tipo de Exame da Requisição (SWAB) inválido!'
                    if lab_test_parasito_swab_reg.request_id_swab.patient_id.name != \
                       lab_test_parasito_swab_reg.lab_test_person_id.name:
                        if lab_test_parasito_swab_reg.notes is False:
                            lab_test_parasito_swab_reg.notes = u'Erro: Pessoa da Requisição (SWAB) inválida!'
                        else:
                            lab_test_parasito_swab_reg.notes += u'\nErro: Pessoa da Requisição (SWAB) inválida!'

                    lab_test_parasito_swab_search = lab_test_parasito_swab_model.search([
                        ('request_code_swab', '=', lab_test_parasito_swab_reg.request_code_swab),
                    ])
                    if len(lab_test_parasito_swab_search) > 1:
                        if lab_test_parasito_swab_reg.notes is False:
                            lab_test_parasito_swab_reg.notes = u'Erro: Codigo da Requisição (SWAB) Duplicado!'
                        else:
                            lab_test_parasito_swab_reg.notes += u'\nErro: Codigo da Requisição (SWAB) Duplicado!'

                if lab_test_parasito_swab_reg.farmaceutico_respons != 'Alice Herminia Serpentino - CRF (SP): 7.891' \
                   and \
                   lab_test_parasito_swab_reg.farmaceutico_respons != 'Valdir Azevedo dos Santos - CRF (SP): 26.169':
                    if lab_test_parasito_swab_reg.notes is False:
                        lab_test_parasito_swab_reg.notes = u'Erro: Farmacẽutico Responsável inválido!'
                    else:
                        lab_test_parasito_swab_reg.notes += u'\nErro: Farmacẽutico Responsável inválido!'
                else:
                    if lab_test_parasito_swab_reg.farmaceutico_respons == \
                       'Alice Herminia Serpentino - CRF (SP): 7.891':
                        professional_search = professional_model.search([
                            ('name', '=', 'Alice Herminia Serpentino'),
                        ])
                        if professional_search.id is not False:
                            lab_test_parasito_swab_reg.professional_id = professional_search.id
                    if lab_test_parasito_swab_reg.farmaceutico_respons == \
                       'Valdir Azevedo dos Santos - CRF (SP): 26.169':
                        professional_search = professional_model.search([
                            ('name', '=', 'Valdir Azevedo dos Santos'),
                        ])
                        if professional_search.id is not False:
                            lab_test_parasito_swab_reg.professional_id = professional_search.id

            if lab_test_parasito_swab_reg.notes is False:
                lab_test_parasito_swab_reg.state = 'checked'
            else:
                lab_test_parasito_swab_reg.state = 'draft'

        return True
