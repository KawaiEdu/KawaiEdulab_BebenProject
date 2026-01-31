import os

projekt_name ="SMART CANTEEN"
folders =[projekt_name] 
files = {
    f"{projekt_name}/main.py": "# main.py\n\nprint('Program siap dijalankan!')\n",
    f"{projekt_name}/utils.py": "# utils.py\n\n# Tambahkan fungsi rekursif, memo, visualisasi di sini\n",
    f"{projekt_name}/data_generator.py": "# data_generator.py\n\n# Tambahan fungsi deret aritmatika, acak, campuran\n",
    f"{projekt_name}/README.md": "# README\n\npenjelasan konsep rekurs, memoization, dan list comprehension untuk siswa SMA.\n"
    }

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)

print(f"struktur {projekt_name} berhasil dibuat!")