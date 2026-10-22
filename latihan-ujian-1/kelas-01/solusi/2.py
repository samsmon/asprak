# Soal 2. Kelulusan Ujian

# Masukan
uts = int(input())
uas = int(input())

# Proses
rata = (uts + uas) / 2

# Keluaran
print(f"Rata-rata: {rata:.1f}")

if rata >= 60:
    print("Status: LULUS")
else:
    print("Status: TIDAK LULUS")
