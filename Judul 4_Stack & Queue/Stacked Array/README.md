# SIMULASI TOMBOL BACK BROWSER DENGAN STACK ARRAY
# Deskripsi Singkat
Program ini dirancang untuk mensimulasikan mekanisme tombol kembali (Back Button) yang terdapat pada aplikasi penjelajah web (web browser). Fungsi utama dari program ini adalah mengelola riwayat kunjungan situs web pengguna secara dinamis, di mana pengguna dapat membuka halaman baru, kembali ke halaman sebelumnya, serta melihat halaman aktif saat ini. Implementasi ini memberikan gambaran nyata bagaimana sistem operasi atau aplikasi memanfaatkan manajemen memori tumpukan dalam aktivitas komputasi sehari-hari.

Struktur data yang diterapkan dalam program ini adalah Stack (Tumpukan) dengan representasi fisik menggunakan Array (List). Karakteristik utama dari Stack adalah pemrosesan data yang mengikuti prinsip LIFO (Last In, First Out), di mana elemen yang terakhir kali dimasukkan (Push) akan menjadi elemen yang pertama kali dikeluarkan (Pop). Dalam studi kasus ini, halaman web yang baru saja dibuka oleh pengguna akan menempati posisi teratas tumpukan (top_idx). Ketika pengguna melakukan aksi navigasi mundur (kembali), sistem secara otomatis menghapus halaman teratas tersebut agar pengguna dapat dialihkan ke halaman yang dikunjungi sebelumnya.

# Source Code
<img width="947" height="702" alt="Screenshot 2026-05-19 230216" src="https://github.com/user-attachments/assets/920899e7-3bfb-4f9e-a1b0-9b4e3cc05ddb" />
<img width="950" height="651" alt="Screenshot 2026-05-19 230316" src="https://github.com/user-attachments/assets/79864a39-1239-4a2c-a984-a73e7a3f68b9" />
<img width="948" height="247" alt="Screenshot 2026-05-19 230410" src="https://github.com/user-attachments/assets/9396c0b1-cd8e-447d-b59e-cff2b9d8d0da" />

# Penjelasan Code
Program ini mengimplementasikan struktur data Stack (Tumpukan) menggunakan Array/List di Python untuk mensimulasikan fitur tombol kembali (Back Button) pada web browser. Operasi data mengikuti prinsip LIFO (Last In, First Out).

1. Atribut Class StackArray
   -self.MAX: Kapasitas maksimal tumpukan riwayat halaman.
   -self.st: Array penyimpan data riwayat kunjungan (diinisialisasi dengan None).
   -self.top_idx: Penunjuk indeks elemen teratas. Bernilai -1 saat tumpukan kosong.

2. Metode/Fungsi Utama
   -is_empty() & is_full(): Memvalidasi kondisi tumpukan apakah sedang kosong (top_idx == -1) atau sudah penuh (top_idx == MAX - 1).
   -push(x): Membuka halaman web baru. Menaikkan top_idx sebesar 1 lalu memasukkan data ke dalam array.
   -pop(): Menekan tombol Back. Mengeluarkan halaman teratas dengan cara menurunkan nilai top_idx sebesar 1.
   -peek(): Menampilkan halaman yang sedang aktif di layar (elemen pada indeks top_idx) tanpa menghapusnya.
   -display(): Menampilkan seluruh daftar riwayat aktif dari yang terbaru hingga terlama menggunakan perulangan mundur (for loop dengan step -1).

3. Fungsi main()
   Mengontrol alur program utama menggunakan perulangan menu interaktif (while) dan dilengkapi dengan fitur error handling (try-except) untuk mencegah program crash akibat kesalahan input dari pengguna.
