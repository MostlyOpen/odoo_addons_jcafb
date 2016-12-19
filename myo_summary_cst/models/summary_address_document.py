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


class SummaryAddressDocument(models.Model):
    _name = 'myo.summary.address.document'

    summary_id = fields.Many2one('myo.summary', string='Summary')
    address_id = fields.Many2one('myo.address', string='Address')
    person_id = fields.Many2one('myo.person', string='Person')
    document_id = fields.Many2one('myo.document', string='Document')
    document_category_ids = fields.Many2many(
        tring='Document Categories',
        related='document_id.category_ids',
        store=False
    )
    document_state = fields.Selection('Document Status', related='document_id.state', store=False)
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the summary address document without removing it.",
        default=1
    )

    _order = 'person_id'


class Summary(models.Model):
    _inherit = 'myo.summary'

    summary_address_document_ids = fields.One2many(
        'myo.summary.address.document',
        'summary_id',
        'Address Documents'
    )
