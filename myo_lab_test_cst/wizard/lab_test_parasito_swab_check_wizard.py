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


class LabTestParasitoSwabCheckWizard(models.TransientModel):
    _name = 'myo.lab_test.parasito_swab.check.wizard'

    def _default_lab_test_parasito_swab_ids(self):
        return self._context.get('active_ids')
    lab_test_parasito_swab_ids = fields.Many2many(
        'myo.lab_test.parasito_swab',
        'myo_lab_test_parasito_swab_check_wizard_rel',
        string='Survey Files',
        default=_default_lab_test_parasito_swab_ids)

    @api.multi
    def do_lab_test_parasito_swab_check(self):
        self.ensure_one()

        for lab_test_parasito_swab_reg in self.lab_test_parasito_swab_ids:
            print '>>>>>', lab_test_parasito_swab_reg.request_code_parasito, lab_test_parasito_swab_reg.request_code_swab

        return True
