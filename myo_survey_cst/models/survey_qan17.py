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


class SurveyQAN17(models.Model):
    _name = "myo.survey.qan17"
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

    QAN17_03_01 = fields.Char(
        string='[QAN17_03_01]',
        help='Peso'
    )
    QAN17_03_03 = fields.Char(
        string='[QAN17_03_03]',
        help='Altura'
    )
    QAN17_04_03 = fields.Char(
        string='[QAN17_04_03]',
        help='Valor da Hemoglobina'
    )
    QAN17_04_05 = fields.Char(
        string='[QAN17_04_05]',
        help='Interpretação da Hemoglobina'
    )
    QAN17_05_01 = fields.Char(
        string='[QAN17_05_01]',
        help='Já realizou exame para diagnosticar Anemia?'
    )
    QAN17_05_02 = fields.Char(
        string='[QAN17_05_02]',
        help='Já foi diagnosticado com Anemia?'
    )
    QAN17_05_03 = fields.Char(
        string='[QAN17_05_03]',
        help='Ainda tem Anemia?'
    )
    QAN17_05_05 = fields.Char(
        string='[QAN17_05_05]',
        help='Você sabe quais cuidados tomar para evitar a anemia?'
    )

    notes = fields.Text(string='Notes')
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the survey qan17 without removing it.",
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
