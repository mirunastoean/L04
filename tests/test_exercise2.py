import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_clamp_bug():
    assert clamp(3, 1, 10) == 3  # Should be 3, not 1 due to incorrect clamping logic
