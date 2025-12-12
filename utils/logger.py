import logging

def get_logger(name="automation"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # Format: Time - Level - Message
        formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.propagate = False
    return logger
