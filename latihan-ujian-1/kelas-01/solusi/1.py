# Soal 1. Kasir Toko

# Konstanta
BIAYA_ADMIN = 2500

# Masukan
harga = int(input())
jumlah = int(input())
uang = int(input())

# Proses
total = harga * jumlah + BIAYA_ADMIN
kembalian = uang - total
cukup = uang >= total

# Keluaran
print("Total:", total)
print("Kembalian:", kembalian)
print("Cukup:", cukup)
