# -*- coding: utf-8 -*-
import csv
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
from nltk.corpus import stopwords, wordnet

topicid = 'food'
topicn = 100
partype = ''
unit = 'file'

with open (topicid+'.csv', 'rb')as f:
    reader = csv.reader(f)
    animal = []
    for row in reader:
        animal.extend(row)

dic = Dictionary.load('wiki_'+unit+'_'+str(topicn)+partype+'.model.id2word')
bow = dic.doc2bow(animal)

lda = LdaModel.load('wiki_'+unit+'_'+str(topicn)+partype+'.model')
topiclist = lda.print_topics(num_topics = topicn, num_words = 100)

aniP = lda.get_document_topics(bow, minimum_probability = 0)
maxpro = []
for pro in aniP:
    each = []
    each.append(pro[0])
    each.append(pro[1])
    maxpro.append(each)


def wordP(word, topic):
    for key in dic.iteritems():
        if key[1] == word:
            wid = key[0]
            wtopic = lda.get_term_topics(wid, minimum_probability=0)
            for wt in wtopic:
                if wt[0] == topic:
                    return wt[1]
    return 0
            
            
with open('wiki_'+unit+'_'+str(topicn)+'_'+partype+topicid+'.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
    frow = []
    frow.append('topic')
    frow.extend(animal)
    wr.writerow(frow)
    for p in aniP:
        plist = []
        plist.append(p[0])
        for ani in animal:
            plist.append(wordP(ani, p[0]))
        wr.writerow(plist)
    

rlist = []
for topic in topiclist:
    rlist.append(topic[1].split("+"))

nlist = []
for n in rlist:
    xlist = []
    for k in n:
        k = k.split("*")
        k = k[1].encode('utf-8')
        k = k.split('\"')[1]
        xlist.append(k)
    nlist.append(xlist)


with open('wiki_'+unit+'_'+str(topicn)+partype+'.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
    for n in nlist:
        wr.writerow(n)

with open('wiki_'+unit+'_'+str(topicn)+partype+'pro.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
    for n in maxpro:
        wr.writerow(n)