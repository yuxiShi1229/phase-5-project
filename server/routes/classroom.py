from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import Classroom, User
from services.dyte_service import create_dyte_meeting, create_dyte_participant_token
from services.email_service import send_class_reminder, send_class_invitation

bp = Blueprint('classroom', __name__, url_prefix='/api/classrooms')

@bp.route('', methods=['POST'])
@jwt_required()
def create_classroom():
    data = request.get_json()
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user.is_teacher:
        return jsonify({"msg": "Only teachers can create classrooms"}), 403
    
    new_classroom = Classroom(name=data['name'], description=data['description'], teacher_id=user_id)
    db.session.add(new_classroom)
    db.session.commit()

    dyte_meeting_id = create_dyte_meeting(new_classroom.id)
    new_classroom.dyte_meeting_id = dyte_meeting_id
    db.session.commit()
    
    return jsonify({"id": new_classroom.id, "name": new_classroom.name}), 201

@bp.route('/<int:id>/join', methods=['POST'])
@jwt_required()
def join_classroom(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    classroom = Classroom.query.get(id)
    
    if not classroom:
        return jsonify({"msg": "Classroom not found"}), 404

    participant_token = create_dyte_participant_token(classroom.dyte_meeting_id, user.id, user.username)
    
    return jsonify({
        "dyte_meeting_id": classroom.dyte_meeting_id,
        "participant_token": participant_token
    }), 200

@bp.route('/<int:classroom_id>/invite', methods=['POST'])
@jwt_required()
def invite_student(classroom_id):
    user_id = get_jwt_identity()
    classroom = Classroom.query.get(classroom_id)

    if not classroom or classroom.teacher_id != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    data = request.json
    student_email = data['email']
    
    send_class_invitation(student_email, classroom.name)
    
    return jsonify({"msg": f"Invitation sent to {student_email}"}), 200