from flaskapp import app
from flask.ext.bootstrap import Bootstrap

bootstrap=Bootstrap(app)
app.run(debug=app.config.get('DEBUG', False))
