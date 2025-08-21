"""Módulo de servicios: services.py
Propósito: Implementa la lógica de negocio sobre los usuarios. 
Gestiona la validación de datos, generación de IDs y delega la persistencia al módulo data_access.

Responsabilidades:
- Validar datos de entrada (campos obligatorios, duplicados).
- Gestionar generación automática de ID para nuevos usuarios.
- Levantar excepciones claras ante errores de negocio.
- Delegar operaciones CRUD en el módulo de acceso a datos."""

from typing import List, Dict
from models import User
import data_access
import uuid

def listar_usuarios() -> List[Dict]:
    return data_access.get_all_users()

def obtener_usuario(user_id: str) -> Dict:
    user = data_access.get_user_by_id(user_id)
    if not user:
        raise KeyError(f"Usuario con id {user_id} no encontrado")
    return user
def crear_usuario(datos: Dict) -> Dict: 
    if not datos.get("id"):
        datos["id"] = str(uuid.uuid4())
    #Validaciones de campos vacios
    campos_obligatorios = ["nombre", "apellido","email","telefono","contrasena", "edad"]
    for campo in campos_obligatorios:
        if not datos.get(campo):
            raise ValueError(f"El campo '{campo}' es obligatorio")
    #Validacion de duplicados
    usuarios = listar_usuarios()
    email_nuevo = datos["email"].strip().lower()
    telefono_nuevo = datos["telefono"].strip()

    for u in usuarios:
        if u["email"].strip().lower() == email_nuevo:
            raise ValueError("El email ya se encuentra en uso")
        if u["telefono"].strip() == telefono_nuevo:
            raise ValueError("El telefono ya se encuentra en uso")
        
    user = User.from_dict(datos)
    return data_access.add_user(user.to_dict())
def actualizar_usuario(user_id: str, nuevos_datos: Dict) -> Dict:
    return data_access.update_user(user_id, nuevos_datos)
def eliminar_usuario(user_id: str) -> None:
    data_access.delete_user(user_id)


