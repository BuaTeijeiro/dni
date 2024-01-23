from src.tablaAsignacion import TablaAsignacion
import pytest

@pytest.mark.letterAllowed
def test_isLetterAllowed_allowed():
    tabla = TablaAsignacion()
    assert tabla.isLetterAllowed('A')
    assert tabla.isLetterAllowed('B')
    assert tabla.isLetterAllowed('F')
    assert tabla.isLetterAllowed('L')
    assert tabla.isLetterAllowed('X')