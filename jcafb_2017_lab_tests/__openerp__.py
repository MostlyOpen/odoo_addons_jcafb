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
    'name': 'JCAF 2017 Lab Tests',
    'summary': 'This module will install all the JCAF 2017 Lab Tests.',
    'version': '2.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'depends': [
        'myo_survey',
        'myo_lab_test_cst',
    ],
    'data': [
        # 'data/survey_jcafb_EAN17.xml',
        # 'data/survey_jcafb_EDH17.xml',
        # 'data/survey_jcafb_EPC17.xml',
        # 'data/survey_jcafb_EPI17.xml',
        # 'data/survey_jcafb_EUR17.xml',
        'data/lab_test_EAN17_data.xml',
        'data/lab_test_EDH17_data.xml',
        'data/lab_test_EPC17_data.xml',
        'data/lab_test_EPI17_data.xml',
        'data/lab_test_ECP17_data.xml',
        'data/lab_test_EEV17_data.xml',
        'data/lab_test_EUR17_data.xml',
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
