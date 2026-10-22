# A1. Kasir Toko
BIAYA_ADMIN = 2500
harga = int(input())
jumlah = int(input())
uang = int(input())
total = harga * jumlah + BIAYA_ADMIN
kembalian = uang - total
print("Total:", total)
print("Kembalian:", kembalian)
print("Cukup:", uang >= total)
