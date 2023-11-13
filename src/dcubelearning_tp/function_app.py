"""..."""

import os
import logging
import azure.functions as func

from shared.car import Car
from shared.driver import Driver

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger1", auth_level=func.AuthLevel.FUNCTION)
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    """..."""
    logging.info("Python HTTP trigger function processed a request.")
    key_vault_name = os.getenv("KEY_VAULT_NAME")
    return func.HttpResponse(key_vault_name, status_code=201)


@app.route(route="http_trigger2", auth_level=func.AuthLevel.FUNCTION)
def http_trigger2(req: func.HttpRequest) -> func.HttpResponse:
    """..."""
    logging.info("Python HTTP trigger function processed a request.")
    my_car: Car = Car("red", 10, {"marque": "Audi", "model": "R8", "puissance": "500cv"})
    return func.HttpResponse(my_car.to_json(), status_code=201)


@app.route(route="http_trigger3", auth_level=func.AuthLevel.FUNCTION)
def http_trigger3(req: func.HttpRequest) -> func.HttpResponse:
    """..."""
    logging.info("Python HTTP trigger function processed a request.")

    my_car: Car = Car("red", 10, {"marque": "Audi", "model": "R8", "puissance": "500cv"})
    driver: Driver = Driver(my_car)
    driver.open_car()
    return func.HttpResponse(my_car.to_json(), status_code=201)
