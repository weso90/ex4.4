operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

def get_number(number):
    while True:
        value = input(number)
        try:
            return float(value)
        except ValueError:
            print("Podana wartość nie jest liczbą!")

a = get_number("Podaj składnik 1. ")
b = get_number("Podaj składnik 2. ")

if operation == 1:
    c = a + b
    print(f"Dodaję {a} i {b}")
elif operation == 2:
    c = a - b
    print(f"Odejmuję {a} i {b}")
elif operation == 3:
    c = a * b
    print(f"Mnożę {a} i {b}")
elif operation == 4:
    c = a / b
    print(f"Dzielę {a} i {b}")
print(f"Wynik to: {c}")