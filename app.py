from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Vengers.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Vengers(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(500), unique=True)


@app.route("/")
def mcu():
    return "HI WELCOME TO MARVEL CINEMATIC UNIVERSE"


@app.route("/insert", methods=["POST"])
def mcu2():
    c_name = request.form.get("c_name")
    new_c_name = Vengers(c_name=c_name)
    db.session.add(new_c_name)
    db.session.commit()
    return redirect(url_for("mcu1"))


@app.route("/delete/<int:c_id>")
def delete(c_id):
    c_name = Vengers.query.get_or_404(c_id)
    db.session.delete(c_name)
    return redirect(url_for("mcu1"))


@app.route("/tony")
def mcu1():
    my_list = Vengers.query.all()
    return render_template("tony.html", my_list=my_list)


if __name__ == "__main__":
    app.run()
