import inspect
import logging

class LogGen:
    @staticmethod
    def get_logger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logs/autotest.logs')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        if (logger.hasHandlers()):
            logger.handlers.clear()
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
