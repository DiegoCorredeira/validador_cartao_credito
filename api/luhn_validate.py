def luhn(card_number):
    card_number = card_number.replace(' ', '').replace('-', '')

    if not card_number.isdigit() or len(card_number) < 16:
        return False

    digitos_card = list(map(int, card_number[::-1]))
    digitos_dob = [x * 2 if i % 2 == 1 else x for i, x in enumerate(digitos_card)]
    digitos_sub = [x - 9 if x > 9 else x for x in digitos_dob]
    total = sum(digitos_sub)

    return total % 10 == 0


def validador(card_number, expiration_date, cvv):
    if not luhn(card_number):
        return False

    expiration_date = expiration_date.split('/')
    if len(expiration_date) == 2:
        try:
            month, year = map(int, expiration_date)
            if 1 <= month <= 12 and 0 <= year <= 99:
                return True
        except ValueError:
            pass

    return False
