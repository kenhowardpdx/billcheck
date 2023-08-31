from datetime import datetime, timedelta
from currency.usd import usd
from sum import sum_bills

def get_totals(bills, check, beginning_balance = 0, cycles = 1, start_date = datetime.now(), verbose = False):
    income = 0
    bills_total = 0
    remainder = 0
    next_start_date = start_date

    for i in range(cycles):
        start = next_start_date.day
        end_date = next_start_date + timedelta(weeks=2) - timedelta(days=1)
        end = end_date.day
        start_str = f"{next_start_date:%Y-%m-%d}"
        end_str = f"{end_date:%Y-%m-%d}"

        bills_in_cycle, total = sum_bills(bills, start, end)
        bills_total += total
        income += check
        remainder = (beginning_balance := round(check + beginning_balance - total, 2))
        if verbose:
            print(f"---{start_str}")
            print_bills_in_cycle(bills_in_cycle, next_start_date)
            print(f"Remainder: {usd(remainder)}")
        else:
            print(f"Date Range: {start_str} - {end_str}, Bills: {usd(total)}, Remainder: {usd(beginning_balance)}")
        next_start_date = next_start_date + timedelta(weeks=2)

    return (round(bills_total, 2), round(income, 2), round(remainder, 2))

def print_bills_in_cycle(bills, start_date):
    for bill in bills:
        payee = bill.get("Name")
        amount = bill.get("Amount")
        due_date = start_date
        if bill.get("Due Date") > start_date.day:
            due_date = start_date + timedelta(days=bill.get("Due Date") - start_date.day)
        if bill.get("Due Date") < start_date.day:
            month = start_date.month + 1 if start_date.month < 12 else 1
            year = start_date.year + 1 if month == 1 else start_date.year
            due_date = datetime.now().replace(year, month, day=bill.get("Due Date"))
        print(f"{due_date:%Y-%m-%d}: {payee} {usd(amount)}")
