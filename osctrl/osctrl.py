# -*- coding: utf-8 -*-

from osv import fields, osv
import time

class osctrl(osv.osv):
    _name = 'osctrl'
    _description = 'Order Service Control'
    _columns = {
                'reference'      : fields.char('Reference', size=30, required=True),
            }
osctrl()
