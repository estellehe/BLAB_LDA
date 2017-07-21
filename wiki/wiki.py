import logging, gensim, bz2file, csv
from gensim.models.ldamodel import LdaModel
from numpy import ones

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = gensim.corpora.Dictionary.load_from_text(bz2file.BZ2File('wiki_wordids.txt.bz2'))
corpus = gensim.corpora.MmCorpus('wiki_tfidf.mm')

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
lda.save('wiki_file_25_a0.05eta.model')

