from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ReportAdmin(models.Model):
    _name = "report.admin"
    _description = "CATATAN MEDIS PASIEN"

    nama_admin = fields.Text(string='Nama Admin', required=True)

    reference_nama_pasien = fields.Reference(selection=[('pasien.umum','Nama Pasien')], string='Nama Pasien', ondelete='cascade')

    tanggal_admin = fields.Date(string='Tanggal Pemeriksaan', required=True)

    catatan = fields.Text(string='Catatan', required=True)

    diagnosa = fields.Text(string='Diagnosa Penyakit', required=True)

    poli_admin = fields.Selection([
            ('umum','Poli Umum'),
            ('gigi','Poli Gigi')], 
            required=True, default = 'umum', tracking = True, string='Asal Poli')
    