from odoo import api, fields, models, _
from odoo import api, fields, models, _
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime
from datetime import date

class PasienUmum(models.Model):
    _name = "pasien.umum"
    _description = "PASIEN DARI POLI UMUM PT.PAL"
    _rec_name = 'name_umum'

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
    
    # state = fields.Selection([
    #     ('darft', 'Draft'),
    #     ('confirm', 'Confirmed')], 
    #     required=True, string='status', default='draft', tracking=True)

    # def action_confirm(self):
    #     self.state = 'confirm'

    # def action_confirm(self):
    #     self.state = 'draft'

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            if vals.get('poli') == 'umum':
                vals['reference'] = self.env['ir.sequence'].next_by_code('pasien.umum.poli') or _('New')
            elif vals.get('poli') == 'gigi':
                vals['reference'] = self.env['ir.sequence'].next_by_code('pasien.umum.gigi') or _('New')
        return super(PasienUmum, self).create(vals)

    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', string="Status")

    def action_confirm(self):
        self.state = 'done'
    
    def action_cancel(self):
        self.state = 'cancel'

    def action_draft(self):
        self.state = 'draft'

    








    def duplicate_confirmation(self):
        for pasien in self:
            vals = {
                'reference': pasien.reference,
                'name_umum': pasien.name_umum,
                'tanggal_umum': pasien.tanggal_umum,
                'nip_umum': pasien.nip_umum,
                'posisi_umum': pasien.posisi_umum,
                'kode_work_center_umum': pasien.kode_work_center_umum,
                'jam_umum': pasien.jam_umum,
                'poli': pasien.poli,
                'state': pasien.state,
            }
            
            konfirmasi_umum = self.env['pasien.konfirmasi'].create(vals)