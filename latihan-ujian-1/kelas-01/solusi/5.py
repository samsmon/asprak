# Soal 5. Seleksi Beasiswa

# Masukan
ipk = float(input())
gaji = int(input())
organisasi = input()

if ipk < 3.0:
    hasil = "Tidak memenuhi syarat IPK"

elif ipk >= 3.5:
    # IPK tinggi: cukup lihat penghasilan
    if gaji <= 3000000:
        hasil = "Beasiswa Penuh"
    elif gaji <= 6000000:
        hasil = "Beasiswa 50%"
    else:
        hasil = "Tidak memenuhi syarat penghasilan"

else:
    # IPK 3.0 sampai kurang dari 3.5: wajib aktif organisasi
    if organisasi == "y":
        if gaji <= 3000000:
            hasil = "Beasiswa 50%"
        elif gaji <= 6000000:
            hasil = "Beasiswa 25%"
        else:
            hasil = "Tidak memenuhi syarat penghasilan"
    else:
        hasil = "Syarat organisasi tidak terpenuhi"

# Keluaran
print(hasil)
