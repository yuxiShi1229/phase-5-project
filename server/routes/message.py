from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Message, Classroom
from app import db

bp = Blueprint('message', __name__, url_prefix='/api/messages')

@bp.route('/<int:classroom_id>', methods=['GET'])
@jwt_required()
def get_messages(classroom_id):
    messages = Message.query.filter_by(classroom_id=classroom_id).order_by(Message.timestamp.asc()).all()
    return jsonify([{
        'id': m.id,
        'content': m.content,
        'timestamp': m.timestamp,
        'user': m.user.username
    } for m in messages]), 200

@bp.route('/<int:classroom_id>', methods=['POST'])
@jwt_required()
def create_message(classroom_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    classroom = Classroom.query.get(classroom_id)
    if not classroom:
        return jsonify({"msg": "Classroom not found"}), 404
    new_message = Message(content=data['content'], user_id=user_id, classroom_id=classroom_id)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({
        'id': new_message.id,
        'content': new_message.content,
        'timestamp': new_message.timestamp,
        'user': new_message.user.username
    }), 201