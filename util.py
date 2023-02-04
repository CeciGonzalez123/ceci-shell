import emoji
import getpass
import readline
import re
from colorama import init, Fore

init(autoreset=True)

def entrada_teclado(prompt):    
    """
        Permitir usar teclas de cursor
    """
    readline.set_startup_hook(lambda: readline.insert_text(prompt))
    try:
        #return input().replace("ceci-shell>", "")
        return re.sub("ceci-shell>", "", input())
    finally:
        readline.set_startup_hook(None)


def respuesta(msg, tipo='ok'):
    """
    Imprime informacion en color verde o rojo si se pasa parametro tipo distinto a ok
    """
    if tipo == 'ok':        
        resp = emoji.emojize(':thumbs_up: ')
        fcolor = Fore.GREEN
    else:
        resp = emoji.emojize(':thumbs_down: ')
        fcolor = Fore.RED

    print(resp + f"{fcolor} {msg}")

def negrita(cadena):
    """
    Sencuencia ANSI para ponder texto en negrita
    """
    inicio = '\033[1m'
    fin = '\033[0m'
    return f'{inicio}{cadena}{fin}'

def guardar_historial(comando):
    with open("historial.txt", "a") as log_file:
        log_file.write(str(comando) + "\n")

def leer_historial():
    """
    Muestra contenido de archiuvo historial
    """
    archivo = open("historial.txt")
    print(f"{Fore.YELLOW}{archivo.read()}")

def time_in_range(start, end, x): 
    """
    Retorna True si la hora actual esta dentro del rango [start, end]
    """ 
    if start <= end:
        return start <= x <= end 
    else:
        return start <= x or x <= end

def generar_id():
    """
    La función devuelve el mayor ID de usuario existente en el archivo más 1
    """
    with open("/etc/passwd") as f:
        lines = f.readlines()
    max_id = 0
    for line in lines:
        line = line.strip().split(':')
        max_id = max(max_id, int(line[2]))
    return str(max_id + 1)

def existe_usuario(username):
    """
    Devuelve True si el usuario existe
    """
    with open("/etc/passwd") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip().split(':')
        if line[0] == username:
            return True
    return False

def agregar_informacion(filename, texto):
    """
    Agregar informacion en archivo
    """
    with open(filename, "a") as file:
        file.write(texto)
    return

def es_root():
    """
    Verifica si usuario tiene privilegio para tareas administrativas
    """
    if not getpass.getuser() == "root":
        respuesta("Debe tener privilegios de usuario root", "error")
        return False
    
    return True
