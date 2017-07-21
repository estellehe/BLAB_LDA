import csv
from numpy import ones

with open ('cdi_id.csv', 'rb')as f:
    reader = csv.reader(f)
    idlist = []
    for row in reader:
        idlist.append(row)

a = 0.05
ntopic = 25
eta_arr = ones((ntopic, len(dictionary))) * 0.5
for x in range(0, len(idlist)):
    for id in idlist[x]:
        eta_arr[x][id] = 0.9
