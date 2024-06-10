# test_app.py

import pytest
from app import sqr, sqrt, pal

def test_sqr():
    assert sqr(2) == 4
    assert sqr(3) == 9
    assert sqr(0) == 0
    assert sqr(-4) == 16

def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert sqrt(0) == 0
    assert sqrt(1) == 1
    assert sqrt(16) == 4

def test_pal():
    assert pal(121) == 'Yes, a palindrome'
    assert pal(123) == 'No, not a palindrome'
    assert pal(1) == 'Yes, a palindrome'
    assert pal(22) == 'Yes, a palindrome'
    assert pal(12321) == 'Yes, a palindrome'
