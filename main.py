operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

def get_number(number):
    while True:
        value = input(number)
        try:
            return float(value)
        except ValueError:
            print("Podana wartość nie jest liczbą!")

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
            print("Podana wartość nie jest liczbą!")
    return numbers

if operation == 1:
    summing = get_numbers()
    c = sum(summing)
    print(f"Dodaję liczby {summing}")
    
elif operation == 2:
    a = get_number("Podaj składnik 1. ")
    b = get_number("Podaj składnik 2. ")
    c = a - b
    print(f"Odejmuję {a} i {b}")

elif operation == 3:
    multipling = get_numbers()
    c = 1
    for i in multipling:
        c*= i
    print(f"Mnożę liczby {multipling}")

elif operation == 4:
    a = get_number("Podaj składnik 1. ")
    b = get_number("Podaj składnik 2. ")
    c = a / b
    print(f"Dzielę {a} i {b}")

print(f"Wynik to: {c}")