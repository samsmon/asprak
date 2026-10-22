# Latihan Ujian 1 Algoritma Pemrograman (Python)

Materi: variabel, konstanta, operator (aritmatika, logika), tipe data; if-then-else; switch case; percabangan bersarang.

## Petunjuk

- Bahasa Python 3.10 ke atas (`match-case` butuh 3.10).
- Baca masukan dengan `input()` tanpa teks prompt, urutan baris sesuai soal.
- Teks keluaran harus persis sama dengan format di soal, termasuk huruf besar dan spasi.
- Tiap kelas 6 soal: 2 Mudah, 2 Sedang, 2 Susah. Bobot: Mudah 10, Sedang 15, Susah 25 (total 100).
- Contoh hanya dua kasus; program harus benar untuk semua kemungkinan masukan.

## Format pengumpulan (file .ipynb)

- Sel pertama berisi identitas dalam sel teks (Markdown): nama lengkap, NIM, dan kelas (A atau B).
- Satu sel kode untuk satu soal, berurutan dari soal 1 sampai 6.
- Baris pertama setiap sel kode adalah komentar label soal, misalnya `# A3` atau `# B5`.
- Jangan menaruh dua soal dalam satu sel, dan jangan memecah satu soal ke beberapa sel.
- Tulis jawaban sebagai program yang membaca `input()`, bukan nilai yang di-hardcode. Penilaian dilakukan dengan menjalankan kode kamu pada masukan lain.
- Hapus sel percobaan atau kode lain yang tidak termasuk jawaban, lalu simpan notebook sebelum dikirim.
- Nama berkas: `NIM_Nama_Kelas.ipynb`, misalnya `2301001_Budi_A.ipynb`.

## Kelas A

### A1. Kasir Toko (Mudah, 10 poin)

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

### A2. Kelulusan Ujian (Mudah, 10 poin)

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

### A3. Diskon Member (Sedang, 15 poin)

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

### A4. Tiket Wahana (Sedang, 15 poin)

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

### A5. Seleksi Beasiswa (Susah, 25 poin)

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

### A6. Simulasi ATM (Susah, 25 poin)

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

## Kelas B

### B1. Konversi Durasi (Mudah, 10 poin)

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

### B2. Cek Suhu Tubuh (Mudah, 10 poin)

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

### B3. Tiket Bioskop (Sedang, 15 poin)

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

### B4. Jenis Segitiga (Sedang, 15 poin)

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

### B5. Ongkos Kirim Paket (Susah, 25 poin)

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

### B6. Penilaian Lomba (Susah, 25 poin)

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
