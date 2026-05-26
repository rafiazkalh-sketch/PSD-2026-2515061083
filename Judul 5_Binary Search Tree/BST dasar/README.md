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
