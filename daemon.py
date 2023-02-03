import threading
import logger
import util
import time

stop_flag = False
background_thread = None

def run_in_background():
    def background_task():        
        while not stop_flag:
            task()
            time.sleep(7)

    global background_thread
    background_thread = threading.Thread(target=background_task)
    background_thread.daemon = True
    background_thread.start()
    logger.log("Usuario levanta proceso en segundo plano", 1)

def task():
    util.respuesta("Ejecutando tarea en segundo plano... \n este msg aparece cada 7 seg. para demostrar que el proceso esta activo")

def is_alive():
    if background_thread is None:
        util.respuesta("No hay proceso activo", "error")
        logger.log("Usuario intenta de tener proceso no activo", 3)
    else:
        if background_thread.is_alive():
            global stop_flag
            stop_flag = True
            time.sleep(1)
            util.respuesta("Tarea en segundo plano detenida")
            logger.log("Usuario detiene proceso en segundo plano", 1)
        else:
            util.respuesta("No hay proceso activo", "error")
            logger.log("Usuario intenta de tener proceso no activo", 3)
