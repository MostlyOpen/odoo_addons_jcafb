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
import shutil

_logger = logging.getLogger(__name__)


class SurveyFileArquiveWizard(models.TransientModel):
    _name = 'myo.survey.file.arquive.wizard'

    def _default_survey_file_ids(self):
        return self._context.get('active_ids')
    survey_file_ids = fields.Many2many(
        'myo.survey.file',
        string='Survey Files',
        default=_default_survey_file_ids)

    dir_path = fields.Char(
        'Directory Path',
        required=True,
        help="Directory Path",
        default='/opt/openerp/mostlyopen_clvhealth_jcafb/survey_files/input'
    )
    arquive_dir_path = fields.Char(
        'Arquive Directory Path',
        required=True,
        help="Arquive Directory Path",
        default='/opt/openerp/mostlyopen_clvhealth_jcafb/survey_files/arquive'
    )

    @api.multi
    def do_survey_file_arquive(self):
        self.ensure_one()

        for survey_file_reg in self.survey_file_ids:

            filepath = self.dir_path + '/' + survey_file_reg.name
            arquive_filepath = self.arquive_dir_path + '/' + survey_file_reg.name

            print '>>>>>', filepath, survey_file_reg.state

            # print '>>>>>', survey_file_reg.survey_id.description

            if survey_file_reg.state == 'imported':

                shutil.move(filepath, arquive_filepath)

                survey_file_reg.state = 'arquived'

        return True
