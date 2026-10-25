# Business Constants
SHORT_STAY = 4
LONG_STAY = 14
MINIMUM_DISCOUNT = 0.06
MAXIMUM_DISCOUNT = 0.18
NO_DISCOUNT = 0
CLEANING_FEE = 40.00
CLEANING_FEE_MAX = 300.00
CREDIT_CHECK_MAX = 2000.00
WELCOME_PACKAGE_NIGHTS = 5
WELCOME_PACKAGE_LIMIT = 1000.00
FULL_RATE = 1.0
INITIAL_TOTAL = 0.0


def calculate_room_cost(nightly_rate: float, nights: int) -> float:
    """Calculate room cost before discount."""
    return nightly_rate * nights

def get_stay_discount(nights: int, corporate: bool = False) -> float:
    """Returns discount rate for stay."""
    if nights >= LONG_STAY:
        return MAXIMUM_DISCOUNT
    if nights >= SHORT_STAY or corporate:
         return MINIMUM_DISCOUNT
    return NO_DISCOUNT

def calculate_stay_total(nightly_rate: float, nights: int, corporate: bool = False) -> float:
    """Calculate discounted stay total."""
    room_cost = calculate_room_cost(nightly_rate, nights)
    discount = get_stay_discount(nights, corporate)
    discounted_cost = room_cost * (FULL_RATE - discount)
    if discounted_cost <= CLEANING_FEE_MAX:
        return discounted_cost + CLEANING_FEE
    return discounted_cost

def requires_credit_check(total: float) -> bool:
    """Determines if there needs to be a credit check."""
    return total >= CREDIT_CHECK_MAX


def gets_welcome_package(nights: int, total: float) -> bool:
    """Calculates if you get the welcome package."""
    return nights > WELCOME_PACKAGE_NIGHTS and total >= WELCOME_PACKAGE_LIMIT

def total_reserved(stays: list) -> float:
    """Calculates combined total of stay."""
    total = 0.0
    for stay in stays:
        total += calculate_stay_total(stay['nightly_rate'], stay['nights'], stay['corprate'])
        return total

def largest_stay(stays: list) -> str:
    """Gives the guest name for the largest total."""
    largest_guest = ""
    largest_total = 0.0
    first_stay = True
    stay_total = calculate_stay_total(stay['nightly_rate'], stay['nights'], stay['corprate'])
    if stay_total or first_stay > largest_total:
        largest_guest = stay["guest"]
        largest_total = stay_total
        first_stay = False

def format_stay_line(guest: str, total: float, credit_check: bool, welcome_package: bool) -> str:
    """Format one stay as a report line."""
    credit_status = "yes" if credit_check else "no"
    package_status = "yes" if welcome_package else "no"
    return (f"{guest}: ${total:.2f}| credit check: {credit_status}"
            f"| welcome package: {package_staus}")