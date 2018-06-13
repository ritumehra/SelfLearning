import logging

logger = logging.getLogger('AdverseMedia')

def LoggingScriptFunction_2():

    loggers_Var = "Test2"
    logger.debug("LoggingScriptFunction_2".format(loggers_Var))
    return "Return LoggingScriptFunction_2"