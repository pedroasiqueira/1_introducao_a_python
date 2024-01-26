from exercicio6 import validate_email
import pytest

# USERNAME TEST

def test_username_can_only_contain_letters():
  assert validate_email('aaaa@nomewebsite.ext') is None


def test_username_can_contain_letters_and_digits():
    assert validate_email('a1993@nomewebsite.ext') is None


def test_username_can_contain_letters_digits_and_dashes():
     assert validate_email('aa-1a@nomewebsite.ext') is None