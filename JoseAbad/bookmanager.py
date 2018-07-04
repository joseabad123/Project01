import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

# enlace a base de datos vía sqlalchemy
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

# modelado
class Persona(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    apellido = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<Nombre: {}>".format(self.nombre) 

# vistas
# @app.route("/")
@app.route("/", methods=["GET", "POST"])
def home():
    # return "My flask app"
    if request.form:
        print(request.form)
        persona = Persona(nombre=request.form.get("nombre"),apellido=request.form.get("apellido"))
        db.session.add(persona)
        db.session.commit()
    
    personas = Persona.query.all()
    return render_template("home.html", personas=personas)
    # return render_template("home.html")
    
@app.route("/update", methods=["POST"])
def update():
    newname = request.form.get("newname")
    new_ape = request.form.get("new_ape")
    idpersona = request.form.get("idpersona")
    persona = Persona.query.get(idpersona)
    persona.apellido = new_ape
    persona.nombre = newname
    db.session.commit()
    return redirect("/")  

@app.route("/delete", methods=["POST"])
def delete():
    idpersona = request.form.get("idpersona")
    persona = Persona.query.get(idpersona)
    db.session.delete(persona)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)



