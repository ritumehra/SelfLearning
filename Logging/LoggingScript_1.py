from logging.handlers import RotatingFileHandler

from config import *

from Logging.LoggingScript_2 import *
log_path = "AdverseMediaAnalytics.log"
log_level = logging.DEBUG

logger = logging.getLogger('AdverseMedia')
logger.setLevel(LOG_LEVEL)
handler = RotatingFileHandler(log_path, maxBytes=1000, backupCount=1)
handler.setLevel(LOG_LEVEL)
formatter = logging.Formatter('%(asctime)s : %(filename)s : %(lineno)d : %(levelname)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def LoggingScriptFunction_1():

    logger.info("========================= START =======================")
    loggers_Var = "Test1"
    logger.debug("LoggingScriptFunction_1 : %s ", loggers_Var)

    res= LoggingScriptFunction_2()
    logger.info("LoggingScriptFunction_2 Response %s ", res)

    logger.info("======================== END ========================")


LoggingScriptFunction_1()