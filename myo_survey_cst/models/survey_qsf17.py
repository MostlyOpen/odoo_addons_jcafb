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


class SurveyQSF17(models.Model):
    _name = "myo.survey.qsf17"
    _log_access = False

    person_code = fields.Char(string='Person Code', required=True)
    address_code = fields.Char(string='Address Code')
    document_code = fields.Char(string='Document Code')
    survey_title = fields.Char(string='Survey Title')

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

    gender = fields.Char(string='Gender')
    age = fields.Char(string='Age')
    person_category = fields.Char(string='Person Category')
    person_status = fields.Char(string='Person Status')
    address_city = fields.Char(string='Cidade')
    address_category = fields.Char(string='Address Category')
    address_ditrict = fields.Char(string='Address District')

    QSF17_05_01 = fields.Char(
        string='[QSF17_05_01]',
        help='De onde vem a água da casa?'
    )
    QSF17_05_02 = fields.Char(
        string='[QSF17_05_02]',
        help='Existe contato das pessoas da casa com o local de armazenamento (por exemplo caixa d’água)?'
    )
    QSF17_05_03 = fields.Char(
        string='[QSF17_05_03]',
        help='Na falta de água, onde é obtida?'
    )
    QSF17_05_04 = fields.Char(
        string='[QSF17_05_04]',
        help='Antes do consumo de água, é realizado algum dos tratamentos abaixo? (pode-se marcar mais de uma opção)'
    )
    QSF17_06_06 = fields.Char(
        string='[QSF17_06_06]',
        help='Ao preparar os alimentos crus (pode-se marcar mais de uma opção), costumam:'
    )
    QSF17_07_01 = fields.Char(
        string='[QSF17_07_01]',
        help='Costumam tomar medicamentos sem receita médica? (por exemplo, pegar remédio com a vizinha, etc. '
             'Desconsiderar remédios que não necessitam de receita)'
    )
    QSF17_07_04 = fields.Char(
        string='[QSF17_07_04]',
        help='Onde guardam os remédios?'
    )
    QSF17_07_05 = fields.Char(
        string='[QSF17_07_05]',
        help='Como descartam os medicamentos?'
    )
    QSF17_08_01 = fields.Char(
        string='[QSF17_08_01]',
        help='Conhecem algum verme (parasitose)?'
    )
    QSF17_08_03 = fields.Char(
        string='[QSF17_08_03]',
        help='Alguém na casa já pegou verme? Qual?'
    )

    notes = fields.Text(string='Notes')
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the survey qsf17 without removing it.",
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
