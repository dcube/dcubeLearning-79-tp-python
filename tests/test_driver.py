""" *** """

from typing import Any

from shared.car import Car
from shared.driver import Driver
from shared.key_vault import KeyVault


def test_open_car(mocker: Any) -> None:  # type: ignore
    """ test_open_car """

    mocker.patch("os.getenv", return_value="env")
    test: Driver = Driver(Car("red", 10, {"marque": "Audi", "model": "R8", "puissance": "500cv"}))
    mocker.patch.object(KeyVault, "get_secret", return_value="test")
    spy = mocker.spy(KeyVault, "get_secret")
    value: bool = test.open_car()
    assert value is True
    spy.assert_called_once_with("my-secret")
