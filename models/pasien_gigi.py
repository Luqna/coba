from odoo import api, fields, models, _
from odoo import api, fields, models, _
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime
from datetime import date

class PasienGigi(models.Model):
    _name = "pasien.gigi"
    _description = "PASIEN DARI POLI GIGI PT.PAL"


    name_gigi = fields.Char(string='Nama Pasien', required=True)
    
    nip_gigi = fields.Char(string='NIP', required=True)

    tanggal_gigi = fields.Date(string='Tanggal', required=True)
    @api.constrains('tanggal_gigi')
    def _check_tanggal_penerbangan(self):
        for record in self:
            if record.tanggal_gigi and record.tanggal_gigi < fields.Date.today():
                raise UserError("Anda tidak dapat memilih tanggal sebelum dari hari ini.")
            elif record.tanggal_gigi and record.tanggal_gigi > fields.Date.today():
                raise UserError("Anda tidak dapat memilih tanggal yang akan datang.")
    
    posisi_gigi = fields.Text(string='Job Position', required=True)
    
    kode_work_center_gigi = fields.Char(string='Kode Work Center',  required=True)
    
    jam_gigi = fields.Selection([
        ('pagi', 'PAGI'),
        ('siang', 'SIANG'),
        ('sore', 'SORE')], string='Waktu Periksa', default='pagi', tracking=True)
    
    def duplicate_to_confirmation(self):
        for pasien in self:
            vals = {
                'name_gigi': pasien.name_gigi,
                'tanggal_gigi': pasien.tanggal_gigi,
                'nip_gigi': pasien.nip_gigi,
                'posisi_gigi': pasien.posisi_gigi,
                'kode_work_center_gigi': pasien.kode_work_center_gigi,
                'jam_gigi': pasien.jam_gigi,
            }
            
            pasien_konfirmasi = self.env['pasien.konfirmasi'].create(vals)
