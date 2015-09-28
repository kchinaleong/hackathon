from flaskapp import app

app.run(debug=app.config.get('DEBUG', False))
