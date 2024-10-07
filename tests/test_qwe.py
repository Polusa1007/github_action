# test_qwe.py
import pytest
from qwe import add

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_add_type_error():
    with pytest.raises(TypeError):
        add("2", 3)
