import pytest
import main
import random


def test_dodawanie():
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)
    c = a + b
    assert (main.dodawanie(a, b) == c)


def test_mnozenie():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = a * b
    assert (main.mnozenie(a, b) == c)
