import logging

def log(message, log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.INFO)

    log_file = "/var/log/shell/{}.log".format(log_type)
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)

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
