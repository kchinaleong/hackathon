#!/usr/bin/env python
import os
from flaskapp import app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from flaskapp.models import User, Agency, Adoptable, Matches

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Agency=Agency, Adoptable=Adoptable, Matches=Matches)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
