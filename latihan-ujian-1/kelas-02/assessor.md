# Latihan Ujian 1 Algoritma Pemrograman, Berkas Assessor Kelas 02

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
| 1 | Mudah | 15 | Konversi Durasi |
| 2 | Mudah | 15 | Cek Suhu Tubuh |
| 3 | Sedang | 30 | Tiket Bioskop |
| 4 | Sedang | 30 | Jenis Segitiga |
| 5 | Susah | 40 | Ongkos Kirim Paket |
| 6 | Susah | 40 | Penilaian Lomba |

### Soal 1. Konversi Durasi (Mudah, 15 poin)

Kode solusi:

```python
# Konstanta
DETIK_PER_JAM = 3600
DETIK_PER_MENIT = 60

# Masukan
total = int(input())

# Proses
jam = total // DETIK_PER_JAM
sisa = total % DETIK_PER_JAM
menit = sisa // DETIK_PER_MENIT
detik = sisa % DETIK_PER_MENIT
lebih_satu_jam = total > DETIK_PER_JAM

# Keluaran
print(jam, "jam", menit, "menit", detik, "detik")
print("Lebih dari 1 jam:", lebih_satu_jam)
```

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| Konstanta dipakai, bukan angka langsung di rumus | 20 |
| Operator // dan % benar untuk jam, menit, detik | 40 |
| Ekspresi pembanding menghasilkan bool (tepat 3600 berarti False) | 20 |
| Format keluaran sesuai | 20 |
| Total | 100 |

Poin soal = skor / 100 x 15.

Test case (baris masukan dipisah `/`):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 3725 | 1 jam 2 menit 5 detik / Lebih dari 1 jam: True |
| 2 | 59 | 0 jam 0 menit 59 detik / Lebih dari 1 jam: False |
| 3 | 3600 | 1 jam 0 menit 0 detik / Lebih dari 1 jam: False |
| 4 | 7384 | 2 jam 3 menit 4 detik / Lebih dari 1 jam: True |

### Soal 2. Cek Suhu Tubuh (Mudah, 15 poin)

Kode solusi:

```python
# Masukan
suhu = float(input())

# Keluaran berdasarkan rentang suhu
if suhu < 36.0:
    print("Suhu rendah")
elif suhu < 37.5:
    print("Suhu normal")
else:
    print("Demam")
```

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| Input dikonversi ke float | 20 |
| Tiga cabang if-elif-else | 40 |
| Batas 36.0 dan 37.5 tepat | 20 |
| Teks keluaran persis | 20 |
| Total | 100 |

Poin soal = skor / 100 x 15.

Test case (baris masukan dipisah `/`):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 35.5 | Suhu rendah |
| 2 | 36.0 | Suhu normal |
| 3 | 37.4 | Suhu normal |
| 4 | 37.5 | Demam |
| 5 | 39.1 | Demam |

### Soal 3. Tiket Bioskop (Sedang, 30 poin)

Kode solusi:

```python
# Masukan
kode = input().upper()
tiket = int(input())

# Tentukan nama studio dan harga dari kode
match kode:
    case "R":
        studio = "Reguler"
        harga = 40000
    case "D":
        studio = "Deluxe"
        harga = 60000
    case "I":
        studio = "IMAX"
        harga = 90000
    case _:
        studio = None
        harga = 0

# Validasi lalu hitung total
if studio is None:
    print("Kode studio tidak dikenal")
elif tiket < 1:
    print("Jumlah tiket tidak valid")
else:
    total = harga * tiket

    # Diskon 10% untuk 4 tiket atau lebih
    if tiket >= 4:
        total -= total * 10 // 100

    print("Studio:", studio)
    print("Total:", total)
```

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| Memakai match-case untuk kode studio | 25 |
| Huruf kecil dan besar diterima (.upper()) | 15 |
| case _ dan jumlah tiket tidak valid ditangani | 20 |
| Diskon 10% mulai 4 tiket, hitungan bilangan bulat | 30 |
| Format keluaran sesuai | 10 |
| Total | 100 |

Poin soal = skor / 100 x 30.

Test case (baris masukan dipisah `/`):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | d / 2 | Studio: Deluxe / Total: 120000 |
| 2 | I / 4 | Studio: IMAX / Total: 324000 |
| 3 | R / 1 | Studio: Reguler / Total: 40000 |
| 4 | x / 3 | Kode studio tidak dikenal |
| 5 | r / 0 | Jumlah tiket tidak valid |
| 6 | D / 5 | Studio: Deluxe / Total: 270000 |

### Soal 4. Jenis Segitiga (Sedang, 30 poin)

Kode solusi:

```python
# Masukan
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

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| Validasi sisi positif | 20 |
| Validasi ketidaksamaan segitiga (tiga kombinasi, jumlah tepat sama berarti bukan segitiga) | 30 |
| Sama sisi dicek sebelum sama kaki | 30 |
| Operator and dan or dipakai dengan benar | 10 |
| Teks keluaran persis | 10 |
| Total | 100 |

Poin soal = skor / 100 x 30.

Test case (baris masukan dipisah `/`):

| No | Masukan | Keluaran |
|---|---|---|
| 1 | 5 / 5 / 5 | Segitiga sama sisi |
| 2 | 5 / 5 / 8 | Segitiga sama kaki |
| 3 | 3 / 4 / 5 | Segitiga sembarang |
| 4 | 1 / 2 / 3 | Bukan segitiga |
| 5 | 0 / 4 / 5 | Sisi harus positif |
| 6 | 7 / 2 / 7 | Segitiga sama kaki |
| 7 | 10 / 3 / 4 | Bukan segitiga |

### Soal 5. Ongkos Kirim Paket (Susah, 40 poin)

Kode solusi:

```python
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
```

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| Validasi berat sebagai lapisan luar | 12 |
| Percabangan tujuan bersarang benar (L/N dan I dipisah) | 24 |
| Tambahan ekspres 20% pada L dan N, bilangan bulat | 20 |
| Aturan internasional: batas 10 kg, ekspres ditolak, urutan cek benar | 24 |
| Tujuan tidak dikenal ditangani | 8 |
| Teks keluaran persis | 12 |
| Total | 100 |

Poin soal = skor / 100 x 40.

Test case (baris masukan dipisah `/`):

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

### Soal 6. Penilaian Lomba (Susah, 40 poin)

Kode solusi:

```python
# Masukan
kategori = input()

match kategori:
    case "1":
        # Individu
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
        # Tim: jumlah anggota dicek dulu sebelum skor dibaca
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

Rubrik (skor soal 0 sampai 100):

| Kriteria | Skor |
|---|---|
| match-case untuk kategori, termasuk case _ | 16 |
| Cabang individu benar (batas 90, 75, validasi 0-100) | 20 |
| Anggota 3-5 divalidasi sebelum skor dibaca | 20 |
| Cabang tim benar, termasuk bonus anggota tepat 5 | 24 |
| Input skor dibaca hanya saat dibutuhkan | 12 |
| Teks keluaran persis | 8 |
| Total | 100 |

Poin soal = skor / 100 x 40.

Test case (baris masukan dipisah `/`):

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
