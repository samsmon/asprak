# B1. Konversi Durasi
DETIK_PER_JAM = 3600
DETIK_PER_MENIT = 60
total = int(input())
jam = total // DETIK_PER_JAM
sisa = total % DETIK_PER_JAM
menit = sisa // DETIK_PER_MENIT
detik = sisa % DETIK_PER_MENIT
print(jam, "jam", menit, "menit", detik, "detik")
print("Lebih dari 1 jam:", total > DETIK_PER_JAM)
