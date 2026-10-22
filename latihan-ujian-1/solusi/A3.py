# A3. Diskon Member
kode = input().upper()
belanja = int(input())
match kode:
    case "S":
        nama, persen = "Silver", 5
    case "G":
        nama, persen = "Gold", 10
    case "P":
        nama, persen = "Platinum", 15
    case _:
        nama, persen = None, 0
if nama is None:
    print("Kode member tidak dikenal")
else:
    diskon = belanja * persen // 100
    print("Member:", nama)
    print("Diskon:", diskon)
    print("Bayar:", belanja - diskon)
