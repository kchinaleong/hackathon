from flask import render_template, redirect, url_for, request, flash
from flask.ext.login import current_user, login_user
from flaskapp import app
from flaskapp.lib.errors import AppError
from ..views.auth_forms import LoginForm
from ..models import User

@app.route('/', methods=['GET', 'POST'])
def home():
    """ Home page """
    form = LoginForm() 
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('find'))
        flash('Invalid username or password.')
    return render_template('home.html', form=form)
