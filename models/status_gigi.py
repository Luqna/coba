from odoo import api, fields, models, _

class StatusGigi(models.Model):
    _name = "status.gigi"
    _description = "STATUS KONFIRMASI DARI POLI GIGI PT.PAL"

    # reference_pasien_umum = fields.Char(string='Reference', required=True, readonly=True, copy=False, default=lambda self: _('New'))

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
    
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, 
                            default=lambda self: _('New'))

    def action_confirm(self):
        self.state_gigi = 'done'
    
    def action_cancel(self):
        self.state_gigi = 'cancel'

    def action_draft(self):
        self.state_gigi = 'draft'

    @api.model
    def create(self, vals):
        if vals.get('note'):
            vals['note'] = 'New Pasien'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('status.gigi') or _('New')
        res = super(StatusGigi, self).create(vals)
        return res
  
