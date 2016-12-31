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

import logging

from openerp import exceptions

_logger = logging.getLogger(__name__)


class LabTestEditWizard(models.TransientModel):
    _name = 'myo.lab_test.edit.wizard'

    def _get_default(self, lab_test_type_id_code, criterion_code):
        active_id = self.env['myo.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == lab_test_type_id_code:
            result = active_id.criterion_ids.search([
                ('lab_test_result_id', '=', active_id.id),
                ('code', '=', criterion_code),
            ]).result
        else:
            result = False
        return result

    def _set_result(self, lab_test_type_id_code, criterion_code, result):
        active_id = self.env['myo.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == lab_test_type_id_code:
            criterion_reg = active_id.criterion_ids.search([
                ('lab_test_result_id', '=', active_id.id),
                ('code', '=', criterion_code),
            ])
            criterion_reg.result = result

    def _default_lab_test_code(self):
        return self.env['myo.lab_test.result'].browse(self._context.get('active_id')).name
    lab_test_code = fields.Char(
        'Lab Test Result', help="Lab Test Result", readonly=True, default=_default_lab_test_code
    )

    def _default_lab_test_type_id(self):
        return self.env['myo.lab_test.result'].browse(self._context.get('active_id')).lab_test_type_id
    lab_test_type_id = fields.Many2one(
        'myo.lab_test.type', 'Lab Test Type', readonly=True, default=_default_lab_test_type_id
    )

    def _default_patient_id(self):
        return self.env['myo.lab_test.result'].browse(self._context.get('active_id')).patient_id
    patient_id = fields.Many2one(
        'myo.person', 'Patient', readonly=True, default=_default_patient_id
    )

    def _default_is_EAN(self):
        active_id = self.env['myo.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EAN17':
            is_EAN = True
        else:
            is_EAN = False
        return is_EAN
    is_EAN = fields.Boolean('Is EAN', readonly=True, default=_default_is_EAN)

    def _default_EAN_peso(self):
        return self._get_default('EAN17', 'EAN-01-01')
    EAN_peso = fields.Char(
        'Peso', readonly=False, default=_default_EAN_peso
    )

    def _write_EAN_peso(self):
        self._set_result('EAN17', 'EAN-01-01', self.EAN_peso)

    def _default_EAN_peso_resp(self):
        return self._get_default('EAN17', 'EAN-01-02')
    EAN_peso_resp = fields.Char(
        'Responsável pela medida do Peso', readonly=False, default=_default_EAN_peso_resp
    )

    def _write_EAN_peso_resp(self):
        self._set_result('EAN17', 'EAN-01-02', self.EAN_peso_resp)

    @api.onchange('EAN_peso_resp')
    def onchange_EAN_peso_resp(self):
        employee_model = self.env['hr.employee']
        if self.EAN_peso_resp is not False:
            employee_search = employee_model.search([
                ('code', '=', self.EAN_peso_resp),
            ])
            if employee_search.id is False:
                raise exceptions.ValidationError(
                    'Erro! O Código do Responsável pela medida do Peso não é válido!')

    def _default_EAN_altura(self):
        return self._get_default('EAN17', 'EAN-01-03')
    EAN_altura = fields.Char(
        'Altura', readonly=False, default=_default_EAN_altura
    )

    def _write_EAN_altura(self):
        self._set_result('EAN17', 'EAN-01-03', self.EAN_altura)

    def _default_EAN_altura_resp(self):
        return self._get_default('EAN17', 'EAN-01-04')
    EAN_altura_resp = fields.Char(
        'Responsável pela medida da Altura', readonly=False, default=_default_EAN_altura_resp
    )

    def _write_EAN_altura_resp(self):
        self._set_result('EAN17', 'EAN-01-04', self.EAN_altura_resp)

    @api.onchange('EAN_altura_resp')
    def onchange_EAN_altura_resp(self):
        employee_model = self.env['hr.employee']
        if self.EAN_altura_resp is not False:
            employee_search = employee_model.search([
                ('code', '=', self.EAN_altura_resp),
            ])
            if employee_search.id is False:
                raise exceptions.ValidationError(
                    'Erro! O Código do Responsável pela medida da Altura não é válido!')

    def _default_EAN_hemoglobina_coleta_horario(self):
        return self._get_default('EAN17', 'EAN-02-01')
    EAN_hemoglobina_coleta_horario = fields.Datetime(
        'Horário da coleta', readonly=False, default=_default_EAN_hemoglobina_coleta_horario
    )

    def _write_EAN_hemoglobina_coleta_horario(self):
        self._set_result('EAN17', 'EAN-02-01', self.EAN_hemoglobina_coleta_horario)

    def _default_EAN_hemoglobina_coleta_resp(self):
        return self._get_default('EAN17', 'EAN-02-02')
    EAN_hemoglobina_coleta_resp = fields.Char(
        'Responsável pela coleta', readonly=False, default=_default_EAN_hemoglobina_coleta_resp
    )

    def _write_EAN_hemoglobina_coleta_resp(self):
        self._set_result('EAN17', 'EAN-02-02', self.EAN_hemoglobina_coleta_resp)

    @api.onchange('EAN_hemoglobina_coleta_resp')
    def onchange_EAN_hemoglobina_coleta_resp(self):
        employee_model = self.env['hr.employee']
        if self.EAN_hemoglobina_coleta_resp is not False:
            employee_search = employee_model.search([
                ('code', '=', self.EAN_hemoglobina_coleta_resp),
            ])
            if employee_search.id is False:
                raise exceptions.ValidationError(
                    'Erro! O Código do Responsável pela coleta não é válido!')

    def _default_EAN_hemoglobina_valor(self):
        return self._get_default('EAN17', 'EAN-02-03')
    EAN_hemoglobina_valor = fields.Char(
        'Valor da Hemoglobina', readonly=False, default=_default_EAN_hemoglobina_valor
    )

    def _write_EAN_hemoglobina_valor(self):
        self._set_result('EAN17', 'EAN-02-03', self.EAN_hemoglobina_valor)

    def _default_EAN_hemoglobina_valor_resp(self):
        return self._get_default('EAN17', 'EAN-02-04')
    EAN_hemoglobina_valor_resp = fields.Char(
        'Responsável pela dosagem', readonly=False, default=_default_EAN_hemoglobina_valor_resp
    )

    def _write_EAN_hemoglobina_valor_resp(self):
        self._set_result('EAN17', 'EAN-02-04', self.EAN_hemoglobina_valor_resp)

    @api.onchange('EAN_hemoglobina_valor_resp')
    def onchange_EAN_hemoglobina_valor_resp(self):
        employee_model = self.env['hr.employee']
        if self.EAN_hemoglobina_valor_resp is not False:
            employee_search = employee_model.search([
                ('code', '=', self.EAN_hemoglobina_valor_resp),
            ])
            if employee_search.id is False:
                raise exceptions.ValidationError(
                    'Erro! O Código do Responsável pela dosagem não é válido!')

    def _default_EAN_hemoglobina_interpretacao(self):
        return self._get_default('EAN17', 'EAN-02-05')
    EAN_hemoglobina_interpretacao = fields.Selection([
        ('Normal', 'Normal'),
        ('Abaixo do normal (anemia)', 'Abaixo do normal (anemia)'),
        ('Acima do normal', 'Acima do normal'),
    ], 'Interpretação do Resultado de Hemoglobina', readonly=False, default=_default_EAN_hemoglobina_interpretacao)

    def _write_EAN_hemoglobina_interpretacao(self):
        self._set_result('EAN17', 'EAN-02-05', self.EAN_hemoglobina_interpretacao)

    def _default_EAN_obs(self):
        return self._get_default('EAN17', 'EAN-02-06')
    EAN_obs = fields.Char(
        'Observações', readonly=False, default=_default_EAN_obs
    )

    def _write_EAN_obs(self):
        self._set_result('EAN17', 'EAN-02-06', self.EAN_obs)

    def _default_is_EPC(self):
        active_id = self.env['myo.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EPC17':
            is_EPC = True
        else:
            is_EPC = False
        return is_EPC
    is_EPC = fields.Boolean('Is EPC', readonly=True, default=_default_is_EPC)

    @api.multi
    def do_result_update(self):
        self.ensure_one()

        active_id = self.env['myo.lab_test.result'].browse(self._context.get('active_id'))

        if active_id.lab_test_type_id.code == 'EAN17':

            self._write_EAN_peso()
            self._write_EAN_peso_resp()
            self._write_EAN_altura()
            self._write_EAN_altura_resp()
            self._write_EAN_hemoglobina_coleta_horario()
            self._write_EAN_hemoglobina_coleta_resp()
            self._write_EAN_hemoglobina_valor()
            self._write_EAN_hemoglobina_valor_resp()
            self._write_EAN_hemoglobina_interpretacao()
            self._write_EAN_obs()

        return True

    @api.multi
    def do_reopen_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,  # this model
            'res_id': self.id,  # the current wizard record
            'view_type': 'form',
            'view_mode': 'form, tree',
            'target': 'new'}

    @api.multi
    def do_populate_marked_persons(self):
        self.ensure_one()
        self.person_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
