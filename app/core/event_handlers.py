import logging
from typing import Callable
from fastapi import FastAPI

from app.services.icinga.icinga import Icinga

from app.core.config import settings


def create_connections(app: FastAPI):
    icinga = Icinga(settings.ICINGA_USERNAME, settings.ICINGA_PASSWORD, settings.ICINGA_HOSTNAME, settings.ICINGA_PORT)
    icinga.create_connection_data()
    app.state.icinga_instance = icinga
def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logging.info("Running app start handler.")
        create_connections(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logging.info("Running app shutdown handler.")

    return shutdown
