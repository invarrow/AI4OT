from flask import Flask,redirect, url_for, request

app = Flask(__name__)

@app.route('/dashboard/<user>')
def dashboard(user):
    return "<H1>welcome %s to Dashboard</H1>"%user

@app.route('/admin',methods =['POST','GET'])
def admin():
        user  = request.form['uname']
        if user== 'smart':
            return redirect(url_for('dashboard',user=user))


if __name__ == "__main__":
    app.run(debug = True)
