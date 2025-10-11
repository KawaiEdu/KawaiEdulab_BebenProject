print ("Program payung hujan")
rain = float(input("berapa skala intensitas hujan: "))
if rain > 0 and rain < 2.5:
  print("hujan grimis")
elif rain > 2.6 and rain < 7.5:
  print("hujan sedang")
else:
  print("hujan lebat")