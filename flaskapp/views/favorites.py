from flask import render_template, redirect, url_for, request
from flaskapp import app,db
from ..models import User, Matches
from flask.ext.login import current_user

@app.route('/favorites')
def favorites():
    """ Favorites page """
    user = User.query.filter(User.id == current_user.get_id()).one()
    results = []
    for favorite in user.matches:
        results.append((favorite.adoptable.agency,favorite.adoptable))
    return render_template('favorites.html', results=results)

@app.route('/add', methods=['POST'])
def add_to_favorites():
    print "did I get here"
    favorite = Matches()
    favorite.adopt_id = request.form['pup_id']
    favorite.user_id = current_user.get_id()
    db.session.add(favorite)
    db.session.commit()
    return "",201 
