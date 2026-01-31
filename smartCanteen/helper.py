import os, platform

APP_NAME = "SMART CANTEEN"

def cls():
    os.system("cls" if platform.system()=="Windows" else "clear")
    
def banner():
    print("="*36)
    print(f"{APP_NAME:^36}")
    print("="*36)

def confirm(msg="Yakin? (Y/N): "):
    ans = input(msg).strip().lower()
    return ans in ("y","ya","yes")