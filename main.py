import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

def get_number(number):
    while True:
        value = input(number)
        try:
            return float(value)
        except ValueError:
            logging.info("Podana wartość nie jest liczbą!")

def get_numbers():
    numbers = []

    while True:
        value = input("Podaj liczbę, aby zakończyć podawanie liczb i wykonać działanie wpisz 'end': ")
        if value.lower() == 'end':
            break
        try:
            number = float(value)
            numbers.append(number)
        except ValueError:
            logging.info("Podana wartość nie jest liczbą!")
    return numbers

if operation == 1:
    summing = get_numbers()
    c = sum(summing)
    logging.info(f"Dodaję liczby {summing}")
    
elif operation == 2:
    a = get_number("Podaj składnik 1. ")
    b = get_number("Podaj składnik 2. ")
    c = a - b
    logging.info(f"Odejmuję {a} i {b}")

elif operation == 3:
    multipling = get_numbers()
    c = 1
    for i in multipling:
        c*= i
    logging.info(f"Mnożę liczby {multipling}")

elif operation == 4:
    a = get_number("Podaj składnik 1. ")
    b = get_number("Podaj składnik 2. ")
    c = a / b
    logging.info(f"Dzielę {a} i {b}")

logging.info(f"Wynik to: {c}")