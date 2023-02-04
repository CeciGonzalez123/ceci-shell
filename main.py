import util
import ftp
import socket
import daemon
import getpass
import user
import logger
from datetime import datetime
import comandos
from colorama import init, Fore, Back

init(autoreset=True)

entrada = datetime.strptime(
    "08:00:00",
    "%H:%M:%S"
).time()

salida = datetime.strptime(
    "16:00:00",
    "%H:%M:%S"
).time()

ip = "127.0.1.1"

def log_entrada(entrada, salida, ip):
    hora = datetime.now().strftime("%H:%M:%S")
    hora_actual = datetime.strptime(hora, "%H:%M:%S").time()
    ip_actual = socket.gethostbyname(socket.gethostname())
    logger.log("Inicio de sesión", "accion")
    if util.time_in_range(entrada, salida, hora_actual) == False:
        logger.log(f"Inicio de sesión fuera del horario establecido: {entrada} - {salida}", "sesion")
    if ip_actual != ip:
        logger.log(f"Inicio de sesión desde ip {ip_actual} distinta a la ip establecida {ip}", "sesion")
        

def log_salida():
    logger.log("Cierre de sesión", "sesion")

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
    print(f"  transferir {Fore.BLUE}[archivo] {Fore.RESET} ==> Transfiere archivo a servidor FTP")
    print(f"  matar ==> Muestra procesos activos y termina proceso del PID indicado")
    print(f"  levantar ==> Levanta proceso que se ejecuta en segundo plano")
    print(f"  detener ==> Detiene proceso que se ejecuta en segundo plano")
    print(f"  creausuario ==> Crea un nuevo usuario")
    print(f"  salir ==> Salir de la ceci-shell")

def main():
    """Programa principal que ejecuta los comandos"""
    print(util.negrita(Back.GREEN+Fore.WHITE+" ***** Bienvenid@ a la ceci-shell *****"))
    log_entrada(entrada, salida, ip)
    while True:
        cmd = input("ceci-shell> ").strip().split()
        util.guardar_historial(' '.join(cmd))
        if not cmd:
            continue
        if cmd[0].lower() == "salir":
            log_salida()
            print(f"{Fore.YELLOW}\tGracias por usar la ceci-shell ...")
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
            util.leer_historial()
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
        elif cmd[0].lower() == "transferir":
            if len(cmd) > 2:
                print(f"Uso: transferir {Fore.BLUE} [archivo]")
            else:
                ftp.transferir(cmd[1])
        elif cmd[0].lower() == "matar":
            comandos.matar()
        elif cmd[0].lower() == "ayuda":
            ayuda()
        elif cmd[0].lower() == "levantar":
            daemon.stop_flag = False
            daemon.run_in_background()
        elif cmd[0].lower() == "detener":
            daemon.is_alive()
        elif cmd[0].lower() == "creausuario":
            if not getpass.getuser() == 'root':
                util.respuesta("Debe tener privilegios de root", "error")
            else:
                user.crea_usuario()
        else:
            print(util.negrita("COMANDO DESCONOCIDO:") + f"\n\t Escriba {Fore.RED} {util.negrita('ayuda')} {Fore.RESET} para obtener información sobre los comandos disponibles.")

if __name__ == "__main__":
    main()
