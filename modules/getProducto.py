import storage.producto as pro
from tabulate import tabulate

#muestra una lista con los productos disponibles y su precio

def getAllProcuctoPrecio():
    PrecioProducto = []
    for val in pro.producto:
        PrecioProducto.append({
        "nombre": val.get("nombre"),
        "precio_venta": val.get("precio_venta"),
        "precio_proveedor": val.get("precio_proveedor")
    })
    return PrecioProducto
