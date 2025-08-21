""" Módulo principal: app.py
Propósito: Configura y arranca la aplicación Flask, define las rutas HTTP y conecta con los servicios de negocio.
Responsabilidades:
-Inicializar la aplicación Flask con ngrok para exponer localmente.
-Definir endpoints REST para operaciones CRUD de usuarios.
-Gestionar formularios HTML para crear/editar usuarios.
-Renderizar plantillas (formulario, tabla, menú).
-Delegar toda la lógica de negocio a funciones en services.py.
 """

from services import *
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_ngrok import run_with_ngrok
import uuid

app = Flask(__name__)
run_with_ngrok(app)
app.secret_key = uuid.uuid4().hex # Clave necesaria para sesiones/flash

@app.route("/users", methods=["GET"]) #Devuelve todos los usuarios en formato JSON.
def get_users():
    return jsonify(listar_usuarios()), 200

@app.route("/users/<user_id>", methods=["GET"]) # Devuelve un usuario específico. (Implementacion en un futuro)
def get_user(user_id):
    try:
        user = obtener_usuario(user_id)
        return jsonify(user), 200
    except KeyError:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/users", methods=["POST"]) # Crea un nuevo usuario a partir de un JSON.
def create_user():
    datos = request.json
    try:
        nuevo = crear_usuario(datos)
        return jsonify(nuevo), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/users/<user_id>", methods=["PUT"]) # Actualiza un usuario existente.
def update_user(user_id):
    nuevos_datos = request.json
    try:
        actualizado = actualizar_usuario(user_id, nuevos_datos)
        return jsonify(actualizado), 200
    except KeyError:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/users/<user_id>", methods=["DELETE"]) # Elimina un usuario por su ID. 
def delete_user(user_id):
    try:
        eliminar_usuario(user_id)
        return '', 204 
    except KeyError:
        return jsonify({"error": "Usuario no encontrado"}), 404


@app.route("/form" , methods=["GET", "POST"]) # Muestra o procesa el formulario de usuario.
def form():
    if request.method == "POST":
        datos = request.form.to_dict()
        try:
            # ¿Ya existe ese usuario (mismo id)? Entonces actualizar
            if obtener_usuario(datos["id"]):
                actualizar_usuario(datos["id"], datos)
        except KeyError:
            try:
                crear_usuario(datos)  # Podría lanzar Error si email o teléfono ya existen
            except ValueError as e:
                flash(str(e))  # Mostramos el mensaje de error en el menú
                return redirect(url_for('menu'))

        return redirect(url_for('tabla'))

    user_id = request.args.get("id")
    user = obtener_usuario(user_id) if user_id else None
    return render_template("form.html", user=user)
@app.route("/delete/<user_id>") # Elimina usuario desde vista HTML (con redirección).
def delete_user_html(user_id):
    try:
        eliminar_usuario(user_id)
    except KeyError:
        pass
    return redirect(url_for("tabla"))

@app.route("/tabla") # Renderiza la tabla con todos los usuarios.
def tabla():
    usuarios = listar_usuarios()
    return render_template("tabla.html", usuarios=usuarios)

@app.route("/menu") # Renderiza el menú principal.
def menu():
    return render_template("menu.html")


            

@app.route("/") # Redirige a la vista de menú.
def home():
    return redirect(url_for("menu"))

if __name__ == "__main__":
    app.run() 



    
