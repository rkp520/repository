from flask import Flask, render_template,request,session
import sqlite3

app=Flask(__name__)
app.secret_key='mykey'


@app.route('/',methods=['GET','POST'])
def web():
   error=None
   if request.method=='POST':
        if request.form['empname']!='admin' or request.form['emplocation']!='noida':
            error="Please insert valid details"
        else:
            session['logged_in']=True
            return render_template('show.html')
   return render_template('index.html',error=error)

@app.route('/logout')
def show():
    session.pop('logged_in',None)
    return render_template('index.html')






app.run()