# SISTEM MANAJEMEN DAN PELACAKAN KOLEKSI BUKU PERPUSTAKAAN BERBASIS BST
# Deskripsi Singkat
Program ini dirancang untuk mensimulasikan sistem manajemen dan katalogisasi pada perpustakaan digital secara dinamis. Fungsi utama dari program ini adalah mengelola penyimpanan data koleksi buku, melakukan pelacakan (pencarian) posisi buku secara cepat berdasarkan Kode ID uniknya, serta menyajikan data statistik perpustakaan seperti total koleksi dan nilai buku. Dengan adanya sistem ini, proses pengelompokan buku di dalam rak virtual dapat dilakukan secara otomatis dan terstruktur, meniru bagaimana perpustakaan nyata mengorganisasikan ribuan buku agar mudah ditemukan oleh pengunjung.

Struktur data utama yang diterapkan dalam program ini adalah Binary Search Tree (BST) Dasar. Algoritma ini bekerja dengan membagi percabangan data menjadi dua arah berdasarkan nilai Key (Kode ID Buku). Ketika sebuah buku baru didaftarkan (Insert), sistem akan membandingkannya dengan komponen pusat (Root). Jika ID buku baru lebih kecil, maka ia akan dialokasikan ke cabang sebelah kiri (Left Child), dan jika lebih besar akan dialokasikan ke cabang sebelah kanan (Right Child). Penggunaan konsep BST ini memastikan efisiensi waktu pencarian (Search) yang optimal, serta memungkinkan penyajian data katalog yang otomatis terurut dari nilai terkecil ke terbesar melalui metode pembacaan tumpukan pohon secara Inorder Traversal.
# Source Code

<img width="1011" height="881" alt="Screenshot 2026-05-26 211044" src="https://github.com/user-attachments/assets/5142568d-bb31-4c8b-ba36-f330cad21c3d" />
<img width="1013" height="852" alt="Screenshot 2026-05-26 211137" src="https://github.com/user-attachments/assets/6dc6db36-be3e-4247-afc0-4f9c1082460e" />
<img width="1015" height="830" alt="Screenshot 2026-05-26 211225" src="https://github.com/user-attachments/assets/1189c469-e7de-4d6b-a590-db92c505518a" />
<img width="1013" height="850" alt="Screenshot 2026-05-26 211310" src="https://github.com/user-attachments/assets/f7c11dad-660c-499a-923f-a2ed24d1a985" />
<img width="1014" height="478" alt="Screenshot 2026-05-26 211359" src="https://github.com/user-attachments/assets/391c2c1b-2241-464a-93ab-7054cf9248bc" />

# Penjelasan Code
Proyek ini adalah program simulasi pengorganisasian rak dan katalog perpustakaan digital menggunakan struktur data **Binary Search Tree (BST)** Dasar. Program ini dibuat menggunakan bahasa pemrograman Python dan berjalan secara interaktif melalui terminal/CLI.

---

## 📖 Deskripsi Studi Kasus
Pada perpustakaan konvensional, buku ditata di rak berdasarkan kategori atau kode tertentu agar mudah dicari. Program ini mengadopsi konsep tersebut ke dalam ekosistem digital. Setiap buku direpresentasikan sebagai sebuah **Node** yang memiliki `id_buku` (sebagai *Key* unik) dan `judul`. 

Sistem akan menata penempatan buku secara otomatis menggunakan algoritma **BST**:
* Buku dengan Kode ID yang **lebih kecil** dari Buku Pusat (*Root*) akan dialokasikan ke cabang rak sebelah **kiri**.
* Buku dengan Kode ID yang **lebih besar** dari Buku Pusat (*Root*) akan dialokasikan ke cabang rak sebelah **kanan**.

Konsep ini menjamin efisiensi waktu pencarian data buku serta memungkinkan penyajian katalog yang otomatis berurutan.

---

## 🧠 Struktur Blok Kode & Logika Program

Kode program ini dibagi secara terstruktur menjadi tiga bagian utama:

### 1. Objek Data (`class NodeBuku`)
* **Baris 1 - 6:** Berfungsi sebagai cetak biru (*blueprint*) dari wadah informasi buku. Setiap kali buku didaftarkan, objek ini akan menyimpan `id_buku`, `judul`, serta menyediakan pointer `left` dan `right` untuk menghubungkan antar-cabang rak.

### 2. Logika Utama BST (`class KategoriBukuBST`)
Bagian ini mengatur manipulasi data pohon (*tree operations*):
* **`tambah_buku` & `_tambah_node` (Baris 12 - 25):** Memasukkan data buku baru secara rekursif ke posisi rak kiri atau kanan yang tepat berdasarkan perbandingan angka ID.
* **`cari_buku` & `_cari_node` (Baris 27 - 37):** Melacak keberadaan buku. Pencarian di BST sangat efisien karena sistem langsung mengeliminasi setengah cabang data di setiap percabangan.
* **Fungsi Traversal (Baris 39 - 58):** * **`katalog_inorder`**: Mencetak katalog secara berurutan dari ID terkecil ke terbesar.
  * **`struktur_preorder`**: Membaca struktur hierarki penempatan dari root (pohon atas) ke anak-anaknya (bawah).
  * **`arsip_postorder`**: Membaca alur pemrosesan dari elemen terdalam/bawah menuju ke atas.
* **Fungsi Statistik (Baris 60 - 84):**
  * `id_terkecil` & `id_terbesar`: Menelusuri ujung kiri terdalam untuk nilai minimum, dan ujung kanan terdalam untuk nilai maksimum.
  * `total_buku`: Menghitung jumlah keseluruhan node buku secara rekursif.
  * `total_nilai_id`: Menghitung hasil akumulasi matematika dari seluruh *key* ID buku.

### 3. Antarmuka Utama (`def main()`)
* **Baris 87 - 164:** Mengatur perulangan menu interaktif (Menu 1-10) di terminal. Dilengkapi dengan fitur *Error Handling* (`try-except ValueError`) untuk mencegah aplikasi *crash* jika pengguna salah memasukkan tipe data (misalnya mengetik huruf pada menu angka).

---

## 🚀 Skenario Pengujian Sistem (Output Terminal)

Untuk menguji seluruh logika algoritma berjalan dengan sempurna, jalankan program lalu masukkan data dengan urutan acak berikut (agar membentuk pohon seimbang):

1. **Menu 1 (Tambah Buku):** ID `50`, Judul `Algoritma Dasar` (Otomatis menjadi Root)
2. **Menu 1 (Tambah Buku):** ID `30`, Judul `Pemrograman Python` (Belok ke Rak Kiri karena $30 < 50$)
3. **Menu 1 (Tambah Buku):** ID `70`, Judul `Sistem Jaringan` (Belok ke Rak Kanan karena $70 > 50$)

### Hasil Visualisasi Struktur BST di Memori:
```text
           [50: Algoritma Dasar]
               /           \
[30: Pemrograman Python]   [70: Sistem Jaringan]
