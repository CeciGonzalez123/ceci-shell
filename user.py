from __future__ import print_function
from builtins import *
import util
import logger
import getpass
import re
import pwd 
import os 

def username_prompt(): 
    util.respuesta("El nombre de usuario debe contener solo caracteres validos 'a-z', por ejemplo: ana") 

    while True: 
        username = str(input("Ingrese nombre de usuario: "))
        confirm_name = str(input("Confirme, re-ingrese nombre de usuario: "))

        if username != confirm_name or not re.match("^[a-z]+$", username):
            util.respuesta("Error, intente nuevamente", "error")
            continue 

        else: 
            return username 

def username_check(): 
    """Verificar si usuario existe"""

    while True: 
        check = username_prompt()

        try: 
            pwd.getpwnam(check)
            util.respuesta("Usuario existe intente con otro diferente") 

        except KeyError: 
            return check 

def comment_prompt(): 

    while True: 
        nombre = str(input("Ingrese nombre completo: "))
        entrada = str(input("Ingrese horario de entrada: "))
        salida = str(input("Ingrese horario de salida: "))
        ip = str(input("Ingrese direccion IP: "))
        
        
        confirmar = str(input("Confirme que los datos son correctos: "))

        if confirmar:
            return [nombre, entrada, salida, ip]
            
        else:
            continue 
            

def passwd_prompt(): 
    util.respuesta("La clave debe contener al menos: una letra en minuscula, un numero un simbolo y un minimo de 8 caracteres")

    while True:

        passy = getpass.getpass(prompt="Ingrese password para el usuario: ")
        confirm_passy = getpass.getpass(prompt="Confirme password: ")

        # Verificar: 
        # coincidencia de password y confirmacion
        # longitud de al menos 8 caracteres
        # clave contiene al menos 1 numero
        # clave contiene al menos 1 letra
        # clave contiene al menos 1 simbolo
  
        if passy != confirm_passy \
        or len(passy) <8 \
        or not re.search('\d', passy) \
        or not re.search(r"[a-z]",passy) \
        or not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', passy):  
        
            util.respuesta("Clave no permitida, intente nuevamente")
            continue 
        
        else:
            return passy 

def crea_usuario(): 
    name = username_check()
    datos = comment_prompt()
    code = passwd_prompt()
  
    # crea usuario
    # crea grupo con el mismo nombre de usuario, agrega usuario a grupo
    # commentario (apellido, nombre) 
    # crea directorio en home
    # login shell 
    # password (encriptado via openssl) 
 
    os.system("useradd --create-home \
    --user-group \
    --nombre "+datos[0]+" \
    --entrada "+datos[1]+" \
    --salida "+datos[2]+" \
    --ip "+datos[3]+" \
    --home /home/"+name+" \
    --shell /bin/bash \
    --password $(printf %s "+code+" |openssl passwd -1 -stdin) "+name+"")
 
    msg = f"Usuario {name} creado con exito"
    util.respuesta(msg)
    logger.log(msg, "sistema")
