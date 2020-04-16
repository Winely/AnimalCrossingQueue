from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from db import db

manager = Manager(app)

db.init_app(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
