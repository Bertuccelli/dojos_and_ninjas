from flask import render_template, session, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/dojos')
def dojo_page():
    list_of_dojos = Dojo.get_all()
    return render_template("dojo.html", list_dojos = list_of_dojos)

@app.route('/dojos', methods = ['POST'] )
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos') 


@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id" : id
    }
    selected_dojo = Dojo.get_dojo_id(data)
    list_of_ninjas = Ninja.get_ninja_by_dojo(data)
    return render_template("dojo_show.html", list_of_ninjas=list_of_ninjas, selected_dojo = selected_dojo)


@app.route('/ninjas')
def ninja_form():
    list_of_dojos = Dojo.get_all()
    return render_template("ninja.html", list_of_dojos= list_of_dojos)


@app.route('/ninjas', methods= ['POST'])
def add_ninja():
    Ninja.create_ninja(request.form)
    dojoid = request.form["dojos_id"]
    return redirect (f"/dojos/{dojoid}")


@app.route('/dojo_show')
def show_all_dojos(name):
    data = {
        "name" : name
    }
    single_dojo = Dojo.single_dojo(data)
    list_of_ninjas = Ninja.get_ninja_by_dojo(data)
    return render_template("dojo_show.html", list_of_ninjas=list_of_ninjas, single_dojo = single_dojo)