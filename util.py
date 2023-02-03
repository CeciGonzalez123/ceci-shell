import emoji
from datetime import datetime
from colorama import init, Fore

init(autoreset=True)

def respuesta(msg, tipo='ok'):
    if tipo == 'ok':        
        resp = emoji.emojize(':thumbs_up: ')
        fcolor = Fore.GREEN
    else:
        resp = emoji.emojize(':thumbs_down: ')
        fcolor = Fore.RED

    print(resp + f"{fcolor} {msg}")

def negrita(cadena):
    return "\033[1m" + cadena

def guardar_historial(comando):
    with open("historial.txt", "a") as log_file:
        log_file.write(str(comando) + "\n")

def leer_historial():
    archivo = open("historial.txt")
    print(f"{Fore.YELLOW}{archivo.read()}")

def time_in_range(start, end, x): 
    """Retorna True si la hora actual esta dentro del rango [start, end]""" 
    if start <= end:
        return start <= x <= end 
    else:
        return start <= x or x <= end
