from wtforms import StringField, IntegerField, EmailField, DateField, Form, SelectField, validators
grados_academicos = [('Ingeniero', 'Ingeniero'), ('Licenciado', 'Licenciado'), ('Maestro', 'Maestro'), ('Doctor', 'Doctor')]

class MaestroForm(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre', [validators.DataRequired(message="Campo requerido")])
    apellidos = StringField('Apellidos', [validators.DataRequired(message="Campo requerido")])
    email = EmailField('Correo', [validators.DataRequired(message="Campo requerido"), validators.Email(message="Ingresa un correo valido")])
    fecha_nacimiento = DateField('Fecha de Nacimiento', [validators.DataRequired(message="Campo requerido")])
    grado_academico = SelectField('Grado academico', [validators.DataRequired(message="Campo requerido")], choices=grados_academicos)

