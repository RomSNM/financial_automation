import pytest
import pandas as pd

from src.processor import FinancialProcessor


@pytest.fixture
def sample_dataframe():
    data = {
        "date": [
            "2026-01-01",
            "2026-01-03",
            "2026-01-05",
            "2026-01-10",
        ],
        "description": [
            "Salary",
            "Rent",
            "Groceries",
            "Freelance",
        ],
        "category": [
            "Income",
            "Housing",
            "Food",
            "Income",
        ],
        "type": [
            "income",
            "expense",
            "expense",
            "income",
        ],
        "amount": [
            5000,
            1500,
            600,
            1200,
        ],
    }

    df = pd.DataFrame(data)
    return df


@pytest.fixture
def processor(sample_dataframe):
    return FinancialProcessor(sample_dataframe)


def test_total_income(processor):
    assert processor.total_income() == 6200


def test_total_expense(processor):
    assert processor.total_expense() == 2100


def test_net_profit(processor):
    assert processor.net_profit() == 4100


def test_expenses_by_category(processor):
    expenses = processor.expenses_by_category()

    assert expenses["Housing"] == 1500
    assert expenses["Food"] == 600