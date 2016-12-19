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


class SummaryAddressLabTestRequest(models.Model):
    _name = 'myo.summary.address.lab_test.request'

    summary_id = fields.Many2one('myo.summary', string='Summary')
    address_id = fields.Many2one('myo.address', string='Address')
    person_id = fields.Many2one('myo.person', 'Person', help="Patient")
    lab_test_type_id = fields.Many2one('myo.lab_test.type', 'Lab Test Type')
    lab_test_request_id = fields.Many2one('myo.lab_test.request', string='Lab Test Request')
    lab_test_request_state = fields.Selection(
        'Lab Test Request Status',
        related='lab_test_request_id.state', store=False
    )
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the summary address lab test request without removing it.",
        default=1
    )

    _order = 'person_id'


class Summary(models.Model):
    _inherit = 'myo.summary'

    summary_address_lab_test_request_ids = fields.One2many(
        'myo.summary.address.lab_test.request',
        'summary_id',
        'Address Lab Test Requests'
    )
