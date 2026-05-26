# SISTEM MANAJEMEN DAN PELACAKAN KOLEKSI BUKU PERPUSTAKAAN BERBASIS BST
# Deskripsi Singkat
Program ini dirancang untuk mensimulasikan sistem manajemen dan katalogisasi pada perpustakaan digital secara dinamis. Fungsi utama dari program ini adalah mengelola penyimpanan data koleksi buku, melakukan pelacakan (pencarian) posisi buku secara cepat berdasarkan Kode ID uniknya, serta menyajikan data statistik perpustakaan seperti total koleksi dan nilai buku. Dengan adanya sistem ini, proses pengelompokan buku di dalam rak virtual dapat dilakukan secara otomatis dan terstruktur, meniru bagaimana perpustakaan nyata mengorganisasikan ribuan buku agar mudah ditemukan oleh pengunjung.

Struktur data utama yang diterapkan dalam program ini adalah Binary Search Tree (BST) Dasar. Algoritma ini bekerja dengan membagi percabangan data menjadi dua arah berdasarkan nilai Key (Kode ID Buku). Ketika sebuah buku baru didaftarkan (Insert), sistem akan membandingkannya dengan komponen pusat (Root). Jika ID buku baru lebih kecil, maka ia akan dialokasikan ke cabang sebelah kiri (Left Child), dan jika lebih besar akan dialokasikan ke cabang sebelah kanan (Right Child). Penggunaan konsep BST ini memastikan efisiensi waktu pencarian (Search) yang optimal, serta memungkinkan penyajian data katalog yang otomatis terurut dari nilai terkecil ke terbesar melalui metode pembacaan tumpukan pohon secara Inorder Traversal.
# Source Code

<img width="1013" height="876" alt="Screenshot 2026-05-26 214029" src="https://github.com/user-attachments/assets/e5d40a38-f58e-4bbc-b8cb-8f6677a1cef5" />
<img width="1013" height="852" alt="Screenshot 2026-05-26 211137" src="https://github.com/user-attachments/assets/6dc6db36-be3e-4247-afc0-4f9c1082460e" />
<img width="1015" height="830" alt="Screenshot 2026-05-26 211225" src="https://github.com/user-attachments/assets/1189c469-e7de-4d6b-a590-db92c505518a" />
<img width="1013" height="850" alt="Screenshot 2026-05-26 211310" src="https://github.com/user-attachments/assets/f7c11dad-660c-499a-923f-a2ed24d1a985" />
<img width="1014" height="478" alt="Screenshot 2026-05-26 211359" src="https://github.com/user-attachments/assets/391c2c1b-2241-464a-93ab-7054cf9248bc" />

# Penjelasan Code
Program ini adalah sistem simulasi manajemen katalog perpustakaan digital yang menggunakan struktur data Binary Search Tree (BST) Dasar. Sistem ini berfungsi untuk mengotomatiskan penataan letak buku di dalam rak virtual dan melakukan pelacakan secara cepat berdasarkan Kode ID unik buku. Buku dengan ID yang lebih kecil dari Buku Pusat (Root) akan otomatis belok ke rak kiri, sedangkan ID yang lebih besar akan belok ke rak kanan. Selain untuk menambah dan mencari buku, program ini juga dilengkapi dengan fungsi navigasi cetak data (traversal) serta penampil statistik perpustakaan.

Baris 1 – 6: Struktur Data Buku (class NodeBuku).
Bagian ini adalah cetak biru untuk membuat wadah informasi setiap buku. Setiap kali buku baru didaftarkan, objek ini akan menyimpan data id_buku (sebagai penanda utama), judul buku, serta menyediakan tangan left (kiri) dan right (kanan) untuk menghubungkan cabang-cabang rak buku lainnya.

Baris 8 – 10: Inisialisasi Pohon (class KategoriBukuBST).
Blok ini berfungsi untuk membuat sistem perpustakaannya itu sendiri. Saat pertama kali dibuat, variabel self.root diatur ke nilai None sebagai penanda bahwa perpustakaan digital ini statusnya masih kosong total.

Baris 12 – 25: Logika Tambah Buku (Insert).
Fungsi tambah_buku dan _tambah_node bekerja secara rekursif (memanggil dirinya sendiri) untuk menaruh buku baru di posisi yang tepat. Aturannya konsisten: jika ID buku baru lebih kecil dari ID buku yang dicek, sistem akan mengarahkannya ke cabang kiri; jika lebih besar, sistem akan mengarahkannya ke cabang kanan.

Baris 27 – 37: Logika Lacak Posisi Buku (Search).
Fungsi cari_buku dan _cari_node digunakan untuk mencari buku berdasarkan ID-nya. Karena menggunakan konsep BST, proses pencarian menjadi sangat cepat karena komputer tidak perlu mengecek seluruh buku satu per satu, melainkan langsung mengeliminasi setengah cabang rak di setiap langkah penelusuran.

Baris 39 – 58: Logika Penelusuran Katalog (Traversal).
Bagian ini berisi 3 metode untuk membaca dan mencetak seluruh koleksi buku yang ada di dalam rak:
-Inorder (katalog_inorder): Membaca rak kiri, pusat, lalu kanan. Hasilnya akan mencetak katalog buku secara rapi dan otomatis berurutan dari ID terkecil ke terbesar.
-Preorder (struktur_preorder): Membaca pusat dulu, baru rak kiri dan kanan. Ini dipakai untuk melihat struktur hierarki atas ke bawah (peta penempatan buku).
-Postorder (arsip_postorder): Membaca rak kiri dan kanan dulu, baru pusatnya. Biasanya digunakan sistem untuk alur pengarsipan data dari elemen terdalam.

Baris 60 – 74: Logika Deteksi ID Ekstrem (Min & Max).
Fungsi id_terkecil akan terus berjalan ke arah cabang kiri paling ujung untuk menemukan buku dengan ID paling rendah. Sebaliknya, fungsi id_terbesar akan terus berjalan ke arah cabang kanan paling ujung untuk menemukan buku dengan ID paling tinggi.

Baris 76 – 84: Logika Hitung Statistik Perpustakaan (Count & Sum).
Fungsi total_buku bekerja menghitung total seluruh buku yang ada di dalam pohon secara matematis, sedangkan fungsi total_nilai_id bertugas menjumlahkan semua angka ID buku yang terdaftar untuk kebutuhan akumulasi nilai sistem.

Baris 87 – 164: Antarmuka Terminal & Pengaman Kode (def main()).
Blok terakhir ini bertugas menampilkan menu interaktif pilihan 1 sampai 10 di layar terminal. Di dalamnya juga disisipkan fitur pengaman try-except ValueError agar jika pengguna tidak sengaja mengetik huruf pada menu yang seharusnya angka, program tidak akan rusak atau mati mendadak, melainkan hanya menampilkan pesan error dan mengulang menunya kembali.
# Output

<img width="1011" height="908" alt="Screenshot 2026-05-26 213039" src="https://github.com/user-attachments/assets/4c81340a-1953-4327-a9e8-ecc5fc69ac07" />
<img width="1015" height="902" alt="Screenshot 2026-05-26 213135" src="https://github.com/user-attachments/assets/06d62d58-7e8b-4555-bec0-ee0eb8149d62" />
<img width="1017" height="904" alt="Screenshot 2026-05-26 213211" src="https://github.com/user-attachments/assets/44af772c-031e-4f42-a07d-6dc277a0b530" />
<img width="1016" height="912" alt="Screenshot 2026-05-26 213316" src="https://github.com/user-attachments/assets/5fa77341-20f9-4522-9ed5-96fb893bfe93" />
<img width="1014" height="905" alt="Screenshot 2026-05-26 213416" src="https://github.com/user-attachments/assets/cc9c80ce-98d3-4367-a624-762427ef7908" />
<img width="1012" height="904" alt="Screenshot 2026-05-26 213458" src="https://github.com/user-attachments/assets/71333f60-7e0a-4290-a995-54b00e231fcf" />

