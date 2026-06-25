from app.core.logging import configure_logging, get_logger

configure_logging()

logger = get_logger(__name__)

logger.info("Platform started")
