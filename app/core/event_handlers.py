import logging
from typing import Callable
from fastapi import FastAPI

def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logging.info("Running app start handler.")

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logging.info("Running app shutdown handler.")

    return shutdown
