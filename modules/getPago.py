import storage.pago as pa

def getAllFormapagoTotal():
    FormapagoTotal = []
    for val in pa.pago:
        if val.get("forma_pago") == "PayPal":
            FormapagoTotal.append({
                "Forma_pago": val.get("forma_pago"),
                "Total": val.get("total")

        })
    return FormapagoTotal

#devuelve un listado con el codigo de cliente de aquellos clientes que realizaron algun pago en 2008, tenga en cuenta que debe eliminar aquellos codigos de cliente que aparezcan repetidos
def getAllFechaPago():
    añoPago= "2008"
    FechaPago = []
    repetidos = {}
    for val in pa.pago:
            if val.get("fecha_pago").startswith(añoPago) and val.get("codigo_cliente") not in repetidos:
                 repetidos[val.get("codigo_cliente")]=True
                 FechaPago.append({
                
                "codigo": val.get("codigo_cliente"),
                "Fecha_pago": val.get("fecha_pago"),
                "Total": val.get("total")

        })
    return FechaPago


#devuelve in listado con todos los pagos que se realizaron en el año 2008 mediante paypal, ordene el resultado de mayor a menor


#devuelve un listado con todas las formas de pago que aparecen en la lista pago . Tenga en cuenta  que no deben  aparecer formas de pago repetidas