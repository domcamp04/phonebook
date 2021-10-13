from app import db
import os
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Entry(db.Model):
    name = db.Column(db.String(150), primary_key=True)
    phone_number = db.Column(db.String(150), nullable=False, unique=True)
   

    def __init__(self, name, phone_number):
        self.name= name
        self.phone_number= phone_number