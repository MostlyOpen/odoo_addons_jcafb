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


class SummaryAddressEvent(models.Model):
    _name = 'myo.summary.address.event'

    summary_id = fields.Many2one('myo.summary', string='Summary')
    address_id = fields.Many2one('myo.address', string='Address')
    event_id = fields.Many2one('myo.event', string='Event')
    event_category_ids = fields.Many2many(string='Event Categories', related='event_id.category_ids', store=False)
    event_state = fields.Selection('Event Status', related='event_id.state', store=False)
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the summary address event without removing it.",
        default=1
    )


class Summary(models.Model):
    _inherit = 'myo.summary'

    summary_address_event_ids = fields.One2many(
        'myo.summary.address.event',
        'summary_id',
        'Address Events'
    )
