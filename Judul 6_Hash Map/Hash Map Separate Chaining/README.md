# SISTEM MANAJEMEN KONTAK PELANGGAN (Hash Map dengan Separate Chaining)

# Deskripsi Singkat

Program ini dirancang untuk mensimulasikan sistem manajemen data kontak pelanggan berbasis digital. Fungsi utama dari program ini adalah untuk menyimpan, mencari, dan menghapus nama kontak telepon secara instan hanya berdasarkan Kode ID unik milik pelanggan. Dengan adanya simulasi ini, sistem dapat mengorganisasikan database dalam skala besar secara rapi ke dalam beberapa slot memori terpisah, sehingga pencarian data kontak tidak perlu menelusuri seluruh isi tabel satu per satu dari awal.

Logika utama yang diterapkan dalam kodingan ini adalah struktur data Hash Map dengan metode Separate Chaining. Program memetakan ID pelanggan ke indeks slot memori tertentu menggunakan operasi matematika modulo sebagai fungsi hash-nya. Jika terjadi tabrakan data (collision) di mana dua ID pelanggan yang berbeda menghasilkan slot indeks yang sama, program mengatasinya dengan logika Separate Chaining, yaitu membuat rantai Linked List pada slot tersebut agar data baru otomatis mengantre di belakang data lama tanpa saling menimpa atau merusak memori sistem.

# Source Code

