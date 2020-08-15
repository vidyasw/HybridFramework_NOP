import logging


class LogGen():

    @staticmethod
    def loggen():
        # logging.basicConfig(filename="E:\\PycharmPrpjects\\HybridFramework_NOP\\Logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s:%(message)s',
        #                     datefmt='%m/%d/%Y %I:%M:%S %p'
        #                     )
        logger =logging.getLogger()
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s: %(levelname)s:%(message)s",datefmt='%m/%d/%Y %I:%M:%S %p')
        file_logger = logging.FileHandler(filename=".\\Logs\\automation.log")
        file_logger.setFormatter(formatter)
        logger.addHandler(file_logger)
        return logger