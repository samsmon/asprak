# Soal 3. Diskon Member

# Masukan
kode = input().upper()
belanja = int(input())

# Tentukan nama member dan persen diskon dari kode
match kode:
    case "S":
        nama = "Silver"
        persen = 5
    case "G":
        nama = "Gold"
        persen = 10
    case "P":
        nama = "Platinum"
        persen = 15
    case _:
        nama = None
        persen = 0

# Hitung dan cetak
if nama is None:
    print("Kode member tidak dikenal")
else:
    diskon = belanja * persen // 100
    bayar = belanja - diskon

    print("Member:", nama)
    print("Diskon:", diskon)
    print("Bayar:", bayar)
