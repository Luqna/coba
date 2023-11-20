from odoo import api, fields, models, _
from odoo import api, fields, models, _
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime
from datetime import date

class PasienUmum(models.Model):
    _name = "pasien.umum"
    _description = "PASIEN DARI POLI UMUM PT.PAL"

    # reference_pasien_umum = fields.Char(string='Reference', required=True, readonly=True, copy=False, default=lambda self: _('New'))

    name_umum = fields.Char(string='Nama Pasien', required=True)
    
    nip_umum = fields.Char(string='NIP', required=True)
    
    tanggal_umum = fields.Date(string='Tanggal', required=True)
    @api.constrains('tanggal_umum')
    def _check_tanggal_penerbangan(self):
        for record in self:
            if record.tanggal_umum and record.tanggal_umum < fields.Date.today():
                raise UserError("Anda tidak dapat memilih tanggal sebelum dari hari ini.")
            elif record.tanggal_umum and record.tanggal_umum > fields.Date.today():
                raise UserError("Anda tidak dapat memilih tanggal yang akan datang.")
    
    posisi_umum = fields.Text(string='Job Position', required=True)
    
    kode_work_center_umum = fields.Char(string='Kode Work Center',  required=True)
    
    jam_umum = fields.Selection([
        ('pagi', 'PAGI'),
        ('siang', 'SIANG'),
        ('sore', 'SORE')], string='Waktu Periksa', default='pagi', tracking=True)


    poli = fields.Selection([
            ('umum','Poli Umum'),
            ('gigi','Poli Gigi')], 
            required=True, default = 'umum', tracking = True)

    kode_poli_umum = fields.Char(store=True, string='Nomor Urut Poli Umum', compute='_compute_kode_poli', readonly=True)
    kode_poli_gigi = fields.Char(store=True, string='Nomor Urut Poli Gigi', compute='_compute_kode_poli', readonly=True)


    # @api.depends('poli')
    # def _compute_kode_poli(self):
    #     for record in self:
    #         nomor_urut = self.env['ir.sequence'].next_by_code('my_module.poli.common.sequence')
    #         if record.poli == 'umum':
    #             record.kode_poli_umum = f'PU-{nomor_urut}'
    #             record.kode_poli_gigi = False
    #         elif record.poli == 'gigi':
    #             record.kode_poli_gigi = f'PG-{nomor_urut}'
    #             record.kode_poli_umum = False


    








    def duplicate_confirmation(self):
        for pasien in self:
            vals = {
                'name_umum': pasien.name_umum,
                'tanggal_umum': pasien.tanggal_umum,
                'nip_umum': pasien.nip_umum,
                'posisi_umum': pasien.posisi_umum,
                'kode_work_center_umum': pasien.kode_work_center_umum,
                'jam_umum': pasien.jam_umum,
                'poli': pasien.poli,
                'kode_poli_umum': pasien.kode_poli_umum,
                'kode_poli_gigi': pasien.kode_poli_gigi,
            }
            
            konfirmasi_umum = self.env['pasien.konfirmasi'].create(vals)