from flask import render_template, request, session, redirect 

from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja


@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def show():
    dojos = Dojo.muestra_dojos()
    return render_template("index.html", dojos=dojos)

@app.route('/addDojos', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.guardar_dojo(request.form)
    return redirect('/dojos')

@app.route('/show/<int:id>')
def show_dojo(id):
    data = {
        "id":id
    }
    dojo = Dojo.muestra_ninjas_dojo(data)
    return render_template("show.html",dojo=dojo)

@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.muestra_dojos()
    return render_template("ninjas.html", dojos=dojos)

@app.route('/create/ninja', methods=['POST'])
def guardar():
    print(request.form)
    session['dojo_id'] = request.form['dojo_id']
    print(session['dojo_id'])
    Ninja.guardar(request.form)
    
    return redirect('/')
