from restaurant import app
from flask import render_template, redirect, url_for, flash
from restaurant.models import Table, User
from restaurant.forms import RegisterForm, LoginForm, OrderIDForm
from restaurant import db

@app.route('/')
#HOME PAGE
@app.route('/home')
def home_page(): 
    return render_template('index.html')

#MENU PAGE
@app.route('/menu')
def menu_page():
    return render_template('menu.html')

#TABLE RESERVATION PAGE
@app.route('/table')
def table_page():
    tables = Table.query.all()
    return render_template('table.html', tables = tables)

#LOGIN PAGE
@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    forml = LoginForm()
    form = RegisterForm()
    return render_template('login.html', forml = forml, form = form)

#REGISTER PAGE
@app.route('/register', methods = ['GET', 'POST'])
def register_page():
    forml = LoginForm()
    form = RegisterForm()
    #checks if form is valid
    if form.validate_on_submit():
         user_to_create = User(username = form.username.data,
                               email_address = form.email_address.data,
                               password = form.password1.data)
         db.session.add(user_to_create)
         db.session.commit()
         return redirect(url_for('menu_page'))
    if form.errors != {}: #if there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}')
    return render_template('login.html', form = form, forml = forml)

#DELIVERY TRACKING
@app.route('/track')
def track_page():
    orderid = OrderIDForm()
    return render_template('order-id.html', orderid = orderid)
