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

from openerp import models, fields


class LabTestResult(models.Model):
    _inherit = 'myo.lab_test.result'

    survey_user_input_id = fields.Many2one('survey.user_input', 'Survey User Input', help="Survey User Input")
    base_document_id = fields.Many2one('myo.document', 'Base Document', help="Base Document")
    base_survey_user_input_id = fields.Many2one(
        'survey.user_input',
        'Base Survey User Input',
        help="Base Survey User Input"
    )


class LabTestRequest(models.Model):
    _inherit = 'myo.lab_test.request'

    survey_user_input_id = fields.Many2one('survey.user_input', 'Survey User Input', help="Survey User Input")
