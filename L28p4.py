def rata(lst):
    assert isinstance(lst, list), "harus list"
    if not lst:
        return 0
    total = 0
    for x  in lst:
        if not isinstance(x,(int,float)):
            print("[WARN abaikan:]", x); continue
        total += x
        return total/len(lst) if lst else 0
    assert rata([10,20,30]) == 20
print("[INFO] rata valid")