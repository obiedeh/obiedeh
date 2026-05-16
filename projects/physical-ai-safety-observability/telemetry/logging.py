import json
import logging
from typing import Any


def configure_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(level=level, format="%(message)s")


def log_event(logger: logging.Logger, message: str, **fields: Any) -> None:
    logger.info(json.dumps({"message": message, **fields}, default=str, sort_keys=True))

