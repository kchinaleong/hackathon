from flask import render_template, flash, redirect, url_for, request
from flaskapp import app,db
from flaskapp.lib.errors import AppError
from flask.ext.wtf import Form
from wtforms import SubmitField, BooleanField, SelectMultipleField, widgets, RadioField
from wtforms.validators import Required
from flask.ext.login import current_user
from ..models import User

@app.route('/find', methods=['GET', 'POST'])
def find():
    """ Search page """
    referrer =  request.referrer.rsplit('/',1)[-1]
    profile_set = db.session.query(User.profile_id).filter(User.id==current_user.get_id()).scalar()
    if referrer == ('login') and profile_set:
       return redirect(url_for('home'))
    if profile_set is not None:
        return redirect(url_for('results'))
    form = CriteriaForm()
    if form.validate_on_submit():
    	""" criteria = Criteria(all bool fields to be put in db)
	if form.save_to_profile.data
	    save form criteria to user profile if user is signed in
	 """
        if form.save.data is True:
            current_user.profile_id=current_user.get_id()
            db.session.commit()
        return redirect(url_for('results'))
    return render_template('find.html', form=form)

class CriteriaForm(Form):
    age1 = BooleanField('Puppy')
    age2 = BooleanField('Adult')
    age3 = BooleanField('Retirement Age')
    size1 = BooleanField('Small')
    size2 = BooleanField('Medium')
    size3 = BooleanField('Large')
    low = BooleanField('Low')
    normal = BooleanField('Normal')
    high = BooleanField('High')
    health = RadioField('Health', validators=[Required()], choices=[('1','Yes'),('0','No')])
    behavior = RadioField('Behavior', validators=[Required()],choices=[('1','Yes'),('0','No')])
    children = RadioField('Children', validators=[Required()],choices=[('1','Yes'),('0','No')])	
    pets = RadioField('Pets', validators=[Required()],choices=[('1','Yes'),('0','No')])
    home = RadioField('Home', validators=[Required()],choices=[('1','Apartment'),('2','House with yard'),('3', 'Acreage')])
    experience = RadioField('Experience', validators=[Required()],choices=[('1','Little'),('3','Medium'),('3', 'High')])
    save = BooleanField('save_to_profile', default=True)
