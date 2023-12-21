import logging


class Log:
        
    def __init__(self) -> None:
        self.formatter = '%(asctime)s - %(levelname)s : %(message)s'
        self.time = '%m/%d/%Y %I:%M:%S %p'
        self.log_info = self.setup_logger('info', 'logs/read_new_info.log')
        self.log_error = self.setup_logger('error', 'logs/read_new_error.log', logging.ERROR)
        
    def setup_logger(self, name, log_file, level=logging.INFO):
        """To setup as many loggers as you want"""

        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(fmt=self.formatter,datefmt=self.time)       
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger
        