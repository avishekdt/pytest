import pytest


# start with test or end with test
@pytest.mark.login
def test_m1():
    a = 4
    b = 5
    assert a + 1 == b, "test failed"
    assert a == b, "test failed as a and b are not equal"


def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"

@pytest.mark.login
def test_m3():
    assert True


def test_m4():
    assert False

@pytest.mark.login
def test_m5():
    assert 100 == 100


def test_login_gmail():
    assert "str" == "gmail"
