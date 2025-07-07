from models import db
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import SQLAlchemyError
import enum
from datetime import datetime

IST = datetime.now().astimezone().tzinfo

class UserRole(enum.Enum):
    ADMIN = 'admin'
    USER = 'user'

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False, default=UserRole.USER)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(IST))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(IST), onupdate=datetime.now(IST))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def is_admin(self):
        return self.role == UserRole.ADMIN
    
    def __repr__(self):
        return '<User %r>' % self.username
    

class SymptomLog(db.Model):
    __tablename__ = "symptom_logs"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)
    response = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(IST))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(IST), onupdate=datetime.now(IST))

    user = db.relationship("User", backref=db.backref("symptom_logs", lazy=True))

    def __repr__(self):
        return f"<SymptomLog {self.symptom_text[:30]}... at {self.timestamp}>"

def create_admin(app):
    if not User.query.filter_by(role=UserRole.ADMIN).first():
        try:
            admin = User(username='admin', email='admin@gmail.com', password=generate_password_hash('admin123'), role=UserRole.ADMIN)
            db.session.add(admin)
            db.session.commit()
            current_app.logger.info('Admin user created successfully')
        except SQLAlchemyError as e:
            db.session.rollback()
            current_app.logger.error('Error creating admin user: %s', str(e))
        finally:
            db.session.close()
            