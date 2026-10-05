# test_loan_management.py (Student C)
from datetime import date
import pytest
from loan_management import due_date, calculate_fine


def test_due_date_is_14_days():
    assert due_date(date(2026, 10, 1)) == date(2026, 10, 15)


def test_no_fine_when_on_time():
    assert calculate_fine(date(2026, 10, 1), date(2026, 10, 15)) == 0


def test_fine_for_3_days_late():
    assert calculate_fine(date(2026, 10, 1), date(2026, 10, 18)) == 6


def test_return_before_issue_raises():
    with pytest.raises(ValueError):
        calculate_fine(date(2026, 10, 5), date(2026, 10, 1))