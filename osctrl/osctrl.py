# -*- coding: utf-8 -*-

import time
import datetime
from osv import fields, osv

class osctrl(osv.osv):
    _name = 'osctrl'
    _description = 'Order Service Control'

    def _get_name(self, cr, uid,context, *args):
        obj_sequence = self.pool.get('ir.sequence')    
        return obj_sequence.next_by_code(cr, uid, 'osctrl.sequence', context=context)
    
    def _get_delivery(self, cr, uid, ids, context=None):
        dt_atual = datetime.datetime.today()
        dt_new   = dt_atual + datetime.timedelta(days=5)
        return dt_new.strftime('%Y-%m-%d')
        
    def _get_user(self, cr, uid, context=None):
        res={}
        return self.pool.get('res.users').browse(cr, uid, uid).id
        
    _columns = {
                'name'          : fields.char('Reference', size=30, required=True),
                'in_date'       : fields.date('Input Date', required=True),
                'delivery_date' : fields.date('Scheduled Output Date'),
                'user_id'       : fields.many2one('res.users', 'Attendant', required=True),
                'partner_id'    : fields.many2one('res.partner', 'Partner', required=True),  
                'product_type'  : fields.selection([
                    ('notebo','NoteBook/LapTop'),
                    ('tablet','Tablet/IPad'),
                    ('deskto','Desktop'),
                    ('monito','Monitor'),
                    ('impres','Impressora'),
                    ('multfu','Multifuncional'),
                    ('celula','Telefone Celular'),
                    ('nbreak','No-Break'),
                    ('fontes','Fonte'),
                    ('redewk','Rede Dados'),
                    ('servic','Serviços em Geral'),
                    ('outros','Outros'),
                    ],'Product',required=True, select=True),
                'manufacturer'  : fields.char('Manufacturer', size=40, required=True),
                'model'         : fields.char('Model', size=40, required=True),
                'serial'        : fields.char('Serial', size=30, required=True),
                'accessories'   : fields.text('Accessories'),
                'defect'        : fields.text('Claimed Defect'),
                'guarant_days'  : fields.integer('Warranty Time', required=True),
                'guarant_limit' : fields.date('Warranty Expiration',readonly=True),
                'state'         : fields.selection([
                    ('draft','Quotation'),
                    ('cancel','Cancelled'),
                    ('confirmed','Confirmed'),
                    ('under_repair','Under Repair'),
                    ('ready','Ready to Repair'),
                    ('2binvoiced','To be Invoiced'),
                    ('invoice_except','Invoice Exception'),
                    ('done','Repaired')
                    ], 'Status', readonly=True),

            }
    _defaults = {
                 'name'             : _get_name,
                 'state'            : lambda *a: 'draft',
                 'in_date'          : lambda *a: time.strftime('%Y-%m-%d'),
                 'delivery_date'    : _get_delivery,
                 'guarant_days'     : lambda *a: 30,
                 'user_id'          : _get_user,
                 }
osctrl()
