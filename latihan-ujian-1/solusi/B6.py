# B6. Penilaian Lomba
kategori = input()
match kategori:
    case "1":
        skor = int(input())
        if skor < 0 or skor > 100:
            print("Skor tidak valid")
        elif skor >= 90:
            print("Juara")
        elif skor >= 75:
            print("Finalis")
        else:
            print("Peserta")
    case "2":
        anggota = int(input())
        if anggota < 3 or anggota > 5:
            print("Jumlah anggota harus 3 sampai 5")
        else:
            skor = int(input())
            if skor < 0 or skor > 100:
                print("Skor tidak valid")
            elif skor >= 85:
                if anggota == 5:
                    print("Juara (bonus anggota lengkap)")
                else:
                    print("Juara")
            elif skor >= 70:
                print("Finalis")
            else:
                print("Peserta")
    case _:
        print("Kategori tidak dikenal")
