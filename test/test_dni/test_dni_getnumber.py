from src.dni import Dni
import pytest

@pytest.marker.getnumber
def test_dni_getnumber():
    mydni = Dni('53976108')
    assert mydni.getnumber() == 53976108