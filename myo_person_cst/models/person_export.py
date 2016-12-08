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

from openerp import fields, models


class PersonExport(models.Model):
    _name = 'myo.person.export'
    _log_access = False

    name = fields.Char('Name')
    code = fields.Char('Person Code')
    birthday = fields.Date("Date of Birth")
    age = fields.Char('Age')
    estimated_age = fields.Char('Estimated Age')
    date_reference = fields.Date("Reference Date")
    age_reference = fields.Char('Reference Age')
    gender = fields.Selection(
        [('M', 'Male'),
         ('F', 'Female')
         ], 'Gender'
    )
    categories = fields.Char('Categories')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('revised', 'Revised'),
        ('waiting', 'Waiting'),
        ('selected', 'Selected'),
        ('unselected', 'Unselected'),
        ('canceled', 'Canceled'),
    ], string='Status', default='draft', readonly=True, required=True, help="")
    responsible_name = fields.Char('Responsible Name')
    responsible_code = fields.Char('Responsible Code')

    address_name = fields.Char('Address Name')
    address_code = fields.Char('Address Code')
    address_categories = fields.Char('Address Categories')
    street = fields.Char('Street')
    number = fields.Char(u'Number', size=10)
    street2 = fields.Char('Street2')
    district = fields.Char('District')
    l10n_br_city = fields.Char('City')
    country_state = fields.Char('State')
    country = fields.Char('Country')
    zip_code = fields.Char('ZIP code')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    mobile = fields.Char('Mobile')
