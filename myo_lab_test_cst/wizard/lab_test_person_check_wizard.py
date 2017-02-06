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


class LabTestPersonCheckWizard(models.TransientModel):
    _name = 'myo.lab_test.person.check.wizard'

    def _default_lab_test_person_ids(self):
        return self._context.get('active_ids')
    lab_test_person_ids = fields.Many2many(
        'myo.lab_test.person',
        string='Survey Files',
        default=_default_lab_test_person_ids)

    @api.multi
    def do_lab_test_person_check(self):
        self.ensure_one()

        for lab_test_person_reg in self.lab_test_person_ids:
            print '>>>>>', lab_test_person_reg.code

        return True