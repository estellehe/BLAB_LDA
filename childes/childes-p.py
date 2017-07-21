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
    filew = []
    for sent in sents:
        result_lower = [item.lower() for item in sent]
        #result_stem = [stemmer.stem(item) for item in result_lower]
        result_clean = [item for item in result_lower if '\'' not in item 
        and '_' not in item and len(item) > 1]
        result = [item for item in result_clean if item not in sw]
        filew.extend(result)
    resultlist.append(filew)
print(resultlist[0])

  
dictionary = corpora.Dictionary(resultlist)
corpus = [dictionary.doc2bow(text) for text in resultlist]

lda = LdaModel(corpus = corpus, id2word = dictionary, num_topics = 50)
topiclist = lda.print_topics(num_topics = 50, num_words = 50)
lda.save('childs_file_50.model')
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

with open('childes_file_400.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
    for n in nlist:
        wr.writerow(n)
        
        '''