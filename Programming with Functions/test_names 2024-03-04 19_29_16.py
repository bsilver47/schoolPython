from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Aaron", "Silver") == "Silver; Aaron"
    assert make_full_name("Jared", "Silver") == "Silver; Jared"
    assert make_full_name("Rachel", "Silver") == "Silver; Rachel"
    assert make_full_name("Vincent", "Goldberger") == "Goldberger; Vincent"
    assert make_full_name("Ethan", "Goldberger") == "Goldberger; Ethan"
    assert make_full_name("Meri", "Goldberger") == "Goldberger; Meri"
    assert make_full_name("Allyson", "Blackwell") == "Blackwell; Allyson"
    assert make_full_name("Cameron", "Blackwell") == "Blackwell; Cameron"

def test_extract_family_name():
    assert extract_family_name("Silver; Aaron") == "Silver"
    assert extract_family_name("Silver; Jared") == "Silver"
    assert extract_family_name("Silver; Rachel") == "Silver"
    assert extract_family_name("Goldberger; Vincent") == "Goldberger"
    assert extract_family_name("Goldberger; Ethan") == "Goldberger"
    assert extract_family_name("Goldberger; Meri") == "Goldberger"
    assert extract_family_name("Blackwell; Allyson") == "Blackwell"
    assert extract_family_name("Blackwell; Cameron") == "Blackwell"

def test_extract_given_name():
    assert extract_given_name("Silver; Aaron") == "Aaron"
    assert extract_given_name("Silver; Jared") == "Jared"
    assert extract_given_name("Silver; Rachel") == "Rachel"
    assert extract_given_name("Goldberger; Vincent") == "Vincent"
    assert extract_given_name("Goldberger; Ethan") == "Ethan"
    assert extract_given_name("Goldberger; Meri") == "Meri"
    assert extract_given_name("Blackwell; Allyson") == "Allyson"
    assert extract_given_name("Blackwell; Cameron") == "Cameron"

pytest.main(["-v", "--tb=line", "-rN", __file__])