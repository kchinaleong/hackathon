# README #

### Install ###

1) Setup and activate your `virtualenv`

2) Install the requirements.txt file:

- `pip install --no-deps -e . -r requirements.txt`

3) Create your Flask instance `config.py` file in `/instance/config.py`.

(Note: This file isn't checked into the repo.)

```
DEBUG = True
```

4) Run the app:

- `python run.py`

### Project Structure ###

```
config.py
/instance/config.py
flaskapp/
	__init__.py
	public/
		public/styles
	templates/
		home.html
	views/
		home.py
requirements.txt
run.py
setup.py
```
