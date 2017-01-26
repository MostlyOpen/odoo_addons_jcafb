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


class LabTestUrina(models.Model):
    _name = "myo.lab_test.urina"

    access_id = fields.Integer('Access ID', help="Access ID")
    lab_test_person_id = fields.Many2one(
        'myo.lab_test.person',
        'Related Lab Test Person'
    )

    request_code_urina = fields.Char('Lab Request Code (Urina)')
    request_id_urina = fields.Many2one(
        'myo.lab_test.request',
        'Related Lab Test Request (Urina)'
    )
    farmaceutico_resp = fields.Char('Farmacêutico Responsável')
    date_urina = fields.Char("Data do Exame)")
    volume = fields.Char("Volume)")
    densidade = fields.Char("Densidade)")
    aspecto = fields.Char("Aspecto)")
    cor = fields.Char("Cor)")
    odor = fields.Char("Odor)")
    ph = fields.Char("pH)")
    proteinas = fields.Char("Proteínas)")
    glicose = fields.Char("Glicose)")
    cetona = fields.Char("Cetona)")
    pig_biliares = fields.Char("Pigmentos biliares)")
    sangue = fields.Char("Sangue)")
    urobilinogenio = fields.Char("Urobilinogênio)")
    nitrito = fields.Char("Nitrito)")
    cels_epitcels_epit = fields.Char("Células Epiteliais)")
    muco = fields.Char("Muco)")
    cristais = fields.Char("Cristais)")
    leucocitos = fields.Char("Leucócitos)")
    hemacias = fields.Char("Hemácias)")
    cilindros = fields.Char("Cilindros)")
    hialinos = fields.Char("Cilindros Hialinos)")
    ganulosos = fields.Char("Cilindros Granulosos)")
    leucocitarios = fields.Char("Cilindros Leucocitários)")
    hematicos = fields.Char("Cilindros Hemáticos)")
    cereos = fields.Char("Cilindros Céreos)")
    outros_tipos = fields.Char("Outros tipos de Cilindros)")
    obs = fields.Char("Observações)")
    obs_int = fields.Char("Observações Internas)")
    date_laudo = fields.Char("Laudo Emitido em)")
    examinador = fields.Char("Examinador)")
    status_urina = fields.Char("Status Urina)")

    notes = fields.Text(string='Notes')
    active = fields.Boolean(
        'Active',
        help="If unchecked, it will allow you to hide the lab test urina without removing it.",
        default=1
    )

    _rec_name = 'access_id'

    _order = 'access_id'
