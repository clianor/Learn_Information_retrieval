#!/Users/ejrgu/Anaconda3/python
# -*- coding: utf-8 -*-
import cgi,cgitb

print('Content-type: text/html\n') # \r\n\r\n
print('<html><head><meta charset=utf-8></head><body>')

cgitb.enable()
form = cgi.FieldStorage()
inputData=form.getvalue('inputData')


print('<br>')
print('<a href=echo.html>HOME</a>')
print('</body></html>')