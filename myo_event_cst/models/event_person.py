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


class EventPerson(models.Model):
    _name = 'myo.event.person'

    event_id = fields.Many2one('myo.event', string='Event',
                               help='Event', required=False)
    person_id = fields.Many2one('myo.person', string='Person')
    role = fields.Many2one('myo.event.participant.role', 'Role', required=False)
    notes = fields.Text(string='Notes')
    active = fields.Boolean('Active',
                            help="If unchecked, it will allow you to hide the event person without removing it.",
                            default=1)


class Event(models.Model):
    _inherit = 'myo.event'

    person_ids = fields.One2many(
        'myo.event.person',
        'event_id',
        'Persons'
    )


class Person(models.Model):
    _inherit = 'myo.person'

    event_person_ids = fields.One2many(
        'myo.event.person',
        'person_id',
        'Event Persons'
    )
