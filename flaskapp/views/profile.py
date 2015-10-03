from flask import render_template

from flaskapp import app
from flaskapp.lib.errors import AppError


@app.route('/profile')
def profile():
    """ Profile page """

    return render_template(
        'profile.html',
    )
