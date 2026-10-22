# Soal 4. Tiket Wahana

# Masukan
umur = int(input())
akhir_pekan = input()

if umur < 0:
    print("Umur tidak valid")
else:
    # Tarif dasar berdasarkan umur
    if umur < 5:
        tarif = 0
    elif umur <= 12:
        tarif = 20000
    elif umur < 60:
        tarif = 40000
    else:
        tarif = 15000

    # Tambahan akhir pekan, hanya untuk yang berbayar
    if tarif > 0 and akhir_pekan == "y":
        tarif += 10000

    print("Tarif:", tarif)
