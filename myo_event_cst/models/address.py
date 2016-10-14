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

from openerp import api, fields, models


class Address(models.Model):
    _inherit = 'myo.address'

    event_ids = fields.One2many(
        'myo.event',
        'address_id',
        'Events'
    )
    count_events = fields.Integer(
        'Number of Events',
        compute='_compute_count_events'
    )

    @api.depends('event_ids')
    def _compute_count_events(self):
        for r in self:
            r.count_events = len(r.event_ids)


class Event(models.Model):
    _inherit = 'myo.event'

    address_id = fields.Many2one('myo.address', 'Address', ondelete='restrict')
    event_phone = fields.Char('Phone', related='address_id.phone')
    mobile_phone = fields.Char('Mobile', related='address_id.mobile')
    event_email = fields.Char('Email', related='address_id.email')
