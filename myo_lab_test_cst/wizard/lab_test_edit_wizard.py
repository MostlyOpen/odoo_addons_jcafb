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

# from openerp import exceptions

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

    #
    # EAN17
    #

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
        employee_model = self.env['hr.employee']
        code = self._get_default('EAN17', 'EAN-01-02')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EAN_peso_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida do Peso',
        readonly=False,
        default=_default_EAN_peso_resp
    )

    def _write_EAN_peso_resp(self):
        self._set_result('EAN17', 'EAN-01-02', self.EAN_peso_resp.name + ' [' + self.EAN_peso_resp.code + ']')

    def _default_EAN_altura(self):
        return self._get_default('EAN17', 'EAN-01-03')
    EAN_altura = fields.Char(
        'Altura', readonly=False, default=_default_EAN_altura
    )

    def _write_EAN_altura(self):
        self._set_result('EAN17', 'EAN-01-03', self.EAN_altura)

    def _default_EAN_altura_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EAN17', 'EAN-01-04')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EAN_altura_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida da Altura',
        readonly=False,
        default=_default_EAN_altura_resp
    )

    def _write_EAN_altura_resp(self):
        self._set_result('EAN17', 'EAN-01-04', self.EAN_altura_resp.name + ' [' + self.EAN_altura_resp.code + ']')

    # def _default_EAN_altura_resp(self):
    #     return self._get_default('EAN17', 'EAN-01-04')
    # EAN_altura_resp = fields.Char(
    #     'Responsável pela medida da Altura', readonly=False, default=_default_EAN_altura_resp
    # )

    # def _write_EAN_altura_resp(self):
    #     self._set_result('EAN17', 'EAN-01-04', self.EAN_altura_resp)

    # @api.onchange('EAN_altura_resp')
    # def onchange_EAN_altura_resp(self):
    #     employee_model = self.env['hr.employee']
    #     if self.EAN_altura_resp is not False:
    #         employee_search = employee_model.search([
    #             ('code', '=', self.EAN_altura_resp),
    #         ])
    #         if employee_search.id is False:
    #             raise exceptions.ValidationError(
    #                 'Erro! O Código do Responsável pela medida da Altura não é válido!')

    def _default_EAN_hemoglobina_coleta_horario(self):
        return self._get_default('EAN17', 'EAN-02-01')
    EAN_hemoglobina_coleta_horario = fields.Datetime(
        'Horário da coleta', readonly=False, default=_default_EAN_hemoglobina_coleta_horario
    )

    def _write_EAN_hemoglobina_coleta_horario(self):
        self._set_result('EAN17', 'EAN-02-01', self.EAN_hemoglobina_coleta_horario)

    def _default_EAN_hemoglobina_coleta_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EAN17', 'EAN-02-02')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EAN_hemoglobina_coleta_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela coleta',
        readonly=False,
        default=_default_EAN_hemoglobina_coleta_resp
    )

    def _write_EAN_hemoglobina_coleta_resp(self):
        self._set_result(
            'EAN17', 'EAN-02-02',
            self.EAN_hemoglobina_coleta_resp.name + ' [' + self.EAN_hemoglobina_coleta_resp.code + ']'
        )

    # def _default_EAN_hemoglobina_coleta_resp(self):
    #     return self._get_default('EAN17', 'EAN-02-02')
    # EAN_hemoglobina_coleta_resp = fields.Char(
    #     'Responsável pela coleta', readonly=False, default=_default_EAN_hemoglobina_coleta_resp
    # )

    # def _write_EAN_hemoglobina_coleta_resp(self):
    #     self._set_result('EAN17', 'EAN-02-02', self.EAN_hemoglobina_coleta_resp)

    # @api.onchange('EAN_hemoglobina_coleta_resp')
    # def onchange_EAN_hemoglobina_coleta_resp(self):
    #     employee_model = self.env['hr.employee']
    #     if self.EAN_hemoglobina_coleta_resp is not False:
    #         employee_search = employee_model.search([
    #             ('code', '=', self.EAN_hemoglobina_coleta_resp),
    #         ])
    #         if employee_search.id is False:
    #             raise exceptions.ValidationError(
    #                 'Erro! O Código do Responsável pela coleta não é válido!')

    def _default_EAN_hemoglobina_valor(self):
        return self._get_default('EAN17', 'EAN-02-03')
    EAN_hemoglobina_valor = fields.Char(
        'Valor da Hemoglobina', readonly=False, default=_default_EAN_hemoglobina_valor
    )

    def _write_EAN_hemoglobina_valor(self):
        self._set_result('EAN17', 'EAN-02-03', self.EAN_hemoglobina_valor)

    def _default_EAN_hemoglobina_valor_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EAN17', 'EAN-02-04')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EAN_hemoglobina_valor_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela dosagem',
        readonly=False,
        default=_default_EAN_hemoglobina_valor_resp
    )

    def _write_EAN_hemoglobina_valor_resp(self):
        self._set_result(
            'EAN17', 'EAN-02-04',
            self.EAN_hemoglobina_valor_resp.name + ' [' + self.EAN_hemoglobina_valor_resp.code + ']'
        )

    # def _default_EAN_hemoglobina_valor_resp(self):
    #     return self._get_default('EAN17', 'EAN-02-04')
    # EAN_hemoglobina_valor_resp = fields.Char(
    #     'Responsável pela dosagem', readonly=False, default=_default_EAN_hemoglobina_valor_resp
    # )

    # def _write_EAN_hemoglobina_valor_resp(self):
    #     self._set_result('EAN17', 'EAN-02-04', self.EAN_hemoglobina_valor_resp)

    # @api.onchange('EAN_hemoglobina_valor_resp')
    # def onchange_EAN_hemoglobina_valor_resp(self):
    #     employee_model = self.env['hr.employee']
    #     if self.EAN_hemoglobina_valor_resp is not False:
    #         employee_search = employee_model.search([
    #             ('code', '=', self.EAN_hemoglobina_valor_resp),
    #         ])
    #         if employee_search.id is False:
    #             raise exceptions.ValidationError(
    #                 'Erro! O Código do Responsável pela dosagem não é válido!')

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

    #
    # EDH17
    #

    def _default_is_EDH(self):
        active_id = self.env['myo.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EDH17':
            is_EDH = True
        else:
            is_EDH = False
        return is_EDH
    is_EDH = fields.Boolean('Is EDH', readonly=True, default=_default_is_EDH)

    def _default_EDH_tempo_jejum(self):
        return self._get_default('EDH17', 'EDH-01-01')
    EDH_tempo_jejum = fields.Char(
        'Tempo de Jejum', readonly=False, default=_default_EDH_tempo_jejum
    )

    def _write_EDH_tempo_jejum(self):
        self._set_result('EDH17', 'EDH-01-01', self.EDH_tempo_jejum)

    #
    # ECP17
    #

    def _default_is_ECP(self):
        active_id = self.env['myo.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'ECP17':
            is_ECP = True
        else:
            is_ECP = False
        return is_ECP
    is_ECP = fields.Boolean('Is ECP', readonly=True, default=_default_is_ECP)

    def _default_ECP_data_entrada_material(self):
        return self._get_default('ECP17', 'ECP-01-01')
    ECP_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_ECP_data_entrada_material
    )

    def _write_ECP_data_entrada_material(self):
        self._set_result('ECP17', 'ECP-01-01', self.ECP_data_entrada_material)

    def _default_ECP_liberacao_resultado(self):
        return self._get_default('ECP17', 'ECP-01-02')
    ECP_liberacao_resultado = fields.Date(
        'Liberação do Resultado', readonly=False, default=_default_ECP_liberacao_resultado
    )

    def _write_ECP_liberacao_resultado(self):
        self._set_result('ECP17', 'ECP-01-02', self.ECP_liberacao_resultado)

    def _default_ECP_resultado(self):
        return self._get_default('ECP17', 'ECP-01-03')
    ECP_resultado = fields.Selection([
        ('Positivo', 'Positivo'),
        ('Negativo', 'Negativo'),
        ('Não Realizado', 'Não Realizado'),
    ], 'Resultado', readonly=False, default=_default_ECP_resultado)

    def _write_ECP_resultado(self):
        self._set_result('ECP17', 'ECP-01-03', self.ECP_resultado)

    def _default_ECP_obs(self):
        return self._get_default('ECP17', 'ECP-01-04')
    ECP_obs = fields.Char(
        'Observações', readonly=False, default=_default_ECP_obs
    )

    def _write_ECP_obs(self):
        self._set_result('ECP17', 'ECP-01-04', self.ECP_obs)

    def _default_ECP_metodo_utilizado(self):
        return self._get_default('ECP17', 'ECP-01-05')
    ECP_metodo_utilizado = fields.Selection([
        ('Ritchie', 'Ritchie'),
        ('Hoffmann', 'Hoffmann'),
        ('Ritchie e Hoffmann', 'Ritchie e Hoffmann'),
    ], 'Medtodologia(s) Empregada(s)', readonly=False, default=_default_ECP_metodo_utilizado)

    def _write_ECP_metodo_utilizado(self):
        self._set_result('ECP17', 'ECP-01-05', self.ECP_metodo_utilizado)

    #
    # EEV17
    #

    def _default_is_EEV(self):
        active_id = self.env['myo.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EEV17':
            is_EEV = True
        else:
            is_EEV = False
        return is_EEV
    is_EEV = fields.Boolean('Is EEV', readonly=True, default=_default_is_EEV)

    def _default_EEV_data_entrada_material(self):
        return self._get_default('EEV17', 'EEV-01-01')
    EEV_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_EEV_data_entrada_material
    )

    def _write_EEV_data_entrada_material(self):
        self._set_result('EEV17', 'EEV-01-01', self.EEV_data_entrada_material)

    def _default_EEV_liberacao_resultado(self):
        return self._get_default('EEV17', 'EEV-01-02')
    EEV_liberacao_resultado = fields.Date(
        'Liberação do Resultado', readonly=False, default=_default_EEV_liberacao_resultado
    )

    def _write_EEV_liberacao_resultado(self):
        self._set_result('EEV17', 'EEV-01-02', self.EEV_liberacao_resultado)

    def _default_EEV_resultado(self):
        return self._get_default('EEV17', 'EEV-01-03')
    EEV_resultado = fields.Selection([
        ('Positivo', 'Positivo'),
        ('Negativo', 'Negativo'),
        ('Não Realizado', 'Não Realizado'),
    ], 'Resultado', readonly=False, default=_default_EEV_resultado)

    def _write_EEV_resultado(self):
        self._set_result('EEV17', 'EEV-01-03', self.EEV_resultado)

    def _default_EEV_examinador(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EEV17', 'EEV-01-04')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EEV_examinador = fields.Many2one(
        'hr.employee',
        string='Examinador',
        readonly=False,
        default=_default_EEV_examinador
    )

    def _write_EEV_examinador(self):
        self._set_result(
            'EEV17', 'EEV-01-04',
            self.EEV_examinador.name + ' [' + self.EEV_examinador.code + ']'
        )

    def _default_EEV_metodo_utilizado(self):
        return self._get_default('EEV17', 'EEV-01-05')
    EEV_metodo_utilizado = fields.Selection([
        ('Swab Anal', 'Swab Anal'),
        ('Outro', 'Outro'),
    ], 'Método utilizado', readonly=False, default=_default_EEV_metodo_utilizado)

    def _write_EEV_metodo_utilizado(self):
        self._set_result('EEV17', 'EEV-01-05', self.EEV_metodo_utilizado)

    def _default_EEV_obs(self):
        return self._get_default('EEV17', 'EEV-01-06')
    EEV_obs = fields.Char(
        'Observações', readonly=False, default=_default_EEV_obs
    )

    def _write_EEV_obs(self):
        self._set_result('EEV17', 'EEV-01-06', self.EEV_obs)

    def _default_ECP_ritchie_resultado(self):
        return self._get_default('ECP17', 'ECP-02-01')
    ECP_ritchie_resultado = fields.Selection([
        ('Não Realizado', 'Não Realizado'),
        ('Negativo', 'Negativo'),
        ('Cistos de Endolimax nana', 'Cistos de Endolimax nana'),
        ('Cistos de Entamoeba coli', 'Cistos de Entamoeba coli'),
        ('Cistos de Entamoeba histolytica', 'Cistos de Entamoeba histolytica'),
        ('Cistos de Giardia lamblia', 'Cistos de Giardia lamblia'),
        ('Cistos de Iodamoeba butschlii', 'Cistos de Iodamoeba butschlii'),
        ('Cistos de Chilomastix mesnil', 'Cistos de Chilomastix mesnil'),
        ('Oocistos de Isospora belli', 'Oocistos de Isospora belli'),
        ('Ovos de Ascaris lumbricoides', 'Ovos de Ascaris lumbricoides'),
        ('Ovos de Ancilostomídeo', 'Ovos de Ancilostomídeo'),
        ('Ovos de Trichuris trichiura', 'Ovos de Trichuris trichiura'),
        ('Ovos de Taenia sp', 'Ovos de Taenia sp'),
        ('Ovos de Hymenolepis nana', 'Ovos de Hymenolepis nana'),
        ('Ovos de Schistosoma mansoni', 'Ovos de Schistosoma mansoni'),
        ('Ovos de Enterobius vermicularis', 'Ovos de Enterobius vermicularis'),
        ('Larvas de Strongyloides stercoralis', 'Larvas de Strongyloides stercoralis'),
        ('Outro', 'Outro'),
    ], 'Resultado', readonly=False, default=_default_ECP_ritchie_resultado)

    def _write_ECP_ritchie_resultado(self):
        self._set_result('ECP17', 'ECP-02-01', self.ECP_ritchie_resultado)

    #
    # EUR17
    #

    def _default_is_EUR(self):
        active_id = self.env['myo.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EUR17':
            is_EUR = True
        else:
            is_EUR = False
        return is_EUR
    is_EUR = fields.Boolean('Is EUR', readonly=True, default=_default_is_EUR)

    def _default_EUR_data_entrada_material(self):
        return self._get_default('EUR17', 'EUR-01-01')
    EUR_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_EUR_data_entrada_material
    )

    def _write_EUR_data_entrada_material(self):
        self._set_result('EUR17', 'EUR-01-01', self.EUR_data_entrada_material)

    def _default_EUR_liberacao_resultado(self):
        return self._get_default('EUR17', 'EUR-01-02')
    EUR_liberacao_resultado = fields.Date(
        'Liberação do Resultado', readonly=False, default=_default_EUR_liberacao_resultado
    )

    def _write_EUR_liberacao_resultado(self):
        self._set_result('EUR17', 'EUR-01-02', self.EUR_liberacao_resultado)

    def _default_EUR_examinador(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EUR17', 'EUR-01-03')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EUR_examinador = fields.Many2one(
        'hr.employee',
        string='Examinador',
        readonly=False,
        default=_default_EUR_examinador
    )

    def _write_EUR_examinador(self):
        self._set_result(
            'EUR17', 'EUR-01-03',
            self.EUR_examinador.name + ' [' + self.EUR_examinador.code + ']'
        )

    def _default_EUR_volume(self):
        return self._get_default('EUR17', 'EUR-02-01')
    EUR_volume = fields.Char(
        'Volume', readonly=False, default=_default_EUR_volume
    )

    def _write_EUR_volume(self):
        self._set_result('EUR17', 'EUR-02-01', self.EUR_volume)

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

        if active_id.lab_test_type_id.code == 'EDH17':

            self._write_EDH_tempo_jejum()

        if active_id.lab_test_type_id.code == 'ECP17':

            self._write_ECP_data_entrada_material()
            self._write_ECP_liberacao_resultado()
            self._write_ECP_resultado()
            self._write_ECP_obs()
            self._write_ECP_metodo_utilizado()
            self._write_ECP_ritchie_resultado()

        if active_id.lab_test_type_id.code == 'EEV17':

            self._write_EEV_data_entrada_material()
            self._write_EEV_liberacao_resultado()
            self._write_EEV_resultado()
            self._write_EEV_examinador()
            self._write_EEV_metodo_utilizado()
            self._write_EEV_obs()

        if active_id.lab_test_type_id.code == 'EUR17':

            self._write_EUR_data_entrada_material()
            self._write_EUR_liberacao_resultado()
            self._write_EUR_examinador()
            self._write_EUR_volume()

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
