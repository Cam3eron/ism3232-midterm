from business_rules import (calculate_stay_total, requires_credit_check, gets_welcome_package, total_reserved, largest_stay, format_stay_line)

stays = [
    {"guest": "Kessler", "nightly_rate": 110.00, "nights": 2, "corporate": False},
    {"guest": "Lindqvist", "nightly_rate": 150.00, "nights": 2, "corporate": True},
    {"guest": "Moreno", "nightly_rate": 125.00, "nights": 6, "corporate": False},
    {"guest": "Nakata", "nightly_rate": 140.00, "nights": 20, "corporate": False},
    {"guest": "Osei", "nightly_rate": 95.00, "nights": 15, "corporate": True},
    {"guest": "Petrov", "nightly_rate": 200.00, "nights": 5, "corporate": False},
    {"guest": "Quinn", "nightly_rate": 180.00, "nights": 6, "corporate": False},
    {"guest": "Rahman", "nightly_rate": 260.00, "nights": 10, "corporate": True},
]

print("Seabreeze Inn - Stay Report")

credit_checks = 0
welcome_packages = 0

for stay in stays:
    stay_total = calculate_stay_total(
        stay["nightly_rate"], stay["nights"], stay["corporate"]
    )
    credit_check = requires_credit_check(stay_total)
    welcome_package = gets_welcome_package(stay["nights"], stay_total)

    print(
        format_stay_line(
            stay["guest"], stay_total, credit_check, welcome_package
        )
    )

    if credit_check:
        credit_checks += 1

    if welcome_package:
        welcome_packages += 1

total = total_reserved(stays)
average = total / len(stays)
largest = largest_stay(stays)

print(f"Stays:{len(stays)}")
print(f"Total reserved: ${total:.2f}")
print(f"Average stay total: ${average:.2f}")
print(f"Largest stay total: {largest}")
print(f"Credit Checks required: {credit_checks}")
print(f"Welcome packages: {welcome_packages}")