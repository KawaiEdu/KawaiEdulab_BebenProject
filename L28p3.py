def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def is_even(n):
    return n % 2 == 0

assert faktorial(8) == 40320
assert faktorial(9) == 362880
assert faktorial(10) == 3628800
assert is_even(77) == False
assert is_even(20) == True
assert is_even(9) == False
print("berhasil?")