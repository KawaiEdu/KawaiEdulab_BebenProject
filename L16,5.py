hero_MLBB1 = {"valir", "vale","wu zetian", "obsidia", "aqil"}
hero_MLBB2 = {"gusion", "aamon", "wu zetian", "obsidia", "lylia"}

ok = hero_MLBB1.union(hero_MLBB2)
ko = hero_MLBB1.difference(hero_MLBB2)
k = hero_MLBB1.symmetric_difference(hero_MLBB2)
o = hero_MLBB1.intersection(hero_MLBB2)

print("hero yang sama adalah ", o )
print("hero yang berbeda adalah ", ko )
print("semua hero adalah ", ok )
print("hero yang sendiri " , k )
