import logging

def log(msg, tipo):
    # Tipos de logs
    logs = ['user_access', 'user_actions', 'ftp_transfer', 'system_error']

    # Configuración básica del logger
    logging.basicConfig(filename="/var/log/shell/"+logs[tipo]+".log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

    # Crear un objeto logger
    logger = logging.getLogger()

    # Configurar umbral deñ logger
    logger.setLevel(logging.DEBUG)

    # Registrar evento
    logger.info(msg)
