import functools
import math as m
import random as r
import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fibocci_recursive(n):
    if n <= 1:
        return n
    return fibocci_recursive(n-1) + fibocci_recursive(n-2)

@functools.lru_cache(maxsize=None)
def fibonaci_memo(n):
    if n <=1:
        return n
    return fibonaci_memo(n-1) + fibonaci_memo(n-2)

def generate_fibonacci_series(n, use_memo=True):
    series = []
    for i in range(n):
        val = fibonaci_memo(i) if use_memo else fibocci_recursive(i)
        series.append(val)
    return series
 
def normalize_series(series):
    arr = np.array(series)
    return (arr - arr.min()) / (arr.max() - arr.min())

def plot_series(series, title="fibonacci series"):
  plt.figure(figsize=(10, 4))
  plt.plot(series, marker='o')
  plt.title(title)
  plt.xlabel("index")
  plt.ylabel("value")
  plt.grid(True)
  plt.show()

def save_series_to_json(series, filename="series.json"):
    with open(filename, "w") as f:
        json.dump(series, f)

def load_series_from_json(filename="series.json"):
    with open(filename, "r") as f:
        return json.load(f)