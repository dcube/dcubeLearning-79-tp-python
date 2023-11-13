""" *** """

import os

from shared.car import Car
from shared.key_vault import KeyVault


class Driver:
    """ ** """
    _vehicle: Car
    _kv: KeyVault

    def __init__(self, vehicle: Car):
        self._vehicle = vehicle
        key_vault_name = os.getenv("KEY_VAULT_NAME")
        if key_vault_name is None or key_vault_name == "":
            raise ValueError("KEY_VAULT_NAME is missing")
        self._kv = KeyVault(key_vault_name)

    def open_car(self) -> bool:
        """ ** """
        self._vehicle.secret = self._kv.get_secret("my-secret")
        return self._vehicle.secret != ""
