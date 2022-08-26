
from flask import Flask, jsonify, render_template, request
import webbrowser
import time,csv
from pyModbusTCP.client import ModbusClient
import csv
from time import sleep
import numpy as np
import joblib
import asyncio
import pandas as pd
app = Flask(__name__)
bigrow = []
model = joblib.load('bruno.joblib')
client = ModbusClient('localhost',port = 502)



newrow = []
data = pd.read_csv('dataset1.csv')
df = pd.DataFrame(data)
    

df.columns = ['address','function','length','setpoint','gain','reset rate','deadband','cycle time','rate','system mode','control scheme','pump','solenoid','pressure measurement','crc rate','command response','time','binary result','categorized result','specific result']
df = df.replace('?',-1)
df = df.drop(columns = ['time','binary result','categorized result','specific result'])

def write_dat(row):
    for row in range(0,df.size):
        #print(df.iloc[row])
        r = pd.DataFrame([df.iloc[row]])
        pred = model.predict(r)
        print(pred)
        if pred!=[1]:
            
            try:
                rt =client.write_single_register(row,int(df.iloc[0,row]))

                return rt
                # print(rt)
            except:
                pass
        else:
            return False
            

@app.route('/_stuff', methods = ['GET'])
def stuff():

    for row in range(0,df.size):
        print(df.size)
        dfObj= df.iloc[row]
        dfObj = df.to_numpy()[row].tolist()
        
        # dfObj = dfObj.to_list()
        
        
        bigrow.append(dfObj)    
        return jsonify(result=bigrow,nothing = write_dat())


@app.route('/')
def index():
   
    return render_template('dy1.html')

    
if __name__ == '__main__':
    
    app.run()