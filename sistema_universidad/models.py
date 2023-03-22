from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime


class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    email = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)

class Maestros(db.Model):
    __tablename__ = 'maestros'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    email = db.Column(db.String(50))
    fecha_nacimiento = db.Column(db.Date)
    grado_academico = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)