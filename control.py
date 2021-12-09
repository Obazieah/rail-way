from flask import Flask, render_template, request, redirect, session,url_for
from flask.helpers import get_root_path
from db import mydb, mycursor
import random
import string


app = Flask(__name__)
app.secret_key='any random string'

size = 590
randomlink = ''.join(random.choices(string.ascii_letters + string.digits, k = size))
randomString = str(randomlink)

@app.route('/')
def second():
    mycursor.execute(f'SELECT * FROM customers')
    customers = mycursor.fetchall()
    return render_template('base.html', customers= customers)

@app.route('/system', methods=['POST', 'GET'])
def form(): 
    if request.method=='POST':
        _name= request.form['name']
        _password =request.form['password']
        _age = request.form['age']
        _address= request.form['address']
        mycursor.execute(f'INSERT INTO customers(name, password, age, address) VALUES("{_name}", "{_password}","{_age}", "{_address}" )')
        mydb.commit()
        return redirect('/login_trvl')
    return render_template('form.html')
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/system')
@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/login_trvl', methods= ['GET','POST'])
def logintrv():
    msg=""
    if request.method=='POST':
        _name = request.form['name']
        _password = request.form['password']
        
        mycursor.execute(f'SELECT * FROM customers WHERE name = "{_name}" AND password = "{_password}"')
        verify=mycursor.fetchone()
        if verify:
            return render_template('travel_d.html', verify=verify)
        else:
            msg='Wrong Username or Passworg'
    return render_template('login_trvl.html' , msg=msg)
# ====================
# Admin login details
# =====================
name = "obadiah baron"
password = "baron"
# =====================
# =====================
@app.route('/')
def index():
    mycursor.execute("SELECT * FROM delists")
    delist = mycursor.fetchall()
    return render_template('base.html', delist = delist)

@app.route('/html', methods=['GET','POST'])
def html():
    if request.method == 'POST':
        mycursor.execute("SELECT * FROM delists")
    delist = mycursor.fetchall()
    return render_template('index.html', delist = delist)
@app.route('/trvl_d', methods=['GET', 'POST'])
def trvl_d():
    # if request.method == 'GET':
    #     return render_template('travel_d.html')
    if request.method == 'POST':
        _traveller_name = request.form['traveller_name']
        _from_where = request.form['from_where']
        _to_where = request.form['to_where']
        _departure_time = request.form['departure_time']
        sql = 'INSERT INTO delists (traveller_name, from_where, to_where, departure_time) VALUES (%s, %s, %s, %s)'
        val = (_traveller_name, _from_where, _to_where,_departure_time)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('win.html')
    return render_template('travel_d.html')
@app.route('/close')
def close():
    return render_template('travel_d.html')
@app.route('/bck')
def bck():
    return render_template('register.html')
@app.route('/range', methods=['GET','POST'])
def range():
    if request.method == 'GET':
        return render_template('range.html')
    if request.method == 'POST':
        _travel = request.form['travel']
        _form_text = request.form['form_text']
        sql = 'INSERT INTO checks(travel, form_text) VALUES(%s, %s)'
        val = (_travel, _form_text)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/close')
    return render_template('range.html')
@app.route('/details/<int:id>')
def customer_details(id):
    mycursor.execute(f'SELECT * FROM delists WHERE ID={id}')
    delist = mycursor.fetchone()
    return render_template('customer_detail.html', delist = delist)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM delists WHERE ID={id}')
        delist = mycursor.fetchone()
        return render_template('edit_customer.html', delist = delist)
    if request.method == 'POST':
        _traveller_name = request.form['traveller_name']
        _from_where = request.form['from_where']
        _to_where = request.form['to_where']
        _departure_time = request.form['departure_time']
        sql = (f'UPDATE delists SET traveller_name = %s, from_where = %s, to_where = %s, departure_time =%s WHERE ID = %s')
        values = (_traveller_name, _from_where, _to_where, _departure_time, id)
        mycursor.execute(sql, values)
        mydb.commit()
        return redirect('/back')

@app.route('/new')
def new():
    return render_template('base.html')
@app.route('/back')
def back():
    mycursor.execute("SELECT * FROM delists")
    delists = mycursor.fetchall()
    return render_template('details.html', delists =delists)
@app.route('/clear')
def clear():
    return render_template('base.html')
@app.route('/delete/<int:id>')
def delete_customer(id):
    sql = f'DELETE FROM delists WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    return redirect('/back')
# ==========================================
@app.route('/clog', methods=['POST', 'GET'])
def clog():
    if request.method == "POST":
        _name = request.form['username']
        _password = request.form['password']
        if _name == name and _password == password:
            return render_template('det.html')
    return render_template('register.html')
#  ============================================
# @app.route('/ind')
# def ind():
#     ycursor.execute("SELECT * FROM checks")
#     checks = mycursor.fetchall()
#     return render_template('view_changes.html', checks = checks)
# =============================================
@app.route('/clar', methods=['GET', 'POST'])
def clar():
    if request.method == 'GET':
        return render_template('range.html')
    if request.method == 'POST':
        _traveller_name = request.form['traveller_name']
        _from_text = request.form['from_text']
        sql = 'INSERT INTO checks(traveller_name, from_text) VALUES(%s, %s)'
        val = (_traveller_name, _from_text)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')
    return render_template('range.html')

# =============================================
@app.route('/hack')
def hack():
    mycursor.execute("SELECT * FROM checks")
    checks = mycursor.fetchall()
    return render_template('view_changes.html', checks = checks)
# =============================================
if __name__ =='__main__':
    app.run(debug = True)   
