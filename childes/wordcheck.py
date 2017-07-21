import csv
from gensim.corpora.dictionary import Dictionary

with open ('mcdi_word.csv', 'rb')as f:
    reader = csv.reader(f)
    wlist = []
    for row in reader:
        wlist.append(row)

dic = Dictionary.load('childs_file_25_asym.model.id2word')
idlist = []

for row in wlist:
    idrow = []
    idrow.append(row[0])
    for key in dic.iteritems():
        if key[1].encode('utf-8') in row:
            idrow.append(key[0])
    idlist.append(idrow)

csv_out = open('cdi_id.csv', 'wb')
writer = csv.writer(csv_out)

for row in idlist:
    writer.writerow(row)
