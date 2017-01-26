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


class LabTestPerson(models.Model):
    _name = "myo.lab_test.person"

    access_id = fields.Integer('Access ID', help="Access ID")
    name = fields.Char('Person Name', required=True, help="Person Name")
    code = fields.Char('Person Code', required=False, help="Person Code")
    person_id = fields.Many2one('myo.person', 'Related Person', help="Related Person")
    notes = fields.Text(string='Notes')
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the lab test person without removing it.",
        default=1
    )

    # _sql_constraints = [
    #     (
    #         'name_uniq',
    #         'UNIQUE (name)',
    #         'Error! The Person Name must be unique!'
    #     ),
    # ]

    _order = 'name'
