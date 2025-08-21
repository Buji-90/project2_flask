"""
Módulo de modelos: models.py
Propósito: Define la entidad User usada en la aplicación, con atributos básicos y métodos de conversión a/desde diccionarios.
Responsabilidaddes:
- Representar un usuario como objeto Python.
- Facilitar la conversión bidireccional entre objeto y diccionario JSON-serializable."""

from typing import Optional, Dict

# Modelo de datos, atributos basicos y metodos auxiliares
class User:
    def __init__(self, id: str, nombre: str, apellido: str, email: str, telefono: str, contrasena: str, edad: int):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.contrasena = contrasena
        self.edad = edad
    # Metodo para convertir el objeto en un diccionario para JSON
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "contrasena": self.contrasena,
            "edad": self.edad
        }
    # Metodo para crear un objeto User desde un diccionario
    @staticmethod
    def from_dict(data: Dict) -> 'User':
        try:
            edad = int(float(data.get("edad", 0)))
        except (ValueError, TypeError):
            edad = 0
        return User(
            id=data.get("id"),
            nombre=data.get("nombre"),
            apellido=data.get("apellido"),
            email=data.get("email"),
            telefono=data.get("telefono"),
            contrasena=data.get("contrasena"),
            edad=edad
        )

        
