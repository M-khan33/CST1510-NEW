"""
RECORD CHECK  -  my version
===========================

Name  : mohammed khan
Lane  :  cyber
Date  :

Run it:   python template.py


class Record:
    """Store information about a security record."""

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit


r1 = Record("10.0.0.5", 12.0, 400.0)
r2 = Record("10.0.0.9", 95.0, 100.0)

records = [r1, r2]

for r in records:
    print("=" * 34)
    print("RECORD CHECK -", r.label)
    print("=" * 34)
    print("Failed logins:", r.value)
    print("Total attempts:", r.limit)
    print("=" * 34)

# Check that the objects are independent
r1.value = 20.0
print("Updated first record:", r1.value)
print("Second record:", r2.value)




records = []   # replace with your code



for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here

    print("=" * 34)


