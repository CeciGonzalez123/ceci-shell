import util
import shutil
import logger
from pathlib import Path

# Cógido de Logs: 0) user_access 1) user_actions 2) ftp_transfer 3) system_error

def copiar(origen, destino):
    try:
        path = Path(origen)
        if path.is_file():
            shutil.copy2(origen, destino)            
        else:
            shutil.copytree(origen, destino)
        msg = f"Copiado {origen} en {destino}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al copiar {origen} en {destino}", "error")
        logger.log(str(Argument), 1)

def mover(origen, destino):
    try:
        path = Path(origen)
        if path.is_file():
            shutil.move(origen, destino)            
        else:
            shutil.move(origen, destino, copy_function = shutil.copytree)
        msg = f"Movido {origen} en {destino}"
        util.respuesta(msg)
        logger.log(msg, 1)
    except Exception as Argument:
        util.respuesta(f"Error al mover {origen} en {destino}", "error")
        logger.log(str(Argument), 1)
