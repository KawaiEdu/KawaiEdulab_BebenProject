# data_generator.py

# Tambahan fungsi deret aritmatika, acak, campuran
import random

def generate_aritmetic_series(n, start=0, step=2):
    return [start + i * step for i in range(n)]

def generate_random_series(n, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(n)]

def generate_mixed_series(n):
    fib = generate_aritmetic_series(n, start=1, step=2)
    rand = generate_random_series(n, 10, 50)
    return [(f + r) // 2 for f,r in zip(fib, rand)]