from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)

    sent_transactions = db.relationship('Transaction', foreign_keys='Transaction.sender_id', back_populates='sender', cascade="all, delete-orphan")
    received_transactions = db.relationship('Transaction', foreign_keys='Transaction.receiver_id', back_populates='receiver', cascade="all, delete-orphan")

    sent_friendships = db.relationship('Friendship', foreign_keys='Friendship.requester_id', back_populates='requester', cascade="all, delete-orphan")
    received_friendships = db.relationship('Friendship', foreign_keys='Friendship.requestee_id', back_populates='requestee', cascade="all, delete-orphan")

    transactions = association_proxy('sent_transactions', 'receiver')
    friendships = association_proxy('sent_friendships', 'requestee')

    serialize_rules = ('-sent_transactions.sender', '-received_transactions.receiver', '-sent_friendships.requester', '-received_friendships.requestee')

    def __repr__(self):
        return f"<User {self.username}>"

class Transaction(db.Model, SerializerMixin):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    complete = db.Column(db.Boolean, default=False)

    sender = db.relationship('User', foreign_keys=[sender_id], back_populates='sent_transactions')
    receiver = db.relationship('User', foreign_keys=[receiver_id], back_populates='received_transactions')

    serialize_rules = ('-sender.sent_transactions', '-receiver.received_transactions')

    def __repr__(self):
        return f"<Transaction from User {self.sender_id} to User {self.receiver_id} - Amount: {self.amount} - Complete: {self.complete}>"

class Friendship(db.Model, SerializerMixin):
    __tablename__ = "friendships"

    id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    requestee_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    requester = db.relationship('User', foreign_keys=[requester_id], back_populates='sent_friendships')
    requestee = db.relationship('User', foreign_keys=[requestee_id], back_populates='received_friendships')

    serialize_rules = ('-requester.sent_friendships', '-requestee.received_friendships')

    def __repr__(self):
        return f"<Friendship from User {self.requester_id} to User {self.requestee_id}>"
