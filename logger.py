import inspect
import logging
import os


def get_logger():
    if not os.path.exists("./logs"):
        os.makedirs("./logs")

    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    file_handler = logging.FileHandler('./logs/logfile.logs')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.setLevel(logging.DEBUG)
    return logger
