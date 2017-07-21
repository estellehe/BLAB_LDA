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

lda = LdaModel(corpus = corpus, id2word = dictionary, num_topics = 400)
topiclist = lda.print_topics(num_topics = 400, num_words = 50)
lda.save('childs_sent_400.model')