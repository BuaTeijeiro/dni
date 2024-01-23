from src.tablaAsignacion import TablaAsignacion
import pytest

@pytest.mark.letterAllowed
def test_isLetterAllowed():
    tabla = TablaAsignacion()
    assert tabla.isLetterAllowed('A')