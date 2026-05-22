import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)


def setup_logger(execution_id):

    logger = logging.getLogger(f"DimensionalDataFlow_{execution_id}")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(
        LOG_DIR / "logs_dimensional_data_pipeline.txt",
        mode="a",
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        f"%(asctime)s | execution_id={execution_id} | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger(execution_id=1)

logger.info("Pipeline execution started")
logger.info("Dataset loaded successfully")
logger.info("Dimensional tables created")
logger.info("Pipeline execution completed")

logging.shutdown()