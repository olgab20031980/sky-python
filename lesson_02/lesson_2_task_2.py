year = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]


def is_year_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False


for year in year:
    if is_year_leap(year):
        print(f"год {year} - True")
    else:
        print(f"год {year} - False")
