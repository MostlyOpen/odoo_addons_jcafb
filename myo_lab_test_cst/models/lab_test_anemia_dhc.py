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

# from datetime import datetime

from openerp import api, fields, models


class LabTestAnemiaDHC(models.Model):
    _name = "myo.lab_test.anemia_dhc"

    # name = fields.Char('Lab Request Code', required=True, help="Lab Request Code")
    access_id = fields.Integer('Access ID', help="Access ID")
    lab_test_person_id = fields.Many2one(
        'myo.lab_test.person',
        'Related Lab Test Person',
        ondelete='restrict'
    )

    request_code_anemia = fields.Char('Lab Request Code (Anemia)')
    request_id_anemia = fields.Many2one(
        'myo.lab_test.request',
        'Related Lab Test Request (Anemia)'
    )
    result_id_anemia = fields.Many2one(
        'myo.lab_test.result',
        'Related Lab Test Result (Anemia)'
    )
    farmaceutico_anemia = fields.Char('Farmacêutico Responsável (Anemia)')
    date_anemia = fields.Char("Data (Anemia)")
    peso_anemia = fields.Char("Peso (Anemia)")
    altura_anemia = fields.Char("Altura (Anemia)")
    hemoglobina_anemia = fields.Char("Valor da Hemoglobina (Anemia)")
    obs_anemia = fields.Char("Observação (Anemia)")
    obs2_anemia = fields.Char("Observação 2 (Anemia)")

    request_code_dhc = fields.Char('Lab Request Code (DHC)')
    request_id_dhc = fields.Many2one(
        'myo.lab_test.request',
        'Related Lab Test Request (DHC)'
    )
    result_id_dhc = fields.Many2one(
        'myo.lab_test.result',
        'Related Lab Test Result (DHC)'
    )
    farmaceutico_dhc = fields.Char('Farmacêutico Responsável (DHC)')
    date_dhc = fields.Char("Data (DHC)")
    peso_dhc = fields.Char("Peso (DHC)")
    altura_dhc = fields.Char("Altura (DHC)")
    circ_abdm_dhc = fields.Char("Circunferência Abdominal (DHC)")
    pressao_sist_dhc = fields.Char("Pressão Sistólica (DHC)")
    pressao_diast_dhc = fields.Char("Pressão Diastólica (DHC)")
    obs_pressao_dhc = fields.Char("Observação Pressão (DHC)")
    glicemia_dhc = fields.Char("Glicemia (DHC)")
    obs_glicemia_dhc = fields.Char("Observação Glicemia (DHC)")
    colesterol_dhc = fields.Char("Colesterol (DHC)")
    obs_colesterol_dhc = fields.Char("Observação Colesterol (DHC)")
    obs_dhc = fields.Char("Observação (DHC)")

    notes = fields.Text(string='Notes')
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the lab test anemia_dhc without removing it.",
        default=1
    )

    # _sql_constraints = [
    #     (
    #         'name_uniq',
    #         'UNIQUE (name)',
    #         'Error! The Lab Request Code must be unique!'
    #     ),
    # ]

    _rec_name = 'access_id'

    _order = 'access_id'


class LabTestPerson(models.Model):
    _inherit = 'myo.lab_test.person'

    lab_test_anemia_dhc_ids = fields.One2many(
        'myo.lab_test.anemia_dhc',
        'lab_test_person_id',
        'Exames de Anemia e DHC'
    )
    count_lab_test_anemia_dhc = fields.Integer(
        'Number of Exames de Anemia e DHC',
        compute='_compute_count_lab_test_anemia_dhc'
    )

    @api.depends('lab_test_anemia_dhc_ids')
    def _compute_count_lab_test_anemia_dhc(self):
        for r in self:
            r.count_lab_test_anemia_dhc = len(r.lab_test_anemia_dhc_ids)
