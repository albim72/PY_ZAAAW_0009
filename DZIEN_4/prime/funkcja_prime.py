import time

def znajdz_sume_liczb_pierwszych(minimum,maksimum):
    total = 0
    st = time.perf_counter()
    for number in range(minimum,maksimum):
        count=0
        for i in range(2,number//2+1):
            if number%i==0:
                count=count+1
                break
        if count == 0 and number != 1:
            total = total + number
            
    k = time.perf_counter()
    print(f'czas wykonania modułu: {k-st} s')
    return total

