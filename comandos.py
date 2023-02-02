import util
import shutil
import logger
import os
from pathlib import Path
from colorama import init, Fore
import subprocess
import getpass
import pwd
import grp

init(autoreset=True)

# Cógido de Logs: 0) user_access 1) user_actions 2) ftp_transfer 3) system_error

def copiar(args):
    try:
        origenes = args[:-1]
        destino = Path(args[-1])
        for origen in origenes:
            path = Path(origen)
            if path.is_file():
                shutil.copy2(path, destino)
            else:
                shutil.copytree(path, destino, symlinks = False, dirs_exist_ok=True)
        msg = f"Copiado {origenes} en {destino}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al copiar {args[:-1]} en {args[-1]}", "error")
        logger.log(str(Argument), 1)

def mover(args):
    try:
        origenes = args[:-1]
        destino = Path(args[-1])
        for origen in origenes:
            path = Path(origen)
            if path.is_file():
                shutil.move(path, destino)
            else:
                shutil.move(path, destino, copy_function = shutil.copytree)
        msg = f"Movido {origenes} en {destino}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al mover {args[:-1]} en {args[-1]}", "error")
        logger.log(str(Argument), 1)

def renombrar(archivo, nuevo_nombre):
    try:
        path = Path(archivo)
        path.rename(nuevo_nombre)
        msg = f"renombrado {archivo} a {nuevo_nombre}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al renombrar {archivo} a {nuevo_nombre}", "error")
        logger.log(str(Argument), 1)

def listar(ruta = "."):
    try:
        path = Path(ruta)
        msg = f"listar archivos y carpeta de la ruta {path}"
        util.respuesta(msg)
        for recurso in path.iterdir():
            if recurso.is_file():
                print("\t"+Fore.GREEN+f"📄 {recurso.name}")
            else:
                print("\t"+Fore.YELLOW+f"📂 {recurso.name}")        
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al listar archivos y carpeta de la ruta {ruta}", "error")
        logger.log(str(Argument), 1)

def creadir(args):
    try:
        for directorio in args:
            Path(directorio).mkdir(parents=True, exist_ok=True)
            msg = f"Creado(s) directorio(s) {args}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al crear directorio(s) {args}", "error")
        logger.log(str(Argument), 1)

def ir(directorio):
    try:
        os.chdir(directorio)
        msg = f"Cambiado al directorio: {os.getcwd()}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al cambiar al directorio {directorio}", "error")
        logger.log(str(Argument), 1)

def change_password(username = "root"):
    current_password = getpass.getpass("Ingrese password actual:")
    new_password = getpass.getpass("Ingrese nuevo password:")
    confirm_password = getpass.getpass("Confirme nuevo password:")
    
    if new_password != confirm_password:
        return "Nuevo password y confirmacion no coinciden."
    
    result = subprocess.run(["passwd", username], input=current_password + "\n" + new_password + "\n" + new_password + "\n", stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        msg = "Password cambiado exitosamente."
        util.respuesta(f"{msg}")
    else:
        msg = "Fallo al cambiar el password: " + result.stderr
        util.respuesta(f"{msg}", "error")

def permiso(nombre_del_recurso, permiso):    
    try:
        # Convertir permiso a octal
        permiso_octal = int(permiso, 8)
        # Verificar si es archivo o carpeta
        path = Path(nombre_del_recurso)
        if path.is_dir():
            # Aplicar permiso recursivo
            for root, dirs, files in os.walk(path):
                os.chmod(root, permiso_octal)
                for d in dirs:
                    os.chmod(os.path.join(root, d), permiso_octal)
                for f in files:
                    os.chmod(os.path.join(root, f), permiso_octal)            
        else:
            # Aplicar permiso a archivo
            os.chmod(path, permiso_octal)

        msg = f"Asignado {permiso} a recurso {nombre_del_recurso}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al aplicar permiso {permiso} al recurso {nombre_del_recurso}", "error")
        logger.log(str(Argument), 1)

def propiedad(recursos):
    # Pedir el nombre del usuario y el grupo en el prompt
    user_name = input("Ingrese el nombre de usuario: ")
    group_name = input("Ingrese el nombre del grupo: ")

    try:
        uid = pwd.getpwnam(user_name).pw_uid
        gid = grp.getgrnam(group_name).gr_gid

    except KeyError as Argument:
        msg = f"No existe el usuario o el grupo: {user_name}:{group_name}"
        print(msg)
        logger.log(str(Argument), 1)
            
    # Aplicar chown a los recursos
    for path in recursos:
        if (os.path.exists(path)):
            recurso = Path(path)
        else:
            msg = f"No existe recurso {path}"
            util.respuesta(msg, "error")
            logger.log(msg, 1)
            continue
        try:
            if recurso.is_file():
                os.chown(str(recurso), uid, gid)
            elif recurso.is_dir():
                for child in recurso.iterdir():
                    os.chown(str(child), uid, gid)
            
            msg = f"Cambiada propiedad de {recurso} a grupo {group_name} y usuario {user_name}"
            util.respuesta(msg)
            logger.log(msg, 1)
        except Exception as Argument:
            util.respuesta(f"Error al cambiar la propiedad de {recursos} a grupo {group_name} y usuario {user_name}", "error")
            logger.log(str(Argument), 1)


def ruta():
    ruta_actual = os.getcwd() 
    msg = "Ruta actual" + str(ruta_actual)
    util.respuesta(msg)
    logger.log(msg, 1)

def historial():
    with open(os.path.expanduser("~/.bash_history"), "r") as f:
        lines = f.readlines()
        for line in lines:
            print(f"\t{Fore.GREEN}{line.strip()}")
    logger.log("Visualizacion de historial de comandos ejecutados", 1)

def buscar(archivo, busqueda):
    print("TO DO")
