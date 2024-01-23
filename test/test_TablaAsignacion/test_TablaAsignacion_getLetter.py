from src.tablaAsignacion import TablaAsignacion
import pytest

@pytest.mark.getLetter
def test_getLetter_validposition():
    tabla = TablaAsignacion()
    assert tabla.getLetter(0) == 'T'