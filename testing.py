from datetime import date

def calculate_age(birth_year: int) -> int:
    current_year = date.today().year
    if birth_year > current_year:
        raise ValueError("Tug'ilgan yil hozirgi yildan katta bo'lishi mumkin emas")
    return current_year - birth_year


def add(x, y):
    return x + y
