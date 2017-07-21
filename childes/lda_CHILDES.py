'''
import nltk
from gensim.models.ldamodel import LdaModel
from os import listdir
from nltk.corpus.reader import CHILDESCorpusReader
corpus_root = nltk.data.find('corpora/childes/data-xml/Eng-USA-MOR/')



class MyCorpus(object):
    corpus_root = nltk.data.find('corpora/childes/data-xml/Eng-USA-MOR/')
    def __iter__(self):
        folders = listdir('C:/nltk_data/corpora/childes/data-xml/Eng-USA-MOR')
        for f in folders:
            folder = CHILDESCorpusReader(corpus_root, f+'/.*.xml', lazy=False)
            files = folder.fileids()
            for filename in files:
                sents = folder.sents(filename)[0]
                for sent in sents:
                    result = [item.lower() for item in sent]
                    yield result

corpa = MyCorpus()
print(corpa)

lda = LdaModel(num_topics = 12)
#print(lda.show_topics(num_topics = 12))
'''


import nltk
import time
import csv
from gensim import corpora
from gensim.models.ldamodel import LdaModel
from os import listdir
from nltk.corpus.reader import CHILDESCorpusReader
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords, wordnet

start = time.time()
corpus_root = nltk.data.find('corpora/childes/data-xml/Eng-USA-MOR/')
folders = listdir('C:/nltk_data/corpora/childes/data-xml/Eng-USA-MOR')

#stemmer = SnowballStemmer("english")

sw = stopwords.words('english')
sw.extend(['xxx', 'yyy', 'www', 'huh', 'yeah','ever', 'even', 'anyway', 'everybody',  
'yes', 'mhm', 'yep', 'uhhuh', 'alright', 'never', 'sometimes', 'either', 'everyone'
'gonna', 'goin', 'another', 'okay', 'hey', 'anything', 'ready', 'uhuh', 'ouch', 'only', 
'away', 'sure', 'well', 'right', 'okay', 'would', 'around', 'across', 'everything', 
'maybe', 'big', 'little', 'nice', 'wow', 'new', 'cool', 'else', 'ago', 'almost', 'another', 
'ahead', 'always', 'already', 'whoops', 'em', 'wan', 'much', 'nope', 'hum', 'anyways',  
'yet', 'though', 'somethin', 'cha', 'anything', 'somebody', 'may', 'still', 'uhoh', 
'also', 'instead', 'whose', 'without', 'behind', 'anybody', 'any', 'away', 'why', 
'please', 'yay', 'oops', 'any', 'please', 'another', 'something', 'very'])
#sw = [stemmer.stem(item) for item in sw]

with open ('animal.csv', 'rb')as f:
    reader = csv.reader(f)
    animal = []
    for row in reader:
        animal.extend(row)

childes = CHILDESCorpusReader(corpus_root, '.*.xml', lazy=False)
files = childes.fileids()
resultlist = []

for filename in files:
    sents = childes.sents(filename)[0]
    for sent in sents:
        result_lower = [item.lower() for item in sent]
        #result_stem = [stemmer.stem(item) for item in result_lower]
        result_clean = [item for item in result_lower if '\'' not in item 
        and '_' not in item and len(item) > 1]
        result = [item for item in result_clean if item not in sw]
        resultlist.append(result)
print(resultlist[0])

  
dictionary = corpora.Dictionary(resultlist)
corpus = [dictionary.doc2bow(text) for text in resultlist]

with open ('mcdi_word.csv', 'rb')as f:
    reader = csv.reader(f)
    wlist = []
    for row in reader:
        wlist.append(row)

idlist = []

for row in wlist:
    idrow = []
    for key in dictionary.iteritems():
        if key[1].encode('utf-8') in row:
            idrow.append(key[0])
    idlist.append(idrow)

a = 0.05
ntopic = 25
eta_arr = ones((ntopic, len(dictionary))) * 0.5
for x in range(0, len(idlist)):
    for id in idlist[x]:
        eta_arr[x, id] *= 1000


lda = LdaModel(id2word = dictionary, num_topics = ntopic,alpha = a, eta = eta_arr)
lda.update(corpus)
topiclist = lda.print_topics(num_topics = 25, num_words = 50)
lda.save('childs_sent_25_a0.05eta.model')

'''
aniP = lda.get_document_topics(animal)
print aniP

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
        if len(wordnet.synsets(k, wordnet.NOUN))>0:
            xlist.append(k)
    nlist.append(xlist)

end = time.time()
print(end-start)

with open('childes_sent_300.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
    for n in nlist:
        wr.writerow(n)
    '''