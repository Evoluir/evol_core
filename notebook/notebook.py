# -*- coding: utf-8 -*-

from osv import fields, osv
import time

class notebook(osv.osv):
    _name = 'notebook'
    _description = 'Um Simples Notebook'
    _columns = {
                'title'     : fields.char('Titulo', size=30, required=True),
                'note'      : fields.text('Nota'),
                'note_date' : fields.date('Data'),
            }
notebook()
