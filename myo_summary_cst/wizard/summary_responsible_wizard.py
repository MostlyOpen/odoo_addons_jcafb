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

import logging

_logger = logging.getLogger(__name__)


class SummaryResponsibleWizard(models.TransientModel):
    _name = 'myo.summary.responsible.wizard'

    summary_ids = fields.Many2many('myo.summary', string='Summaries')
    new_user_id = fields.Many2one('res.users', string='New Responsible')

    @api.multi
    def do_update_responsible(self):
        self.ensure_one()

        summary_model = self.env['myo.summary']

        if self.new_user_id.id is not False:

            new_user_id = self.new_user_id.id

            for summary_reg in self.summary_ids:

                if summary_reg.is_address_summary:

                    summary_reg.user_id = new_user_id

                    summary_reg.address_id.user_id = new_user_id

                    for address_person_reg in summary_reg.summary_address_person_ids:
                        if address_person_reg.person_id.state == 'selected':
                            address_person_reg.person_id.user_id = new_user_id

                    for address_event_reg in summary_reg.summary_address_event_ids:
                        address_event_reg.event_id.user_id = new_user_id

                    for address_document_reg in summary_reg.summary_address_document_ids:
                        address_document_reg.document_id.user_id = new_user_id

                    summary_search = summary_model.search([
                        ('is_person_summary', '=', True),
                        ('address_id', '=', summary_reg.address_id.id),
                    ])
                    for summary_reg_2 in summary_search:
                        if summary_reg_2.person_id.state == 'selected':
                            summary_reg_2.user_id = new_user_id

                if summary_reg.is_person_summary:

                    pass

            return True

        else:

            for summary_reg in self.summary_ids:

                if summary_reg.is_address_summary and \
                   summary_reg.user_id is not False:

                    new_user_id = summary_reg.user_id

                    summary_reg.address_id.user_id = new_user_id

                    for address_person_reg in summary_reg.summary_address_person_ids:
                        if address_person_reg.person_id.state == 'selected':
                            address_person_reg.person_id.user_id = new_user_id

                    for address_event_reg in summary_reg.summary_address_event_ids:
                        address_event_reg.event_id.user_id = new_user_id

                    for address_document_reg in summary_reg.summary_address_document_ids:
                        address_document_reg.document_id.user_id = new_user_id

                    summary_search = summary_model.search([
                        ('is_person_summary', '=', True),
                        ('address_id', '=', summary_reg.address_id.id),
                    ])
                    for summary_reg_2 in summary_search:
                        if summary_reg_2.person_id.state == 'selected':
                            summary_reg_2.user_id = new_user_id

                if summary_reg.is_person_summary:

                    pass

            return True

        # reopen wizard form on same wizard record
        return self.do_reopen_form()

    @api.multi
    def do_reopen_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,  # this model
            'res_id': self.id,  # the current wizard record
            'view_type': 'form',
            'view_mode': 'form, tree',
            'target': 'new'}

    @api.multi
    def do_populate_marked_summaries(self):
        self.ensure_one()
        self.summary_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
