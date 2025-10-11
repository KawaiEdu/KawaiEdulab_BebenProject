import sys
import time
from functools import lru_cache

def menu():
    print("\n=== PROGRAM UHHH NACHO....SOMETHING PYTHON ===")
    print("1. rekursif normal (fibonachi)")
    print("2. deep recursion (nested list sum)")
    print("3. memoization (fibonacci opotimized)")
    print("4. keluar")
    choice = input("pilih opsi (1-4): ")
    return choice

def fibonachi_recursive(n):
    if n <= 1:
        return n
    return fibonachi_recursive(n-1) + fibonachi_recursive(n-2)

def deep_sum(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += deep_sum(item)
        else:
            total += item
            return total

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n <=1:
        return n
    return fibonacci_memo(n-1) + fibonacci_memo(n-2)

def main():
    while True:
        choice = menu()
        if choice == '1':
            n = int(input("masukan nilai n untuk fibonacci: "))
            start = time.time()
            result = fibonachi_recursive(n)
            end = time.time()
            print(f"hasil: {result} (waktu: {end - start:.4f} detik)")
        elif choice == '2':
            nested = eval(input("masukan list bersarang contoh: [1,[2,[3,4]],5]: "))
            result = deep_sum(nested)
            print(f"total penjumlahan: {result}")
        elif choice == '3':
            n = int(input("masukan nilai n untuk fibonacco (memoization): "))
            start = time.time()
            result = fibonacci_memo(n)
            end = time.time()
            print(f"hasil: {result} (waktu: {end - start:4f} detik)")
        elif choice == '4':
            print("terima kasih program mati")
            sys.exit()
        else:
            print("pilihan tidak valid. silakan coba lagi.")

if __name__== "__main__":
    main()