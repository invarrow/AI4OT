
from flask import Flask, jsonify, render_template, request
import webbrowser
import time,csv

file = open('C:\\Users\\rashe\\OneDrive\\Desktop\\otHack\\AI4OT\\test.csv','r')
csvreader = csv.reader(file)

app = Flask(__name__)

@app.route('/_stuff', methods = ['GET'])
def stuff():
    for row in csvreader:
        print(row)
        return jsonify(str(row))
    
    


@app.route('/')
def index():
    return render_template('dy1.html')

    
if __name__ == '__main__':
    
    app.run()