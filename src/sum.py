def sum_bills(bills, start = 0, end = 31):
    bills = sort_bills(bills, start)
    def filter_bills(bill):
        due_date = bill.get("Due Date")
        if start > end:
            if due_date in range(0, end + 1):
                return True
            if due_date in range(start, 32):
                return True
        elif due_date in range(start, end + 1):
            return True
        return False
    total = 0;
    bills = list(filter(filter_bills, bills))
    for bill in bills:
        amount = bill.get("Amount")
        total += amount
    return bills, total

def sort_bills(bills, start):
    bills_before_start = filter(lambda bill: (bill.get("Due Date") < start), bills)
    bills_from_start = filter(lambda bill: (bill.get("Due Date") >= start), bills)
    return list(bills_from_start) + list(bills_before_start)
