import datetime
from flask import Flask
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for, render_template, flash
from functools import wraps
from models import *
from forms import *

app = Flask(__name__)
app.secret_key = 'Sm9obiBTY2hyb20ga2lja3MgYXNz465Hjjdk'

# Configuration

BCRYPT_LEVEL = 12  # Configuration for the Flask-Bcrypt extension


@app.before_request
def before_request():
    g.db = database
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def homepage():
    # depending on whether the requesting user is logged in or not, show them
    # either the login or their own selection screen
    if session.get('logged_in'):
        return start_page()
    else:
        return login()


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username']:
        try:
            user = User.get(username=request.form['username'],
                            password=request.form['password'])
        except User.DoesNotExist:
            flash('The password entered is incorrect')
        else:
            auth_user(user)
            return redirect(url_for('homepage'))

    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('homepage'))


@app.route('/product/')
def start_page():
    product_list = Product.select()
    return render_template('start_page.html', product_list=product_list)


# flask provides a "session" object, which allows us to store information across
# requests (stored by default in a secure cookie).  this function allows us to
# mark a user as being logged-in by setting some values in the session data:
def auth_user(user):
    session['logged_in'] = True
    session['user_id'] = user.id
    session['username'] = user.username
    if user.is_admin:
        session['is_admin'] = 'y'
    else:
        session['is_admin'] = 'n'
    flash('You are logged in as %s' % (user.username))


# get the user from the session
def get_current_user():
    if session.get('logged_in'):
        return User.get(User.id == session['user_id'])


# view decorator which indicates that the requesting user must be authenticated
# before they can access the view.  it checks the session to see if they're
# logged in, and if not redirects them to the login view.
def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return inner


@app.route('/product/<string:product_code>', methods=['GET', 'POST'])
def product_page(product_code):
    # show the post with the given id, the id is an integer
    try:
        product = Product.get(Product.code == product_code)
    except Product.DoesNotExist:
        flash('The product does not exist')
        return redirect(url_for('homepage'))
    else:
        form = ProductCountForm()
        return render_template('product_page.html', product=product, form=form)


@app.route('/countproduct/<string:product_code>', methods=['GET', 'POST'])
def countproduct(product_code, ):
    # show the post with the given id, the id is an integer
    try:
        product = Product.get(Product.code == product_code)
        user = User.get(User.username == session['username'])

    except Product.DoesNotExist:
        flash('The product does not exist')
        return redirect(url_for('homepage'))
    else:
        form = ProductCountForm()
        if form.validate_on_submit():
            product_count = ProductCount()
            product_count.counted_by = user
            product_count.product = product
            product_count.count = int(form.counted.data)
            product_count.save()
            msg = "You have counted {} of {}".format(str(form.counted.data),
                                product.name)
            flash(msg)
            return redirect(url_for('homepage'))
        else:
            flash('There was an error. Your input should be an integer')
            return redirect(url_for('product_page', product_code=product.code))


@app.route('/letter/')
def product_by_letter_group():
    product_list = Product.select()
    return render_template('start_page.html', product_list=product_list)


@app.route('/view_recent_count/')
def view_recent_count():
    user = User.get(User.username == session['username'])
    count_list = (ProductCount.select().where(ProductCount.counted_by == user)
                 .limit(20))
    return render_template('recent_counts.html', count_list=count_list)


@app.route('/user_recent_counts/<string:username>')
def user_recent_counts(username):
    if session['is_admin'] == 'y':
        return admin_recent_counts(username)
    else:
        flash('You cannot access this page')
        return redirect(url_for('homepage'))


def admin_recent_counts(username=None):
    if username == 'all':
        count_list = ProductCount.select().limit(100)
    else:
        try:
            user = User.get(User.username == username)
        except User.DoesNotExist:
            flash('The user does not exist')
            return redirect(url_for('homepage'))
        else:
            count_list = ProductCount.select().where(
                ProductCount.counted_by == user).limit(100)
    enumerators = User.select()
    return render_template('admin_recent_counts.html', enumerators=enumerators,
        count_list=count_list, username=username)