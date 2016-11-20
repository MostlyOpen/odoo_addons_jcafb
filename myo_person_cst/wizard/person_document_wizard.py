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


class PersonDocumentWizard(models.TransientModel):
    _name = 'myo.person.document.wizard'

    person_ids = fields.Many2many('myo.person', string='Persons')
    survey_ids = fields.Many2many('survey.survey', string='Surveys')
    date_document = fields.Datetime('Document Date')
    date_foreseen = fields.Datetime(string='Foreseen Date')
    date_deadline = fields.Date(string='Deadline')

    @api.multi
    def do_active_update(self):
        self.ensure_one()

        document_model = self.env['myo.document']

        for person_reg in self.person_ids:
            for survey_reg in self.survey_ids:
                name = survey_reg.title
                user_id = person_reg.user_id
                address_id = person_reg.address_id.id
                values = {
                    'name': name,
                    'user_id': user_id,
                    'date_document': self.date_document,
                    'date_foreseen': self.date_foreseen,
                    'date_deadline': self.date_deadline,
                    'survey_id': survey_reg.id,
                    'address_id': address_id,
                }
                # document_id = document_model.create(values)

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
    def do_populate_persons(self):
        self.ensure_one()
        self.person_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
