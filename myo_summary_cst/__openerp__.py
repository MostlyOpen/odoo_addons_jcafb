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

{
    'name': 'Summary (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Summary Module customizations for CLVhealth-JCAFB Solution.',
    'version': '2.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'depends': [
        'myo_summary',
        'myo_address',
        'myo_person',
        'myo_person_address',
        'myo_event',
        'myo_document',
        'myo_lab_test',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/summary_seq.xml',
        'views/summary_view.xml',
        'views/summary_address_person_view.xml',
        'views/summary_address_event_view.xml',
        'views/summary_address_document_view.xml',
        'views/summary_address_lab_test_request_view.xml',
        'views/summary_person_event_view.xml',
        'views/summary_person_document_view.xml',
        'views/summary_person_lab_test_request_view.xml',
        'wizard/summary_update_wizard_view.xml',
        'wizard/summary_export_xls_wizard_view.xml',
        'wizard/summary_responsible_wizard_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
