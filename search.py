#!/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-
import  codecs,sys,collections
import cgi,cgitb

def Indexing(collectionFile):
    PostingDB,Title={},{}
    for v in codecs.open(collectionFile,encoding='utf-8').read().splitlines():
        docNo,docText=v.split('\t')
        Title[docNo]=docText[:40]
        TF=collections.Counter(docText.split())
        for t in TF:
            if t not in PostingDB: PostingDB[t]={}
            PostingDB[t][docNo]=TF[t]
        # end for
    # end for
    return PostingDB,Title
# end def

def Retrieval(query,PostingDB):
    score={}
    for t in query.split():
        if t not in PostingDB: continue
        for docNo in PostingDB[t]:
            if docNo not in score: score[docNo]=0
            score[docNo]+=PostingDB[t][docNo]
        # end for
    # end for
    return score
# end def

print('Content-type: text/html\n')
print('<html><head><meta charset=utf-8></head><body>')
cgitb.enable()
form = cgi.FieldStorage()
inputData = form.getvalue('inputData')
print(inputData, 'Search Result')

PostingDB,Title=Indexing('collection')

query = inputData
score = Retrieval(query,PostingDB)
print('<br>score, docNo, Title')
for docNo in sorted(score,key=score.get,reverse=True)[:10]:
	print('<br>', score[docNo], docNo, Title[docNo])

print('<br>')
print('<a href=search.html>HOME</a>')
print('</body></html>')