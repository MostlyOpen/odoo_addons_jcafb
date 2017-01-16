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


class SummaryUpdateyWizard(models.TransientModel):
    _name = 'myo.summary.update.wizard'

    summary_ids = fields.Many2many('myo.summary', string='Summaries')

    @api.multi
    def do_active_update(self):
        self.ensure_one()

        summary_address_person_model = self.env['myo.summary.address.person']
        summary_address_event_model = self.env['myo.summary.address.event']
        summary_address_document_model = self.env['myo.summary.address.document']
        summary_address_lab_test_request_model = self.env['myo.summary.address.lab_test.request']
        summary_person_event_model = self.env['myo.summary.person.event']
        summary_person_document_model = self.env['myo.summary.person.document']
        summary_person_lab_test_request_model = self.env['myo.summary.person.lab_test.request']

        for summary_reg in self.summary_ids:

            if summary_reg.is_address_summary:

                summary_address_person_search = summary_address_person_model.search([
                    ('summary_id', '=', summary_reg.id),
                    ('address_id', '=', summary_reg.address_id.id),
                ])
                summary_address_person_search.unlink()

                for address_person in summary_reg.address_id.person_address_ids:

                    if address_person.sign_out_date is False:

                        values = {
                            'summary_id': summary_reg.id,
                            'address_id': summary_reg.address_id.id,
                            'person_id': address_person.person_id.id,
                            'role_id': address_person.role_id.id,
                            'sign_in_date': address_person.sign_in_date,
                            'sign_out_date': address_person.sign_out_date,
                        }
                        summary_address_person_model.create(values)

                summary_address_event_search = summary_address_event_model.search([
                    ('summary_id', '=', summary_reg.id),
                    ('address_id', '=', summary_reg.address_id.id),
                ])
                summary_address_event_search.unlink()

                for event in summary_reg.address_id.event_ids:

                    values = {
                        'summary_id': summary_reg.id,
                        'address_id': summary_reg.address_id.id,
                        'event_id': event.id,
                    }
                    summary_address_event_model.create(values)

                summary_address_document_search = summary_address_document_model.search([
                    ('summary_id', '=', summary_reg.id),
                    ('address_id', '=', summary_reg.address_id.id),
                ])
                summary_address_document_search.unlink()

                for document in summary_reg.address_id.document_ids:

                    values = {
                        'summary_id': summary_reg.id,
                        'address_id': summary_reg.address_id.id,
                        'document_id': document.id,
                    }
                    new_summary_address_document = summary_address_document_model.create(values)

                    if document.name != '[QSF17]':
                        for document_person in document.person_ids:
                            values = {
                                'person_id': document_person.person_id.id,
                            }
                            new_summary_address_document.write(values)

                summary_address_lab_test_request_search = summary_address_lab_test_request_model.search([
                    ('summary_id', '=', summary_reg.id),
                    ('address_id', '=', summary_reg.address_id.id),
                ])
                summary_address_lab_test_request_search.unlink()

                for address_person in summary_reg.address_id.person_address_ids:

                    for lab_test_request in address_person.person_id.lab_test_request_ids:

                        values = {
                            'summary_id': summary_reg.id,
                            'address_id': summary_reg.address_id.id,
                            'lab_test_type_id': lab_test_request.lab_test_type_id.id,
                            'lab_test_request_id': lab_test_request.id,
                            'person_id': address_person.person_id.id,
                        }
                        summary_address_lab_test_request_model.create(values)

            if summary_reg.is_person_summary:

                summary_person_event_search = summary_person_event_model.search([
                    ('summary_id', '=', summary_reg.id),
                    ('person_id', '=', summary_reg.person_id.id),
                ])
                summary_person_event_search.unlink()

                for event_person in summary_reg.person_id.event_person_ids:

                    values = {
                        'summary_id': summary_reg.id,
                        'person_id': summary_reg.person_id.id,
                        'event_id': event_person.event_id.id,
                    }
                    summary_person_event_model.create(values)

                summary_person_document_search = summary_person_document_model.search([
                    ('summary_id', '=', summary_reg.id),
                    ('person_id', '=', summary_reg.person_id.id),
                ])
                summary_person_document_search.unlink()

                for document_person in summary_reg.person_id.document_person_ids:

                    values = {
                        'summary_id': summary_reg.id,
                        'person_id': summary_reg.person_id.id,
                        'document_id': document_person.document_id.id,
                    }
                    summary_person_document_model.create(values)

                summary_person_lab_test_request_search = summary_person_lab_test_request_model.search([
                    ('summary_id', '=', summary_reg.id),
                    ('person_id', '=', summary_reg.person_id.id),
                ])
                summary_person_lab_test_request_search.unlink()

                for lab_test_request in summary_reg.person_id.lab_test_request_ids:

                    values = {
                        'summary_id': summary_reg.id,
                        'person_id': summary_reg.person_id.id,
                        'lab_test_type_id': lab_test_request.lab_test_type_id.id,
                        'lab_test_request_id': lab_test_request.id,
                    }
                    summary_person_lab_test_request_model.create(values)

        return True

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
