def rupiah(n: int) -> str:
    try:
        return "Rp{:,.0f}".format(int(n)).replace(",", ".")
    except Exception:
        return "Rp0"

def safe_int(text, default=0):
    try: return int(str(text).strip())
    except: return default