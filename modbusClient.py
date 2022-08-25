from pyModbusTCP.client import ModbusClient
import csv
from time import sleep
import numpy as np
import joblib
import pandas as pd
model = joblib.load('bruno.joblib')
client = ModbusClient('localhost',port = 502)

file = open('dataset.csv','r')
csvreader = csv.reader(file)
newrow = []
data = pd.read_csv('dataset.csv')
df = pd.DataFrame(data)
    

df.columns = ['address','function','length','setpoint','gain','reset rate','deadband','cycle time','rate','system mode','control scheme','pump','solenoid','pressure measurement','crc rate','command response','time','binary result','categorized result','specific result']
df = df.replace('?',-1)
df = df.drop(columns = ['time','binary result','categorized result','specific result'])

for row in range(0,df.size):
    #print(df.iloc[row])
    r = pd.DataFrame([df.iloc[row]])
    pred = model.predict(r)
    print(pred)
    if pred!=[1]:
        
        try:
            rt =client.write_single_register(row,int(df.iloc[row]))
            
            # print(rt)
        except:
            pass
    else:
        break

