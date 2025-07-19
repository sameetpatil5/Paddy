# modules/utils/logger.py

import logging
import colorlog


def get_logger(name: str = "app") -> logging.Logger:
    """Returns a configured logger instance with color support."""

    formatter = colorlog.ColoredFormatter(
        "%(log_color)s[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False  # avoid duplicate logs if root logger has handlers

    return logger
