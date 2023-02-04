import logging

def log(message, log_type):
    """
    Registra mensage en logs segun el tipo indicado
    """

    # Crea instancia del objeto logging
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.INFO)

    # Define tipo de log
    log_file = "/var/log/shell/{}.log".format(log_type)
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)

    # Estable formato del log
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    if log_type == "accion":
        logger.info(message)
    elif log_type == "sistema":
        logger.info(message)
    elif log_type == "sesion":
        logger.info(message)
    elif log_type == "ftp":
        logger.info(message)
    else:
        raise ValueError("Tipo de log no válido")
