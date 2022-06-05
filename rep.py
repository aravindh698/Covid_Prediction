from flask import Flask,render_template,request
from flask import *
from flask_mysqldb import MySQL
import numpy as np
import pickle
import re
from flask import Flask, render_template, request, redirect, url_for, session
import MySQLdb.cursors

f = open('model2.pkl', 'rb')
model2=pickle.load(f)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
 
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = '2g2oJGLqTr'
app.config['MYSQL_PASSWORD'] = 'EUMUa2SBAD'
app.config['MYSQL_DB'] = '2g2oJGLqTr'
 
mysql = MySQL(app)
@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ""
    if request.method == 'POST' and 'id' in request.form and 'password' in request.form:
        id = request.form['id']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = % s AND password = % s', (id, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['password'] = account['password']
            return render_template('index2.html')
        else:
            msg = "INVALID ID OR PASSWORD"
    return render_template('register.html',msg = msg)

 
@app.route('/form', methods = ['POST', 'GET'])
def login():
    msg=""
    if request.method == 'GET':
        return render_template("register.html")
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        id = request.form['id']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = % s', (id, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists ! Login to Proceed' 
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (% s , % s, % s, % s)', (id, username, password, email))
            mysql.connection.commit()
            cursor.close()
            return render_template('register.html')
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    mysql.connection.commit()
    cursor.close()
    return render_template('form.html',msg = msg)
    
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model2.predict(final_features)
    output = round(prediction[0], 2)
    if request.method == 'POST':
       contactwithcovidpatient = request.form['Contact_with_covid_patient']
       Age = request.form['Age']
       Bodypain = request.form['Bodypain']
       Severity = request.form['Severity']
       Difficultyinbreathing = request.form['Difficulty_in_breathing']
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('INSERT INTO prediction VALUES (%s,%s,%s,%s,%s)',(contactwithcovidpatient,Age,Bodypain,Severity,Difficultyinbreathing))
       mysql.connection.commit()
       cursor.close()
    
    return render_template('index2.html', prediction_text='Chances of covid is {}'.format(output))

@app.route('/move_forward/',methods=['POST','GET'])
def move_forward():
    return render_template('base.php')

@app.route('/feedback/',methods=['POST','GET'])
def feedback():
    return render_template('base.php')



    
    

    
if __name__ == '__main__':
    app.run(port=5000,debug=True,use_reloader=False) 
