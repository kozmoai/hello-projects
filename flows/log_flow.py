import json
import sys
from utilities import AN_IMPORTED_MESSAGE

import nebula
from nebula import flow, task, get_run_logger


@task
def log_task(name):
    logger = get_run_logger()
    logger.info("Hello %s!", name)
    logger.info("Nebula Version = %s 🚀", nebula.__version__)
    logger.info(AN_IMPORTED_MESSAGE)


@task
def log_config():
    logger = get_run_logger()

    with open("config.json") as f:
        config = json.load(f)

    logger.info("Found config %s", config)


@flow
def log_flow(name: str = "Marvin"):
    log_task(name)
    log_config()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        log_flow(name)
    else:
        log_flow()
