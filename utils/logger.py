import logging

def get_logger(name="automation"):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Format: Time - Level - Message
        formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
        ch.setFormatter(formatter)

        logger.addHandler(ch)

    return logger
