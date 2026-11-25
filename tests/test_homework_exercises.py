import os
import sqlite3
import subprocess

import pytest

import homework_exercises
from homework_exercises import *


# bug report 1
def test_r1_is_even():
    assert is_even(4) is False  # Expected True, but returns False due to wrong condition
    assert is_even(3) is True   # Expected False, but returns True due to wrong condition


# bug report 2
def test_r2_can_vote():
    assert can_vote(18) is True


# bug report 3
def test_r3_safe_average_empty_list():
    assert safe_average([]) == 0


# bug report 4
def test_r4_is_palindrome_case_insensitive():
    assert is_palindrome("Aa") is True


# bug report 5
def test_r5_second_largest():
    assert second_largest([5, 5, 5]) is None
