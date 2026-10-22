# Indeks Assessor Kelas 01

Klik nomor soal untuk membuka kode solusinya, atau Buka di kolom Rubrik untuk melihat skor dan test case. [Soal mahasiswa](soal.md) | [Rubrik lengkap](assessor.md)

Aturan nilai: Mudah 25, Sedang 30, Susah 35, nilai akhir paling tinggi 100. Tiga soal benar penuh minimal 80 (aman), dua soal paling tinggi 70.

| Soal | Tingkat | Bobot | Topik | Kode | Rubrik | Yang sering salah |
|---|---|---|---|---|---|---|
| [1. Kasir Toko](solusi/1.py) | Mudah | 25 | Variabel | [1.py](solusi/1.py) | [Buka](assessor.md#soal-1-kasir-toko-mudah-25-poin) | Input tidak di-int; biaya admin ditulis angka langsung, bukan konstanta; kembalian dihitung terbalik |
| [2. Kelulusan Ujian](solusi/2.py) | Mudah | 25 | Percabangan if-else | [2.py](solusi/2.py) | [Buka](assessor.md#soal-2-kelulusan-ujian-mudah-25-poin) | Memakai // (hasil bulat); batas > 60 padahal 60 sudah lulus; lupa format 1 desimal |
| [3. Diskon Member](solusi/3.py) | Sedang | 30 | Percabangan switch case (match-case) | [3.py](solusi/3.py) | [Buka](assessor.md#soal-3-diskon-member-sedang-30-poin) | Lupa .upper(); tidak ada case _; diskon memakai / sehingga hasil float |
| [4. Tiket Wahana](solusi/4.py) | Sedang | 30 | Percabangan if-elif-else | [4.py](solusi/4.py) | [Buka](assessor.md#soal-4-tiket-wahana-sedang-30-poin) | Batas umur 12/13 dan 60 salah; tambahan akhir pekan ikut menambah tiket gratis; umur negatif tidak ditangani |
| [5. Seleksi Beasiswa](solusi/5.py) | Susah | 35 | Percabangan bersarang | [5.py](solusi/5.py) | [Buka](assessor.md#soal-5-seleksi-beasiswa-susah-35-poin) | Batas 3.0 dan 3.5 salah; if berurutan tanpa elif sehingga mencetak dua baris; cabang organisasi tertukar |
| [6. Simulasi ATM](solusi/6.py) | Susah | 35 | Percabangan bersarang + match-case | [6.py](solusi/6.py) | [Buka](assessor.md#soal-6-simulasi-atm-susah-35-poin) | Jumlah dibaca di luar menu 2 dan 3 (input berlebih); urutan validasi tarik terbalik; PIN salah tetap memproses menu |
