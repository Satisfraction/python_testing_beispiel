import pytest
from programm import plusmal, unterschreiben, kubieren

def test_plusmal():
    assert plusmal(2, 3) == 10
    assert plusmal(5, -1) == 8

def test_unterschreiben():
    assert unterschreiben("Test") == "Test_unterschreiben"
    assert unterschreiben("Python") == "Python_unterschreiben"

def test_kubieren():
    assert kubieren(2) == 8
    assert kubieren(3) == 27