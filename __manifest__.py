{
    'name': 'clinic',
    'version': '1.0',
    'author': 'all',
    'summary': 'module clinic',
    'description': """ MODULE CLINIC TERKAIT PERIZINAN """,
    'application': True,
    'depends': ['base'],
    'data' : [
      'views/pasien.xml',
      'views/konfirmasi.xml',
      'views/status.xml',
      'views/report_admin.xml',
      'report/report_gigi.xml',
      'report/surat_gigi.xml',
      # 'report/report_umum.xml',
      # 'report/surat_umum.xml',
      'data/pasien_urut.xml',
      'security/ir.model.access.csv'
    ]
}

