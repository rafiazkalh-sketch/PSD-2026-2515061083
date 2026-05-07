# SISTEM PENCARIAN PRESENSI MAHASISWA DENGAN BINARY SEARCH
# Deskripsi Singkat
Program ini berfungsi untuk memvalidasi kehadiran mahasiswa dalam daftar presensi digital secara cepat. Dengan menginputkan NIM sebagai target pencarian, program akan secara otomatis menentukan apakah mahasiswa tersebut sudah terdaftar atau belum dalam kumpulan data yang tersedia.

Algoritma yang digunakan adalah Binary Search dengan struktur data Array. Algoritma ini bekerja dengan cara membelah data menjadi dua bagian secara berulang (logika bagi dua) untuk mempersempit ruang pencarian. Metode ini jauh lebih efisien dibandingkan pencarian biasa karena hanya membutuhkan waktu yang singkat meskipun jumlah data mahasiswa sangat banyak, asalkan data tersebut sudah disusun secara berurutan (terurut).
# Source Code
<img width="1086" height="926" alt="Screenshot 2026-05-07 224817" src="https://github.com/user-attachments/assets/d75de944-675c-4fa5-a676-de5703244dd9" />
<img width="1088" height="342" alt="Screenshot 2026-05-07 224936" src="https://github.com/user-attachments/assets/c82a24ed-356b-4a70-a3e4-e0fa2381db2b" />

# Penjelasan Code
Penjelasan Alur Program (Binary Search)
-Inisialisasi Batas: Program menentukan batas awal pencarian menggunakan indeks kiri (l = 0) dan indeks kanan (r = n - 1).
-Perhitungan Titik Tengah (Median): Di dalam perulangan, program menentukan indeks tengah dengan rumus m = l + (r - l) // 2. Langkah ini bertujuan untuk membagi dua area pencarian secara terus-menerus.
-Pengecekan Kondisi:
Data Ditemukan: Jika nilai pada indeks tengah (arr[m]) sama dengan target, posisi disimpan dan pencarian selesai.
Penyempitan Area: Jika nilai tengah lebih kecil dari target, pencarian fokus ke sisi kanan (l = m + 1). Jika lebih besar, pencarian fokus ke sisi kiri (r = m - 1).
-Hasil Akhir: Jika perulangan selesai dan data tidak ditemukan, fungsi mengembalikan nilai -1, yang kemudian akan dikonfirmasi oleh program utama (fungsi main) kepada pengguna.
