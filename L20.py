t = int(input("masukan tinggi piramida"))
for i in range(t):
    space = ' ' * (t-i-1)
    star = '*' * (2*i+1)
    print(space + star)