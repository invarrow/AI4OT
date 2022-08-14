from pyModbusTCP.client import ModbusClient
import csv
from time import sleep
import numpy as np
client = ModbusClient('localhost',port = 502)

file = open('dataset.csv','r')
csvreader = csv.reader(file)

for row in csvreader:
    print(row)

    for i in range(0,20):
        try:
            rt =client.write_single_register(i,int(row[i]))
            print(rt)
        except:
            pass
    sleep(0.5)
