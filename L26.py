def jumlah(n):
    if  n <= 1:
        return n
    else:
        return n + jumlah(n-1)
    
def flip_text(t):
    if len(t) <=1:
        return t
    else:
        return t[-1] + flip_text(t[:-1])
    
def pangkat(a,b):
    if b == 0:
        return 1
    elif b < 0:
        return 1/pangkat(a, - b)
    else:
        return a * pangkat(a,b - 1)
    
def faktorial(n):
    if n <= 1: return 1
    return n * faktorial(n-1)

def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

while True:
    print("\n 1.faktorial \n 2.fibonacci \n 3.pangkat \n 4.flip text \n 5.jumlah \n 6.keluar")
    pp = input("pilih: ")
    if pp == "6": break
    n = int(input("n: "))
    if pp == "1": print("Hasil:", faktorial(n))
    elif pp == "2": print("Hasil:", fib(n))
    elif pp == "3": print("hasil:", pangkat(n))
    elif pp == "4": print("hasil:", flip_text(n))
    elif pp == "5": print("hasil:", jumlah(n))
    elif pp == "6": 
        print("hasil") 
        break
    else:
        print("try again")