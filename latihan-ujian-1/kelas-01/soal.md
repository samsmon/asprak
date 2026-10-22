# Latihan Ujian 1 Algoritma Pemrograman, Kelas 01

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

### Soal 1. Kasir Toko (Mudah, 25 poin)

Topik: Variabel, konstanta, tipe data, operator aritmatika dan perbandingan

Kasir toko menghitung total belanja. Setiap transaksi dikenai biaya admin tetap Rp2.500.

Alur program:

1. Biaya admin disimpan sebagai konstanta (2500).
2. Program membaca harga satuan, jumlah barang, dan uang yang dibayar (semuanya bilangan bulat).
3. Total = harga satuan x jumlah + biaya admin.
4. Kembalian = uang dibayar - total (boleh negatif bila uang kurang).
5. Program mencetak total, kembalian, dan apakah uang cukup (True atau False).

Masukan:

- Baris 1: harga satuan (int)
- Baris 2: jumlah barang (int)
- Baris 3: uang dibayar (int)

Keluaran:

- `Total: <total>`
- `Kembalian: <kembalian>`
- `Cukup: <True/False>`

Contoh:

Masukan 1:
```
5000
3
20000
```
Keluaran 1:
```
Total: 17500
Kembalian: 2500
Cukup: True
```

Masukan 2:
```
12000
2
20000
```
Keluaran 2:
```
Total: 26500
Kembalian: -6500
Cukup: False
```

### Soal 2. Kelulusan Ujian (Mudah, 25 poin)

Topik: Percabangan if-else, operator aritmatika

Dosen menentukan kelulusan dari rata-rata nilai UTS dan UAS.

Alur program:

1. Program membaca nilai UTS lalu nilai UAS (bilangan bulat).
2. Rata-rata = (UTS + UAS) / 2, hasilnya pecahan.
3. Rata-rata dicetak dengan satu angka di belakang koma.
4. Jika rata-rata 60 atau lebih, status LULUS. Selain itu, TIDAK LULUS.

Masukan:

- Baris 1: nilai UTS (int)
- Baris 2: nilai UAS (int)

Keluaran:

- `Rata-rata: <rata-rata, 1 desimal>`
- `Status: <LULUS/TIDAK LULUS>`

Contoh:

Masukan 1:
```
70
80
```
Keluaran 1:
```
Rata-rata: 75.0
Status: LULUS
```

Masukan 2:
```
50
65
```
Keluaran 2:
```
Rata-rata: 57.5
Status: TIDAK LULUS
```

### Soal 3. Diskon Member (Sedang, 30 poin)

Topik: Percabangan switch case (match-case), operator aritmatika

Toko memberi diskon sesuai jenis member: S (Silver) 5%, G (Gold) 10%, P (Platinum) 15%.

Alur program:

1. Program membaca kode member (huruf, boleh besar atau kecil) lalu total belanja (int).
2. Kode dicocokkan dengan jenis member. Kode di luar S, G, P berarti tidak dikenal.
3. Kode tidak dikenal: cetak pesan kesalahan, program selesai.
4. Kode dikenal: diskon (rupiah) = belanja x persen // 100, bayar = belanja - diskon.
5. Cetak nama member, diskon, dan jumlah yang harus dibayar.

Masukan:

- Baris 1: kode member (S/G/P, huruf besar atau kecil)
- Baris 2: total belanja (int)

Keluaran:

- `Bila dikenal: tiga baris  Member: <nama> / Diskon: <rupiah> / Bayar: <rupiah>`
- `Bila tidak dikenal: satu baris  Kode member tidak dikenal`

Contoh:

Masukan 1:
```
g
200000
```
Keluaran 1:
```
Member: Gold
Diskon: 20000
Bayar: 180000
```

Masukan 2:
```
X
50000
```
Keluaran 2:
```
Kode member tidak dikenal
```

### Soal 4. Tiket Wahana (Sedang, 30 poin)

Topik: Percabangan if-elif-else, operator logika

Taman wisata menjual tiket sesuai umur. Akhir pekan ada tambahan Rp10.000, kecuali untuk yang gratis.

Alur program:

1. Program membaca umur (int) dan penanda akhir pekan (y atau t).
2. Umur negatif: cetak pesan umur tidak valid, selesai.
3. Tarif dasar: umur di bawah 5 gratis, 5 sampai 12 Rp20.000, 13 sampai 59 Rp40.000, 60 ke atas Rp15.000.
4. Jika tarif lebih dari 0 dan akhir pekan bernilai y, tambahkan Rp10.000.
5. Cetak tarif akhir.

Masukan:

- Baris 1: umur (int)
- Baris 2: akhir pekan (y/t)

Keluaran:

- `Tarif: <rupiah>`
- `atau  Umur tidak valid`

Contoh:

Masukan 1:
```
25
y
```
Keluaran 1:
```
Tarif: 50000
```

Masukan 2:
```
-1
t
```
Keluaran 2:
```
Umur tidak valid
```

### Soal 5. Seleksi Beasiswa (Susah, 35 poin)

Topik: Percabangan bersarang, operator logika dan perbandingan, tipe data float

Kampus menyeleksi beasiswa dari IPK, penghasilan orang tua, dan keaktifan organisasi.

Alur program:

1. Program membaca IPK (float), penghasilan orang tua per bulan (int), dan aktif organisasi (y atau t).
2. IPK di bawah 3.0: tidak memenuhi syarat IPK.
3. IPK 3.5 ke atas: penghasilan <= 3.000.000 mendapat Beasiswa Penuh, <= 6.000.000 mendapat Beasiswa 50%, selain itu tidak memenuhi syarat penghasilan.
4. IPK 3.0 sampai kurang dari 3.5: wajib aktif organisasi. Bila tidak aktif, cetak syarat organisasi tidak terpenuhi.
5. Bila aktif organisasi: penghasilan <= 3.000.000 mendapat Beasiswa 50%, <= 6.000.000 mendapat Beasiswa 25%, selain itu tidak memenuhi syarat penghasilan.
6. Setiap jalur mencetak tepat satu baris hasil.

Masukan:

- Baris 1: IPK (float)
- Baris 2: penghasilan (int)
- Baris 3: aktif organisasi (y/t)

Keluaran:

- `Satu baris, salah satu dari: Beasiswa Penuh / Beasiswa 50% / Beasiswa 25% / Tidak memenuhi syarat IPK / Tidak memenuhi syarat penghasilan / Syarat organisasi tidak terpenuhi`

Contoh:

Masukan 1:
```
3.6
5000000
y
```
Keluaran 1:
```
Beasiswa 50%
```

Masukan 2:
```
3.2
4000000
t
```
Keluaran 2:
```
Syarat organisasi tidak terpenuhi
```

### Soal 6. Simulasi ATM (Susah, 35 poin)

Topik: Percabangan bersarang + match-case

Mesin ATM sederhana dengan PIN tetap 1234 dan tiga menu: cek saldo, tarik tunai, setor tunai.

Alur program:

1. Program membaca PIN (teks), saldo awal (int), lalu kode menu (teks).
2. PIN selain 1234: cetak PIN salah, selesai (menu tidak diproses).
3. PIN benar, menu 1: cetak saldo.
4. Menu 2 (tarik): baca jumlah. Jumlah harus lebih dari 0 dan kelipatan 50000, bila tidak cetak pesan kelipatan. Bila lebih besar dari saldo, cetak saldo tidak cukup. Selain itu kurangi saldo dan cetak sisa saldo.
5. Menu 3 (setor): baca jumlah. Jumlah <= 0 tidak valid. Selain itu tambahkan ke saldo dan cetak saldo baru.
6. Menu lain: cetak menu tidak tersedia.
7. Jumlah hanya dibaca bila menu 2 atau 3 dipilih.

Masukan:

- Baris 1: PIN (teks)
- Baris 2: saldo awal (int)
- Baris 3: kode menu (1/2/3)
- Baris 4 (hanya menu 2 dan 3): jumlah (int)

Keluaran:

- `PIN salah`
- `Saldo: <n>`
- `Jumlah harus kelipatan 50000`
- `Saldo tidak cukup`
- `Sisa saldo: <n>`
- `Jumlah tidak valid`
- `Saldo baru: <n>`
- `Menu tidak tersedia`

Contoh:

Masukan 1:
```
1234
500000
2
150000
```
Keluaran 1:
```
Sisa saldo: 350000
```

Masukan 2:
```
1234
100000
2
150000
```
Keluaran 2:
```
Saldo tidak cukup
```

## Format pengumpulan (.ipynb)

- Sel pertama berupa sel teks (Markdown) berisi nama lengkap, NIM, dan kelas.
- Satu sel kode untuk satu soal, berurutan dari soal 1 sampai 6.
- Baris pertama setiap sel kode adalah komentar label soal, misalnya `# Soal 3`.
- Satu soal tidak dipecah ke beberapa sel, dan dua soal tidak digabung dalam satu sel.
- Jawaban berupa program yang membaca `input()`. Nilai yang ditulis langsung ke kode tidak diterima, karena penilaian menjalankan kode dengan masukan lain.
- Sel percobaan dan kode di luar jawaban dihapus, lalu notebook disimpan sebelum dikirim.
- Nama berkas: `NIM_Nama_Kelas.ipynb`, misalnya `2301001_Budi_01.ipynb`.
