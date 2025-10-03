"""
    Creación de ususarios con Faker e uso dos mesmos a través dun diccionario.
    Información da librería optida en https://faker.readthedocs.io/en/master/
    Por Carlos Salgado Fernández
    """

from faker import Faker
import random

# inicio do xerador de datos Faker
fake = Faker('es_ES')

# Creo un diccionario valeiro para meter os datos que se xeren
usuarios = {}

"""
Xeramos os usuarios.
Ó crear un bucle for entre 1 e 16 cada usuario xa ten un código único
"""
for i in range(1, 16):
    usuarios[i] = {
        "nombre": fake.name(),
        "direccion": fake.address(),
        "correo_electronico": fake.email(),
        "telefono": fake.phone_number()
    }


# mostramos os datos
print("--- DATOS DOS USUARIOS ---")
for id, datos in usuarios.items():
    print(f"\nID: {id}")
    print(f"Nome: {datos['nombre']}")
    print(f"Dirección: {datos['direccion']}")
    print(f"Correo Electrónico: {datos['correo_electronico']}")
    print(f"Teléfono: {datos['telefono']}")

print("----------------")

# Selección de un usuario aleatoriamente
usuario_afortunado_id = random.choice(list(usuarios.keys()))
usuario_afortunado_nome = usuarios[usuario_afortunado_id]['nombre']
print("SORTEO:")
print(f"O usuario chamado {usuario_afortunado_nome} foi o afortunado!")
