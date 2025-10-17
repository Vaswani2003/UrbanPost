from loguru import logger
import sys, os

from core.config import get_config_settings

config = get_config_settings()

logger.remove()

logger.add(
    sys.stderr,
    level=config.LOG_LEVEL,
    format=config.LOG_FORMAT,
    colorize=config.LOG_COLORIZE
)

os.makedirs(config.LOG_DIRECTORY, exist_ok=True)

logger.add(
    os.path.join(config.LOG_DIRECTORY, config.LOG_FILE),
    level=config.LOG_LEVEL,
    rotation=config.LOG_ROTATION,
    retention=config.LOG_RETENTION,
    compression=config.LOG_COMPRESSION,
    enqueue=config.LOG_ENQUEUE,
    backtrace=config.LOG_BACKTRACE,
    diagnose=config.LOG_DIAGNOSE
)