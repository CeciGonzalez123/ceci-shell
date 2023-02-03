import os
import pwd
import grp
import util
import shutil
import logger
import getpass
import subprocess
from pathlib import Path
from colorama import init, Fore

# Configurar colorama para aplicar reset automaticamente
init(autoreset=True)

"""
    Códigos "del 0 al 3" para registro de Logs en el archivo correspondiente: 
    0 -> user_access 
    1 -> user_actions 
    2 -> ftp_transfer 
    3 -> system_error
"""

def copiar(args):
    """
        Copia archivos(s) y/o carpeta(s) al directorio indicado en el último parámetro
    """
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
        logger.log(str(Argument), 3)

def mover(args):
    """
        Mueve archivos(s) y/o carpeta(s) al directorio indicado en el último parámetro
    """
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
        logger.log(str(Argument), 3)

def renombrar(archivo, nuevo_nombre):
    """
        Renombra archivos o carpeta
    """
    try:
        path = Path(archivo)
        path.rename(nuevo_nombre)
        msg = f"renombrado {archivo} a {nuevo_nombre}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al renombrar {archivo} a {nuevo_nombre}", "error")
        logger.log(str(Argument), 3)

def listar(ruta = "."):
    """
        Lista el contenido del directorio actual o de la ruta indicada
    """
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
        logger.log(str(Argument), 3)

def creadir(args):
    """
        Crea directorio(s) indicado(s) en el parametro
    """
    try:
        for directorio in args:
            Path(directorio).mkdir(parents=True, exist_ok=True)
            msg = f"Creado(s) directorio(s) {args}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al crear directorio(s) {args}", "error")
        logger.log(str(Argument), 3)

def ir(directorio):
    """
        Cambia al directorio indicado
    """
    try:
        os.chdir(directorio)
        msg = f"Cambiado al directorio: {os.getcwd()}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al cambiar al directorio {directorio}", "error")
        logger.log(str(Argument), 3)

def change_password(username = "root"):
    """
        Cambia la contraseña del usuario root o el indicado en el parametro
    """
    current_password = getpass.getpass("Ingrese password actual:")
    new_password = getpass.getpass("Ingrese nuevo password:")
    confirm_password = getpass.getpass("Confirme nuevo password:")
    
    if new_password != confirm_password:
        return "Nuevo password y confirmacion no coinciden."
    
    print("TODO")

def permiso(nombre_del_recurso, permiso):
    """
        Cambia el permiso indicado en los recursos (archivo(s) y/o directorio(s))
    """
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
        logger.log(str(Argument), 3)

def propiedad(recursos):
    """
        Carmbia la propiedad de archivos al usuario y grupo indicado
    """
    # Solicita el nombre del usuario y el grupo
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
            logger.log(str(Argument), 3)


def ruta():
    """
        Despliega la ruta del directorio actual
    """
    ruta_actual = os.getcwd() 
    msg = "Ruta actual " + str(ruta_actual)
    util.respuesta(msg)
    logger.log(msg, 1)

def buscar(file_path, search_string):
    """
        Realiza búsqueda de cadena en un archivo de texto
    """
    try:
        file = Path(file_path)
        if file.is_file():
            with open(file_path, 'r') as f:
                contents = f.read()
                if search_string in contents:
                    print(contents.replace(search_string, Fore.GREEN + "\033[1m" + search_string + "\033[0m"))
                else:
                    util.respuesta("No se encontró la cadena en el archivo.")
            logger.log(f"Busqueda de {search_string} en archivo {file_path}", 1)
        else:
            msg = f"El archivo {file_path} no es válido."
            util.respuesta(msg, "error")
            raise Exception(msg)
    except Exception as Argument:
        msg = f"Ha ocurrido un error: busqueda de cadena {search_string} en archivo {file_path}", str(Argument)
        util.respuesta(msg, "error")
        logger.log(str(Argument), 3)

def ejecutar(args):
    """
        Ejecuta comandos del sistema a excepción de los comandos implementados en la shell
    """
    comando = args[0]
    comandos = {
        'cp': 'copiar',
        'mv': 'mover',
        'historial': 'history',
        'creadir': 'mkfir',
        'chmod': 'permiso',
        'chown': 'propietario',
        'grep': 'buscar',
        'pwd': 'ruta',
        'cd': 'ir',
        'ls': 'listar'
    }

    implementado = comandos.get(comando)
    if implementado:
        util.respuesta(f"Comando implementado, por favor consulte en la {Fore.BLUE}ayuda{Fore.RESET} el comando{Fore.BLUE} {implementado}")
        return

    try:
        subprocess.run(args)

    except Exception as Argument:
        msg = f"Comando de sistema no valido: {' '.join(args)}"
        util.respuesta(msg, "error")
        logger.log(str(Argument), 3)
    
