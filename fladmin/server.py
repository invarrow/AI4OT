
from flask import Flask, jsonify, render_template, request
import webbrowser
import time,csv
app = Flask(__name__)
bigrow = []
f= open(r"C:\Users\Ammar Ismail Baig\.vscode\AI4OT\dataset.csv")
csvreader = csv.reader(f)

@app.route('/_stuff', methods = ['GET'])
def stuff():

    for row in csvreader:
        bigrow.append(row)
        return jsonify(result=bigrow,nothing = "bruhh")


@app.route('/')
def index():
   
    return render_template('dy1.html')

    
if __name__ == '__main__':
    
    app.run()