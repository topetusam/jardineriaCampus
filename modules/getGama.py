# import json
import requests

def getAllGama():
    # json-server storage/gama_producto.json -b 4502
    peticion = requests.get("http://172.16.106.53:4502/gama")
    data = peticion.json()
    return data

def getGamaCodigo(codigo):
    peticion= requests.get(f"http://172.16.106.53:4502/gama/{codigo}")
    return[peticion.json()] if peticion.ok else []

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre