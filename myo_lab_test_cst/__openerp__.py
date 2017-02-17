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
    'name': 'Lab Test (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Lab Test Module customizations for CLVhealth-JCAFB Solution.',
    'version': '2.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'depends': [
        'myo_lab_test',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/lab_test_seq.xml',
        'data/lab_test_unit_data.xml',
        'views/lab_test_request_direct_mail_view.xml',
        'views/lab_test_person_view.xml',
        'views/lab_test_person_state_view.xml',
        'views/lab_test_anemia_dhc_view.xml',
        'views/lab_test_anemia_dhc_state_view.xml',
        'views/lab_test_parasito_swab_view.xml',
        'views/lab_test_parasito_swab_state_view.xml',
        'views/lab_test_urina_view.xml',
        'views/lab_test_urina_state_view.xml',
        'views/lab_test_request_direct_mail_menu_view.xml',
        'wizard/lab_test_edit_wizard_view.xml',
        'wizard/lab_test_request_direct_mail_wizard_view.xml',
        'wizard/lab_test_person_import_wizard_view.xml',
        'wizard/lab_test_person_check_wizard_view.xml',
        'wizard/lab_test_anemia_dhc_import_wizard_view.xml',
        'wizard/lab_test_anemia_dhc_check_wizard_view.xml',
        'wizard/lab_test_anemia_dhc_validate_wizard_view.xml',
        'wizard/lab_test_parasito_swab_import_wizard_view.xml',
        'wizard/lab_test_parasito_swab_check_wizard_view.xml',
        'wizard/lab_test_urina_import_wizard_view.xml',
        'wizard/lab_test_urina_check_wizard_view.xml',
        'wizard/lab_test_urina_validate_wizard_view.xml',
        'views/lab_test_menu_view.xml',
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
