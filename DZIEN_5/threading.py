import threading

def print_cube(num):
    print(f'sześcian wartości {num} wynosi: {num**3}')

def print_square(num):
    print(f'kwadrat wartości {num} wynosi {num**2}')


t1 = threading.Thread(target=print_square,args=(10,))
t2 = threading.Thread(target=print_cube,args=(20000,))

t1.start()
t2.start()

t1.join()
t2.join()
print("wszystko zrobione!")
