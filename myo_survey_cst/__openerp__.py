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
    'name': 'Survey (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Survey Module used by MostlyOpen Solutions (customizations for CLVhealth-JCAFB Solution).',
    'version': '2.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://mostlyopen.org',
    'depends': [
        'myo_survey',
        'myo_lab_test',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/survey_file_view.xml',
        'views/survey_file_state_view.xml',
        'views/survey_qan17_view.xml',
        'views/survey_qdh17_view.xml',
        'views/survey_qmd17_view.xml',
        'views/survey_qsc17_view.xml',
        'views/survey_qsi17_view.xml',
        'views/survey_qsf17_view.xml',
        'wizard/survey_file_refresh_wizard_view.xml',
        'wizard/survey_file_validate_wizard_view.xml',
        'wizard/survey_file_import_wizard_view.xml',
        'wizard/survey_file_arquive_wizard_view.xml',
        'wizard/survey_qan17_refresh_wizard_view.xml',
        'wizard/survey_qdh17_refresh_wizard_view.xml',
        'wizard/survey_qmd17_refresh_wizard_view.xml',
        'wizard/survey_qsc17_refresh_wizard_view.xml',
        'wizard/survey_qsi17_refresh_wizard_view.xml',
        'wizard/survey_qsf17_refresh_wizard_view.xml',
        'wizard/survey_user_input_validate_wizard_view.xml',
        'wizard/survey_user_input_transcribe_wizard_view.xml',
        'views/survey_menu_view.xml',
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
