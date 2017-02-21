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


class LabTestAnemiaDHCCheckWizard(models.TransientModel):
    _name = 'myo.lab_test.anemia_dhc.check.wizard'

    def _default_lab_test_anemia_dhc_ids(self):
        return self._context.get('active_ids')
    lab_test_anemia_dhc_ids = fields.Many2many(
        'myo.lab_test.anemia_dhc',
        'myo_lab_test_anemia_dhc_check_wizard_rel',
        string='Survey Files',
        default=_default_lab_test_anemia_dhc_ids)

    @api.multi
    def do_lab_test_anemia_dhc_check(self):
        self.ensure_one()

        lab_test_request_model = self.env['myo.lab_test.request']
        lab_test_anemia_dhc_model = self.env['myo.lab_test.anemia_dhc']
        professional_model = self.env['myo.professional']

        for lab_test_anemia_dhc_reg in self.lab_test_anemia_dhc_ids:
            print '>>>>>', lab_test_anemia_dhc_reg.request_code_anemia, lab_test_anemia_dhc_reg.request_code_dhc

            lab_test_anemia_dhc_reg.notes = False

            if lab_test_anemia_dhc_reg.request_code_anemia == 'n/d' and \
               lab_test_anemia_dhc_reg.request_code_dhc == 'n/d':

                if lab_test_anemia_dhc_reg.notes is False:
                    lab_test_anemia_dhc_reg.notes = u'Erro: Nenhum resultado de exame definido!'
                else:
                    lab_test_anemia_dhc_reg.notes += u'\nErro: Nenhum resultado de exame definido'

            if lab_test_anemia_dhc_reg.request_code_anemia != 'n/d':

                lab_test_request_search = lab_test_request_model.search([
                    ('name', '=', lab_test_anemia_dhc_reg.request_code_anemia),
                ])
                if lab_test_request_search.id is False:
                    if lab_test_anemia_dhc_reg.notes is False:
                        lab_test_anemia_dhc_reg.notes = u'Erro: Codigo da Requisição (Anemia) inválido!'
                    else:
                        lab_test_anemia_dhc_reg.notes += u'\nErro: Codigo da Requisição (Anemia) inválido!'
                else:
                    if lab_test_anemia_dhc_reg.request_id_anemia.lab_test_type_id.name != \
                       u'JCAFB 2017 - Exames para detecção de Anemia':
                        if lab_test_anemia_dhc_reg.notes is False:
                            lab_test_anemia_dhc_reg.notes = u'Erro: Tipo de Exame da Requisição (Anemia) inválido!'
                        else:
                            lab_test_anemia_dhc_reg.notes += u'\nErro: Tipo de Exame da Requisição (Anemia) inválido!'
                    if lab_test_anemia_dhc_reg.request_id_anemia.patient_id.name != \
                       lab_test_anemia_dhc_reg.lab_test_person_id.name:
                        if lab_test_anemia_dhc_reg.notes is False:
                            lab_test_anemia_dhc_reg.notes = u'Erro: Pessoa da Requisição (Anemia) inválida!'
                        else:
                            lab_test_anemia_dhc_reg.notes += u'\nErro: Pessoa da Requisição (Anemia) inválida!'

                    lab_test_anemia_dhc_search = lab_test_anemia_dhc_model.search([
                        ('request_code_anemia', '=', lab_test_anemia_dhc_reg.request_code_anemia),
                    ])
                    if len(lab_test_anemia_dhc_search) > 1:
                        if lab_test_anemia_dhc_reg.notes is False:
                            lab_test_anemia_dhc_reg.notes = u'Erro: Codigo da Requisição (Anemia) Duplicado!'
                        else:
                            lab_test_anemia_dhc_reg.notes += u'\nErro: Codigo da Requisição (Anemia) Duplicado!'

                if lab_test_anemia_dhc_reg.farmaceutico_anemia != 'Alice Herminia Serpentino - CRF (SP): 7.891' and \
                   lab_test_anemia_dhc_reg.farmaceutico_anemia != 'Valdir Azevedo dos Santos - CRF (SP): 26.169':
                    if lab_test_anemia_dhc_reg.notes is False:
                        lab_test_anemia_dhc_reg.notes = u'Erro: Farmacẽutico Responsável inválido!'
                    else:
                        lab_test_anemia_dhc_reg.notes += u'\nErro: Farmacẽutico Responsável inválido!'
                else:
                    if lab_test_anemia_dhc_reg.farmaceutico_anemia == 'Alice Herminia Serpentino - CRF (SP): 7.891':
                        professional_search = professional_model.search([
                            ('name', '=', 'Alice Herminia Serpentino'),
                        ])
                        if professional_search.id is not False:
                            lab_test_anemia_dhc_reg.professional_id_anemia = professional_search.id
                    if lab_test_anemia_dhc_reg.farmaceutico_anemia == 'Valdir Azevedo dos Santos - CRF (SP): 26.169':
                        professional_search = professional_model.search([
                            ('name', '=', 'Valdir Azevedo dos Santos'),
                        ])
                        if professional_search.id is not False:
                            lab_test_anemia_dhc_reg.professional_id_anemia = professional_search.id

            if lab_test_anemia_dhc_reg.request_code_dhc != 'n/d':

                lab_test_request_search = lab_test_request_model.search([
                    ('name', '=', lab_test_anemia_dhc_reg.request_code_dhc),
                ])
                if lab_test_request_search.id is False:
                    if lab_test_anemia_dhc_reg.notes is False:
                        lab_test_anemia_dhc_reg.notes = u'Erro: Codigo da Requisição (DHC) inválido!'
                    else:
                        lab_test_anemia_dhc_reg.notes += u'\nErro: Codigo da Requisição (DHC) inválido!'
                else:
                    if lab_test_anemia_dhc_reg.request_id_dhc.lab_test_type_id.name != \
                       u'JCAFB 2017 - Exames - Diabetes, Hipertensão Arterial e Hipercolesterolemia':
                        if lab_test_anemia_dhc_reg.notes is False:
                            lab_test_anemia_dhc_reg.notes = u'Erro: Tipo de Exame da Requisição (DHC) inválido!'
                        else:
                            lab_test_anemia_dhc_reg.notes += u'\nErro: Tipo de Exame da Requisição (DHC) inválido!'
                    if lab_test_anemia_dhc_reg.request_id_dhc.patient_id.name != \
                       lab_test_anemia_dhc_reg.lab_test_person_id.name:
                        if lab_test_anemia_dhc_reg.notes is False:
                            lab_test_anemia_dhc_reg.notes = u'Erro: Pessoa da Requisição (DHC) inválida!'
                        else:
                            lab_test_anemia_dhc_reg.notes += u'\nErro: Pessoa da Requisição (DHC) inválida!'

                    lab_test_anemia_dhc_search = lab_test_anemia_dhc_model.search([
                        ('request_code_dhc', '=', lab_test_anemia_dhc_reg.request_code_dhc),
                    ])
                    if len(lab_test_anemia_dhc_search) > 1:
                        if lab_test_anemia_dhc_reg.notes is False:
                            lab_test_anemia_dhc_reg.notes = u'Erro: Codigo da Requisição (DHC) Duplicado!'
                        else:
                            lab_test_anemia_dhc_reg.notes += u'\nErro: Codigo da Requisição (DHC) Duplicado!'

                if lab_test_anemia_dhc_reg.farmaceutico_dhc != 'Alice Herminia Serpentino - CRF (SP): 7.891' and \
                   lab_test_anemia_dhc_reg.farmaceutico_dhc != 'Valdir Azevedo dos Santos - CRF (SP): 26.169':
                    if lab_test_anemia_dhc_reg.notes is False:
                        lab_test_anemia_dhc_reg.notes = u'Erro: Farmacẽutico Responsável inválido!'
                    else:
                        lab_test_anemia_dhc_reg.notes += u'\nErro: Farmacẽutico Responsável inválido!'
                else:
                    if lab_test_anemia_dhc_reg.farmaceutico_dhc == 'Alice Herminia Serpentino - CRF (SP): 7.891':
                        professional_search = professional_model.search([
                            ('name', '=', 'Alice Herminia Serpentino'),
                        ])
                        if professional_search.id is not False:
                            lab_test_anemia_dhc_reg.professional_id_dhc = professional_search.id
                    if lab_test_anemia_dhc_reg.farmaceutico_dhc == 'Valdir Azevedo dos Santos - CRF (SP): 26.169':
                        professional_search = professional_model.search([
                            ('name', '=', 'Valdir Azevedo dos Santos'),
                        ])
                        if professional_search.id is not False:
                            lab_test_anemia_dhc_reg.professional_id_dhc = professional_search.id

            if lab_test_anemia_dhc_reg.notes is False:
                lab_test_anemia_dhc_reg.state = 'checked'
            else:
                lab_test_anemia_dhc_reg.state = 'draft'

        return True
