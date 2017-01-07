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

from openerp import fields, models


class LabTestRequestDirectMail(models.Model):
    _name = 'myo.lab_test.request.direct_mail'
    _log_access = False

    name = fields.Char('Lab Test Code')
    lab_test_type = fields.Char('Lab Test Type')
    person_responsible = fields.Char('Person Responsible')
    person_name = fields.Char('Person Name')
    person_initials = fields.Char('Person Initials')
    person_code = fields.Char('Person Code')
    person_categories = fields.Char('Person Categories')
    person_reference_age = fields.Char('Person Reference Age')
