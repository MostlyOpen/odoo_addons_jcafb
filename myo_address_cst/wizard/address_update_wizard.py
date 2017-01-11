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


class AddressUpdateWizard(models.TransientModel):
    _name = 'myo.address.update.wizard'

    def _default_address_ids(self):
        return self._context.get('active_ids')
    address_ids = fields.Many2many(
        'myo.address',
        string='Addresses',
        default=_default_address_ids)

    @api.multi
    def do_address_update(self):
        self.ensure_one()

        summary_model = self.env['myo.summary']

        summary_category_model = self.env['myo.summary.category']
        # summary_category_id_Pessoa = summary_category_model.search([
        #     ('name', '=', 'Pessoa'),
        # ]).id
        summary_category_id_Endereco = summary_category_model.search([
            ('name', '=', 'Endereço'),
        ]).id

        event_model = self.env['myo.event']
        event_person_model = self.env['myo.event.person']

        event_category_model = self.env['myo.event.category']
        event_category_id_1aVisitaU = event_category_model.search([
            ('name', '=', '1a. Visita (U)'),
        ]).id
        event_category_id_2aVisitaU = event_category_model.search([
            ('name', '=', '2a. Visita (U)'),
        ]).id
        event_category_id_3aVisitaU = event_category_model.search([
            ('name', '=', '3a. Visita (U)'),
        ]).id
        event_category_id_1aVisitaR = event_category_model.search([
            ('name', '=', '1a. Visita (R)'),
        ]).id
        event_category_id_2aVisitaR = event_category_model.search([
            ('name', '=', '2a. Visita (R)'),
        ]).id

        address_category_model = self.env['myo.address.category']
        address_category_id_ZonaRural = address_category_model.search([
            ('name', '=', 'Zona Rural'),
        ]).id
        address_category_id_ZonaUrbana = address_category_model.search([
            ('name', '=', 'Zona Urbana'),
        ]).id

        survey_model = self.env['survey.survey']
        survey_id_QSF17 = survey_model.search([
            ('code', '=', 'QSF17'),
        ]).id

        document_category_model = self.env['myo.document.category']
        # document_category_id_TermoConsentimento = document_category_model.search([
        #     ('name', '=', 'Termo de Consentimento'),
        # ]).id
        document_category_id_Questionario = document_category_model.search([
            ('name', '=', 'Questionário'),
        ]).id

        document_model = self.env['myo.document']
        document_person_model = self.env['myo.document.person']

        survey_model = self.env['survey.survey']

        for address_reg in self.address_ids:

            name = address_reg.name
            user_id = False
            if address_reg.user_id is not False:
                user_id = address_reg.user_id.id
            address_id = address_reg.id

            summary_search = summary_model.search([
                # ('person_id', '=', person_id),
                ('is_address_summary', '=', True),
                ('address_id', '=', address_id),
            ])
            if summary_search.id is False:
                print '>>>>>>>>>>', summary_search.name
                values = {
                    'name': name,
                    'user_id': user_id,
                    'address_id': address_id,
                    # 'person_id': person_id,
                    'is_address_summary': True,
                    'category_ids': [(4, summary_category_id_Endereco)],
                }
                summary_model.create(values)

            else:
                print '>>>>>>>>>>', summary_search.name

            if address_reg.is_residence is True:
                print '>>>>>>>>>>>>>>>', address_reg.is_residence

                event_names = []
                survey_ids = []

                event_search = event_model.search([
                    ('address_id', '=', address_reg.id),
                ])
                for event_reg in event_search:

                    event_names += [event_reg.name]

                    print '>>>>>>>>>>>>>>>>>>>>', event_reg.name

                if address_category_id_ZonaRural == address_reg.category_ids.id:
                    print '>>>>>>>>>>>>>>>', 'Zona Rural'

                    if 'Visita 1' not in event_names:

                        name = 'Visita 1'
                        # description = False
                        planned_hours = 2
                        date_foreseen = '2017-01-10 08:00:00'
                        date_deadline = '2017-01-20'
                        address_id = address_reg.id
                        user_id = False
                        if address_reg.user_id is not False:
                            user_id = address_reg.user_id.id
                        values = {
                            'name': name,
                            # 'description': description,
                            'planned_hours': planned_hours,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'address_id': address_id,
                            'user_id': user_id,
                        }
                        new_event = event_model.create(values)

                        values = {
                            'category_ids': [(4, event_category_id_1aVisitaR)],
                        }
                        new_event.write(values)

                        for person_reg in address_reg.person_ids:
                            if person_reg.state == 'selected':
                                values = {
                                    'event_id': new_event.id,
                                    'person_id': person_reg.id,
                                }
                                event_person_model.create(values)

                    if 'Visita 2' not in event_names:

                        name = 'Visita 2'
                        # description = False
                        planned_hours = 2
                        date_foreseen = '2017-01-17 08:00:00'
                        date_deadline = '2017-01-26'
                        address_id = address_reg.id
                        user_id = False
                        if address_reg.user_id is not False:
                            user_id = address_reg.user_id.id
                        values = {
                            'name': name,
                            # 'description': description,
                            'planned_hours': planned_hours,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'address_id': address_id,
                            'user_id': user_id,
                        }
                        new_event = event_model.create(values)

                        values = {
                            'category_ids': [(4, event_category_id_2aVisitaR)],
                        }
                        new_event.write(values)

                        for person_reg in address_reg.person_ids:
                            if person_reg.state == 'selected':
                                values = {
                                    'event_id': new_event.id,
                                    'person_id': person_reg.id,
                                }
                                event_person_model.create(values)

                if address_category_id_ZonaUrbana == address_reg.category_ids.id:
                    print '>>>>>>>>>>>>>>>', 'Zona Urbana'

                    if 'Visita 1' not in event_names:

                        name = 'Visita 1'
                        # description = False
                        planned_hours = 2
                        date_foreseen = '2017-01-10 08:00:00'
                        date_deadline = '2017-01-15'
                        address_id = address_reg.id
                        user_id = False
                        if address_reg.user_id is not False:
                            user_id = address_reg.user_id.id
                        values = {
                            'name': name,
                            # 'description': description,
                            'planned_hours': planned_hours,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'address_id': address_id,
                            'user_id': user_id,
                        }
                        new_event = event_model.create(values)

                        values = {
                            'category_ids': [(4, event_category_id_1aVisitaU)],
                        }
                        new_event.write(values)

                        for person_reg in address_reg.person_ids:
                            if person_reg.state == 'selected':
                                values = {
                                    'event_id': new_event.id,
                                    'person_id': person_reg.id,
                                }
                                event_person_model.create(values)

                    if 'Visita 2' not in event_names:

                        name = 'Visita 2'
                        # description = False
                        planned_hours = 2
                        date_foreseen = '2017-01-17 08:00:00'
                        date_deadline = '2017-01-22'
                        address_id = address_reg.id
                        user_id = False
                        if address_reg.user_id is not False:
                            user_id = address_reg.user_id.id
                        values = {
                            'name': name,
                            # 'description': description,
                            'planned_hours': planned_hours,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'address_id': address_id,
                            'user_id': user_id,
                        }
                        new_event = event_model.create(values)

                        values = {
                            'category_ids': [(4, event_category_id_2aVisitaU)],
                        }
                        new_event.write(values)

                        for person_reg in address_reg.person_ids:
                            if person_reg.state == 'selected':
                                values = {
                                    'event_id': new_event.id,
                                    'person_id': person_reg.id,
                                }
                                event_person_model.create(values)

                    if 'Visita 3' not in event_names:

                        name = 'Visita 3'
                        # description = False
                        planned_hours = 2
                        date_foreseen = '2017-01-23 08:00:00'
                        date_deadline = '2017-01-26'
                        address_id = address_reg.id
                        user_id = False
                        if address_reg.user_id is not False:
                            user_id = address_reg.user_id.id
                        values = {
                            'name': name,
                            # 'description': description,
                            'planned_hours': planned_hours,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'address_id': address_id,
                            'user_id': user_id,
                        }
                        new_event = event_model.create(values)

                        values = {
                            'category_ids': [(4, event_category_id_3aVisitaU)],
                        }
                        new_event.write(values)

                        for person_reg in address_reg.person_ids:
                            if person_reg.state == 'selected':
                                values = {
                                    'event_id': new_event.id,
                                    'person_id': person_reg.id,
                                }
                                event_person_model.create(values)

                document_search = document_model.search([
                    ('address_id', '=', address_reg.id),
                ])
                for document_reg in document_search:

                    survey_ids += [document_reg.survey_id.id]

                    print '>>>>>>>>>>>>>>>>>>>>', document_reg.survey_id.title

                if survey_id_QSF17 not in survey_ids:

                    survey_search = survey_model.search([
                        ('id', '=', survey_id_QSF17),
                    ])
                    name = survey_search.title
                    if address_category_id_ZonaRural == address_reg.category_ids.id:
                        date_foreseen = '2017-01-10 08:00:00'
                        date_deadline = '2017-01-20'
                    if address_category_id_ZonaUrbana == address_reg.category_ids.id:
                        date_foreseen = '2017-01-10 08:00:00'
                        date_deadline = '2017-01-15'
                    values = {
                        'name': name,
                        'user_id': user_id,
                        # 'date_document': self.date_document,
                        'date_foreseen': date_foreseen,
                        'date_deadline': date_deadline,
                        'survey_id': survey_id_QSF17,
                        'address_id': address_id,
                        'category_ids': [(4, document_category_id_Questionario)],
                    }
                    new_document = document_model.create(values)

                    for person_reg in address_reg.person_ids:
                        if person_reg.state == 'selected':
                            values = {
                                'document_id': new_document.id,
                                'person_id': person_reg.id,
                            }
                            document_person_model.create(values)

            else:
                print '>>>>>>>>>>>>>>>', address_reg.is_residence

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
    def do_populate_marked_addresses(self):
        self.ensure_one()
        self.address_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
