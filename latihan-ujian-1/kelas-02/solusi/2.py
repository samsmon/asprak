# Soal 2. Cek Suhu Tubuh

# Masukan
suhu = float(input())

# Keluaran berdasarkan rentang suhu
if suhu < 36.0:
    print("Suhu rendah")
elif suhu < 37.5:
    print("Suhu normal")
else:
    print("Demam")
