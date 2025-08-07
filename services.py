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
    for u in usuarios:
        if u["email"] == datos["email"]:
            raise ValueError("El email ya se encuentra en uso")
        if u["telefono"] == datos["telefono"]:
            raise ValueError("El telefono ya se encuentra en uso")
        
    user = User.from_dict(datos)
    return data_access.add_user(user.to_dict())
def actualizar_usuario(user_id: str, nuevos_datos: Dict) -> Dict:
    return data_access.update_user(user_id, nuevos_datos)
def eliminar_usuario(user_id: str) -> None:
    data_access.delete_user(user_id)


