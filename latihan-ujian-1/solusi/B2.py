# B2. Cek Suhu Tubuh
suhu = float(input())
if suhu < 36.0:
    print("Suhu rendah")
elif suhu < 37.5:
    print("Suhu normal")
else:
    print("Demam")
