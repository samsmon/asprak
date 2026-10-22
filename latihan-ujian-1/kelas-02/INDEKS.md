# Indeks Assessor Kelas 02

Klik nomor soal untuk membuka kode solusinya, atau Buka di kolom Rubrik untuk melihat skor dan test case. [Soal mahasiswa](soal.md) | [Rubrik lengkap](assessor.md)

Aturan nilai: Mudah 15, Sedang 30, Susah 40, nilai akhir paling tinggi 100. Soal selesai = skor rubrik minimal 70. Tiga soal selesai atau lebih minimal 75 (aman), dua soal selesai paling tinggi 74.

| Soal | Tingkat | Bobot | Topik | Kode | Rubrik | Yang sering salah |
|---|---|---|---|---|---|---|
| [1. Konversi Durasi](solusi/1.py) | Mudah | 15 | Variabel | [1.py](solusi/1.py) | [Buka](assessor.md#soal-1-konversi-durasi-mudah-15-poin) | Sisa detik dihitung dari total, bukan total % 3600; tepat 3600 detik dianggap True; angka 3600 ditulis langsung |
| [2. Cek Suhu Tubuh](solusi/2.py) | Mudah | 15 | Percabangan if-elif-else | [2.py](solusi/2.py) | [Buka](assessor.md#soal-2-cek-suhu-tubuh-mudah-15-poin) | Batas 36.0 dan 37.5 tertukar inklusif/eksklusif; input tidak di-float |
| [3. Tiket Bioskop](solusi/3.py) | Sedang | 30 | Percabangan switch case (match-case) dan if-else | [3.py](solusi/3.py) | [Buka](assessor.md#soal-3-tiket-bioskop-sedang-30-poin) | Diskon dimulai dari > 4, seharusnya >= 4; jumlah tiket kurang dari 1 tidak dicek; huruf kecil tidak diterima |
| [4. Jenis Segitiga](solusi/4.py) | Sedang | 30 | Percabangan if-elif-else | [4.py](solusi/4.py) | [Buka](assessor.md#soal-4-jenis-segitiga-sedang-30-poin) | Sama kaki dicek sebelum sama sisi; a + b == c masih dianggap segitiga; sisi nol tidak dicek |
| [5. Ongkos Kirim Paket](solusi/5.py) | Susah | 40 | Percabangan bersarang | [5.py](solusi/5.py) | [Buka](assessor.md#soal-5-ongkos-kirim-paket-susah-40-poin) | Tarif L dan N tertukar; ekspres internasional diproses; batas 10 kg dicek sesudah ekspres; berat 0 atau 31 lolos |
| [6. Penilaian Lomba](solusi/6.py) | Susah | 40 | Percabangan bersarang + match-case | [6.py](solusi/6.py) | [Buka](assessor.md#soal-6-penilaian-lomba-susah-40-poin) | Skor tim dibaca sebelum anggota divalidasi; bonus berlaku untuk anggota >= 4, seharusnya tepat 5; tidak ada case _ |
