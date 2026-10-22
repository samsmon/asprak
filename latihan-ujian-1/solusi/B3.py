# B3. Tiket Bioskop
kode = input().upper()
tiket = int(input())
match kode:
    case "R":
        studio, harga = "Reguler", 40000
    case "D":
        studio, harga = "Deluxe", 60000
    case "I":
        studio, harga = "IMAX", 90000
    case _:
        studio, harga = None, 0
if studio is None:
    print("Kode studio tidak dikenal")
elif tiket < 1:
    print("Jumlah tiket tidak valid")
else:
    total = harga * tiket
    if tiket >= 4:
        total -= total * 10 // 100
    print("Studio:", studio)
    print("Total:", total)
