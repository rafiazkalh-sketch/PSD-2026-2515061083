# SIMULASI TOMBOL BACK BROWSER DENGAN STACK ARRAY
# Deskripsi Singkat
Program ini dirancang untuk mensimulasikan mekanisme tombol kembali (Back Button) yang terdapat pada aplikasi penjelajah web (web browser). Fungsi utama dari program ini adalah mengelola riwayat kunjungan situs web pengguna secara dinamis, di mana pengguna dapat membuka halaman baru, kembali ke halaman sebelumnya, serta melihat halaman aktif saat ini. Implementasi ini memberikan gambaran nyata bagaimana sistem operasi atau aplikasi memanfaatkan manajemen memori tumpukan dalam aktivitas komputasi sehari-hari.

Struktur data yang diterapkan dalam program ini adalah Stack (Tumpukan) dengan representasi fisik menggunakan Array (List). Karakteristik utama dari Stack adalah pemrosesan data yang mengikuti prinsip LIFO (Last In, First Out), di mana elemen yang terakhir kali dimasukkan (Push) akan menjadi elemen yang pertama kali dikeluarkan (Pop). Dalam studi kasus ini, halaman web yang baru saja dibuka oleh pengguna akan menempati posisi teratas tumpukan (top_idx). Ketika pengguna melakukan aksi navigasi mundur (kembali), sistem secara otomatis menghapus halaman teratas tersebut agar pengguna dapat dialihkan ke halaman yang dikunjungi sebelumnya.

# Source Code
<img width="947" height="702" alt="Screenshot 2026-05-19 230216" src="https://github.com/user-attachments/assets/920899e7-3bfb-4f9e-a1b0-9b4e3cc05ddb" />
<img width="950" height="651" alt="Screenshot 2026-05-19 230316" src="https://github.com/user-attachments/assets/79864a39-1239-4a2c-a984-a73e7a3f68b9" />
<img width="948" height="247" alt="Screenshot 2026-05-19 230410" src="https://github.com/user-attachments/assets/9396c0b1-cd8e-447d-b59e-cff2b9d8d0da" />
