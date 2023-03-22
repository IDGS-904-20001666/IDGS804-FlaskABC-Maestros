from flask import render_template, redirect, request, url_for, Blueprint
from models import Alumnos 
from models import db
from . import forms

alumnos = Blueprint('alumnos', __name__, template_folder='templates')

@alumnos.route("/abcompleto", methods=["GET", "POST"])
def abcompleto():
    create_form = forms.UserForms(request.form)
    alumno = Alumnos.query.all()
    return render_template("abcompleto.html", form = create_form, alumno = alumno)

@alumnos.route("/alumnos", methods=["GET", "POST"])
def iniciar():
    create_form = forms.UserForms(request.form)
    if request.method == 'POST':
        alumn = Alumnos(nombre = create_form.nombre.data, apellidos =  create_form.apellidos.data, email = create_form.email.data)
        db.session.add(alumn)
        db.session.commit()
        return redirect(url_for('alumnos.abcompleto'))
    return render_template("alumnos.html", form = create_form)

@alumnos.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForms(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre  = create_form.nombre.data
        alum.apellidos  = create_form.apellidos.data
        alum.email  = create_form.email.data
        db.session.add(alum)
        db.session.commit()

        return redirect(url_for('alumnos.abcompleto'))
    return render_template("modificar.html", form = create_form)

@alumnos.route('/eliminar', methods=['GET', 'POST'])
def eliminar_alumno():
    id = request.args.get('id')
    alumno = db.session.query(Alumnos).filter(Alumnos.id==id).first()
    db.session.delete(alumno)
    db.session.commit()  
    return redirect(url_for('alumnos.abcompleto'))
