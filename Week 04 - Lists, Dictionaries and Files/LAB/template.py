"""
RECORD CHECK  -  my version
===========================

Name  : mohammed khan
Lane  : cyber
Date  : 09/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def check_record(value, limit)
    "calculate the difference, percentage and status"
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return diffrence, percent, status



"""
RECORD CHECK - my version
=========================

Name  : [Your name]
Lane  : Cyber
Date  : 09/11/2026

Run it: python3 template.py
"""

# ======================== FUNCTIONS

def check_record(value, limit):
    """Calculate the difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the record check report."""
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Failed logins : {value:.2f}")
    print(f"  Total attempts: {limit:.2f}")
    print(f"  Difference    : {difference:.2f}")
    print(f"  Percentage    : {percent:.2f}%")
    print(f"  Status        : {status}")
    print("=" * 34)
    print()


# ======================== STORE

records = [
    {"label": "10.0.0.5", "value": 12.0, "limit": 400.0},
    {"label": "10.0.0.9", "value": 95.0, "limit": 100.0},
    {"label": "10.0.0.7", "value": 120.0, "limit": 100.0}
]


# ======================== PROCESS + OUTPUT

for record in records:
    difference, percent, status = check_record(
        record["value"],
        record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )



# =============================================================== PROCESS + OUTPUT