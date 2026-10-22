# Latihan Ujian 1 Algoritma Pemrograman, Berkas Assessor Kelas 01

Berkas ini khusus asisten dan dosen. Soal untuk mahasiswa ada di [soal.md](soal.md). Ringkasan dan tautan cepat ke kode ada di [INDEKS.md](INDEKS.md).

## Cara menilai

1. Jalankan program peserta dengan setiap test case di tabel soal, lalu bandingkan keluarannya dengan kolom Keluaran. Spasi dan huruf besar kecil dihitung.
2. Isi poin tiap kriteria di rubrik, total 100 per soal. Kriteria struktur (match-case, bersarang, konstanta) dinilai dari kode, bukan dari keluaran.
3. Keluaran benar semua tetapi struktur tidak sesuai perintah soal (misalnya tidak memakai `match-case`): kriteria struktur dapat 0, kriteria lain tetap dihitung.
4. Program error saat dijalankan: skor soal paling tinggi 40, dihitung dari kriteria yang terbukti dari kode.
5. Cara lain yang benar dan sesuai perintah soal tetap mendapat poin penuh.
6. Soal yang kosong bernilai 0 tanpa pengurangan.

## Poin per soal dan nilai akhir

Skor rubrik (0 sampai 100) diubah ke poin soal dengan rumus: poin soal = skor rubrik / 100 x bobot tingkat.

| Tingkat | Soal | Bobot |
|---|---|---|
| Mudah | 1, 2 | 15 |
| Sedang | 3, 4 | 30 |
| Susah | 5, 6 | 40 |

Soal dihitung selesai bila skor rubriknya minimal 70. Misalkan P adalah jumlah poin semua soal.

1. Jumlah soal selesai 3 atau lebih: nilai akhir = min(100, max(P, 75)). Nilai aman (75 ke atas) terjamin.
2. Jumlah soal selesai 2 atau kurang: nilai akhir = min(P, 74).
3. Bobot tingkat tetap menentukan nilai di antara batas itu: soal Susah menyumbang poin paling besar.

Contoh dengan soal selesai dan benar penuh:

| Soal selesai | P | Nilai akhir |
|---|---|---|
| 1 Susah | 40 | 40 |
| 2 Mudah | 30 | 30 |
| Mudah + Sedang | 45 | 45 |
| Mudah + Susah | 55 | 55 |
| 2 Sedang | 60 | 60 |
| Sedang + Susah | 70 | 70 |
| 2 Susah | 80 | 74 (batas dua soal) |
| 2 Mudah + Sedang | 60 | 75 (batas bawah tiga soal) |
| 2 Mudah + Susah | 70 | 75 (batas bawah tiga soal) |
| Mudah + 2 Sedang | 75 | 75 |
| Mudah + Sedang + Susah | 85 | 85 |
| Mudah + 2 Susah | 95 | 95 |
| 2 Sedang + Susah | 100 | 100 |
| Sedang + 2 Susah | 110 | 100 |

Soal yang hanya benar sebagian (skor di bawah 70) tidak dihitung selesai, tetapi poinnya tetap ikut dijumlahkan ke P.

## Indeks nilai

| Nilai | Indeks | Keterangan |
|---|---|---|
| 85 - 100 | A | aman |
| 75 - 84 | B | aman |
| 60 - 74 | C | di bawah aman |
| 45 - 59 | D | di bawah aman |
| 0 - 44 | E | di bawah aman |

Batas indeks adalah usulan dan bisa disesuaikan dengan aturan dosen.

## Soal

| Soal | Tingkat | Bobot | Judul |
|---|---|---|---|
| 1 | Mudah | 15 | Kasir Toko |
| 2 | Mudah | 15 | Kelulusan Ujian |
| 3 | Sedang | 30 | Diskon Member |
| 4 | Sedang | 30 | Tiket Wahana |
| 5 | Susah | 40 | Seleksi Beasiswa |
| 6 | Susah | 40 | Simulasi ATM |

### Soal 1. Kasir Toko (Mudah, 15 poin)

Kode solusi:

```python
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
```

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| Input dibaca dan dikonversi ke int | 20 |
| Biaya admin memakai konstanta, bukan angka langsung di rumus | 20 |
| Rumus total dan kembalian benar | 30 |
| Ekspresi pembanding menghasilkan bool | 20 |
| Format keluaran sesuai | 10 |
| Total | 100 |

Poin soal = skor / 100 x 15.

Test case (baris masukan dipisah `/`):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 5000 / 3 / 20000 | Total: 17500 / Kembalian: 2500 / Cukup: True |
| 2 | 12000 / 2 / 20000 | Total: 26500 / Kembalian: -6500 / Cukup: False |
| 3 | 2500 / 4 / 12500 | Total: 12500 / Kembalian: 0 / Cukup: True |
| 4 | 1000 / 1 / 3500 | Total: 3500 / Kembalian: 0 / Cukup: True |

### Soal 2. Kelulusan Ujian (Mudah, 15 poin)

Kode solusi:

```python
# Masukan
uts = int(input())
uas = int(input())

# Proses
rata = (uts + uas) / 2

# Keluaran
print(f"Rata-rata: {rata:.1f}")

if rata >= 60:
    print("Status: LULUS")
else:
    print("Status: TIDAK LULUS")
```

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| Input dibaca dan dikonversi ke int | 20 |
| Rata-rata memakai pembagian / (hasil float) | 30 |
| if-else dengan batas >= 60 benar | 30 |
| Satu desimal dan teks keluaran sesuai | 20 |
| Total | 100 |

Poin soal = skor / 100 x 15.

Test case (baris masukan dipisah `/`):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 70 / 80 | Rata-rata: 75.0 / Status: LULUS |
| 2 | 50 / 65 | Rata-rata: 57.5 / Status: TIDAK LULUS |
| 3 | 60 / 60 | Rata-rata: 60.0 / Status: LULUS |
| 4 | 59 / 60 | Rata-rata: 59.5 / Status: TIDAK LULUS |

### Soal 3. Diskon Member (Sedang, 30 poin)

Kode solusi:

```python
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
```

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| Memakai match-case untuk kode member | 25 |
| Huruf kecil dan besar sama-sama diterima (.upper()) | 15 |
| case _ menangani kode tidak dikenal | 15 |
| Diskon dan bayar dihitung dengan bilangan bulat (//) | 30 |
| Format keluaran sesuai | 15 |
| Total | 100 |

Poin soal = skor / 100 x 30.

Test case (baris masukan dipisah `/`):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | g / 200000 | Member: Gold / Diskon: 20000 / Bayar: 180000 |
| 2 | S / 150000 | Member: Silver / Diskon: 7500 / Bayar: 142500 |
| 3 | P / 1000000 | Member: Platinum / Diskon: 150000 / Bayar: 850000 |
| 4 | X / 50000 | Kode member tidak dikenal |

### Soal 4. Tiket Wahana (Sedang, 30 poin)

Kode solusi:

```python
# Masukan
umur = int(input())
akhir_pekan = input()

if umur < 0:
    print("Umur tidak valid")
else:
    # Tarif dasar berdasarkan umur
    if umur < 5:
        tarif = 0
    elif umur <= 12:
        tarif = 20000
    elif umur < 60:
        tarif = 40000
    else:
        tarif = 15000

    # Tambahan akhir pekan, hanya untuk yang berbayar
    if tarif > 0 and akhir_pekan == "y":
        tarif += 10000

    print("Tarif:", tarif)
```

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| Rantai if-elif dengan batas umur 5, 12, 60 benar | 35 |
| Umur negatif ditangani | 15 |
| Kondisi gabungan (tarif > 0 and akhir pekan) benar, tiket gratis tetap gratis | 35 |
| Format keluaran sesuai | 15 |
| Total | 100 |

Poin soal = skor / 100 x 30.

Test case (baris masukan dipisah `/`):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 3 / y | Tarif: 0 |
| 2 | 10 / t | Tarif: 20000 |
| 3 | 25 / y | Tarif: 50000 |
| 4 | 60 / y | Tarif: 25000 |
| 5 | -1 / t | Umur tidak valid |
| 6 | 12 / t | Tarif: 20000 |

### Soal 5. Seleksi Beasiswa (Susah, 40 poin)

Kode solusi:

```python
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
```

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| Struktur bersarang sesuai alur (IPK dulu, lalu penghasilan atau organisasi) | 30 |
| Batas IPK 3.0 dan 3.5 tepat | 20 |
| Cabang organisasi pada IPK 3.0 sampai 3.4 benar | 15 |
| Batas penghasilan 3.000.000 dan 6.000.000 tepat | 15 |
| Setiap jalur mencetak tepat satu baris | 10 |
| Teks keluaran persis | 10 |
| Total | 100 |

Poin soal = skor / 100 x 40.

Test case (baris masukan dipisah `/`):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 3.8 / 2500000 / t | Beasiswa Penuh |
| 2 | 3.6 / 5000000 / y | Beasiswa 50% |
| 3 | 3.2 / 2000000 / y | Beasiswa 50% |
| 4 | 3.2 / 4000000 / t | Syarat organisasi tidak terpenuhi |
| 5 | 2.9 / 1000000 / y | Tidak memenuhi syarat IPK |
| 6 | 3.5 / 7000000 / y | Tidak memenuhi syarat penghasilan |
| 7 | 3.0 / 3000000 / y | Beasiswa 50% |
| 8 | 3.4 / 6000001 / y | Tidak memenuhi syarat penghasilan |

### Soal 6. Simulasi ATM (Susah, 40 poin)

Kode solusi:

```python
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
```

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| PIN dicek sebagai lapisan luar, menu tidak diproses bila PIN salah | 15 |
| match-case untuk menu, termasuk case _ | 20 |
| Validasi tarik: kelipatan 50000 (termasuk <= 0), lalu saldo cukup, urutan benar | 25 |
| Cabang setor benar | 10 |
| Jumlah hanya dibaca pada menu 2 dan 3 (tidak ada input berlebih) | 15 |
| Teks keluaran persis | 15 |
| Total | 100 |

Poin soal = skor / 100 x 40.

Test case (baris masukan dipisah `/`):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 1234 / 500000 / 1 | Saldo: 500000 |
| 2 | 1234 / 500000 / 2 / 150000 | Sisa saldo: 350000 |
| 3 | 1234 / 500000 / 2 / 120000 | Jumlah harus kelipatan 50000 |
| 4 | 1234 / 100000 / 2 / 150000 | Saldo tidak cukup |
| 5 | 1234 / 100000 / 3 / 75000 | Saldo baru: 175000 |
| 6 | 1234 / 100000 / 3 / 0 | Jumlah tidak valid |
| 7 | 9999 / 100000 / 1 | PIN salah |
| 8 | 1234 / 100000 / 9 | Menu tidak tersedia |
| 9 | 1234 / 100000 / 2 / 0 | Jumlah harus kelipatan 50000 |
