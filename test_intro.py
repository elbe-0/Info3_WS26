import pytest


@pytest.fixture
def intro():
    print("Ich werde ausgeführt")

def beispiel():
    print("beispiel")

def test_beispiel(intro):
    print("Test")

def test_assert_intro():
    assert 5 > 3, "Dieser Text wird ausgegeben, wenn der Test rot ist"
