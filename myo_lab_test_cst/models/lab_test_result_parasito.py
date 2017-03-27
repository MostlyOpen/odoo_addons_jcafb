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


class LabTestResultParasito(models.Model):
    _name = "myo.lab_test.result.parasito"
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

    ECP_01_03 = fields.Char(
        string='ECP-01-03',
        help='Resultado'
    )
    notes = fields.Text(string='Notes')
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the survey qsc17 without removing it.",
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
