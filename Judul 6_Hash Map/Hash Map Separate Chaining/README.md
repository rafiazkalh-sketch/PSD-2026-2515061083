# SISTEM MANAJEMEN KONTAK PELANGGAN (Hash Map dengan Separate Chaining)

# Deskripsi Singkat

Program ini dirancang untuk mensimulasikan sistem manajemen data kontak pelanggan berbasis digital. Fungsi utama dari program ini adalah untuk menyimpan, mencari, dan menghapus nama kontak telepon secara instan hanya berdasarkan Kode ID unik milik pelanggan. Dengan adanya simulasi ini, sistem dapat mengorganisasikan database dalam skala besar secara rapi ke dalam beberapa slot memori terpisah, sehingga pencarian data kontak tidak perlu menelusuri seluruh isi tabel satu per satu dari awal.

Logika utama yang diterapkan dalam kodingan ini adalah struktur data Hash Map dengan metode Separate Chaining. Program memetakan ID pelanggan ke indeks slot memori tertentu menggunakan operasi matematika modulo sebagai fungsi hash-nya. Jika terjadi tabrakan data (collision) di mana dua ID pelanggan yang berbeda menghasilkan slot indeks yang sama, program mengatasinya dengan logika Separate Chaining, yaitu membuat rantai Linked List pada slot tersebut agar data baru otomatis mengantre di belakang data lama tanpa saling menimpa atau merusak memori sistem.

# Source Code

<img width="1058" height="876" alt="Screenshot 2026-06-09 225415" src="https://github.com/user-attachments/assets/760f96a9-38b1-4f34-833e-7628aa4f4ca7" />
<img width="1060" height="852" alt="Screenshot 2026-06-09 225446" src="https://github.com/user-attachments/assets/28b9c310-8626-49e1-a554-41eb0ce4c95c" />
<img width="1104" height="853" alt="Screenshot 2026-06-09 225529" src="https://github.com/user-attachments/assets/d3bc2bf4-4565-4ca7-9a1c-090fb1cf274e" />
<img width="1058" height="414" alt="Screenshot 2026-06-09 225608" src="https://github.com/user-attachments/assets/d474f600-38f9-45cf-b4be-ea2dfecc0c3a" />

# Penjelasan Code

Kodingan ini membagi sistem menjadi dua bagian utama, yaitu objek data dan logika tabel hash. Bagian pertama adalah NodeKontak yang berfungsi sebagai wadah untuk menyimpan id_pelanggan, nama_kontak, dan pointer next untuk menyambungkan rantai memori. Bagian kedua adalah BukuKontakHashMap yang bertindak sebagai pengelola database dengan menyediakan 10 slot penyimpanan. Sistem ini menggunakan fungsi hash berbasis operasi modulo untuk menentukan lokasi indeks data secara instan berdasarkan ID pelanggan yang dimasukkan.

Untuk memanipulasi data, program ini menyediakan tiga fungsi utama yaitu tambah_kontak, cari_kontak, dan hapus_kontak. Saat menambah data, jika ID pelanggan sudah ada, sistem akan memperbarui namanya; namun jika ID baru tersebut memicu tabrakan data (collision), logika Separate Chaining akan otomatis mengantrekan node baru tersebut ke dalam rantai Linked List pada slot indeks yang sama. Fungsi pencarian dan penghapusan data bekerja sangat efisien karena sistem langsung melompat ke slot indeks hasil kalkulasi hash, lalu menelusuri rantai memori di dalamnya menggunakan perulangan. Seluruh logika ini dibungkus dalam menu interaktif pada fungsi main yang sudah dilengkapi pengaman try-except agar program tidak crash saat dijalankan.

# Output Program

https://youtu.be/NUJr1ElTB00
<img width="1023" height="857" alt="Screenshot 2026-06-09 230441" src="https://github.com/user-attachments/assets/bccfb0d7-3dcc-433d-924b-ebfa2465926d" />
<img width="1019" height="907" alt="Screenshot 2026-06-09 230503" src="https://github.com/user-attachments/assets/5b31b4c4-9183-41e8-8004-e0788bd6e838" />
<img width="1022" height="566" alt="Screenshot 2026-06-09 230531" src="https://github.com/user-attachments/assets/29801f66-260f-4a84-9f16-5b31faa19fc7" />

# Link Youtube
