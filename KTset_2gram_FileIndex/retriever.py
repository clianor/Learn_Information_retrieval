#!/Python27/python
# -*- coding: utf-8 -*-
import  codecs,sys,collections,shelve
import cgi,cgitb

def ngram(T): # T in utf-8
	L=[]
	for t in T.decode('utf-8').split():
		if len(t)==1: L.append(t.encode('utf-8')); continue
		for i in range(len(t)-1):
			L.append(t[i:i+2].encode('utf-8'))
		# end for
	# end for
	return L
# end def

def Retrieval(query,PostingDB):
	score={}
	for t in ngram(query):
		if t not in PostingDB: continue
		TF=PostingDB[t]
		for docNo in TF:
			if docNo not in score: score[docNo]=0
			score[docNo]+=TF[docNo]
		# end for
	# end for
	return score
# end def

print 'Content-type: text/html\n' # \r\n\r\n
print '<html><head><meta charset=utf-8></head><body>'

cgitb.enable()
form = cgi.FieldStorage()
query=form.getvalue('q')

PostingDB=shelve.open('Posting.shelve')
Title=shelve.open('Title.shelve')

score=Retrieval(query,PostingDB)
i=1
for docNo in sorted(score,key=score.get,reverse=True)[:10]:
	print '%02d'%i,score[docNo],docNo,Title[docNo],'<BR>'
	i+=1
# end for
print '<a href=search.html>HOME</a>'
print '</body></html>'