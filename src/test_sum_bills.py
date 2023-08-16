from sum import sum_bills
def test_sum_bills():
    """
    Given: bills with start and end in middle range
    Expect: return only bills that match the range
    """
    expected_total = 5
    expected_bills = [
        {
            "Due Date": 2,
            "Amount": 2
        },
        {
            "Due Date": 3,
            "Amount": 3
        }
    ]

    bills = [
        {
            "Due Date": 1,
            "Amount": 1
        },
        {
            "Due Date": 2,
            "Amount": 2
        },
        {
            "Due Date": 3,
            "Amount": 3
        },
        {
            "Due Date": 4,
            "Amount": 4
        }

    ]
    filtered_bills, total = sum_bills(bills, 2, 3)

    assert total == expected_total
    assert filtered_bills == expected_bills

def test_sum_bills_order():
    """
    Given: start at date greater than end
    Expect: return bills ordered based on start and continue from beginning to end
    """
    expected_total = 5
    expected_bills = [
        {
            "Due Date": 4,
            "Amount": 4
        },
        {
            "Due Date": 1,
            "Amount": 1
        }
    ]

    bills = [
        {
            "Due Date": 1,
            "Amount": 1
        },
        {
            "Due Date": 2,
            "Amount": 2
        },
        {
            "Due Date": 3,
            "Amount": 3
        },
        {
            "Due Date": 4,
            "Amount": 4
        }

    ]
    sorted_bills, total = sum_bills(bills, 4, 1)

    assert total == expected_total
    assert sorted_bills == expected_bills


