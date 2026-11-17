"""Console program for an illustrative slab-based electricity bill.

Lab example tariff (not an official utility tariff):
first 100 units = Rs. 2/unit
next 100 units = Rs. 3/unit
above 200 units = Rs. 5/unit
"""

def calculate_bill(units):
    if units < 0:
        raise ValueError("Units cannot be negative")
    if units <= 100:
        return units * 2
    if units <= 200:
        return 100 * 2 + (units - 100) * 3
    return 100 * 2 + 100 * 3 + (units - 200) * 5


def main():
    try:
        units = int(input("Enter electricity units consumed: "))
        bill = calculate_bill(units)
        print("Electricity Units:", units)
        print("Total Electricity Bill: Rs.", bill)
    except ValueError as exc:
        print("Invalid input:", exc)


if __name__ == "__main__":
    main()
