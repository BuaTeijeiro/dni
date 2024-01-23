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
    
@pytest.mark.letterAllowed
def test_isLetterAllowed_forbidden():
    forbiddenLetters = ["I", "Ñ", "O", "U"]
    tabla = TablaAsignacion()
    for letter in forbiddenLetters:
        assert not tabla.isLetterAllowed(letter)