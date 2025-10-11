def valid_int(s):
    try: return int(s)
    except: return None

def kali(k, kk):
    if kk == 0:
        return 0
    return k + kali(k, kk-1)

def max3(m3, mm3, mmm3):
    if m3>= mm3 and m3>= mmm3:
        return m3
    return max3(mm3, mmm3, m3)

