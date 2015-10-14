from flask import render_template, flash, redirect, url_for
from flaskapp import app
from flaskapp.lib.errors import AppError
from flask.ext.wtf import Form
from wtforms import SubmitField, BooleanField, SelectMultipleField, widgets, RadioField
from wtforms.validators import Required

@app.route('/find', methods=['GET', 'POST'])
def find():
    """ Search page """
    form = CriteriaForm()
    if form.validate_on_submit():
    	""" criteria = Criteria(all bool fields to be put in db)
	if form.save_to_profile.data
	    save form criteria to user profile if user is signed in
	 """
        flash("db stuff, form submitted, search!")
        return redirect(url_for('home'))
    print(dir(form))
    print(form.errors)
    flash("form not validated")
    if form.is_submitted():
        flash("form is submitted")
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
    health = RadioField('Health', validators=[Required()], choices=[('1','Yes'),(0,'No')])
    behavior = RadioField('Behavior', validators=[Required()],choices=[('1','Yes'),(0,'No')])
    children = RadioField('Children', validators=[Required()],choices=[('1','Yes'),(0,'No')])	
    pets = RadioField('Pets', validators=[Required()],choices=[('1','Yes'),(0,'No')])
    home = RadioField('Home', validators=[Required()],choices=[('1','Apartment'),('2','House with yard'),('3', 'Acreage')])
    experience = RadioField('Experience', validators=[Required()],choices=[('1','Little'),('3','Medium'),('3', 'High')])
    save = BooleanField('save_to_profile')
    submit = SubmitField('Find Adoptables!')
