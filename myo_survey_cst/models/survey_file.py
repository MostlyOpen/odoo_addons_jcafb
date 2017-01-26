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

# from datetime import datetime

from openerp import fields, models


class Summary(models.Model):
    _name = "myo.survey.file"

    # @api.multi
    # @api.depends('name', 'code')
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         result.append(
    #             (record.id,
    #              u'%s [%s]' % (record.name, record.code)
    #              ))
    #     return result

    name = fields.Char('File Name', required=True, help="File Name")
    survey_title = fields.Char('Survey Title', help="Survey Title")
    survey_id = fields.Many2one('survey.survey', 'Survey Type', help="Survey Type")
    survey_description = fields.Html(
        'Survey Type Description',
        related='survey_id.description',
        store=False,
        readonly=True
    )
    survey_user_input_id = fields.Many2one('survey.user_input', 'Survey User Input', help="Survey User Input")
    document_code = fields.Char('Document Code', help="Document Code")
    document_id = fields.Many2one('myo.document', 'Related Document', help="Related Document")
    document_state = fields.Selection(
        'Document Status',
        related='document_id.state',
        store=False,
        readonly=True
    )
    person_code = fields.Char('Person Code', help="Person Code")
    person_id = fields.Many2one('myo.person', 'Related Person', help="Related Person")
    address_code = fields.Char('Address Code', help="Address Code")
    address_id = fields.Many2one('myo.address', 'Related Address', help="Related Address")
    lab_test_request_code = fields.Char('Lab Test Request Code', help="Lab Test Request Code")
    lab_test_request_id = fields.Many2one(
        'myo.lab_test.request',
        'Related Lab Test Request',
        help="Related Lab Test Request"
    )
    user_id = fields.Many2one('res.users', 'Document Responsible', required=False, readonly=False)
    date_survey_file = fields.Datetime(
        'Survey File Date',
        # default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    notes = fields.Text(string='Notes')
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the survey file without removing it.",
        default=1
    )

    _sql_constraints = [
        (
            'name_uniq',
            'UNIQUE (name)',
            'Error! The File Name must be unique!'
        ),
    ]

    _order = 'name'
