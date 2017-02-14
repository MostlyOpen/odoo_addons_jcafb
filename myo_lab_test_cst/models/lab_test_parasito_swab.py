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


class LabTestParasitoSWAB(models.Model):
    _name = "myo.lab_test.parasito_swab"

    access_id = fields.Integer('Access ID', help="Access ID")
    lab_test_person_id = fields.Many2one(
        'myo.lab_test.person',
        'Related Lab Test Person',
        ondelete='restrict'
    )

    request_code_parasito = fields.Char('Lab Request Code (Parasito)')
    request_id_parasito = fields.Many2one(
        'myo.lab_test.request',
        'Related Lab Test Request (Parasito)'
    )
    date_parasito = fields.Char("Data (Parasito)")
    resultado_parasito = fields.Char("Resultado Parasito")
    metodos_parasito = fields.Char("Métodos Parasito")
    entrada_parasito = fields.Char("Entrada_Parasito")
    saida_parasito = fields.Char("Saida_Parasito")
    laudo_so_parasito = fields.Char("Laudo só parasito")
    resultado_parasito_2 = fields.Char("Resultado Parasito")
    result_liberado_1a = fields.Char("Resultado liberado 1a")
    result_liberado_1b = fields.Char("Resultado liberado 1b")
    result_liberado_1c = fields.Char("Resultado liberado 1c")
    result_liberado_1d = fields.Char("Resultado liberado 1d")
    result_liberado_1e = fields.Char("Resultado liberado 1e")
    result_liberado_1f = fields.Char("Resultado liberado 1f")
    result_liberado_2a = fields.Char("Resultado liberado 2a")
    result_liberado_2b = fields.Char("Resultado liberado 2b")
    result_liberado_2c = fields.Char("Resultado liberado 2c")
    result_liberado_2d = fields.Char("Resultado liberado 2d")
    result_liberado_2e = fields.Char("Resultado liberado 2e")
    result_liberado_2f = fields.Char("Resultado liberado 2f")
    obs_interno_parasito = fields.Char("obs interno parasito")
    laudo_parasito_swab = fields.Char("Laudo parasito swab")
    realizados = fields.Char("Realizados")
    se_ambos = fields.Char("Se Ambos")
    result_parasito_ritchie = fields.Char("Resultado Parasito Ritchie")
    examinador_ritchie = fields.Char("Examinador Ritchie")
    result_parasito_hoffmann = fields.Char("Resultado Parasito Hoffmann")
    examinador_hoffmann = fields.Char("Examinador Hoffmann")
    status_parasito = fields.Char("Status Parasito")

    request_code_swab = fields.Char('Lab Request Code (SWAB)')
    request_id_swab = fields.Many2one(
        'myo.lab_test.request',
        'Related Lab Test Request (SWAB)'
    )
    date_swab = fields.Char("Data (SWAB)")
    entrada_swab = fields.Char("Entrada Swab")
    saida_swab = fields.Char("Saida Swab")
    metodo_swab = fields.Char("Método Swab")
    result_swab = fields.Char("Resultado swab")
    laudo_so_swab = fields.Char("Laudo só swab")
    examinador_swab = fields.Char("Examinador Swab")
    status_swab = fields.Char("Status Swab")

    farmaceutico_respons = fields.Char('Farmacêutico Responsável')

    notes = fields.Text(string='Notes')
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the lab test parasito_swab without removing it.",
        default=1
    )

    _rec_name = 'access_id'

    _order = 'access_id'


class LabTestPerson(models.Model):
    _inherit = 'myo.lab_test.person'

    lab_test_parasito_swab_ids = fields.One2many(
        'myo.lab_test.parasito_swab',
        'lab_test_person_id',
        'Exames de Parasito e SWAB'
    )
    count_lab_test_parasito_swab = fields.Integer(
        'Number of Exames de Parasito e SWAB',
        compute='_compute_count_lab_test_parasito_swab'
    )

    @api.depends('lab_test_parasito_swab_ids')
    def _compute_count_lab_test_parasito_swab(self):
        for r in self:
            r.count_lab_test_parasito_swab = len(r.lab_test_parasito_swab_ids)
