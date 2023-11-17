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

    kode_poli_umum = fields.Char(compute='_compute_kode_poli_umum', store=True, string='Nomor Urut Poli Umum')
    kode_poli_gigi = fields.Char(compute='_compute_kode_poli_gigi', store=True, string='Nomor Urut Poli Gigi')

    # Counter untuk nomor urut pasien poli umum
    counter_poli_umum = fields.Integer(string='Counter Poli Umum', default=1)

    # Counter untuk nomor urut pasien poli gigi
    counter_poli_gigi = fields.Integer(string='Counter Poli Gigi', default=1)

    @api.depends('poli', 'counter_poli_umum', 'counter_poli_gigi')
    def _compute_kode_poli_umum(self):
        for rec in self:
            if rec.poli == 'umum':
                rec.kode_poli_umum = 'PU-{}'.format(str(rec.counter_poli_umum))
                rec.counter_poli_umum += 1
            else:
                rec.kode_poli_umum = False

    @api.depends('poli', 'counter_poli_gigi', 'counter_poli_umum')
    def _compute_kode_poli_gigi(self):
        for rec in self:
            if rec.poli == 'gigi':
                rec.kode_poli_gigi = 'PG-{}'.format(str(rec.counter_poli_gigi))
                rec.counter_poli_gigi += 1
            else:
                rec.kode_poli_gigi = False
                rec.counter_poli_umum += 1  # Menambahkan counter_poli_umum untuk poli selain 'gigi'


    # kode_poli = fields.Char(compute='_compute_kode_poli', store=True, string='Nomor Urut')

    # @api.depends('poli')
    # def _compute_kode_poli(self):
    #     for rec in self:
    #         if rec.poli == 'umum':
    #             rec.kode_poli = 'PU-{}'.format(str(rec.id))
    #         elif rec.poli == 'gigi':
    #             rec.kode_poli = 'PG-{}'.format(str(rec.id))
    








    def duplicate_confirmation(self):
        for pasien_umum in self:
            vals = {
                'name_umum': pasien_umum.name_umum,
                'tanggal_umum': pasien_umum.tanggal_umum,
                'nip_umum': pasien_umum.nip_umum,
                'posisi_umum': pasien_umum.posisi_umum,
                'kode_work_center_umum': pasien_umum.kode_work_center_umum,
                'jam_umum': pasien_umum.jam_umum,
            }
            
            konfirmasi_umum = self.env['konfirmasi.pasien'].create(vals)