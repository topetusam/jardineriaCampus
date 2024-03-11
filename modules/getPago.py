import storage.pago as pa
from tabulate import tabulate

#Devuelve los pagos realizados por paypal
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
def getAllFechaPagoPyapal():
    añoPago= "2008"
    FechaPagoPaypal = []
    for val in pa.pago:
            if val.get("fecha_pago").startswith(añoPago) and val.get("forma_pago")=="PayPal":
                 FechaPagoPaypal.append({
                
                "codigo": val.get("codigo_cliente"),
                "Fecha_pago": val.get("fecha_pago"),
                "forma_pago": val.get("forma_pago"),
                "Total": val.get("total")

        })
    return FechaPagoPaypal 


#devuelve un listado con todas las formas de pago que aparecen en la lista pago . Tenga en cuenta  que no deben  aparecer formas de pago repetidas

def getAllFormasdepagoSinRepetir():
    FormasDePago = []
    quitarrepetidas = {}
    for val in pa.pago:
            if val.get("forma_pago") not in quitarrepetidas:
                quitarrepetidas[val.get("forma_pago")]=True    
                FormasDePago.append({
                
                "forma_pago": val.get("forma_pago"),

        })
    return FormasDePago
def menu():
    while True:
        print("""
            
                                                

        _______ ____                ____                  
    / ____(_) / /__________     / __ \____ _____ _____ 
    / /_  / / / __/ ___/ __ \   / /_/ / __ `/ __ `/ __ \
    / __/ / / / /_/ /  / /_/ /  / ____/ /_/ / /_/ / /_/ /
    /_/   /_/_/\__/_/   \____/  /_/    \__,_/\__, /\____/ 
                                            /____/        


            0. Regresar
            1. Obtener los pagos realizados por PayPal
            2. Obtener los pagos realizados en el año 2008
            3. Obtener los pagos que se realizaron en 2008 mediante Paypal
            4. Obtener las formas de pago sin repetir
            
            
            """)
        opcion=int(input("\n Elija una de las opciones: "))
        
        
        if(opcion==1):
            print(tabulate(getAllFormapagoTotal(), headers="keys", tablefmt = 'rounded_grid'))
        
        elif(opcion==2):
            
            print(tabulate(getAllFechaPago(), headers="keys", tablefmt = 'rounded_grid'))    
        
        elif(opcion == 3):
        
            print(tabulate(getAllFechaPagoPyapal(), headers="keys", tablefmt='rounded_grid'))
        
        elif(opcion ==4):
            
            print(tabulate(getAllFormasdepagoSinRepetir(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==0):
             break    
