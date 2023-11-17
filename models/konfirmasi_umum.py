from odoo import api, fields, models, _

class KonfirmasiUmum(models.Model):
    _name = "konfirmasi.pasien"
    _description = "KONFIRMASI DARI POLI UMUM PT.PAL"

    name_umum = fields.Char(string='Nama Pasien', required=True)
    
    nip_umum = fields.Char(string='NIP', required=True)
    
    tanggal_umum = fields.Date(string='Tanggal', required=True)
    
    posisi_umum = fields.Text(string='Job Position', required=True)
    
    kode_work_center_umum = fields.Char(string='Kode Work Center',  required=True)
    
    jam_umum = fields.Selection([
        ('pagi', 'PAGI'),
        ('siang', 'SIANG'),
        ('sore', 'SORE')], string='Waktu Periksa', default='pagi', tracking=True)

    state_umum = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', string="Status")

    def action_confirm(self):
        self.state_umum = 'done'
    
    def action_cancel(self):
        self.state_umum = 'cancel'

    def action_draft(self):
        self.state_umum = 'draft'

    def duplikat_umum(self):
        for konfirmasi_umum in self:
            vals = {
                'name_umum': konfirmasi_umum.name_umum,
                'tanggal_umum': konfirmasi_umum.tanggal_umum,
                'nip_umum': konfirmasi_umum.nip_umum,
                'posisi_umum': konfirmasi_umum.posisi_umum,
                'kode_work_center_umum': konfirmasi_umum.kode_work_center_umum,
                'jam_umum': konfirmasi_umum.jam_umum,
                'state_umum': konfirmasi_umum.state_umum,
            }
            
            status_umum = self.env['status.umum'].create(vals)