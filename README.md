# SISTEM MANAJEMEN RAK BUKU DIGITAL
# Deskripi Singkat
Program ini berfungsi untuk mengelola penyimpanan buku secara digital pada rak bertingkat. Pengguna dapat memantau ketersediaan slot dan menyimpan judul buku pada koordinat tertentu secara terorganisir.Algoritma yang digunakan adalah Struktur Data List 2 Dimensi (Matrix). Program memanfaatkan indeks ganda (baris dan kolom) untuk mengakses dan mengubah data pada posisi spesifik di dalam memori secara efisien dan cepat.
# Source Code
<img width="1305" height="926" alt="Screenshot 2026-04-29 223618" src="https://github.com/user-attachments/assets/f788b9d3-9826-4693-ad57-9714d135d368" />
<img width="1323" height="277" alt="Screenshot 2026-04-29 223650" src="https://github.com/user-attachments/assets/6ca8a746-5d21-49df-baae-cdbef72d35c5" />

# Penjelasan Kode

​1.Persiapan Wadah (Inisialisasi):
Program menyiapkan sebuah "Rak" virtual dalam bentuk List 2D berukuran 3 × 2 (3 baris, 2 kolom). Pada awalnya, semua posisi diisi dengan teks "Kosong".
​
2.Sistem Navigasi (Indeks):
Untuk mengelola rak, program menggunakan dua koordinat utama:
​-Baris (Indeks pertama): Menentukan tingkat rak (0, 1, atau 2).
​K-olom (Indeks kedua): Menentukan posisi slot (0 untuk Kiri, 1 untuk Kanan).
​
3.Alur Interaksi:
​-Menampilkan Data: Program melakukan looping (perulangan) untuk membaca seluruh isi list dari baris pertama hingga terakhir, lalu menampilkannya ke layar.
​-Menyimpan Data: Saat user ingin menyimpan buku, program meminta dua nomor indeks (baris dan kolom). Jika nomor yang dimasukkan tersedia (valid), program akan menimpa data di koordinat tersebut dengan judul buku yang baru.
​-Validasi Keamanan: Terdapat pengecekan kondisi (if) untuk memastikan user tidak memasukkan nomor rak/slot yang tidak ada di memori. Jika input di luar jangkauan (misalnya memasukkan rak nomor 4), program akan menolak akses tersebut untuk mencegah error (crash).
​
4.Siklus Program:
Program dibungkus dalam perulangan while, sehingga user bisa terus melakukan manajemen rak sampai user memilih opsi "Keluar".
# Output Program
<img width="943" height="749" alt="Screenshot 2026-04-29 224035" src="https://github.com/user-attachments/assets/943522d4-4b9f-4c44-85dc-6d8c1a89b50d" />
<img width="907" height="799" alt="Screenshot 2026-04-29 224103" src="https://github.com/user-attachments/assets/8700a36a-00f1-4f8c-8521-24b1fb4254ab" />
<img width="898" height="325" alt="Screenshot 2026-04-29 224126" src="https://github.com/user-attachments/assets/45cea7f1-3538-4f6d-9a5f-cbb3bc1e58d1" />
