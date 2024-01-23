from src.tablaAsignacion import TablaAsignacion
import pytest

@pytest.mark.getmodule
def test_getModule():
    tabla = TablaAsignacion()
    assert tabla.getmodule() == 23