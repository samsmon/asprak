# Soal 1. Konversi Durasi

# Konstanta
DETIK_PER_JAM = 3600
DETIK_PER_MENIT = 60

# Masukan
total = int(input())

# Proses
jam = total // DETIK_PER_JAM
sisa = total % DETIK_PER_JAM
menit = sisa // DETIK_PER_MENIT
detik = sisa % DETIK_PER_MENIT
lebih_satu_jam = total > DETIK_PER_JAM

# Keluaran
print(jam, "jam", menit, "menit", detik, "detik")
print("Lebih dari 1 jam:", lebih_satu_jam)
