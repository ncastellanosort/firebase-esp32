import network, time, urequests
from machine import Pin
import json
import time 
import ufirebase as firebase

ledEsp = Pin(2, Pin.OUT)

def conectar(red, passwd):
    global miRed

    miRed = network.WLAN(network.STA_IF)

    if not miRed.isconnected():
        miRed.active(True)
        miRed.connect(red, passwd)
        print(f'Conectando a la red {red} ...')
        timeout = time.time()

        while not miRed.isconnected():
            if (time.ticks_diff(time.time(),timeout) > 10):
                return False

    return True

# with open('C:/Users/Nicolas/Documents/Code/esp32/Firebase/datos.json', 'r') as datosJson:
#     datos = datosJson.read()
    
# objeto = json.loads(datos)       
# print(json.dumps( objeto, indent=4))
    
if conectar('EYE3 2.4G', 'Castellanos2023Ort'):
    print('Conectado exitosamente!')
    print(f'Datos de la red (IP/Netmask/gw/DNS): {miRed.ifconfig()}')

    firebase.setURL("https://pruebavscodemicropython-default-rtdb.firebaseio.com/")

    firebase.put("Carpeta/llave", 888, bg=0)
    time.sleep(2)
    firebase.delete('Carpeta/llave')


    firebase.put("Carpeta2/llave2", {"numeros": [1,2,3], "algo": "saludo"}, bg=0)
    time.sleep(2)
    firebase.put('Carpeta2/llave2/algo', 'hola', bg=0)
    
    firebase.put('Productos/Forros', {
        'Iphone12': 15000,
        'Iphone13': 14000,
        'Iphone14': 15000
    }, bg = 2)   
    
    while(True):

        firebase.get("Productos/Forros", "Forros")
        print(f'\n{firebase.Forros}\n')

        firebase.get('Carpeta2/llave2/numeros', 'numeros')
        print(f'\n{firebase.numeros}\n')
        
        firebase.get("Productos/Forros", "Forros")
        print(f'Iphone 12 :  {firebase.Forros["Iphone12"]}')
        print(f'Iphone 13 :  {firebase.Forros["Iphone13"]}')
        print(f'Iphone 14 :  {firebase.Forros["Iphone14"]}')
        
        firebase.get("Productos", "Productos")

        
        for key, value in firebase.Productos.items():
            print(f'{key} : {value}')
            
            for key2, value2 in value.items():
                print(f'{key2} : {value2}')
        

        
        


        

