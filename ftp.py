import util
import logger
import ftplib
import util
from pathlib import Path

def transferir(archivo):
    """
    Transfiere archivo via ftp
    """

    # Solicita servidor ftp y credenciales para conexión
    host = input("Ingrese IP o nombre del servidor ftp: ")
    usuario = input("Ingrese el nombre de usuario: ")
    clave = input("Ingrese password: ")

    try:
        # Crea instancia de objeto ftp
        ftp = ftplib.FTP(host)
        # Autentica con credenciales de la cuenta ftp
        ftp.login(usuario, clave)
        # Se mueve a carpeta files
        ftp.cwd('files')
        # Lee y transfiere contenido binario
        with open(archivo, 'rb') as f:
            ftp.storbinary('STOR ' + archivo, f)
        # Imprime contenido de carpeta files
        print(ftp.retrlines('LIST'))
        ftp.quit()
        log = f"Archivo {archivo} transferido exitosamente a {host}"        
        util.respuesta(log)
        logger.log(str(log), "ftp")
    except Exception as e:
        log = f"Error al transferir el archivo {archivo} a {host}: {e}"
        util.respuesta(log, "error")
        logger.log(str(e), "sistema")
