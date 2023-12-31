from odoo import api, fields, models, _
from odoo.exceptions import UserError

class KonfirmasiGigi(models.Model):
    _name = "pasien.konfirmasi"
    _description = "KONFIRMASI DARI POLI PT.PAL"

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












    
    def duplicate(self):
        for status in self:
            vals = {
                'reference': status.reference,
                'name_umum': status.name_umum,
                'tanggal_umum': status.tanggal_umum,
                'nip_umum': status.nip_umum,
                'posisi_umum': status.posisi_umum,
                'kode_work_center_umum': status.kode_work_center_umum,
                'jam_umum': status.jam_umum,
                'poli': status.poli,
                'state': status.state,
            }
            
            status_konfirmasi = self.env['status.gigi'].create(vals)
    
    # @api.model
    # def create(self, vals):
    #     if vals.get('reference', _('New')) == _('New'):
    #         if vals.get('poli') == 'umum':
    #             vals['reference'] = self.env['ir.sequence'].next_by_code('pasien.umum.poli') or _('New')
    #         elif vals.get('poli') == 'gigi':
    #             vals['reference'] = self.env['ir.sequence'].next_by_code('pasien.umum.gigi') or _('New')
    #     return super(PasienUmum, self).create(vals)

    






