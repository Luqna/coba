from odoo import api, fields, models, _

class KonfirmasiGigi(models.Model):
    _name = "pasien.konfirmasi"
    _description = "KONFIRMASI DARI POLI GIGI PT.PAL"

  
    name_gigi = fields.Char(string='Nama Pasien', required=True)
    
    nip_gigi = fields.Char(string='NIP', required=True)
    
    tanggal_gigi = fields.Date(string='Tanggal', required=True)
    
    posisi_gigi = fields.Text(string='Job Position', required=True)
    
    kode_work_center_gigi = fields.Char(string='Kode Work Center',  required=True)
    
    jam_gigi = fields.Selection([
        ('pagi', 'PAGI'),
        ('siang', 'SIANG'),
        ('sore', 'SORE')], string='Waktu Periksa', default='pagi', tracking=True)
    
    state_gigi = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', string="Status")

    def action_confirm(self):
        self.state_gigi = 'done'
    
    def action_cancel(self):
        self.state_gigi = 'cancel'

    def action_draft(self):
        self.state_gigi = 'draft'


    def duplicat(self):
        for konfirmasi in self:
            vals = {
                'name_gigi': konfirmasi.name_gigi,
                'tanggal_gigi': konfirmasi.tanggal_gigi,
                'nip_gigi': konfirmasi.nip_gigi,
                'posisi_gigi': konfirmasi.posisi_gigi,
                'kode_work_center_gigi': konfirmasi.kode_work_center_gigi,
                'jam_gigi': konfirmasi.jam_gigi,
                'state_gigi': konfirmasi.state_gigi,
            }
            
            status_gigi = self.env['status.gigi'].create(vals)
