class MojaKlasaBledu(Exception):
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("wywołanie funkcji komunikatu błędu....")
        if self.message:
            return f'{self.__class__.__name__} została wykonana -> {self.message}'
        else:
            return f'{self.__class__.__name__} -> brak komunikatu'


n = input("podaj literę alfabetu: ")
try:
    if n == "a":
        raise MojaKlasaBledu("jest problem .... a jest niedostępne!")
    else:
        print("wyszytko Ok!")
except MojaKlasaBledu as mkb:
    print(mkb)
