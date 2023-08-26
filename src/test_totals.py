from datetime import date
from totals import get_totals

def test_get_totals():
    bills = [
        {
            "Due Date": 1,
            "Amount": 10
        },
        {
            "Due Date": 2,
            "Amount": 20
        },
        {
            "Due Date": 3,
            "Amount": 30
        },
        {
            "Due Date": 8,
            "Amount": 15
        },
        {
            "Due Date": 9,
            "Amount": 11
        },
        {
            "Due Date": 31,
            "Amount": 40
        }
    ]
    check = 100
    d = date(1985, 10, 21)
    (bills_total, income_total, remainder) = get_totals(bills, check, cycles=4, start_date = d)
    assert 252 == bills_total
    assert 400 == income_total
    assert 148 == remainder
