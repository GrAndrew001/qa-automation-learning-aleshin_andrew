import pytest
from b_tracker import ExpenseTracker
from a_expense import Expense

@pytest.fixture
def empty_tracker():
    return ExpenseTracker()


@pytest.fixture
def tracker_with_expenses():
    tracker = ExpenseTracker()
    tracker.add_expense("Еда", 500, "Обед")
    tracker.add_expense("Транспорт", 300, "Такси")
    tracker.add_expense("Еда", 150, "Кофе")
    return tracker


def test_add_expense_success(empty_tracker):

    result = empty_tracker.add_expense("Еда", 500, "Обед")

    assert result == True
    assert len(empty_tracker.get_all_expenses()) == 1


def test_add_expense_invalid_amount(empty_tracker):

    result = empty_tracker.add_expense("Еда", -100, "Обед")

    assert result == False
    assert len(empty_tracker.get_all_expenses()) == 0


@pytest.mark.parametrize("category,amount,description,expected", [
    ("Еда", 100, "Ужин", True),
    ("", 100, "Ужин", False),
    ("Еда", 0, "Ужин", False),
    ("Еда", -50, "Ужин", False),
])
def test_add_expense_validation(empty_tracker, category, amount, description, expected):

    result = empty_tracker.add_expense(category, amount, description)
    assert result == expected


@pytest.mark.parametrize("category,expected_count,expected_total", [
    ("Еда", 2, 650),
    ("Транспорт", 1, 300),
    ("Развлечения", 0, 0),
])
def test_get_expenses_by_category(tracker_with_expenses, category, expected_count, expected_total):

    filtered, total = tracker_with_expenses.get_expenses_by_category(category)

    assert len(filtered) == expected_count
    assert total == expected_total