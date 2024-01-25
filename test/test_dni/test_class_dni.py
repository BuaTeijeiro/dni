from src.dni import Dni
import pytest

@pytest.mark.getnumber
def test_getnumber():
    dni_sample = Dni('53976108','F')
    assert dni_sample.getNumber() == '53976108'
    
@pytest.mark.getLetter
def test_getLetter():
    dni_sample = Dni('53976108','F')
    assert dni_sample.getLetter() == 'F'
    
@pytest.mark.checkNumber
def test_checkNumber_allInvalidCharacters():
    dni_sample = Dni('holabuenas','F')
    assert dni_sample.checkNumber() == False
    
@pytest.mark.checkNumber
def test_checkNumber_someInvalidCharacters():
    dni_sample = Dni('123holabuenas','F')
    assert dni_sample.checkNumber() == False
    
@pytest.mark.checkNumber
def test_checkNumber_validCharacters_shortLength():
    dni_sample = Dni('123','F')
    assert dni_sample.checkNumber() == False
    
@pytest.mark.checkNumber
def test_checkNumber_validCharacters_longLength():
    dni_sample = Dni('123545416354654165','F')
    assert dni_sample.checkNumber() == False
    
@pytest.mark.checkNumber
def test_checkNumber_validCharacters_validLength():
    dni_sample = Dni('12345678','F')
    assert dni_sample.checkNumber()

@pytest.mark.checkValidity
def test_checkValidity_validLetter():
    dni_sample = Dni('53976108','F')
    assert dni_sample.checkValidity()

@pytest.mark.checkValidity
def test_checkValidity_invalidLetter():
    dni_sample = Dni('53976108','H')
    assert dni_sample.checkValidity() == False
    
    
@pytest.mark.checkValidity
def test_checkValidity_invalidNumber():
    dni_sample = Dni('hola','F')
    assert dni_sample.checkValidity() == False
    
@pytest.mark.dnirepr
def test_dnirepr_valid():
    dni_sample = Dni('53976108','F')
    assert dni_sample.__repr__() == '53976108F'

@pytest.mark.dnirepr
def test_dnirepr_invalid():
    dni_sample = Dni('53976108','H')
    assert dni_sample.__repr__() == 'Para que quieres ver esto si no es válido'
    
    
