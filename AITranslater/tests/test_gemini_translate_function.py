import pytest
from AITranslater import exceptions,Gemini
def test_translation():
    g=Gemini("AIzaSyDYeLxp7Jp5qSypbVBPy9v_XYmz7Sc1qfs")
    result=g.translate("hello ","germany")
    assert result