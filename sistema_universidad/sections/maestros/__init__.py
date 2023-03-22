from flask import render_template, redirect, request, url_for, Blueprint
from models import Maestros
from .db import get_connection
from . import forms

maestro = Blueprint('maestro', __name__, template_folder='templates', url_prefix='/maestro')

@maestro.route("/visualizacion", methods=["GET", "POST"])
def visualizacion():
    maestro_form = forms.MaestroForm(request.form)
    maestros_array = []
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consultar_maestros()')
            for row in cursor.fetchall():
                id, nombre, apellidos, email, fecha_nacimiento, grado_academico, create_date = row
                maestro_row = Maestros(id = id, nombre = nombre, apellidos =  apellidos, email = email, fecha_nacimiento = fecha_nacimiento, grado_academico = grado_academico, create_date = create_date)
                maestros_array.append(maestro_row)
    except Exception as ex:
        print(ex)

    print(maestros_array)
    return render_template("visualizacion.html", form = maestro_form, maestros = maestros_array)

@maestro.route("/agregar", methods=["GET", "POST"])
def agregar_maestro():
    maestro_form = forms.MaestroForm(request.form)
    if request.method == 'POST' and maestro_form.validate():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call agregar_maestro(%s, %s, %s, %s, %s)', (maestro_form.nombre.data, maestro_form.apellidos.data, maestro_form.email.data, maestro_form.fecha_nacimiento.data, maestro_form.grado_academico.data))                        
                connection.commit()
                connection.close()
        except Exception as ex:
            print(ex)
        return redirect(url_for('maestro.visualizacion'))
    return render_template("maestro.html", form = maestro_form)

@maestro.route("/modificar", methods=["GET", "POST"])
def modificar_maestro():
    maestro_form = forms.MaestroForm(request.form)
    maestro = None
    if request.method == 'POST':
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call modificar_maestro(%s, %s, %s, %s, %s, %s)', (maestro_form.id.data, maestro_form.nombre.data, maestro_form.apellidos.data, maestro_form.email.data, maestro_form.fecha_nacimiento.data, maestro_form.grado_academico.data))
                connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)
        return redirect(url_for('maestro.visualizacion'))
    else:
        id = int(request.args.get('id'))
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_maestro(%s)', (id,))
                for row in cursor.fetchall():
                    id, nombre, apellidos, email, fecha_nacimiento, grado_academico, create_date = row
                    maestro = Maestros(id = id, nombre = nombre, apellidos =  apellidos, email = email, fecha_nacimiento = fecha_nacimiento, grado_academico = grado_academico, create_date = create_date)
        except Exception as ex:
            print(ex)

        if maestro:
            maestro_form.id.data = id
            maestro_form.nombre.data = maestro.nombre
            maestro_form.apellidos.data = maestro.apellidos
            maestro_form.email.data = maestro.email
            maestro_form.fecha_nacimiento.data = maestro.fecha_nacimiento
            maestro_form.grado_academico.data = maestro.grado_academico
    return render_template("modificacion.html", form = maestro_form)

@maestro.route("/eliminar", methods=["GET", "POST"])
def eliminar_maestro():
    id = int(request.args.get('id'))
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call borrar_maestro(%s)', (id))
            connection.commit()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
    return redirect(url_for('maestro.visualizacion'))