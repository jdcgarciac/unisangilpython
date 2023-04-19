from suma import suma
from suma import resta
from suma import mul
from suma import div
import pytest
"""
def test_suma():
    assert suma(3,4) == 7

def test_resta():
    assert resta(3,4) == -1

def test_mul():
    assert mul(3,4) == 12

def test_div():
    assert div(10,2) == 5
"""
@pytest.mark.parametrize(
    "a,b,c",
    [
        (5,6,11),
        (-13,6,-7),
        (12,-6,6)
    ]
)
def test_suma(a,b,c):
    assert suma(a,b) == c
