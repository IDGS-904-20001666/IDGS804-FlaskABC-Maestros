from sections.maestros import maestro
from sections.alumnos import alumnos
from flask import Flask, render_template
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf_token = CSRFProtect()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

app.register_blueprint(alumnos)
app.register_blueprint(maestro)

if __name__ == "__main__":
    csrf_token.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)