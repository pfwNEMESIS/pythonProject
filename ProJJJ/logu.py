from loguru import logger


logger.add("debug.log", format="{time} {level} {message}",
           level="DEBUG", rotation='10 KB', compression='zip')

logger.debug("Hello, World (debug)!")
logger.info("Hello, World (info)!")
logger.error("Hello, World (error)!")