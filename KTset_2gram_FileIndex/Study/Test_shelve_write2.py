#!/Python27/python
# -*- coding: utf-8 -*-
import  shelve

DB=shelve.open('test2.shelve')
DB['김철수']=95
#DB['김철수'.decode('utf-8')]=95  # String or Integer is allowed for key
DB.close()

DB=shelve.open('test2.shelve')
print DB