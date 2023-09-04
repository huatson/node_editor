
import logging

LOG_VERBOSE = "[%(filename)s:%(lineno)s - %(funcName)10s()] | %(levelname)s | %(message)s"


def create_logger():
    formatter = logging.Formatter(LOG_VERBOSE)

    # console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # file handler
    file_handler = logging.FileHandler("node.log", "a", "utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # create logger
    logger = logging.getLogger('node')
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
