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


class Summary(models.Model):
    _inherit = 'myo.summary'

    is_address_summary = fields.Boolean(
        'Is Address Summary',
        help="If checked, the Summary is for an Address.",
        default=0
    )
    address_id = fields.Many2one('myo.address', 'Address', ondelete='restrict')
    address_code = fields.Char('Address Code', related='address_id.code', readonly=True)
    address_category_ids = fields.Many2many(
        string='Address Categories',
        related='address_id.category_ids',
        store=False
    )
    address_category_names = fields.Char('Address Categories', related='address_id.category_ids.name', store=True)
    address_district = fields.Char('Address District', related='address_id.district', store=True)
    is_person_summary = fields.Boolean(
        'Is Person Summary',
        help="If checked, the Summary is for a Person.",
        default=0
    )
    person_id = fields.Many2one('myo.person', 'Person', ondelete='restrict')
    person_code = fields.Char('Person Code', related='person_id.code', readonly=True)
    person_category_ids = fields.Many2many(
        string='Person Categories',
        related='person_id.category_ids',
        store=False
    )
    person_category_names = fields.Char('Person Categories', related='person_id.category_ids.name', store=True)

    _defaults = {
        'active_log': True,
    }
