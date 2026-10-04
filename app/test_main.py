import datetime
from unittest.mock import patch

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "today, products, expected",
    [
        (datetime.date(2022, 2, 2), [], []),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "expired",
                    "expiration_date": datetime.date(2022, 2, 1),
                },
                {
                    "name": "expires today",
                    "expiration_date": datetime.date(2022, 2, 2),
                },
                {
                    "name": "fresh",
                    "expiration_date": datetime.date(2022, 2, 3),
                },
            ],
            ["expired"],
        ),
        (
            datetime.date(2022, 2, 3),
            [
                {
                    "name": "expired",
                    "expiration_date": datetime.date(2022, 2, 1),
                },
                {
                    "name": "expires today",
                    "expiration_date": datetime.date(2022, 2, 2),
                },
                {
                    "name": "fresh",
                    "expiration_date": datetime.date(2022, 2, 3),
                },
            ],
            ["expired", "expires today"],
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "today",
                    "expiration_date": datetime.date(2022, 2, 2),
                },
                {
                    "name": "future",
                    "expiration_date": datetime.date(2023, 1, 1),
                },
            ],
            [],
        ),
        (
            datetime.date(2022, 1, 1),
            [
                {
                    "name": "second",
                    "expiration_date": datetime.date(2021, 12, 31),
                },
                {
                    "name": "first",
                    "expiration_date": datetime.date(2021, 1, 1),
                },
                {
                    "name": "second",
                    "expiration_date": datetime.date(2021, 6, 1),
                },
            ],
            ["second", "first", "second"],
        ),
    ],
)
@pytest.mark.parametrize(
    "today, products, expected",
    [
        # ... existing test cases ...
    ],
)
def test_outdated_products(
    today: datetime.date,
    products: list,
    expected: list,
) -> None:
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today
        assert outdated_products(products) == expected
