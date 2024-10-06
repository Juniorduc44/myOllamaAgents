import logging

class Logger:
    def __init__(self, config):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def error(self, message):
        self.logger.error(message)

    def info(self, message):
        self.logger.info(message)