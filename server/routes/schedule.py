from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from models import Schedule, Classroom, User
from schemas import schedule_schema
from app import db
from services.email_service import send_class_reminder

bp = Blueprint('schedule', __name__, url_prefix='/api/schedules')

@bp.route('', methods=['POST'])
@jwt_required()
def create_schedule():
    try:
        data = schedule_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user_id = get_jwt_identity()
    classroom = Classroom.query.get(data['classroom_id'])
    if not classroom or classroom.teacher_id != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    new_schedule = Schedule(**data)
    db.session.add(new_schedule)
    db.session.commit()

    for student in classroom.students:
        send_class_reminder(student.email, classroom.name, new_schedule.start_time)

    return jsonify(schedule_schema.dump(new_schedule)), 201

@bp.route('/classroom/<int:classroom_id>', methods=['GET'])
@jwt_required()
def get_schedules(classroom_id):
    schedules = Schedule.query.filter_by(classroom_id=classroom_id).all()
    return jsonify(schedule_schema.dump(schedules, many=True)), 200
