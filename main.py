import util
import comandos
from colorama import init, Fore, Back

init(autoreset=True)

def ayuda():
    print(util.negrita(Fore.YELLOW+"COMANDOS DISPONIBLES"))
    print(f"\tcopiar\t\t{Fore.BLUE}[origen_1] [origen_2] [origen_n] {Fore.GREEN}[destino] {Fore.RESET} ==> Copia archivo(s) o carpeta(s)")
    print(f"\tmover\t\t{Fore.BLUE}[origen_1] [origen_2] [origen_n] {Fore.GREEN}[destino] {Fore.RESET} ==> Mueve archivo o carpeta")
    print(f"\trenombrar\t{Fore.BLUE}[arcivo] {Fore.GREEN}[nuevo_nombre]\t {Fore.RESET} ==> Renombra archivo")
    print(f"\tlistar\t\t{Fore.BLUE}[ruta] (opcional) \t {Fore.RESET} ==> Lista archivos")
    print(f"\tcreadir\t\t{Fore.BLUE}[dir_1] [dir_2] [dir_3]\t{Fore.RESET}  ==> Crea directorios")
    print(f"\tir\t\t{Fore.BLUE}[directotio]\t{Fore.RESET}  ==> Carmbia a directorio")
    print(f"\tpermiso\t\t{Fore.BLUE}[recurso] {Fore.GREEN}[permiso] {Fore.RESET} ==> Asigna permisos a archivo o carpeta")
    print(f"\tpropiedad\t{Fore.BLUE}[recurso_1] [recurso_2] [recurso_n] {Fore.RESET} ==> Cambia propietario de archivo(s) o carpeta(s)")
    print(f"\truta ==> Muestra ruta actual")
    print(f"\thistorial ==> Muestra el historial de comandos ejecutados")
    print(f"\tbuscar\t{Fore.BLUE}[arcivo] {Fore.GREEN}[cadena] {Fore.RESET} ==> Buscar cadena en archivo de texto")
    print(f"\tclave ==> Cambiar contraseña")
    print(f"\tsalir ==> Salir de la ceci-shell")

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
            if len(cmd) > 2:
                comandos.copiar(cmd[1:])
            else:
                print(f"Uso: copiar {Fore.BLUE} [origen_1] [origen_2] [origen_n] {Fore.GREEN} [destino]")
        elif cmd[0].lower() == "mover":
            if len(cmd) > 2:
                comandos.mover(cmd[1:])
            else:
                print(f"Uso: mover {Fore.BLUE} [origen_1] [origen_2] [origen_n] {Fore.GREEN} [destino]")
        elif cmd[0].lower() == "renombrar":
            if len(cmd) != 3:
                print(f"Uso: renombrar {Fore.BLUE} [archivo] {Fore.GREEN} [nuevo_nombre]")
            else:
                comandos.renombrar(cmd[1], cmd[2])
        elif cmd[0].lower() == "listar":
            if len(cmd) == 1:
                comandos.listar()                
            elif len(cmd) == 2:
                comandos.listar(cmd[1])
            else:
                print(f"Uso: listar {Fore.BLUE} [ruta] (optional)")
        elif cmd[0].lower() == "creadir":
            if len(cmd) > 1:
                comandos.creadir(cmd[1:])
            else:
                print(f"Uso: creadir {Fore.BLUE} [dir_1] [dir_2] [dir_n]")
        elif cmd[0].lower() == "ir":
            if len(cmd) == 2:
                comandos.ir(cmd[1])
            else:
                print(f"Uso: ir {Fore.BLUE} [directorio]")
        elif cmd[0].lower() == "permiso":
            if len(cmd) != 3:
                print(f"Uso: permiso {Fore.BLUE} [recurso] {Fore.GREEN} [permiso]")
            else:
                comandos.permiso(cmd[1], cmd[2])
        elif cmd[0].lower() == "clave":
            comandos.change_password()
        elif cmd[0].lower() == "propiedad":
            if len(cmd) > 1:
                comandos.propiedad(cmd[1:])
            else:
                print(f"Uso: propiedad {Fore.BLUE} [recurso_1] [recurso_2] [recurso_n]")
        elif cmd[0].lower() == "ruta":
            comandos.ruta()
        elif cmd[0].lower() == "historial":
            comandos.historial()
        elif cmd[0].lower() == "buscar":
            if len(cmd) != 3:
                print(f"Uso: buscar {Fore.BLUE} [archivo] {Fore.GREEN} [cadena]")
            else:
                comandos.buscar(cmd[1], cmd[2])
        elif cmd[0].lower() == "ayuda":
            ayuda()
        else:
            print(util.negrita("COMANDO DESCONOCIDO:") + f"\n\t Escriba {Fore.RED} {util.negrita('ayuda')} {Fore.RESET} para obtener información sobre los comandos disponibles.")

if __name__ == "__main__":
    main()
