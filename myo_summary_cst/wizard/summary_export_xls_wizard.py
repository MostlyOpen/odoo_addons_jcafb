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
import xlwt

_logger = logging.getLogger(__name__)


class SummaryExportXlsWizard(models.TransientModel):
    _name = 'myo.summary.export_xls.wizard'

    def _default_summary_ids(self):
        return self._context.get('active_ids')
    summary_ids = fields.Many2many('myo.summary', string='Summaries', default=_default_summary_ids)

    @api.multi
    def do_active_export_xls(self):
        self.ensure_one()

        # summary_address_person_model = self.env['myo.summary.address.person']
        # summary_address_event_model = self.env['myo.summary.address.event']
        # summary_address_document_model = self.env['myo.summary.address.document']
        # summary_address_lab_test_request_model = self.env['myo.summary.address.lab_test.request']
        # summary_person_event_model = self.env['myo.summary.person.event']
        # summary_person_document_model = self.env['myo.summary.person.document']
        # summary_person_lab_test_request_model = self.env['myo.summary.person.lab_test.request']

        for summary_reg in self.summary_ids:

            if summary_reg.is_address_summary:

                xls_filename = \
                    '/opt/openerp/mostlyopen_clvhealth_jcafb/export/AddressSummary_' + \
                    summary_reg.code + '.xls'

                book = xlwt.Workbook()
                sheet = book.add_sheet('AddressSummary_' + summary_reg.code)
                row_nr = 0

                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Summary for:')
                row.write(3, summary_reg.name)
                # row_nr += 1
                # row = sheet.row(row_nr)
                # row.write(0, 'Summary Code:')
                # row.write(3, summary_reg.code)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Summary Responsible:')
                if summary_reg.user_id.name is not False:
                    row.write(3, summary_reg.user_id.name)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Summary Date:')
                row.write(3, summary_reg.date_summary)
                row_nr += 1

                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Address:')
                row.write(3, summary_reg.address_id.name)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(3, summary_reg.address_id.district)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Address Categories:')
                row.write(3, summary_reg.address_category_ids.name)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Address Code:')
                row.write(3, summary_reg.address_id.code)
                row_nr += 1

                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Person ')
                row.write(4, 'Code')
                row.write(6, 'Birthday')
                row.write(8, 'Categories')
                # row.write(10, 'Role')
                row.write(10, 'Status')
                row_nr += 2

                for address_person in summary_reg.summary_address_person_ids:

                    row = sheet.row(row_nr)
                    row.write(0, address_person.person_id.name)
                    row.write(4, address_person.person_id.code)
                    if address_person.person_id.birthday is not False:
                        row.write(6, address_person.person_id.birthday)
                    if address_person.person_category_ids.name is not False:
                        row.write(8, address_person.person_category_ids.name)
                    # if address_person.role_id.name is not False:
                    #     row.write(10, address_person.role_id.name)
                    row.write(10, address_person.person_state)
                    row_nr += 1

                # row_nr += 1
                # row = sheet.row(row_nr)
                # row.write(0, 'Event ')
                # row.write(2, 'Code')
                # row.write(4, 'Categories')
                # row_nr += 2

                # for address_event in summary_reg.summary_address_event_ids:

                #     row = sheet.row(row_nr)
                #     row.write(0, address_event.event_id.name)
                #     row.write(2, address_event.event_id.code)
                #     row.write(4, address_event.event_category_ids.name)
                #     row_nr += 1

                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Document ')
                row.write(2, 'Code')
                row.write(4, 'Categories')
                row.write(7, 'Person')
                row_nr += 2

                for address_document in summary_reg.summary_address_document_ids:

                    row = sheet.row(row_nr)
                    row.write(0, address_document.document_id.name)
                    row.write(2, address_document.document_id.code)
                    row.write(4, address_document.document_category_ids.name)
                    if address_document.person_id.name is not False:
                        row.write(7, address_document.person_id.name + ' [' + address_document.person_id.code + ']')
                    row_nr += 1

                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Lab Test Type ')
                row.write(5, 'Lab Test Request')
                row.write(7, 'Person')
                row_nr += 2

                for address_lab_test_request in summary_reg.summary_address_lab_test_request_ids:

                    row = sheet.row(row_nr)
                    row.write(0, address_lab_test_request.lab_test_type_id.name)
                    row.write(5, address_lab_test_request.lab_test_request_id.name)
                    row.write(
                        7, address_lab_test_request.person_id.name +
                        ' [' + address_lab_test_request.person_id.code + ']'
                    )
                    row_nr += 1

            if summary_reg.is_person_summary:

                xls_filename = \
                    '/opt/openerp/mostlyopen_clvhealth_jcafb/export/PersonSummary_' + \
                    summary_reg.code + '.xls'

                book = xlwt.Workbook()
                sheet = book.add_sheet(summary_reg.code)
                row_nr = 0

                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Summary for:')
                row.write(3, summary_reg.name)
                # row_nr += 1
                # row = sheet.row(row_nr)
                # row.write(0, 'Summary Code:')
                # row.write(3, summary_reg.code)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Summary Responsible:')
                if summary_reg.user_id.name is not False:
                    row.write(3, summary_reg.user_id.name)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Summary Date:')
                row.write(3, summary_reg.date_summary)
                row_nr += 1

                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Address:')
                row.write(3, summary_reg.address_id.name)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(3, summary_reg.address_id.district)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Address Categories:')
                row.write(3, summary_reg.address_category_ids.name)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Address Code:')
                row.write(3, summary_reg.address_id.code)
                row_nr += 1

                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Person:')
                row.write(3, summary_reg.person_id.name)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Code:')
                row.write(3, summary_reg.person_id.code)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Person Categories:')
                row.write(3, summary_reg.person_category_ids.name)
                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Birthday:')
                if summary_reg.person_id.birthday is not False:
                    row.write(3, summary_reg.person_id.birthday)
                row_nr += 1

                # row_nr += 1
                # row = sheet.row(row_nr)
                # row.write(0, 'Event ')
                # row.write(2, 'Code')
                # row.write(4, 'Categories')
                # row_nr += 2

                # for person_event in summary_reg.summary_person_event_ids:

                #     row = sheet.row(row_nr)
                #     row.write(0, person_event.event_id.name)
                #     row.write(2, person_event.event_id.code)
                #     row.write(4, person_event.event_category_ids.name)
                #     row_nr += 1

                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Document ')
                row.write(2, 'Code')
                row.write(4, 'Categories')
                row_nr += 2

                for person_document in summary_reg.summary_person_document_ids:

                    row = sheet.row(row_nr)
                    row.write(0, person_document.document_id.name)
                    row.write(2, person_document.document_id.code)
                    row.write(4, person_document.document_category_ids.name)
                    row_nr += 1

                row_nr += 1
                row = sheet.row(row_nr)
                row.write(0, 'Lab Test Type ')
                row.write(5, 'Lab Test Request')
                row_nr += 2

                for person_lab_test_request in summary_reg.summary_person_lab_test_request_ids:

                    row = sheet.row(row_nr)
                    row.write(0, person_lab_test_request.lab_test_type_id.name)
                    row.write(5, person_lab_test_request.lab_test_request_id.name)
                    row_nr += 1

            book.save(xls_filename)

        return True

    # @api.multi
    # def do_reopen_form(self):
    #     self.ensure_one()
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': self._name,  # this model
    #         'res_id': self.id,  # the current wizard record
    #         'view_type': 'form',
    #         'view_mode': 'form, tree',
    #         'target': 'new'}

    # @api.multi
    # def do_populate_marked_summaries(self):
    #     self.ensure_one()
    #     self.summary_ids = self._context.get('active_ids')
    #     # reopen wizard form on same wizard record
    #     return self.do_reopen_form()
