from services import *
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_ngrok import run_with_ngrok
import uuid

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(listar_usuarios()), 200

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = obtener_usuario(user_id)
        return jsonify(user), 200
    except KeyError:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    datos = request.json
    try:
        nuevo = crear_usuario(datos)
        return jsonify(nuevo), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    nuevos_datos = request.json
    try:
        actualizado = actualizar_usuario(user_id, nuevos_datos)
        return jsonify(actualizado), 200
    except KeyError:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        eliminar_usuario(user_id)
        return '', 204 
    except KeyError:
        return jsonify({"error": "Usuario no encontrado"}), 404


@app.route("/form" , methods=["GET", "POST"])
def form():
    if request.method == "POST":
        datos = {
            "id": request.form.get("id") or str(uuid.uuid4()),
            "nombre": request.form.get("nombre"),
            "apellido": request.form.get("apellido"),
            "email": request.form.get("email"),
            "telefono": request.form.get("telefono"),      
            "contrasena": request.form.get("contrasena"),  
            "edad": request.form.get("edad")
            }
        try:
            obtener_usuario(datos["id"])
            actualizar_usuario(datos["id"], datos)
        except KeyError:    
            crear_usuario(datos)
        
        return redirect(url_for("tabla"))
    #GET
    user_id = request.args.get("id")
    if user_id:
        try:
            user = obtener_usuario(user_id)
        except KeyError:
            user = {"id" : "",
                "nombre" : "",
                "apellido" : "",
                "email" : "",
                "telefono" : "",
                "contrasena" : "",
                "edad" : ""

        } 
    else:
        user = {"id" : "",
                "nombre" : "",
                "apellido" : "",
                "email" : "",
                "telefono" : "",
                "contrasena" : "",
                "edad" : ""

        }
    return render_template("form.html", user=user)
@app.route("/delete/<user_id>")
def delete_user_html(user_id):
    try:
        eliminar_usuario(user_id)
    except KeyError:
        pass
    return redirect(url_for("tabla"))

@app.route("/tabla")
def tabla():
    usuarios = listar_usuarios()
    return render_template("tabla.html", usuarios=usuarios)

@app.route("/menu")
def menu():
    return render_template("menu.html")


            

@app.route("/")
def home():
    return redirect(url_for("menu"))
   
app.run()


    
