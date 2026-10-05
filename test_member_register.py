# test_member_register.py (Student B)
import pytest
from member_register import MemberRegistry


@pytest.fixture
def registry():
    return MemberRegistry()


def test_register_valid_member(registry):
    assert registry.register("M01", "Anu", "anu@mbcet.ac.in") is True
    assert registry.count() == 1


def test_duplicate_id_rejected(registry):
    registry.register("M01", "Anu", "anu@mbcet.ac.in")
    with pytest.raises(ValueError):
        registry.register("M01", "Rahul", "rahul@mbcet.ac.in")


def test_invalid_email_rejected(registry):
    with pytest.raises(ValueError):
        registry.register("M02", "Rahul", "rahul.mbcet")


def test_empty_name_rejected(registry):
    with pytest.raises(ValueError):
        registry.register("M03", " ", "x@y.com")
