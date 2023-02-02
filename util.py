import emoji
from colorama import init, Fore, Back
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
