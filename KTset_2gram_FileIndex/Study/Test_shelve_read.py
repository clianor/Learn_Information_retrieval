#!/Python27/python
# -*- coding: utf-8 -*-
import  shelve

DB=shelve.open('test.shelve')
print DB['Kim']
print DB
DB.close()
