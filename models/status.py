from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StatusGigi(models.Model):
    _name = "status.gigi"
    _description = "STATUS KONFIRMASI DARI POLI PT.PAL"

   
    reference = fields.Char(string='Reference', required=True, readonly=True, copy=False, default=lambda self: _('New'))
  
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

    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', string="Status")

    def action_confirm(self):
        self.state = 'done'
    
    def action_cancel(self):
        self.state = 'cancel'

    def action_draft(self):
        self.state = 'draft'


