from flask import render_template

from flaskapp import app
from flaskapp.lib.errors import AppError


@app.route('/')
def home():
    """ Home page """

    return render_template(
        'home.html',
    )
