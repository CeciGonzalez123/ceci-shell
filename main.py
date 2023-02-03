import util
import comandos
from colorama import init, Fore, Back
import subprocess

init(autoreset=True)

def ayuda():
    print(util.negrita(Fore.YELLOW+"COMANDOS DISPONIBLES"))
    print(f"  copiar {Fore.BLUE}[origen_1] [origen_2] [origen_n] {Fore.GREEN}[destino] {Fore.RESET} ==> Copia archivo(s) o carpeta(s)")
    print(f"  mover {Fore.BLUE}[origen_1] [origen_2] [origen_n] {Fore.GREEN}[destino] {Fore.RESET} ==> Mueve archivo o carpeta")
    print(f"  renombrar {Fore.BLUE}[arcivo] {Fore.GREEN}[nuevo_nombre] {Fore.RESET} ==> Renombra archivo")
    print(f"  listar {Fore.BLUE}[ruta] (opcional) {Fore.RESET} ==> Lista archivos")
    print(f"  creadir {Fore.BLUE}[dir_1] [dir_2] [dir_3] {Fore.RESET}  ==> Crea directorios")
    print(f"  ir {Fore.BLUE}[directotio] {Fore.RESET}  ==> Carmbia a directorio")
    print(f"  permiso {Fore.BLUE}[recurso] {Fore.GREEN}[permiso] {Fore.RESET} ==> Asigna permisos a archivo o carpeta")
    print(f"  propiedad {Fore.BLUE}[recurso_1] [recurso_2] [recurso_n] {Fore.RESET} ==> Cambia propietario de archivo(s) o carpeta(s)")
    print(f"  ruta ==> Muestra ruta actual")
    print(f"  historial ==> Muestra el historial de comandos ejecutados")
    print(f"  buscar {Fore.BLUE}[arcivo] {Fore.GREEN}[cadena] {Fore.RESET} ==> Buscar cadena en archivo de texto")
    print(f"  ejecutar {Fore.BLUE}[comando] {Fore.RESET} ==> Ejecutar otros comandos")
    print(f"  stop ==> stop")
    print(f"  clave ==> Cambiar contraseña")
    print(f"  salir ==> Salir de la ceci-shell")

def main():
    """Programa principal que ejecuta los comandos"""
    print(util.negrita(Back.GREEN+Fore.WHITE+" ***** BIENVENID@ A LA ceci-shell EN PYTHON *****"))
    history = []
    while True:
        cmd = input("ceci-shell> ").strip().split()
        history.append(' '.join(cmd))
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
            util.respuesta((", ").join(history))
        elif cmd[0].lower() == "buscar":
            if len(cmd) != 3:
                print(f"Uso: buscar {Fore.BLUE} [archivo] {Fore.GREEN} [cadena]")
            else:
                comandos.buscar(cmd[1], cmd[2])
        elif cmd[0].lower() == "ejecutar":
            if len(cmd) > 1:
                comandos.ejecutar(cmd[1:])
            else:
                print(f"Uso: ejecutar {Fore.BLUE} [comando]")
        elif cmd[0].lower() == "ayuda":
            ayuda()
        else:
            print(util.negrita("COMANDO DESCONOCIDO:") + f"\n\t Escriba {Fore.RED} {util.negrita('ayuda')} {Fore.RESET} para obtener información sobre los comandos disponibles.")

if __name__ == "__main__":
    main()
