from odoo import api, fields, models, _
from odoo.exceptions import UserError

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

    # @api.depends('poli', 'counter_poli_umum', 'counter_poli_gigi')
    # def _compute_kode_poli_umum(self):
    #     for rec in self:
    #         if rec.poli == 'umum':
    #             rec.kode_poli_umum = 'PU-{}'.format(str(rec.counter_poli_umum))
    #             rec.counter_poli_umum += 1
    #         else:
    #             rec.kode_poli_umum = False

    # @api.depends('poli', 'counter_poli_gigi', 'counter_poli_umum')
    # def _compute_kode_poli_gigi(self):
    #     for rec in self:
    #         if rec.poli == 'gigi':
    #             rec.kode_poli_gigi = 'PG-{}'.format(str(rec.counter_poli_gigi))
    #             rec.counter_poli_gigi += 1
    #         else:
    #             rec.kode_poli_gigi = False
    #             rec.counter_poli_umum += 1  # Menambahkan counter_poli_umum untuk poli selain 'gigi'
