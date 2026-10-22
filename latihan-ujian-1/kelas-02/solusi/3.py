# Soal 3. Tiket Bioskop

# Masukan
kode = input().upper()
tiket = int(input())

# Tentukan nama studio dan harga dari kode
match kode:
    case "R":
        studio = "Reguler"
        harga = 40000
    case "D":
        studio = "Deluxe"
        harga = 60000
    case "I":
        studio = "IMAX"
        harga = 90000
    case _:
        studio = None
        harga = 0

# Validasi lalu hitung total
if studio is None:
    print("Kode studio tidak dikenal")
elif tiket < 1:
    print("Jumlah tiket tidak valid")
else:
    total = harga * tiket

    # Diskon 10% untuk 4 tiket atau lebih
    if tiket >= 4:
        total -= total * 10 // 100

    print("Studio:", studio)
    print("Total:", total)
