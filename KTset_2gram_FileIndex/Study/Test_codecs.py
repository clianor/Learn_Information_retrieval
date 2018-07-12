#!/Python27/python
# -*- coding: utf-8 -*-
import  codecs,sys

for line in open('Test_utf8.txt'):
	line=line.rstrip()
	print len(line),line
	
print sys.stdin.encoding
print sys.stdout.encoding
	
for line in open('Test_utf8.txt'):
	line=line.rstrip()
	print len(line.decode('utf-8')),line.decode('utf-8').encode(sys.stdout.encoding)
	
for line in codecs.open('Test_utf8.txt',encoding='utf-8'):
	line=line.rstrip()
	print len(line),line.encode(sys.stdout.encoding)