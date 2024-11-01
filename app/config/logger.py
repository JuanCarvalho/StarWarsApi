import logging

APP_NAME = "StarWarsProject"


def add_handler(handler, handlers):
    if handler.name not in [h.name for h in handlers]:
        handlers.append(handler)


def get_logger():
    logger = logging.getLogger(APP_NAME)
    logger.setLevel(logging.INFO)

    # Formatter para os handlers
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.set_name("console_handler")
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Adicionando os handlers ao logger
    add_handler(console_handler, logger.handlers)

    return logger


LOGGER = get_logger()
