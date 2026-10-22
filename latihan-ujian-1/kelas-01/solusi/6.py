# Soal 6. Simulasi ATM

# Masukan awal
pin = input()
saldo = int(input())
menu = input()

if pin == "1234":
    match menu:
        case "1":
            # Cek saldo
            print("Saldo:", saldo)

        case "2":
            # Tarik tunai
            jumlah = int(input())

            if jumlah <= 0 or jumlah % 50000 != 0:
                print("Jumlah harus kelipatan 50000")
            elif jumlah > saldo:
                print("Saldo tidak cukup")
            else:
                saldo -= jumlah
                print("Sisa saldo:", saldo)

        case "3":
            # Setor tunai
            jumlah = int(input())

            if jumlah <= 0:
                print("Jumlah tidak valid")
            else:
                saldo += jumlah
                print("Saldo baru:", saldo)

        case _:
            print("Menu tidak tersedia")
else:
    print("PIN salah")
