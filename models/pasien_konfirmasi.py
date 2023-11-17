from odoo import api, fields, models, _

class PasienKonfirmasi(models.Model):
    _name = "pasien.konfirmasi"
    _description = "KONFIRMASI DARI POLI PT.PAL"

    # reference_pasien_umum = fields.Char(string='Reference', required=True, readonly=True, copy=False, default=lambda self: _('New'))

    name_gigi = fields.Char(string='Nama Pasien', required=True)
    
    nip_gigi = fields.Char(string='NIP', required=True)
    
    tanggal_gigi = fields.Date(string='Tanggal', required=True)
    
    posisi_gigi = fields.Text(string='Job Position', required=True)
    
    kode_work_center_gigi = fields.Char(string='Kode Work Center',  required=True)
    
    
    # state_umum = fields.Selection([ 
    #     ('inprogress', 'Inprogress'),
    #     ('confirm', 'Confirmed'),
    #     ('done', 'Done'),
    #     ('cancel', 'Cancelled')], string='Status', default='inprogress', tracking=True)
    
    jam_gigi = fields.Selection([
        ('pagi', 'PAGI'),
        ('siang', 'SIANG'),
        ('sore', 'SORE')], string='Waktu Periksa', default='pagi', tracking=True)

    # def action_confirm(self):
    #     self.state = 'confirm'

    # def action_done(self):
    #     self.state = 'done'
    
    # def action_inprogress(self):
    #     self.state = 'inprogress'

    # def action_cancel(self):
    #     self.state = 'cancel'

class PasienUmum(models.Model):
    _name = "pasien.umum"
    _description = "PASIEN DARI POLI UMUM PT.PAL"

    # reference_pasien_umum = fields.Char(string='Reference', required=True, readonly=True, copy=False, default=lambda self: _('New'))

    name_umum = fields.Char(string='Nama Pasien', required=True)
    
    nip_umum = fields.Char(string='NIP', required=True)
    
    tanggal_umum = fields.Date(string='Tanggal', required=True)
    
    posisi_umum = fields.Text(string='Job Position', required=True)
    
    kode_work_center_umum = fields.Char(string='Kode Work Center',  required=True)
    
    
    # state_umum = fields.Selection([ 
    #     ('inprogress', 'Inprogress'),
    #     ('confirm', 'Confirmed'),
    #     ('done', 'Done'),
    #     ('cancel', 'Cancelled')], string='Status', default='inprogress', tracking=True)
    
    jam_umum = fields.Selection([
        ('pagi', 'PAGI'),
        ('siang', 'SIANG'),
        ('sore', 'SORE')], string='Waktu Periksa', default='pagi', tracking=True)

    