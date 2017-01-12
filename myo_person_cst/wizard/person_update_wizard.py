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


class PersonUpdateWizard(models.TransientModel):
    _name = 'myo.person.update.wizard'

    person_ids = fields.Many2many('myo.person', string='Persons')

    @api.multi
    def do_person_update(self):
        self.ensure_one()

        summary_model = self.env['myo.summary']

        summary_category_model = self.env['myo.summary.category']
        summary_category_id_Pessoa = summary_category_model.search([
            ('name', '=', 'Pessoa'),
        ]).id

        person_category_model = self.env['myo.person.category']
        person_category_id_Crianca = person_category_model.search([
            ('name', '=', 'Criança'),
        ]).id
        person_category_id_Idoso = person_category_model.search([
            ('name', '=', 'Idoso'),
        ]).id

        address_category_model = self.env['myo.address.category']
        address_category_id_ZonaRural = address_category_model.search([
            ('name', '=', 'Zona Rural'),
        ]).id
        address_category_id_ZonaUrbana = address_category_model.search([
            ('name', '=', 'Zona Urbana'),
        ]).id

        survey_model = self.env['survey.survey']
        survey_id_QAN17 = survey_model.search([
            ('code', '=', 'QAN17'),
        ]).id
        survey_id_QDH17 = survey_model.search([
            ('code', '=', 'QDH17'),
        ]).id
        survey_id_QMD17 = survey_model.search([
            ('code', '=', 'QMD17'),
        ]).id
        survey_id_QSC17 = survey_model.search([
            ('code', '=', 'QSC17'),
        ]).id
        # survey_id_QSF17 = survey_model.search([
        #     ('code', '=', 'QSF17'),
        # ]).id
        survey_id_QSI17 = survey_model.search([
            ('code', '=', 'QSI17'),
        ]).id
        survey_id_TCP17 = survey_model.search([
            ('code', '=', 'TCP17'),
        ]).id
        survey_id_TCR17 = survey_model.search([
            ('code', '=', 'TCR17'),
        ]).id
        survey_id_TID17 = survey_model.search([
            ('code', '=', 'TID17'),
        ]).id

        document_category_model = self.env['myo.document.category']
        document_category_id_TermoConsentimento = document_category_model.search([
            ('name', '=', 'Termo de Consentimento'),
        ]).id
        document_category_id_Questionario = document_category_model.search([
            ('name', '=', 'Questionário'),
        ]).id

        lab_test_type_model = self.env['myo.lab_test.type']
        lab_test_type_id_EAN17 = lab_test_type_model.search([
            ('code', '=', 'EAN17'),
        ]).id
        lab_test_type_id_EDH17 = lab_test_type_model.search([
            ('code', '=', 'EDH17'),
        ]).id
        lab_test_type_id_EPC17 = lab_test_type_model.search([
            ('code', '=', 'EPC17'),
        ]).id
        lab_test_type_id_EPI17 = lab_test_type_model.search([
            ('code', '=', 'EPI17'),
        ]).id
        lab_test_type_id_EUR17 = lab_test_type_model.search([
            ('code', '=', 'EUR17'),
        ]).id

        document_model = self.env['myo.document']
        document_person_model = self.env['myo.document.person']

        survey_model = self.env['survey.survey']

        lab_test_request_model = self.env['myo.lab_test.request']

        for person_reg in self.person_ids:

            name = person_reg.name
            user_id = False
            if person_reg.user_id is not False:
                user_id = person_reg.user_id.id
            person_id = person_reg.id
            address_id = False
            if person_reg.address_id.id is not False:
                address_id = person_reg.address_id.id

            summary_search = summary_model.search([
                ('person_id', '=', person_id),
                ('address_id', '=', address_id),
            ])
            if summary_search.id is False:
                # print '>>>>>>>>>>', summary_search.name
                values = {
                    'name': name,
                    'user_id': user_id,
                    'address_id': address_id,
                    'person_id': person_id,
                    'is_person_summary': True,
                    'category_ids': [(4, summary_category_id_Pessoa)],
                }
                summary_model.create(values)

            else:
                # print '>>>>>>>>>>', summary_search.name
                pass

            if person_reg.is_patient is True:
                # print '>>>>>>>>>>>>>>>', person_reg.is_patient

                survey_ids = []
                lab_test_type_ids = []

                if person_category_id_Crianca == person_reg.category_ids.id:
                    # print '>>>>>>>>>>>>>>>', 'Criança'

                    document_person_search = document_person_model.search([
                        ('person_id', '=', person_reg.id),
                    ])
                    for document_person_reg in document_person_search:

                        survey_ids += [document_person_reg.document_id.survey_id.id]

                        # print '>>>>>>>>>>>>>>>>>>>>', document_person_reg.document_id.survey_id.title

                    if survey_id_TCR17 not in survey_ids:

                        survey_search = survey_model.search([
                            ('id', '=', survey_id_TCR17),
                        ])
                        name = survey_search.title
                        if address_category_id_ZonaRural == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-10 08:00:00'
                            date_deadline = '2017-01-20'
                        if address_category_id_ZonaUrbana == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-10 08:00:00'
                            date_deadline = '2017-01-15'
                        values = {
                            'name': name,
                            'user_id': user_id,
                            # 'date_document': self.date_document,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'survey_id': survey_id_TCR17,
                            'address_id': address_id,
                            'category_ids': [(4, document_category_id_TermoConsentimento)],
                        }
                        new_document = document_model.create(values)

                        values = {
                            'document_id': new_document.id,
                            'person_id': person_id,
                        }
                        document_person_model.create(values)

                    if survey_id_QSC17 not in survey_ids:

                        survey_search = survey_model.search([
                            ('id', '=', survey_id_QSC17),
                        ])
                        name = survey_search.title
                        if address_category_id_ZonaRural == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-10 08:00:00'
                            date_deadline = '2017-01-20'
                        if address_category_id_ZonaUrbana == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-10 08:00:00'
                            date_deadline = '2017-01-15'
                        values = {
                            'name': name,
                            'user_id': user_id,
                            # 'date_document': self.date_document,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'survey_id': survey_id_QSC17,
                            'address_id': address_id,
                            'category_ids': [(4, document_category_id_Questionario)],
                        }
                        new_document = document_model.create(values)

                        values = {
                            'document_id': new_document.id,
                            'person_id': person_id,
                        }
                        document_person_model.create(values)

                    if survey_id_QAN17 not in survey_ids:

                        survey_search = survey_model.search([
                            ('id', '=', survey_id_QAN17),
                        ])
                        name = survey_search.title
                        if address_category_id_ZonaRural == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-14 13:00:00'
                            date_deadline = '2017-01-22'
                        if address_category_id_ZonaUrbana == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-14 13:00:00'
                            date_deadline = '2017-01-22'
                        values = {
                            'name': name,
                            'user_id': user_id,
                            # 'date_document': self.date_document,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'survey_id': survey_id_QAN17,
                            'address_id': address_id,
                            'category_ids': [(4, document_category_id_Questionario)],
                        }
                        new_document = document_model.create(values)

                        values = {
                            'document_id': new_document.id,
                            'person_id': person_id,
                        }
                        document_person_model.create(values)

                    lab_test_request_search = lab_test_request_model.search([
                        ('patient_id', '=', person_reg.id),
                    ])
                    for lab_test_request_reg in lab_test_request_search:

                        lab_test_type_ids += [lab_test_request_reg.lab_test_type_id.id]

                        # print '>>>>>>>>>>>>>>>>>>>>', lab_test_request_reg.lab_test_type_id.name

                    if lab_test_type_id_EAN17 not in lab_test_type_ids:

                        values = {
                            'lab_test_type_id': lab_test_type_id_EAN17,
                            'patient_id': person_id,
                        }
                        lab_test_request_model.create(values)

                    if lab_test_type_id_EPC17 not in lab_test_type_ids:

                        values = {
                            'lab_test_type_id': lab_test_type_id_EPC17,
                            'patient_id': person_id,
                        }
                        lab_test_request_model.create(values)

                if person_category_id_Idoso == person_reg.category_ids.id:
                    # print '>>>>>>>>>>>>>>>', 'Idoso'

                    document_person_search = document_person_model.search([
                        ('person_id', '=', person_reg.id),
                    ])
                    for document_person_reg in document_person_search:

                        survey_ids += [document_person_reg.document_id.survey_id.id]

                        # print '>>>>>>>>>>>>>>>>>>>>', document_person_reg.document_id.survey_id.title

                    if survey_id_TID17 not in survey_ids:

                        survey_search = survey_model.search([
                            ('id', '=', survey_id_TID17),
                        ])
                        name = survey_search.title
                        if address_category_id_ZonaRural == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-10 08:00:00'
                            date_deadline = '2017-01-20'
                        if address_category_id_ZonaUrbana == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-10 08:00:00'
                            date_deadline = '2017-01-15'
                        values = {
                            'name': name,
                            'user_id': user_id,
                            # 'date_document': self.date_document,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'survey_id': survey_id_TID17,
                            'address_id': address_id,
                            'category_ids': [(4, document_category_id_TermoConsentimento)],
                        }
                        new_document = document_model.create(values)

                        values = {
                            'document_id': new_document.id,
                            'person_id': person_id,
                        }
                        document_person_model.create(values)

                    if survey_id_QSI17 not in survey_ids:

                        survey_search = survey_model.search([
                            ('id', '=', survey_id_QSI17),
                        ])
                        name = survey_search.title
                        if address_category_id_ZonaRural == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-10 08:00:00'
                            date_deadline = '2017-01-20'
                        if address_category_id_ZonaUrbana == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-10 08:00:00'
                            date_deadline = '2017-01-15'
                        values = {
                            'name': name,
                            'user_id': user_id,
                            # 'date_document': self.date_document,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'survey_id': survey_id_QSI17,
                            'address_id': address_id,
                            'category_ids': [(4, document_category_id_Questionario)],
                        }
                        new_document = document_model.create(values)

                        values = {
                            'document_id': new_document.id,
                            'person_id': person_id,
                        }
                        document_person_model.create(values)

                    if survey_id_QMD17 not in survey_ids:

                        survey_search = survey_model.search([
                            ('id', '=', survey_id_QMD17),
                        ])
                        name = survey_search.title
                        if address_category_id_ZonaRural == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-10 08:00:00'
                            date_deadline = '2017-01-26'
                        if address_category_id_ZonaUrbana == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-10 08:00:00'
                            date_deadline = '2017-01-22'
                        values = {
                            'name': name,
                            'user_id': user_id,
                            # 'date_document': self.date_document,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'survey_id': survey_id_QMD17,
                            'address_id': address_id,
                            'category_ids': [(4, document_category_id_Questionario)],
                        }
                        new_document = document_model.create(values)

                        values = {
                            'document_id': new_document.id,
                            'person_id': person_id,
                        }
                        document_person_model.create(values)

                    if survey_id_QAN17 not in survey_ids:

                        survey_search = survey_model.search([
                            ('id', '=', survey_id_QAN17),
                        ])
                        name = survey_search.title
                        if address_category_id_ZonaRural == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-14 13:00:00'
                            date_deadline = '2017-01-22'
                        if address_category_id_ZonaUrbana == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-14 13:00:00'
                            date_deadline = '2017-01-22'
                        values = {
                            'name': name,
                            'user_id': user_id,
                            # 'date_document': self.date_document,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'survey_id': survey_id_QAN17,
                            'address_id': address_id,
                            'category_ids': [(4, document_category_id_Questionario)],
                        }
                        new_document = document_model.create(values)

                        values = {
                            'document_id': new_document.id,
                            'person_id': person_id,
                        }
                        document_person_model.create(values)

                    if survey_id_TCP17 not in survey_ids:

                        survey_search = survey_model.search([
                            ('id', '=', survey_id_TCP17),
                        ])
                        name = survey_search.title
                        if address_category_id_ZonaRural == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-14 07:00:00'
                            date_deadline = '2017-01-22'
                        if address_category_id_ZonaUrbana == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-14 07:00:00'
                            date_deadline = '2017-01-22'
                        values = {
                            'name': name,
                            'user_id': user_id,
                            # 'date_document': self.date_document,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'survey_id': survey_id_TCP17,
                            'address_id': address_id,
                            'category_ids': [(4, document_category_id_TermoConsentimento)],
                        }
                        new_document = document_model.create(values)

                        values = {
                            'document_id': new_document.id,
                            'person_id': person_id,
                        }
                        document_person_model.create(values)

                    if survey_id_QDH17 not in survey_ids:

                        survey_search = survey_model.search([
                            ('id', '=', survey_id_QDH17),
                        ])
                        name = survey_search.title
                        if address_category_id_ZonaRural == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-14 07:00:00'
                            date_deadline = '2017-01-22'
                        if address_category_id_ZonaUrbana == person_reg.address_id.category_ids.id:
                            date_foreseen = '2017-01-14 07:00:00'
                            date_deadline = '2017-01-22'
                        values = {
                            'name': name,
                            'user_id': user_id,
                            # 'date_document': self.date_document,
                            'date_foreseen': date_foreseen,
                            'date_deadline': date_deadline,
                            'survey_id': survey_id_QDH17,
                            'address_id': address_id,
                            'category_ids': [(4, document_category_id_Questionario)],
                        }
                        new_document = document_model.create(values)

                        values = {
                            'document_id': new_document.id,
                            'person_id': person_id,
                        }
                        document_person_model.create(values)

                    lab_test_request_search = lab_test_request_model.search([
                        ('patient_id', '=', person_reg.id),
                    ])
                    for lab_test_request_reg in lab_test_request_search:

                        lab_test_type_ids += [lab_test_request_reg.lab_test_type_id.id]

                        # print '>>>>>>>>>>>>>>>>>>>>', lab_test_request_reg.lab_test_type_id.name

                    if lab_test_type_id_EAN17 not in lab_test_type_ids:

                        values = {
                            'lab_test_type_id': lab_test_type_id_EAN17,
                            'patient_id': person_id,
                        }
                        lab_test_request_model.create(values)

                    if lab_test_type_id_EDH17 not in lab_test_type_ids:

                        values = {
                            'lab_test_type_id': lab_test_type_id_EDH17,
                            'patient_id': person_id,
                        }
                        lab_test_request_model.create(values)

                    if lab_test_type_id_EPI17 not in lab_test_type_ids:

                        values = {
                            'lab_test_type_id': lab_test_type_id_EPI17,
                            'patient_id': person_id,
                        }
                        lab_test_request_model.create(values)

                    if lab_test_type_id_EUR17 not in lab_test_type_ids:

                        values = {
                            'lab_test_type_id': lab_test_type_id_EUR17,
                            'patient_id': person_id,
                        }
                        lab_test_request_model.create(values)

                # print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', survey_ids
                # print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', lab_test_type_ids

            else:
                # print '>>>>>>>>>>>>>>>', person_reg.is_patient
                pass

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
    def do_populate_marked_persons(self):
        self.ensure_one()
        self.person_ids = self._context.get('active_ids')
        # reopen wizard form on same wizard record
        return self.do_reopen_form()
