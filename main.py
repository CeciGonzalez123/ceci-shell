import util
import comandos
from colorama import init, Fore, Back

init(autoreset=True)

def ayuda():
    print(util.negrita(Fore.YELLOW+"COMANDOS DISPONIBLES"))
    print(f"\tcopiar\t\t {Fore.BLUE}[origen] {Fore.GREEN}[destino] \t {Fore.RESET}:: Copiar archivo 0 carpeta")
    print(f"\tmover\t\t {Fore.BLUE}[origen] {Fore.GREEN}[destino] \t {Fore.RESET}:: Mover archivo o carpeta")
    print(f"\tsalir\t\t\t\t\t :: Salir de la ceci-shell")

def main():
    """Programa principal que ejecuta los comandos"""
    print(util.negrita(Back.GREEN+Fore.WHITE+" ***** BIENVENID@ A LA ceci-shell EN PYTHON *****"))
    while True:
        cmd = input("ceci-shell> ").strip().split()
        if not cmd:
            continue
        if cmd[0].lower() == "salir":
            print("Adiós")
            break
        elif cmd[0].lower() == "copiar":
            if len(cmd) != 3:
                print(f"Uso: copiar {Fore.BLUE} [origen] {Fore.GREEN} [destino]")
            else:
                comandos.copiar(cmd[1], cmd[2])
        elif cmd[0].lower() == "mover":
            if len(cmd) != 3:
                print(f"Uso: mover {Fore.BLUE} [origen] {Fore.GREEN} [destino]")
            else:
                comandos.mover(cmd[1], cmd[2])
        elif cmd[0].lower() == "ayuda":
            ayuda()
        else:
            print(util.negrita("COMANDO DESCONOCIDO:") + f"\n\t Escriba {Fore.RED} {util.negrita('ayuda')} {Fore.RESET} para obtener información sobre los comandos disponibles.")

if __name__ == "__main__":
    main()
