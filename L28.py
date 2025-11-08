def bagi(a, b):
    print("DEBUG:", a,b)
    return a / b

print(bagi(10, 2))

def akar(X):
    assert X >= 0, "X harus >= 0"
    return X ** 0.5

print(akar(9))
print(akar(-1))