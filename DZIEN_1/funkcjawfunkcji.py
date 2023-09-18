# przykład 1

def witaj(imie):
    return f"Miło Cię widzieć {imie}!"


def konkurs(imie, punkty, laureat):
    return f"uczestnik konkursu: {imie}, liczba punktów {punkty}, czy jest laureatem? ({laureat})"


def osoba(funkcja, *args):
    return funkcja(*args)


print(osoba(witaj, "Leon"))
print(osoba(konkurs, "Olga", 77, "tak"))


# przykład 2

def rejestracja(oplata):
    def lista():
        return "jesteś na liście zawodników"

    def brak():
        return "dokonaj wpłaty w terminie 3 dni!"

    def error():
        return "wpłata - 1, brak - 0, błąd - inna wartość"

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)())
print(rejestracja(22)())
print(rejestracja(0)())

#przykład 3
def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu...")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper


def zawijanie(czego):
    print(f'zawijanie {czego} w sreberka....')

zw = startstop(zawijanie)

zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f'dmuchanie {czego} na torcie urodzinowym...')

dmuchanie("świeczek")
