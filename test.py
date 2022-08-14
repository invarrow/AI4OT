import requests
r = requests.get('http://www.ece.uah.edu/~thm0009/icsdatasets/IanArffDataset.arff')
with open('dataset.csv','w+') as dt:
    dt.write(r.text)

