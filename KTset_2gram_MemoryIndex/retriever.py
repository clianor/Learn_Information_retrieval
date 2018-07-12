#!/Python27/python
# -*- coding: utf-8 -*-
import codecs,sys,collections,math
import cgi,cgitb

def ngram(T):
	L=[]
	for t in T.split():
		if len(t)==1: L.append(t); continue
		for i in range(len(t)-1):
			L.append(t[i:i+2])
		# end for
	# end for
	#print ' '.join(L).encode('utf-8'),'<BR>'
	return L
# end def

def Indexing(collectionFile):
	TF,Title,original_Title,DF,MaxTF,N,avdl={},{},{},{},{},0,0
	for v in codecs.open(collectionFile,encoding='utf-8').read().splitlines():
		N+=1
		docNo,docText=v.split('\t')
		avdl+=len(docText)
		original_Title[docNo]=docText
		Title[docNo]=docText[:40]
		docTF=collections.Counter(ngram(docText))
		for t in docTF:
			if t not in TF: TF[t]={}
			TF[t][docNo]=docTF[t]	# TF
		# end for
	# end for
	MaxTF[docNo]=docNo
	DF = {t:len(TF[t]) for t in TF}
	avdl=avdl/float(N)
	IndexDB = {'TF':TF, 'DF':DF, 'Title':Title, 'original_Title':original_Title, 'N':N, 'MaxTF':MaxTF,'avdl':avdl}
	return IndexDB
# end def

def Retrieval_BM25(query,IndexDB,k1=1.2,k2=100,b=0.75):
	score,N,avdl,TF,DF = {},IndexDB['N'],IndexDB['avdl'],IndexDB['TF'],IndexDB['DF']
	qTF = collections.Counter(ngram(query))
	qTF = {qt:qTF[qt] for qt in qTF if qt in IndexDB['TF']}
	for qt in qTF:
		if qt not in DF: continue
		qtw = (k2+1)*qTF[qt]/float(k2+qTF[qt])
		df = float(DF[qt])
		idf = math.log((N-df+0.5)/df+0.5)
		for docNo in TF[qt]:
			if docNo not in score: score[docNo] = 0
			tf = TF[qt][docNo]
			dtw = (k1+1)*tf/(k1*((1-b)+b*(len(IndexDB['original_Title'][docNo])/avdl))+tf)
			score[docNo] = score[docNo]+idf*dtw*qtw if docNo in score else idf*dtw*qtw
		# end for
	# end for
	return score
# end def

def Retrieval_Vector(query,IndexDB):
	# lnn.ltn
	score,vector_docLength,N,TF,DF,queryLength={},{},IndexDB['N'],IndexDB['TF'],IndexDB['DF'],0.
	qTF = collections.Counter(ngram(query))
	qTF = {qt:qTF[qt] for qt in qTF if qt in IndexDB['TF']}
	for qt in qTF:
		if qt not in DF: continue
		qtw = (1+math.log(qTF[qt]))*math.log(1+N/float(DF[qt]))	# lt
		queryLength += qtw*qtw
		for docNo in TF[qt]:
			if docNo not in score: score[docNo]=0
			if docNo not in vector_docLength: vector_docLength[docNo]=0
			dtw = (1+math.log(TF[qt][docNo]))	# ln
			score[docNo] += score[docNo]+qtw*dtw if docNo in score else qtw*dtw
			vector_docLength[docNo]+=dtw*dtw
		# end for
	# end for
	
	for docNo in score:
		score[docNo] /= math.sqrt(queryLength)*math.sqrt(vector_docLength[docNo]) # c
	# end for
	
	return score
# end def

print 'Content-type: text/html\n' # \r\n\r\n
print '<html><head><meta charset=utf-8></head><body>'

cgitb.enable()
form = cgi.FieldStorage()
IndexDB=Indexing('collection')
query=form.getvalue('q').decode('utf-8')
#score=Retrieval_Vector(query,IndexDB)
score=Retrieval_BM25(query,IndexDB,k1=1.2,k2=100,b=0.75)
i=1
for docNo in sorted(score,key=score.get,reverse=True)[:10]:
	print '%02d'%i,score[docNo],docNo,IndexDB['Title'][docNo].encode('utf-8'),'<BR>'
	i+=1
# end for
print '<a href=search.html>HOME</a>'
print '</body></html>'