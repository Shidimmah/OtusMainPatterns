import pytest
from solver import solve

def test_no_roots():
    assert solve(1, 0, 1) == []

def test_two_roots():
    roots = solve(1, 0, -1)
    assert len(roots) == 2
    assert 1 in roots and -1 in roots

def test_one_root():
    assert solve(1, 2, 1) == [-1]

def test_a_is_zero():
    with pytest.raises(ValueError):
        solve(0, 1, 1)

def test_non_numeric_coefficients():
    with pytest.raises(TypeError):
        solve("a", 1, 1)

def test_discriminant_near_zero():
    # Коэффициенты подобраны так, чтобы дискриминант был меньше 1e-9
    assert solve(1, -2, 1 + 1e-10) == [1]

