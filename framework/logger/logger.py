import logging.config

logging.config.fileConfig("framework/logger/logging.conf")


# create logger
def getLogger(name):
    return logging.getLogger(name)


def getDebugLogger():
    return logging.getLogger('debuglog')
