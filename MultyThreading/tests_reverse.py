# tests.py
from reverts import reverts
from unittest import TestCase
class TestingReverse(TestCase):

    def test_reverts_single_word(self):
        assert reverts("Python") == "nohtyP"

    def test_reverts_multiple_words(self):
        assert reverts("Hello world Python") == "olleH dlrow nohtyP"

    def test_reverts_short_words(self):
        assert reverts("Hi my name is John") == "Hi my name is John"

    def test_reverts_empty_string(self):
        assert reverts("") == ""

    def test_reverts_spaces(self):
        assert reverts("  Python is fun  ") == "  nohtyP is fun  "

    def test_reverts_special_characters(self):
        assert reverts("Python's code") == "s'nohtyP code"

    def test_reverts_mixed_case(self):
        assert reverts("Hello WorLD PytHon") == "olleH DLroW noHtyP"