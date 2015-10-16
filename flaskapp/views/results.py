from flask import render_template, flash, redirect, url_for
from flaskapp import app, db
from ..models import Agency, Adoptable, Matches

@app.route('/results') 
def results():
    """ Query DB for all matches to profile"""
    results = db.session.query(Agency,Adoptable).filter(Agency.id==Adoptable.agency_id).all()
    return render_template('results.html', results=results)
