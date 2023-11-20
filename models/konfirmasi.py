from odoo import api, fields, models, _
from odoo.exceptions import UserError

class KonfirmasiGigi(models.Model):
    _name = "pasien.konfirmasi"
    _description = "KONFIRMASI DARI POLI GIGI PT.PAL"

  
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

    kode_poli_umum = fields.Char(store=True, string='Nomor Urut Poli Umum')
    kode_poli_gigi = fields.Char(store=True, string='Nomor Urut Poli Gigi')

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


    kode_poli = fields.Char(compute='_compute_kode_poli', store=True, string='Nomor Urut')

    @api.depends('poli')
    def _compute_kode_poli(self):
        for rec in self:
            if rec.poli == 'umum':
                rec.kode_poli = 'PU-{}'.format(str(rec.id))
            elif rec.poli == 'gigi':
                rec.kode_poli = 'PG-{}'.format(str(rec.id))
    










    # def duplicat(self):
    #     for konfirmasi in self:
    #         vals = {
    #             'name_gigi': konfirmasi.name_gigi,
    #             'tanggal_gigi': konfirmasi.tanggal_gigi,
    #             'nip_gigi': konfirmasi.nip_gigi,
    #             'posisi_gigi': konfirmasi.posisi_gigi,
    #             'kode_work_center_gigi': konfirmasi.kode_work_center_gigi,
    #             'jam_gigi': konfirmasi.jam_gigi,
    #             'state_gigi': konfirmasi.state_gigi,
    #             'poli':konfirmasi.poli,
    #             'kode_poli_umum': konfirmasi.kode_poli_umum,
    #             'kode_poli_gigi': konfirmasi.kode_poli_gigi
    #         }
            
    #         status_gigi = self.env['status.gigi'].create(vals)
