from flask_marshmallow import Marshmallow
from models import User, Classroom, Message

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ('password_hash',)

class ClassroomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Classroom
        load_instance = True
        include_fk = True

class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
        load_instance = True
        include_fk = True

user_schema = UserSchema()
classroom_schema = ClassroomSchema()
message_schema = MessageSchema()