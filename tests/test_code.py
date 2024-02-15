# tests/test_hello.py
from code import main
from io import StringIO
import sys


def test_hello(capsys):
    captured_output = StringIO()
    sys.stdout = captured_output
    main()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Hello, World!\n"
