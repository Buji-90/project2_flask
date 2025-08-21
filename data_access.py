"""Módulo de acceso a datos: data_access.py
Propósito: Encapsula la persistencia de usuarios en un archivo JSON. Implementa operaciones CRUD (crear, leer, actualizar, eliminar) directamente sobre el fichero. Pertenece a: capa de repositorios/DAO (Data Access Object).
Responsabilidades:
- Gestionar lectura y escritura de users.json.
- Asegurar existencia del directorio de datos.
- Proporcionar API de funciones CRUD basadas en ID."""

import json
import os
from typing import List, Dict, Optional

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'users.json')
#Si no existe el archivo, se crea.
if not os.path.exists(os.path.dirname(DATA_FILE)):
    os.makedirs(os.path.dirname(DATA_FILE))

# Aceso a los datos y modificacion de datos.

# Funciones del CRUD
def get_all_users() -> List[Dict]:
    """Devuelve la lista completa de usuarios y si no hay ninguno devuelve una lista vacia."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
def get_user_by_id(user_id: str) -> Optional[Dict]:
    """Devuelve un usuario como diccionario por su ID o None si no existe."""
    users = get_all_users()
    for user in users:
        if user.get("id") == user_id:
            return user
    return None
def add_user(user: Dict) -> Dict:
    """Añade un nuevo usuario y comprueba que no exista ya."""
    users = get_all_users()

    if any(usr.get("id") == user.get("id") for usr in users):
        raise ValueError(f"Ya existe un usuario con el ID '{user.get('id')}'.")
    users.append(user)
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=4)
    return user
def update_user(user_id: str, new_data: Dict) -> Dict:
    """Actualiza un usuario existente y comprueba que exista primero.
    Devuelve el usuario actualizado o error si no existe.
"""
    users = get_all_users()

    for i, user in enumerate(users):
        if user.get("id") == user_id:
            # Actualizar los datos del usuario existente con los nuevos datos
            users[i] = {**user, **new_data}
            # Guardar los cambios en el archivo JSON
            with open(DATA_FILE, 'w', encoding='utf-8') as file:
                json.dump(users, file, ensure_ascii=False, indent=4)
            return users[i]
    raise ValueError(f"No existe un usuario con el ID '{user_id}'.")

def delete_user(user_id: str) -> None:
    """Elimina un usuario por su ID y comprueba que exista primero."""
    users = get_all_users()

    new_list = [usr for usr in users if usr.get("id") != user_id]
    if len(new_list) == len(users):
        raise KeyError(f"Usuario con ID '{user_id}' no encontrado.")
    # Guardar la nueva lista
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(new_list, file, ensure_ascii=False, indent=4)



