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


class DocumentValidateWizard(models.TransientModel):
    _name = 'myo.document.validate.wizard'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        'myo.document',
        'myo_document_validate_wizard_rel',
        string='Documents',
        default=_default_document_ids)

    @api.multi
    def do_document_validate(self):
        self.ensure_one()

        # survey_model = self.env['survey.survey']
        # survey_id_TID17 = survey_model.search([
        #     ('title', '=', '[TID17]'),
        # ]).id

        # survey_model = self.env['survey.survey']
        # survey_id_TCR17 = survey_model.search([
        #     ('title', '=', '[TCR17]'),
        # ]).id

        for document_reg in self.document_ids:
            print '>>>>>', document_reg.name, document_reg.code

            if document_reg.survey_id.title == '[QAN17]':

                for document_person in document_reg.person_ids.person_id.document_person_ids:
                    if document_person.document_id.survey_id.title == '[TID17]' or \
                       document_person.document_id.survey_id.title == '[TCR17]':
                        document_reg.base_document_id = document_person.document_id.id
                        if document_person.document_id.survey_user_input_id.id is not False:
                            document_reg.base_survey_user_input_id = \
                                document_person.document_id.survey_user_input_id.id

            if document_reg.survey_id.title == '[QDH17]':

                for document_person in document_reg.person_ids.person_id.document_person_ids:
                    if document_person.document_id.survey_id.title == '[TCP17]':
                        document_reg.base_document_id = document_person.document_id.id
                        if document_person.document_id.survey_user_input_id.id is not False:
                            document_reg.base_survey_user_input_id = \
                                document_person.document_id.survey_user_input_id.id

            if document_reg.survey_id.title == '[QSC17]':

                for document_person in document_reg.person_ids.person_id.document_person_ids:
                    if document_person.document_id.survey_id.title == '[TCR17]':
                        document_reg.base_document_id = document_person.document_id.id
                        if document_person.document_id.survey_user_input_id.id is not False:
                            document_reg.base_survey_user_input_id = \
                                document_person.document_id.survey_user_input_id.id

            if document_reg.survey_id.title == '[QSI17]':

                for document_person in document_reg.person_ids.person_id.document_person_ids:
                    if document_person.document_id.survey_id.title == '[TID17]':
                        document_reg.base_document_id = document_person.document_id.id
                        if document_person.document_id.survey_user_input_id.id is not False:
                            document_reg.base_survey_user_input_id = \
                                document_person.document_id.survey_user_input_id.id

            if document_reg.survey_id.title == '[QMD17]':

                for document_person in document_reg.person_ids.person_id.document_person_ids:
                    if document_person.document_id.survey_id.title == '[TID17]':
                        document_reg.base_document_id = document_person.document_id.id
                        if document_person.document_id.survey_user_input_id.id is not False:
                            document_reg.base_survey_user_input_id = \
                                document_person.document_id.survey_user_input_id.id

            if document_reg.survey_id.title == '[QSF17]':

                for person in document_reg.person_ids:
                    for document_person in person.person_id.document_person_ids:
                        if document_person.document_id.survey_id.title == '[TID17]' or \
                           document_person.document_id.survey_id.title == '[TCR17]':
                            document_reg.base_document_id = document_person.document_id.id
                            if document_person.document_id.survey_user_input_id.id is not False:
                                document_reg.base_survey_user_input_id = \
                                    document_person.document_id.survey_user_input_id.id

        return True
