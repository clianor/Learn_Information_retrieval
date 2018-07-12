#!/Python27/python
# -*- coding: utf-8 -*-
import  shelve

DB=shelve.open('test.shelve')
DB['Kim']=95
DB['Park']=100
DB['Lee']=86
DB.close()

