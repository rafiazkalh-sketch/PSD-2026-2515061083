# SISTEM MANAJEMEN RAK BUKU DIGITAL
# Deskripi Singkat
Program ini berfungsi untuk mengelola penyimpanan buku secara digital pada rak bertingkat. Pengguna dapat memantau ketersediaan slot dan menyimpan judul buku pada koordinat tertentu secara terorganisir.Algoritma yang digunakan adalah Struktur Data List 2 Dimensi (Matrix). Program memanfaatkan indeks ganda (baris dan kolom) untuk mengakses dan mengubah data pada posisi spesifik di dalam memori secara efisien dan cepat.
# Source Code
<img width="1305" height="926" alt="Screenshot 2026-04-29 223618" src="https://github.com/user-attachments/assets/f788b9d3-9826-4693-ad57-9714d135d368" />
<img width="1323" height="277" alt="Screenshot 2026-04-29 223650" src="https://github.com/user-attachments/assets/6ca8a746-5d21-49df-baae-cdbef72d35c5" />
# Penjelasan Kode

​Persiapan Wadah (Inisialisasi):
Program menyiapkan sebuah "Rak" virtual dalam bentuk List 2D berukuran 3 × 2 (3 baris, 2 kolom). Pada awalnya, semua posisi diisi dengan teks "Kosong".
​Sistem Navigasi (Indeks):
Untuk mengelola rak, program menggunakan dua koordinat utama:
​Baris (Indeks pertama): Menentukan tingkat rak (0, 1, atau 2).
​Kolom (Indeks kedua): Menentukan posisi slot (0 untuk Kiri, 1 untuk Kanan).
​Alur Interaksi:
​Menampilkan Data: Program melakukan looping (perulangan) untuk membaca seluruh isi list dari baris pertama hingga terakhir, lalu menampilkannya ke layar.
​Menyimpan Data: Saat user ingin menyimpan buku, program meminta dua nomor indeks (baris dan kolom). Jika nomor yang dimasukkan tersedia (valid), program akan menimpa data di koordinat tersebut dengan judul buku yang baru.
​Validasi Keamanan: Terdapat pengecekan kondisi (if) untuk memastikan user tidak memasukkan nomor rak/slot yang tidak ada di memori. Jika input di luar jangkauan (misalnya memasukkan rak nomor 4), program akan menolak akses tersebut untuk mencegah error (crash).
​Siklus Program:
Program dibungkus dalam perulangan while, sehingga user bisa terus melakukan manajemen rak sampai user memilih opsi "Keluar".
