from business_rules import(calculate_room_cost, get_stay_discount, calculate_stay_total, requires_credit_check, gets_welcome_package, total_reserved, largest_stay, format_stay_line)

def test_calculate_room_cost():
    assert calculate_room_cost(100,3) == 300

def test_calculate_room_cost_zero_nights():
    assert calculate_room_cost(100,0) == 0

def test_get_stay_discount_at_four_nights():
    assert get_stay_discount(4) == 0.06

def test_get_stay_discount_under_four_nights():
    assert get_stay_discount(2) == 0

def test_get_stay_discount_at_thirteen_nights():
    assert get_stay_discount(13) == 0.06

def test_get_stay_discount_at_fourteen_nights():
    assert get_stay_discount(14) == 0.18

def test_get_stay_discount_corporate_changes_answer():
    assert get_stay_discount(2,True) != get_stay_discount(2,False)

def test_calculate_stay_total_cleaning_fee():
    assert round(calculate_stay_total(100,2),2) == 240.00

def test_calculate_stay_total_cleaning_limit():
    assert round(calculate_stay_total(300,1),2) == 340.00

def test_calculate_stay_total_above_cleaning_limit():
    assert round(calculate_stay_total(301, 1), 2) == 301.00

def test_calculate_stay_discount_four_nights():
    assert round(calculate_stay_total(100,4),2) == 376.00

def test_calculate_stay_discount_fourteen_nights():
    assert round(calculate_stay_total(100,14),2) == 1148.00

def test_calculate_stay_large_total():
    assert round(calculate_stay_total(200,14),2) == 2296.00

def test_requires_credit_check_above_limit():
    assert requires_credit_check(2000.01) is True

def test_requires_credit_check_at_limit():
    assert requires_credit_check(2000) is True

def test_requires_credit_check_below_limit():
    assert requires_credit_check(1999.99) is False

def test_welcome_package_met():
    assert gets_welcome_package(6,1000) is True

def test_welcome_package_five_nights():
    assert gets_welcome_package(5,1000) is False

def test_welcome_package_below_limit():
    assert gets_welcome_package(6,999) is False

def test_welcome_package_not_met():
    assert gets_welcome_package(4,700) is False

def test_total_reserved_two_stays():
    stays = [
        {"guest": "Kessler", "nightly_rate": 100, "nights": 2, "corporate": False},
        {"guest": "Moreno", "nightly_rate": 125, "nights": 6, "corporate": False},
    ]
    assert round(total_reserved(stays),2) == 945.00

def test_largest_stay_tie_returns_first_guest():
    stays = [
        {"guest": "Kessler", "nightly_rate": 100, "nights": 2, "corporate": False},
        {"guest": "Moreno", "nightly_rate": 100, "nights": 2, "corporate": False},
    ]
    assert largest_stay(stays) == "Kessler"

def test_largest_stay_returns_largest_guest():
    stays = [
        {"guest": "Kessler", "nightly_rate": 100, "nights": 2, "corporate": False},
        {"guest": "Moreno", "nightly_rate": 200, "nights": 14, "corporate": False},
    ]
    assert largest_stay(stays) == "Moreno"

def test_largest_stay_empty_list():
    assert largest_stay([]) == ""

def test_format_stay_line():
    result = format_stay_line("Kessler", 260, False, False)
    assert result == "Kessler: $260.00| credit check: no| welcome package: no"

def test_format_stay_line_formats_money():
    result = format_stay_line("Rahman", 2444, True, True)
    assert "$2444.00" in result