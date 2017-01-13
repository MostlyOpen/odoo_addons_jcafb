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


class PersonExportXlsWizard(models.TransientModel):
    _name = 'myo.person.export_xls.wizard'

    def _default_person_ids(self):
        return self._context.get('active_ids')
    person_ids = fields.Many2many(
        'myo.person',
        string='Persons',
        default=_default_person_ids)

    @api.multi
    def do_active_export_xls(self):
        self.ensure_one()

        for person_reg in self.person_ids:

            xls_filename = \
                '/opt/openerp/mostlyopen_clvhealth_jcafb/export/Person_' + \
                person_reg.code + '.xls'

            book = xlwt.Workbook()
            sheet = book.add_sheet(person_reg.code)
            row_nr = 0

            # row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Summary for:')
            # row.write(3, person_reg.name)
            # row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Summary Code:')
            # row.write(3, person_reg.code)
            # row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Summary Responsible:')
            # if person_reg.user_id.name is not False:
            #     row.write(3, person_reg.user_id.name)
            # row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Summary Date:')
            # row.write(3, person_reg.date_person)
            # row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Person:')
            row.write(3, person_reg.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Code:')
            row.write(3, person_reg.code)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Person Categories:')
            row.write(3, person_reg.category_ids.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Birthday:')
            if person_reg.birthday is not False:
                row.write(3, person_reg.birthday)
            row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address:')
            row.write(3, person_reg.address_id.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address Code:')
            row.write(3, person_reg.address_id.code)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(3, person_reg.address_id.district)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address Categories:')
            row.write(3, person_reg.address_id.category_ids.name)
            row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Event ')
            row.write(2, 'Code')
            row.write(4, 'Categories')
            row_nr += 2

            for event_person in person_reg.event_person_ids:

                row = sheet.row(row_nr)
                row.write(0, event_person.event_id.name)
                row.write(2, event_person.event_id.code)
                row.write(4, event_person.event_id.category_ids.name)
                row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Document ')
            row.write(2, 'Code')
            row.write(4, 'Categories')
            row_nr += 2

            for document_person in person_reg.document_person_ids:

                row = sheet.row(row_nr)
                row.write(0, document_person.document_id.name)
                row.write(2, document_person.document_id.code)
                row.write(4, document_person.document_id.category_ids.name)
                row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Lab Test Type ')
            row.write(5, 'Lab Test Request')
            row_nr += 2

            for lab_test_request in person_reg.lab_test_request_ids:

                row = sheet.row(row_nr)
                row.write(0, lab_test_request.lab_test_type_id.name)
                row.write(5, lab_test_request.name)
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
    # def do_populate_marked_persons(self):
    #     self.ensure_one()
    #     self.person_ids = self._context.get('active_ids')
    #     # reopen wizard form on same wizard record
    #     return self.do_reopen_form()
