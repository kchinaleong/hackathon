from flask import render_template

from flaskapp import app
from flaskapp.lib.errors import AppError
from flask.ext.wtf import Form
from wtforms import SubmitField, BooleanField


@app.route('/find')
def find():
    """ Search page """
    form = CriteriaForm()
    if form.validate_on_submit():
    	""" criteria = Criteria(all bool fields to be put in db)
	if form.save_to_profile.data
	    save form criteria to user profile if user is signed in
	 """
        flash("DB Stuff, Form Submitted, Search!")
	return redirect(url_for('home'))
    return render_template('find.html', form=form)

class CriteriaForm(Form):
     s1 = BooleanField('search')
     s2 = BooleanField('search')
     s3 = BooleanField('search')
     s4 = BooleanField('search')
     s5 = BooleanField('search')
     s6 = BooleanField('search')
     s7 = BooleanField('search')
     s8 = BooleanField('search')
     s9 = BooleanField('search')
     save = BooleanField('save_to_profile')
     submit = SubmitField('Search')
