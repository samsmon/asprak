# Latihan Ujian 1 Algoritma Pemrograman, Kelas 02

Materi: variabel, konstanta, operator (aritmatika, logika), tipe data; if-then-else; switch case; percabangan bersarang.

## Petunjuk

- Bahasa Python 3.10 ke atas, karena `match-case` baru ada di versi itu.
- Masukan dibaca dengan `input()` tanpa teks prompt, urutan baris sesuai soal.
- Teks keluaran harus persis sama dengan format di soal, termasuk huruf besar dan spasi.
- Contoh hanya dua kasus. Program harus benar untuk semua kemungkinan masukan.

## Penilaian

- Ada 6 soal dengan bobot menurut tingkat: Mudah 25 poin, Sedang 30 poin, Susah 35 poin.
- Nilai akhir adalah jumlah poin dan paling tinggi 100.
- Tiga soal yang benar sudah cukup untuk nilai aman (75 ke atas). Dua soal yang benar menghasilkan nilai di bawah 75.
- Soal yang tidak dikerjakan boleh dikosongkan, tidak ada pengurangan poin.

## Soal

### Soal 1. Konversi Durasi (Mudah, 25 poin)

Topik: Variabel, konstanta, operator aritmatika (// dan %), tipe data bool

Aplikasi video mengubah durasi dalam detik menjadi format jam, menit, dan detik.

Alur program:

1. Konstanta: 3600 detik per jam dan 60 detik per menit.
2. Program membaca total detik (int).
3. Jam = total // 3600. Sisa detik = total % 3600.
4. Menit = sisa // 60. Detik = sisa % 60.
5. Cetak durasi dalam format jam, menit, detik.
6. Cetak apakah durasi lebih dari 1 jam (True atau False).

Masukan:

- Baris 1: total detik (int)

Keluaran:

- `<jam> jam <menit> menit <detik> detik`
- `Lebih dari 1 jam: <True/False>`

Contoh:

Masukan 1:
```
3725
```
Keluaran 1:
```
1 jam 2 menit 5 detik
Lebih dari 1 jam: True
```

Masukan 2:
```
3600
```
Keluaran 2:
```
1 jam 0 menit 0 detik
Lebih dari 1 jam: False
```

### Soal 2. Cek Suhu Tubuh (Mudah, 25 poin)

Topik: Percabangan if-elif-else, tipe data float

Petugas screening mengelompokkan suhu tubuh pengunjung.

Alur program:

1. Program membaca suhu tubuh (float).
2. Suhu di bawah 36.0: cetak Suhu rendah.
3. Suhu 36.0 sampai di bawah 37.5: cetak Suhu normal.
4. Suhu 37.5 ke atas: cetak Demam.

Masukan:

- Baris 1: suhu (float)

Keluaran:

- `Suhu rendah / Suhu normal / Demam`

Contoh:

Masukan 1:
```
36.0
```
Keluaran 1:
```
Suhu normal
```

Masukan 2:
```
37.5
```
Keluaran 2:
```
Demam
```

### Soal 3. Tiket Bioskop (Sedang, 30 poin)

Topik: Percabangan switch case (match-case) dan if-else

Bioskop punya tiga studio: R (Reguler) Rp40.000, D (Deluxe) Rp60.000, I (IMAX) Rp90.000. Beli 4 tiket atau lebih dapat diskon 10%.

Alur program:

1. Program membaca kode studio (huruf besar atau kecil) dan jumlah tiket (int).
2. Kode di luar R, D, I: cetak kode studio tidak dikenal, selesai.
3. Jumlah tiket kurang dari 1: cetak jumlah tiket tidak valid, selesai.
4. Total = harga x jumlah tiket. Bila tiket >= 4, total dikurangi total x 10 // 100.
5. Cetak nama studio dan total.

Masukan:

- Baris 1: kode studio (R/D/I)
- Baris 2: jumlah tiket (int)

Keluaran:

- `Studio: <nama>`
- `Total: <rupiah>`
- `atau  Kode studio tidak dikenal`
- `atau  Jumlah tiket tidak valid`

Contoh:

Masukan 1:
```
d
2
```
Keluaran 1:
```
Studio: Deluxe
Total: 120000
```

Masukan 2:
```
I
4
```
Keluaran 2:
```
Studio: IMAX
Total: 324000
```

### Soal 4. Jenis Segitiga (Sedang, 30 poin)

Topik: Percabangan if-elif-else, operator logika (and, or)

Program menentukan jenis segitiga dari panjang tiga sisi.

Alur program:

1. Program membaca tiga sisi (int): a, b, c.
2. Ada sisi 0 atau negatif: cetak sisi harus positif.
3. Bukan segitiga bila jumlah dua sisi mana pun tidak lebih besar dari sisi ketiga: cetak bukan segitiga.
4. Tiga sisi sama: segitiga sama sisi.
5. Tepat dua sisi sama: segitiga sama kaki.
6. Selain itu: segitiga sembarang.

Masukan:

- Baris 1-3: sisi a, b, c (int)

Keluaran:

- `Sisi harus positif / Bukan segitiga / Segitiga sama sisi / Segitiga sama kaki / Segitiga sembarang`

Contoh:

Masukan 1:
```
5
5
8
```
Keluaran 1:
```
Segitiga sama kaki
```

Masukan 2:
```
1
2
3
```
Keluaran 2:
```
Bukan segitiga
```

### Soal 5. Ongkos Kirim Paket (Susah, 35 poin)

Topik: Percabangan bersarang, operator logika dan aritmatika

Ekspedisi menghitung ongkir dari berat, tujuan, dan layanan ekspres.

Alur program:

1. Program membaca berat (kg, int), tujuan (L lokal, N nasional, I internasional; besar atau kecil), dan ekspres (y atau t).
2. Berat <= 0 atau > 30: cetak berat tidak valid, selesai.
3. Tujuan L: Rp8.000 per kg. Tujuan N: Rp15.000 per kg. Keduanya bila ekspres y, total ditambah 20% (total x 20 // 100). Cetak ongkir.
4. Tujuan I: tarif Rp50.000 per kg, berat maksimal 10 kg. Berat > 10 cetak melebihi batas. Bila ekspres y cetak ekspres tidak tersedia. Selain itu cetak ongkir.
5. Tujuan lain: cetak tujuan tidak dikenal.

Masukan:

- Baris 1: berat (int)
- Baris 2: tujuan (L/N/I)
- Baris 3: ekspres (y/t)

Keluaran:

- `Ongkir: <rupiah>`
- `Berat tidak valid`
- `Berat melebihi batas internasional`
- `Ekspres tidak tersedia untuk internasional`
- `Tujuan tidak dikenal`

Contoh:

Masukan 1:
```
5
n
y
```
Keluaran 1:
```
Ongkir: 90000
```

Masukan 2:
```
8
I
y
```
Keluaran 2:
```
Ekspres tidak tersedia untuk internasional
```

### Soal 6. Penilaian Lomba (Susah, 35 poin)

Topik: Percabangan bersarang + match-case

Panitia lomba menilai peserta kategori individu dan tim dengan aturan berbeda.

Alur program:

1. Program membaca kategori: 1 untuk individu, 2 untuk tim.
2. Kategori 1: baca skor (0 sampai 100). Di luar rentang cetak skor tidak valid. Skor >= 90 Juara, >= 75 Finalis, selain itu Peserta.
3. Kategori 2: baca jumlah anggota. Harus 3 sampai 5, bila tidak cetak pesan jumlah anggota, selesai tanpa membaca skor.
4. Anggota sah: baca skor tim. Di luar 0 sampai 100 cetak skor tidak valid. Skor >= 85 Juara, dan bila anggota tepat 5 cetak Juara (bonus anggota lengkap). Skor >= 70 Finalis, selain itu Peserta.
5. Kategori lain: cetak kategori tidak dikenal.
6. Input skor hanya dibaca bila dibutuhkan.

Masukan:

- Baris 1: kategori (1/2)
- Kategori 1, baris 2: skor (int)
- Kategori 2, baris 2: jumlah anggota (int)
- Kategori 2, baris 3 (bila anggota sah): skor (int)

Keluaran:

- `Juara / Juara (bonus anggota lengkap) / Finalis / Peserta`
- `Skor tidak valid`
- `Jumlah anggota harus 3 sampai 5`
- `Kategori tidak dikenal`

Contoh:

Masukan 1:
```
2
4
90
```
Keluaran 1:
```
Juara
```

Masukan 2:
```
2
2
```
Keluaran 2:
```
Jumlah anggota harus 3 sampai 5
```

## Format pengumpulan (.ipynb)

- Sel pertama berupa sel teks (Markdown) berisi nama lengkap, NIM, dan kelas.
- Satu sel kode untuk satu soal, berurutan dari soal 1 sampai 6.
- Baris pertama setiap sel kode adalah komentar label soal, misalnya `# Soal 3`.
- Satu soal tidak dipecah ke beberapa sel, dan dua soal tidak digabung dalam satu sel.
- Jawaban berupa program yang membaca `input()`. Nilai yang ditulis langsung ke kode tidak diterima, karena penilaian menjalankan kode dengan masukan lain.
- Sel percobaan dan kode di luar jawaban dihapus, lalu notebook disimpan sebelum dikirim.
- Nama berkas: `NIM_Nama Lengkap.ipynb`, misalnya `6703220051_Bakti Surya Atmaja.ipynb`.
- Berkas diunggah ke folder Google Drive Kelas 02: https://drive.google.com/drive/folders/18dHnI4B3LkzHQ41KBf6U56ozs1TE6hb7?usp=drive_link
