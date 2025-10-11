print("program BMI")
BMI = float(input("masukan angka: "))
if BMI < 18.5:
  print("under weight")
elif BMI<= 24.9:
  print("normal weight")
elif BMI<= 29.9:
  print("over weight")
else:
  print("obesitas")