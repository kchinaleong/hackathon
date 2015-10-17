from flask import render_template
from flaskapp import app

@app.route('/favorites')
def favorites():
    """ Favorites page """

    return render_template(
        'favorites.html',
    )
