from flask.cli import FlaskGroup
from app import create_app, db
from models import User, Classroom, Message, Schedule  # Import your models here

cli = FlaskGroup(create_app=create_app)

@cli.command("create_db")
def create_db():
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()