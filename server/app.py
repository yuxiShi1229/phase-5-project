#!/usr/bin/env python3

from flask import request, session as flask_session
from flask_restful import Resource
from sqlalchemy.orm import Session as SQLAlchemySession

from config import app, db, api, bcrypt
from models import User, Transaction, Friendship

class Signup(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {'error': 'Username and password are required'}, 422

        if User.query.filter_by(username=username).first():
            return {'error': 'Username already exists'}, 409

        user = User(username=username)
        user.password_hash = password  # bcrypt handles the hashing

        db.session.add(user)
        db.session.commit()

        flask_session['user_id'] = user.id

        return {
            'id': user.id,
            'username': user.username
        }, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.authenticate(password):
            flask_session['user_id'] = user.id
            return {
                'id': user.id,
                'username': user.username
            }, 200
        else:
            return {'error': 'Invalid username or password'}, 401

class Logout(Resource):
    def delete(self):
        if 'user_id' in flask_session:
            flask_session.pop('user_id')
            return '', 204
        else:
            return {'error': 'Unauthorized'}, 401

class TransactionList(Resource):
    def get(self):
        user_id = flask_session.get('user_id')
        if not user_id:
            return {'error': 'Unauthorized'}, 401

        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        transactions = user.sent_transactions + user.received_transactions
        transactions.sort(key=lambda x: x.id, reverse=True)

        return [{
            'sender': trans.sender.username,
            'receiver': trans.receiver.username,
            'amount': trans.amount,
            'complete': trans.complete
        } for trans in transactions], 200

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(TransactionList, '/transactions', endpoint='transactions')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
