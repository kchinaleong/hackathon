from flask import render_template, redirect, url_for, request
from flaskapp import app

@app.route('/favorites')
def favorites():
    """ Favorites page """

    return render_template(
        'favorites.html',
    )

@app.route('/add', methods=['POST'])
def add_to_favorites():
    #form = request.form
    print 'am I getting here?'
    #if form.is_submitted()
    return redirect(url_for('results'))

