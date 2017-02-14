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


class LabTestPersonCheckWizard(models.TransientModel):
    _name = 'myo.lab_test.person.check.wizard'

    def _default_lab_test_person_ids(self):
        return self._context.get('active_ids')
    lab_test_person_ids = fields.Many2many(
        'myo.lab_test.person',
        string='Survey Files',
        default=_default_lab_test_person_ids)

    @api.multi
    def do_lab_test_person_check(self):
        self.ensure_one()

        person_model = self.env['myo.person']
        lab_test_person_model = self.env['myo.lab_test.person']

        for lab_test_person_reg in self.lab_test_person_ids:
            print '>>>>>', lab_test_person_reg.code

            lab_test_person_reg.notes = False

            person_search = person_model.search([
                ('code', '=', lab_test_person_reg.code),
            ])
            if person_search.id is False:
                if lab_test_person_reg.notes is False:
                    lab_test_person_reg.notes = 'Erro: Codigo da pessoa invalido!'
                else:
                    lab_test_person_reg.notes += '\nErro: Codigo da pessoa invalido!'
            else:
                if lab_test_person_reg.name != person_search.name:
                    if lab_test_person_reg.notes is False:
                        lab_test_person_reg.notes = 'Erro: Nome da Pessoa Invalido!'
                    else:
                        lab_test_person_reg.notes += '\nErro: Nome da Pessoa Invalido!'

                lab_test_person_search = lab_test_person_model.search([
                    ('code', '=', lab_test_person_reg.code),
                ])
                if len(lab_test_person_search) > 1:
                    if lab_test_person_reg.notes is False:
                        lab_test_person_reg.notes = 'Erro: Codigo da Pessoa Duplicado!'
                    else:
                        lab_test_person_reg.notes += '\nErro: Codigo da Pessoa Duplicado!'

            if lab_test_person_reg.notes is False:
                lab_test_person_reg.state = 'checked'
            else:
                lab_test_person_reg.state = 'draft'

        return True
