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


class LabTestResultUrina(models.Model):
    _name = "myo.lab_test.result.urina"
    _log_access = False

    person_code = fields.Char(string='Person Code', required=True)
    address_code = fields.Char(string='Address Code')
    lab_test_code = fields.Char(string='Lab Test Code')
    lab_test_type = fields.Char(string='Lab Test Type')

    gender = fields.Char(string='Gender')
    age = fields.Char(string='Age')
    person_category = fields.Char(string='Person Category')
    person_status = fields.Char(string='Person Status')
    address_city = fields.Char(string='Cidade')
    address_category = fields.Char(string='Address Category')
    address_ditrict = fields.Char(string='Address District')

    EUR_02_01 = fields.Char(
        string='EUR-02-01',
        help='Volume'
    )
    EUR_02_02 = fields.Char(
        string='EUR-02-02',
        help='Densidade'
    )
    EUR_02_03 = fields.Char(
        string='EUR-02-03',
        help='Aspecto'
    )
    EUR_02_04 = fields.Char(
        string='EUR-02-04',
        help='Cor'
    )
    EUR_02_05 = fields.Char(
        string='EUR-02-05',
        help='Odor'
    )

    EUR_03_01 = fields.Char(
        string='EUR-03-01',
        help='ph'
    )
    EUR_03_02 = fields.Char(
        string='EUR-03-02',
        help='Proteínas'
    )
    EUR_03_03 = fields.Char(
        string='EUR-03-03',
        help='Glicose'
    )
    EUR_03_04 = fields.Char(
        string='EUR-03-04',
        help='Cetona'
    )
    EUR_03_05 = fields.Char(
        string='EUR-03-05',
        help='Pigmentos biliares'
    )
    EUR_03_06 = fields.Char(
        string='EUR-03-06',
        help='Sangue'
    )
    EUR_03_07 = fields.Char(
        string='EUR-03-07',
        help='Urobilinogênio'
    )
    EUR_03_08 = fields.Char(
        string='EUR-03-08',
        help='Nitrito'
    )

    EUR_04_01 = fields.Char(
        string='EUR-04-01',
        help='Células Epiteliais'
    )
    EUR_04_02 = fields.Char(
        string='EUR-04-02',
        help='Muco'
    )
    EUR_04_03 = fields.Char(
        string='EUR-04-03',
        help='Cristais'
    )
    EUR_04_04 = fields.Char(
        string='EUR-04-04',
        help='Leucócitos'
    )
    EUR_04_05 = fields.Char(
        string='EUR-04-05',
        help='Hemácias'
    )
    EUR_04_06 = fields.Char(
        string='EUR-04-06',
        help='Cilindros'
    )
    EUR_04_07 = fields.Char(
        string='EUR-04-07',
        help='Cilindros Hialinos'
    )
    EUR_04_08 = fields.Char(
        string='EUR-04-08',
        help='Cilindros Granulosos'
    )
    EUR_04_09 = fields.Char(
        string='EUR-04-09',
        help='Cilindros Leucocitários'
    )
    EUR_04_10 = fields.Char(
        string='EUR-04-10',
        help='Cilindros Hemáticos'
    )
    EUR_04_11 = fields.Char(
        string='EUR-04-11',
        help='Cilindros Céreos'
    )
    EUR_04_12 = fields.Char(
        string='EUR-04-12',
        help='Outros tipos de Cilindros'
    )

    EUR_05_01 = fields.Char(
        string='EUR-05-01',
        help='Observações'
    )

    notes = fields.Text(string='Notes')
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the lab test result urina without removing it.",
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
