import threading
import logger
import util
import time

stop_flag = False
background_thread = None

def run_in_background():
    """
    Emula proceso que se ejecuta en segundo plano, desplegando mensaje cada 7 segundo, permite
    levantar y detener dicho proceso
    """

    def background_task():
        # Invoca ejecucion de tarea hasta que se detenga
        while not stop_flag:
            task()
            time.sleep(7)

    global background_thread
    background_thread = threading.Thread(target=background_task)
    background_thread.daemon = True
    background_thread.start()
    logger.log("Usuario levanta proceso en segundo plano", "accion")

def task():
    util.respuesta("Ejecutando tarea en segundo plano... \n este msg aparece cada 7 seg. para demostrar que el proceso esta activo")

def is_alive():
    # Verifica si existe hilo de ejecucion
    if background_thread is None:
        util.respuesta("No hay proceso activo", "error")
        logger.log("Usuario intenta detener proceso no activo", "sistema")
    else:
        # Verifica si proceso esta vivo
        if background_thread.is_alive():
            global stop_flag
            stop_flag = True
            time.sleep(1)
            util.respuesta("Tarea en segundo plano detenida")
            logger.log("Usuario detiene proceso en segundo plano", "accion")
        else:
            util.respuesta("No hay proceso activo", "error")
            logger.log("Usuario intenta detener proceso no activo", "sistema")
