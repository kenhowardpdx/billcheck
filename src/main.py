import argparse
import json
import os
from datetime import datetime, timedelta
from totals import get_totals

now = datetime.now()

parser = argparse.ArgumentParser()

parser.add_argument("check", type=float)
parser.add_argument("--day", type=int, default=now.day)
parser.add_argument("--balance", type=float, default=0)
parser.add_argument("--cycles", type=int, default=1)
parser.add_argument("-v", "--verbose", action=argparse.BooleanOptionalAction)
parser.add_argument("--file", required=True)

if __name__ == "__main__":
    args = parser.parse_args()

    cwd = os.getcwd()
    file = os.path.join(cwd, args.file)
    with open(file, newline="") as billsfile:
        columns = next(billsfile).strip().split(",")
        data = []
        for line in map(str.strip, billsfile):
            row = {}
            b = line.strip().split(",")
            for idx, col in enumerate(columns):
                val = b[idx]
                if col == "Amount":
                    val = float(b[idx])
                if col == "Due Date":
                    val = int(b[idx])
                row[col] = val
            data.append(row)

    if now.day > args.day:
        now = now - timedelta(days = now.day - args.day)
    if now.day < args.day:
        now = now + timedelta(days = args.day - now.day)
    end = (now + timedelta(weeks = 2)).day - 1

    (bills, income, remainder) = get_totals(data, args.check, beginning_balance = args.balance, cycles = args.cycles, start_date = now, verbose = args.verbose)
    print(f"Total Income: ${income}")
    print(f"Total Bills: ${bills}")
    print(f"Remaining Balance: ${remainder}")
