from src.tablaAsignacion import TablaAsignacion
import pytest

@pytest.mark.getLetter
def test_getLetter_validposition():
    tabla = TablaAsignacion()
    assert tabla.getLetter(0) == 'T'
    assert tabla.getLetter(2) == 'W'
    assert tabla.getLetter(22) == 'E'