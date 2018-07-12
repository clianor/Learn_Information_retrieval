#!/Python27/python
# -*- coding: utf-8 -*-
import codecs,sys,collections,shelve
import cgi,cgitb

def ngram(T): # T in utf-8
	L=[]
	for t in T.decode('utf-8').split():
		if len(t)==1: L.append(t.encode('utf-8')); continue
		for i in range(len(t)-1):
			L.append(t[i:i+2].encode('utf-8'))
		# end for/
	# end for
	return L
# end def

def Indexing(collectionFile):
	PostingDB,Title={},{}
	for v in codecs.open(collectionFile).read().splitlines(): # in utf-8
		docNo,docText=v.split('\t')
		Title[docNo]=docText.decode('utf-8')[:40].encode('utf-8')
		TF=collections.Counter(ngram(docText))
		for t in TF:
			if t not in PostingDB: PostingDB[t]={}
			PostingDB[t][docNo]=TF[t]
		# end for
	# end for
	return PostingDB,Title
# end def

def WriteToShelve(DB,oF):
	DB2=shelve.open(oF)
	for k in DB:
		DB2[k]=DB[k]
	# end for
# end def

PostingDB, Title=Indexing('collection')
WriteToShelve(PostingDB,'Posting.shelve')
WriteToShelve(Title,'Title.shelve')