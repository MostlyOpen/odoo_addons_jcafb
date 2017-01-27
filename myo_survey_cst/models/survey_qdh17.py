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

from openerp import fields, models


class SurveyQDH17(models.Model):
    _name = "myo.survey.qdh17"
    _log_access = False

    person_code = fields.Char('Person Code', required=True)
    address_code = fields.Char('Address Code')
    document_code = fields.Char('Document Code')
    survey_title = fields.Char('Survey Title')

    # person_id = fields.Many2one('myo.person', 'Related Person')
    # address_id = fields.Many2one('myo.address', 'Related Address')
    # document_id = fields.Many2one('myo.document', 'Related Document')
    # survey_id = fields.Many2one('survey.survey', 'Survey Type')

    # survey_user_input_id = fields.Many2one('survey.user_input', 'Survey User Input')

    # survey_description = fields.Html(
    #     'Survey Type Description',
    #     related='survey_id.description',
    #     store=False,
    #     readonly=True
    # )

    gender = fields.Char('Gender')
    age = fields.Char('Age')
    person_category = fields.Char('Person Category')
    person_status = fields.Char('Person Status')
    address_city = fields.Char('Cidade')
    address_category = fields.Char('Address Category')
    address_ditrict = fields.Char('Address District')

    QDH17_03_01 = fields.Char('Escolaridade do paciente')
    QDH17_04_07 = fields.Char('Interpretação do valor de IMC')
    QDH17_04_10 = fields.Char('Interpretação do valor de Circunferência Abdominal')
    QDH17_05_05 = fields.Char('Interpretação do valor de Pressão Arteria')
    QDH17_06_03 = fields.Char('Interpretação do valor de Glicemia')
    QDH17_06_06 = fields.Char('Interpretação do valor de Colesterol')
    QDH17_07_01 = fields.Char('Possui DIABETES?')
    QDH17_07_05 = fields.Char('Possui HIPERTENSÃO?')
    QDH17_07_08 = fields.Char('Possui HIPERCOLESTEROLEMIA?')
    QDH17_09_01 = fields.Char('Que motivo(s) o leva(m) a procurar atendimento médico?')
    QDH17_09_02 = fields.Char('O(A) Sr.(a) tem ou teve o hábito de fumar?')
    QDH17_09_04 = fields.Char('Tem o hábito de tomar bebidas alcoólicas?')
    QDH17_09_05 = fields.Char('Pratica uma ou mais das atividades físicas abaixo?')
    QDH17_09_06 = fields.Char('Quantos dias por semana costuma praticar essa atividade?')

    notes = fields.Text(string='Notes')
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the survey qdh17 without removing it.",
        default=1
    )

    _sql_constraints = [
        (
            'person_code_uniq',
            'UNIQUE (person_code)',
            'Error! The Person Code must be unique!'
        ),
    ]

    _rec_name = 'person_code'

    _order = 'person_code'
