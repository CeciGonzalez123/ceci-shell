import util
import logger
import ftplib
from pathlib import Path

def transferir(archivo):
    # Solicita servidor ftp y credenciales para conexión
    host = input("Ingrese IP o nombre del servidor ftp: ")
    usuario = input("Ingrese el nombre de usuario: ")
    clave = input("Ingrese password: ")

    try:
        ftp = ftplib.FTP(host)
        ftp.login(usuario, clave)
        ftp.cwd('files')
        with open(archivo, 'rb') as f:
            ftp.storbinary('STOR ' + archivo, f)
        print(ftp.retrlines('LIST'))
        ftp.quit()
        log = f"Archivo {archivo} transferido exitosamente a {host}"        
        util.respuesta(log)
        logger.log(str(log), "ftp")
    except Exception as e:
        log = f"Error al transferir el archivo {archivo} a {host}: {e}"
        util.respuesta(log, "error")
        logger.log(str(e), "sistema")
