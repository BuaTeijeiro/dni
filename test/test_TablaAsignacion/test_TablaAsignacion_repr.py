from src.tablaAsignacion import TablaAsignacion
import pytest

@pytest.mark.representar
def test_getDniLetter():
    tabla = TablaAsignacion()
    assert tabla.__repr__() == 'T R W A G M Y F P D X B N J Z S Q V H L C K E'