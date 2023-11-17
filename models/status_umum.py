from odoo import api, fields, models, _

class StatusUmum(models.Model):
    _name = "status.umum"
    _description = "STATUS KONFIRMASI DARI POLI UMUM PT.PAL"

    name_umum = fields.Char(string='Nama Pasien', required=True)

    
    nip_umum = fields.Char(string='NIP', required=True)

    
    tanggal_umum = fields.Date(string='Tanggal', required=True)

    poli = fields.Selection([
            ('umum','Poli Umum'),
            ('gigi','Poli Gigi')], 
            required=True, default = 'umum', tracking = True)

    def _get_kode_poli(self):
        if self.poli == 'umum':
            return 'PU-{}'.format(self.id)
        else:
            return 'PG-{}'.format(self.id)
    
    kode_poli = fields.Char(compute=_get_kode_poli, store=True)
    

    posisi_umum = fields.Text(string='Job Position', required=True)

    
    kode_work_center_umum = fields.Char(string='Kode Work Center',  required=True)
    
    jam_umum = fields.Selection([
        ('pagi', 'PAGI'),
        ('siang', 'SIANG'),
        ('sore', 'SORE')], string='Waktu Periksa', default='pagi', tracking=True)


    state_umum = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', string="Status")


    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, 
                            default=lambda self: _('New'))

    def action_confirm(self):
        self.state_umum = 'done'
    def action_cancel(self):
        self.state_umum = 'cancel'
    def action_draft(self):
        self.state_umum = 'draft'

    @api.model
    def create(self, vals):
        if vals.get('note'):
            vals['note'] = 'New Pasien'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('status.umum') or _('New')
        res = super(StatusUmum, self).create(vals)
        return res
