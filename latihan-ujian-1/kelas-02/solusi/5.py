# Soal 5. Ongkos Kirim Paket

# Masukan
berat = int(input())
tujuan = input().upper()
ekspres = input()

if berat <= 0 or berat > 30:
    print("Berat tidak valid")
else:
    if tujuan == "L" or tujuan == "N":
        # Lokal dan nasional: tarif per kg, ekspres tambah 20%
        if tujuan == "L":
            total = berat * 8000
        else:
            total = berat * 15000

        if ekspres == "y":
            total += total * 20 // 100

        print("Ongkir:", total)

    elif tujuan == "I":
        # Internasional: maksimal 10 kg, tanpa ekspres
        if berat > 10:
            print("Berat melebihi batas internasional")
        elif ekspres == "y":
            print("Ekspres tidak tersedia untuk internasional")
        else:
            print("Ongkir:", berat * 50000)

    else:
        print("Tujuan tidak dikenal")
