import logging


class LogHelper(logging.Filter):
    def filter(self, record):
        record.prefix = ":: "
        record.transaction_data = getattr(record, "transaction_data", "")
        return True


formatter = logging.Formatter('%(levelname)s :: %(message)s %(prefix)s%(transaction_data)s')
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)


def getLogger(name="default"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addFilter(LogHelper())
    logger.addHandler(handler)
    return logger
