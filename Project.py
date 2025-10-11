from collections import defaultdict

# 1. menggunakan Tuple Sebagai Key Dictionary
student_score = {
    ("Aqil", "machine learning"): 90,
    ("Aqil", "web development"): 85,
    ("Danish", "Wordpress Development"): 90,
    ("Danish", "Python Developer"): 85,
    ("Dyandra", "Roblox Developer"): 90,
    ("Dyandra", "Unity Developer"): 85
}

# Menampilkan Nilai tiap siswa
def display_student_scores(scores):
    for (name, subject), score in scores.items():
        print(f"{name} - {subject}: {score}")

print("\n --- Student Scores --- ")
display_student_scores(student_score)

# 2. Dictionary bersarang (Nested Dictionary) Dengan Rekursi
nested_data = {
    "IDN": {
        "Jawa Timur": {"Surabaya": 10_000_000, "Malang": 8_000_000},
        "Jakarta": {"Houston": 2_300_000, "Bekasi": 1_300_000}
    },
    "MALAY": {
        "Kuala Lumpur": {"Durian Runtuh": 2_900_000, "Petaling Jaya": 1_300_000},
        "Johor": {"Johor Bahru": 1_500_000, "Kota Tinggi": 1_000_000}
    },
}

# Fungsi Rekursif untuk mencari Kota dalam Dictionary
def find_population(data, city):
    for country, states in data.items():
        for state, cities in states.items():
            if city in cities:
                return f"{city} Mempunyai Populasi Sekitar {cities[city]} in {state}, {country}"
    return f"{city} Tidak Ditemukan Di Data"

print("\n--- Searching for City Population ---")
print(find_population(nested_data, "Surabaya"))
print(find_population(nested_data, "Durian Runtuh"))
print(find_population(nested_data, "Johor Baru"))