# Latihan Ujian 1 Algoritma Pemrograman: Berkas Assessor

Berkas ini rahasia, jangan dibagikan ke peserta. Pasangannya: `2026-10-22-latihan-ujian-1-soal.md`.

## Cara menilai

1. Jalankan program peserta dengan setiap test case di tabel soal, bandingkan keluaran dengan kolom Keluaran (persis, spasi dan huruf besar kecil dihitung).
2. Isi poin per kriteria di rubrik. Kriteria struktur (match-case, nested, konstanta) dinilai dari kode, bukan dari keluaran.
3. Keluaran benar semua tetapi struktur tidak sesuai perintah soal (mis. tidak memakai `match-case`): poin kriteria struktur 0, kriteria lain tetap.
4. Program error saat dijalankan: nilai maksimal 40% dari bobot soal untuk kriteria yang terbukti dari kode.
5. Cara lain yang benar dan sesuai perintah soal tetap diberi poin penuh.

## Bobot dan indeks nilai

| Tingkat | Soal per kelas | Bobot per soal | Subtotal |
|---|---|---|---|
| Mudah | 2 | 10 | 20 |
| Sedang | 2 | 15 | 30 |
| Susah | 2 | 25 | 50 |
| Total | 6 | | 100 |

Indeks nilai akhir (usulan, sesuaikan dengan aturan dosen):

| Nilai | Indeks |
|---|---|
| 85 - 100 | A |
| 70 - 84 | B |
| 55 - 69 | C |
| 40 - 54 | D |
| 0 - 39 | E |

## Kelas A

| Soal | Tingkat | Bobot | Judul |
|---|---|---|---|
| A1 | Mudah | 10 | Kasir Toko |
| A2 | Mudah | 10 | Kelulusan Ujian |
| A3 | Sedang | 15 | Diskon Member |
| A4 | Sedang | 15 | Tiket Wahana |
| A5 | Susah | 25 | Seleksi Beasiswa |
| A6 | Susah | 25 | Simulasi ATM |

### A1. Kasir Toko (Mudah, 10 poin)

Kode solusi:

```python
BIAYA_ADMIN = 2500
harga = int(input())
jumlah = int(input())
uang = int(input())
total = harga * jumlah + BIAYA_ADMIN
kembalian = uang - total
print("Total:", total)
print("Kembalian:", kembalian)
print("Cukup:", uang >= total)
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| Input dibaca dan dikonversi ke int | 2 |
| Biaya admin memakai konstanta, bukan angka langsung di rumus | 2 |
| Rumus total dan kembalian benar | 3 |
| Ekspresi pembanding menghasilkan bool | 2 |
| Format output sesuai | 1 |
| Total | 10 |

Test case (masukan dipisah `/` per baris):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 5000 / 3 / 20000 | Total: 17500 / Kembalian: 2500 / Cukup: True |
| 2 | 12000 / 2 / 20000 | Total: 26500 / Kembalian: -6500 / Cukup: False |
| 3 | 2500 / 4 / 12500 | Total: 12500 / Kembalian: 0 / Cukup: True |
| 4 | 1000 / 1 / 3500 | Total: 3500 / Kembalian: 0 / Cukup: True |

### A2. Kelulusan Ujian (Mudah, 10 poin)

Kode solusi:

```python
uts = int(input())
uas = int(input())
rata = (uts + uas) / 2
print(f"Rata-rata: {rata:.1f}")
if rata >= 60:
    print("Status: LULUS")
else:
    print("Status: TIDAK LULUS")
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| Input dibaca dan dikonversi | 2 |
| Rata-rata memakai pembagian / (hasil float) | 3 |
| Kondisi if-else dengan batas >= 60 benar | 3 |
| Format 1 desimal dan teks output sesuai | 2 |
| Total | 10 |

Test case (masukan dipisah `/` per baris):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 70 / 80 | Rata-rata: 75.0 / Status: LULUS |
| 2 | 50 / 65 | Rata-rata: 57.5 / Status: TIDAK LULUS |
| 3 | 60 / 60 | Rata-rata: 60.0 / Status: LULUS |
| 4 | 59 / 60 | Rata-rata: 59.5 / Status: TIDAK LULUS |

### A3. Diskon Member (Sedang, 15 poin)

Kode solusi:

```python
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
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| Memakai match-case untuk kode member | 4 |
| Huruf kecil dan besar sama-sama diterima (.upper()) | 2 |
| case _ menangani kode tidak dikenal | 2 |
| Diskon dan bayar dihitung dengan bilangan bulat (//) | 4 |
| Format output sesuai | 3 |
| Total | 15 |

Test case (masukan dipisah `/` per baris):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | g / 200000 | Member: Gold / Diskon: 20000 / Bayar: 180000 |
| 2 | S / 150000 | Member: Silver / Diskon: 7500 / Bayar: 142500 |
| 3 | P / 1000000 | Member: Platinum / Diskon: 150000 / Bayar: 850000 |
| 4 | X / 50000 | Kode member tidak dikenal |

### A4. Tiket Wahana (Sedang, 15 poin)

Kode solusi:

```python
umur = int(input())
akhir_pekan = input()
if umur < 0:
    print("Umur tidak valid")
else:
    if umur < 5:
        tarif = 0
    elif umur <= 12:
        tarif = 20000
    elif umur < 60:
        tarif = 40000
    else:
        tarif = 15000
    if tarif > 0 and akhir_pekan == "y":
        tarif += 10000
    print("Tarif:", tarif)
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| Rantai if-elif dengan batas umur 5, 12, 60 benar | 5 |
| Umur negatif ditangani | 2 |
| Kondisi gabungan (tarif > 0 and akhir pekan) benar, gratis tetap gratis | 5 |
| Format output sesuai | 3 |
| Total | 15 |

Test case (masukan dipisah `/` per baris):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 3 / y | Tarif: 0 |
| 2 | 10 / t | Tarif: 20000 |
| 3 | 25 / y | Tarif: 50000 |
| 4 | 60 / y | Tarif: 25000 |
| 5 | -1 / t | Umur tidak valid |
| 6 | 12 / t | Tarif: 20000 |

### A5. Seleksi Beasiswa (Susah, 25 poin)

Kode solusi:

```python
ipk = float(input())
gaji = int(input())
organisasi = input()
if ipk < 3.0:
    hasil = "Tidak memenuhi syarat IPK"
elif ipk >= 3.5:
    if gaji <= 3000000:
        hasil = "Beasiswa Penuh"
    elif gaji <= 6000000:
        hasil = "Beasiswa 50%"
    else:
        hasil = "Tidak memenuhi syarat penghasilan"
else:
    if organisasi == "y":
        if gaji <= 3000000:
            hasil = "Beasiswa 50%"
        elif gaji <= 6000000:
            hasil = "Beasiswa 25%"
        else:
            hasil = "Tidak memenuhi syarat penghasilan"
    else:
        hasil = "Syarat organisasi tidak terpenuhi"
print(hasil)
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| Struktur bersarang sesuai alur (IPK dulu, lalu penghasilan atau organisasi) | 8 |
| Batas IPK 3.0 dan 3.5 tepat (inklusif/eksklusif benar) | 5 |
| Cabang organisasi pada IPK 3.0 sampai 3.4 benar | 4 |
| Batas penghasilan 3.000.000 dan 6.000.000 tepat | 4 |
| Setiap jalur mencetak tepat satu baris | 2 |
| Teks output persis | 2 |
| Total | 25 |

Test case (masukan dipisah `/` per baris):

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

### A6. Simulasi ATM (Susah, 25 poin)

Kode solusi:

```python
pin = input()
saldo = int(input())
menu = input()
if pin == "1234":
    match menu:
        case "1":
            print("Saldo:", saldo)
        case "2":
            jumlah = int(input())
            if jumlah <= 0 or jumlah % 50000 != 0:
                print("Jumlah harus kelipatan 50000")
            elif jumlah > saldo:
                print("Saldo tidak cukup")
            else:
                saldo -= jumlah
                print("Sisa saldo:", saldo)
        case "3":
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

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| PIN dicek sebagai lapisan luar, menu tidak diproses bila PIN salah | 4 |
| match-case untuk menu termasuk case _ | 5 |
| Validasi tarik: kelipatan 50000 (termasuk <= 0), lalu saldo cukup, urutan benar | 6 |
| Cabang setor benar | 3 |
| Jumlah hanya dibaca pada menu 2 dan 3 (tidak ada input berlebih) | 4 |
| Teks output persis | 3 |
| Total | 25 |

Test case (masukan dipisah `/` per baris):

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

## Kelas B

| Soal | Tingkat | Bobot | Judul |
|---|---|---|---|
| B1 | Mudah | 10 | Konversi Durasi |
| B2 | Mudah | 10 | Cek Suhu Tubuh |
| B3 | Sedang | 15 | Tiket Bioskop |
| B4 | Sedang | 15 | Jenis Segitiga |
| B5 | Susah | 25 | Ongkos Kirim Paket |
| B6 | Susah | 25 | Penilaian Lomba |

### B1. Konversi Durasi (Mudah, 10 poin)

Kode solusi:

```python
DETIK_PER_JAM = 3600
DETIK_PER_MENIT = 60
total = int(input())
jam = total // DETIK_PER_JAM
sisa = total % DETIK_PER_JAM
menit = sisa // DETIK_PER_MENIT
detik = sisa % DETIK_PER_MENIT
print(jam, "jam", menit, "menit", detik, "detik")
print("Lebih dari 1 jam:", total > DETIK_PER_JAM)
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| Konstanta dipakai, bukan angka langsung di rumus | 2 |
| Operator // dan % benar untuk jam, menit, detik | 4 |
| Ekspresi pembanding menghasilkan bool (tepat 3600 = False) | 2 |
| Format output sesuai | 2 |
| Total | 10 |

Test case (masukan dipisah `/` per baris):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 3725 | 1 jam 2 menit 5 detik / Lebih dari 1 jam: True |
| 2 | 59 | 0 jam 0 menit 59 detik / Lebih dari 1 jam: False |
| 3 | 3600 | 1 jam 0 menit 0 detik / Lebih dari 1 jam: False |
| 4 | 7384 | 2 jam 3 menit 4 detik / Lebih dari 1 jam: True |

### B2. Cek Suhu Tubuh (Mudah, 10 poin)

Kode solusi:

```python
suhu = float(input())
if suhu < 36.0:
    print("Suhu rendah")
elif suhu < 37.5:
    print("Suhu normal")
else:
    print("Demam")
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| Input dikonversi ke float | 2 |
| Tiga cabang if-elif-else | 4 |
| Batas 36.0 dan 37.5 tepat | 2 |
| Teks output persis | 2 |
| Total | 10 |

Test case (masukan dipisah `/` per baris):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 35.5 | Suhu rendah |
| 2 | 36.0 | Suhu normal |
| 3 | 37.4 | Suhu normal |
| 4 | 37.5 | Demam |
| 5 | 39.1 | Demam |

### B3. Tiket Bioskop (Sedang, 15 poin)

Kode solusi:

```python
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
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| Memakai match-case untuk kode studio | 4 |
| Huruf kecil dan besar diterima (.upper()) | 2 |
| case _ dan jumlah tiket tidak valid ditangani | 3 |
| Diskon 10% mulai 4 tiket, hitungan bilangan bulat | 4 |
| Format output sesuai | 2 |
| Total | 15 |

Test case (masukan dipisah `/` per baris):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | d / 2 | Studio: Deluxe / Total: 120000 |
| 2 | I / 4 | Studio: IMAX / Total: 324000 |
| 3 | R / 1 | Studio: Reguler / Total: 40000 |
| 4 | x / 3 | Kode studio tidak dikenal |
| 5 | r / 0 | Jumlah tiket tidak valid |
| 6 | D / 5 | Studio: Deluxe / Total: 270000 |

### B4. Jenis Segitiga (Sedang, 15 poin)

Kode solusi:

```python
a = int(input())
b = int(input())
c = int(input())
if a <= 0 or b <= 0 or c <= 0:
    print("Sisi harus positif")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Bukan segitiga")
elif a == b and b == c:
    print("Segitiga sama sisi")
elif a == b or b == c or a == c:
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| Validasi sisi positif | 3 |
| Validasi ketidaksamaan segitiga (ketiga kombinasi, tepat sama berarti bukan segitiga) | 4 |
| Sama sisi dicek sebelum sama kaki | 4 |
| Operator and dan or dipakai dengan benar | 2 |
| Teks output persis | 2 |
| Total | 15 |

Test case (masukan dipisah `/` per baris):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 5 / 5 / 5 | Segitiga sama sisi |
| 2 | 5 / 5 / 8 | Segitiga sama kaki |
| 3 | 3 / 4 / 5 | Segitiga sembarang |
| 4 | 1 / 2 / 3 | Bukan segitiga |
| 5 | 0 / 4 / 5 | Sisi harus positif |
| 6 | 7 / 2 / 7 | Segitiga sama kaki |
| 7 | 10 / 3 / 4 | Bukan segitiga |

### B5. Ongkos Kirim Paket (Susah, 25 poin)

Kode solusi:

```python
berat = int(input())
tujuan = input().upper()
ekspres = input()
if berat <= 0 or berat > 30:
    print("Berat tidak valid")
else:
    if tujuan == "L" or tujuan == "N":
        if tujuan == "L":
            total = berat * 8000
        else:
            total = berat * 15000
        if ekspres == "y":
            total += total * 20 // 100
        print("Ongkir:", total)
    elif tujuan == "I":
        if berat > 10:
            print("Berat melebihi batas internasional")
        elif ekspres == "y":
            print("Ekspres tidak tersedia untuk internasional")
        else:
            print("Ongkir:", berat * 50000)
    else:
        print("Tujuan tidak dikenal")
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| Validasi berat sebagai lapisan luar | 3 |
| Percabangan tujuan bersarang benar (L/N dan I dipisah) | 6 |
| Tambahan ekspres 20% pada L dan N, bilangan bulat | 5 |
| Aturan internasional: batas 10 kg, ekspres ditolak, urutan cek benar | 6 |
| Tujuan tidak dikenal ditangani | 2 |
| Teks output persis | 3 |
| Total | 25 |

Test case (masukan dipisah `/` per baris):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 5 / L / t | Ongkir: 40000 |
| 2 | 5 / n / y | Ongkir: 90000 |
| 3 | 12 / I / t | Berat melebihi batas internasional |
| 4 | 8 / I / y | Ekspres tidak tersedia untuk internasional |
| 5 | 8 / I / t | Ongkir: 400000 |
| 6 | 31 / L / t | Berat tidak valid |
| 7 | 4 / X / t | Tujuan tidak dikenal |
| 8 | 10 / i / t | Ongkir: 500000 |
| 9 | 0 / L / t | Berat tidak valid |

### B6. Penilaian Lomba (Susah, 25 poin)

Kode solusi:

```python
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
```

Indeks penilaian:

| Kriteria | Poin |
|---|---|
| match-case untuk kategori termasuk case _ | 4 |
| Cabang individu benar (batas 90, 75, validasi 0-100) | 5 |
| Anggota 3-5 divalidasi sebelum skor dibaca | 5 |
| Cabang tim benar termasuk bonus anggota tepat 5 | 6 |
| Input skor dibaca hanya saat dibutuhkan | 3 |
| Teks output persis | 2 |
| Total | 25 |

Test case (masukan dipisah `/` per baris):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 1 / 95 | Juara |
| 2 | 1 / 80 | Finalis |
| 3 | 1 / 101 | Skor tidak valid |
| 4 | 2 / 5 / 90 | Juara (bonus anggota lengkap) |
| 5 | 2 / 4 / 90 | Juara |
| 6 | 2 / 3 / 72 | Finalis |
| 7 | 2 / 2 | Jumlah anggota harus 3 sampai 5 |
| 8 | 3 | Kategori tidak dikenal |
| 9 | 2 / 3 / 50 | Peserta |
