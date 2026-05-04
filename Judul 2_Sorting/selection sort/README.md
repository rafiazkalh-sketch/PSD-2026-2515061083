# Program Pengurutan Daftar Harga Paket Ayam Geprek Menggunakan Algoritma Selection Sort
# Deskripsi Singkat
Program ini dirancang sebagai solusi sederhana untuk membantu pembeli dalam menentukan pilihan menu makanan berdasarkan budget yang dimiliki dengan cara mengurutkan daftar harga secara otomatis. Program ini menyimpan data nama paket ayam geprek dan harganya ke dalam struktur data array atau list. Dengan adanya program ini, daftar menu yang sebelumnya berantakan dapat ditampilkan secara rapi dari harga yang paling ekonomis hingga yang paling mahal.
Algoritma struktur data yang diterapkan dalam studi kasus ini adalah Selection Sort. Cara kerja algoritma ini adalah dengan memindai seluruh elemen dalam daftar untuk mencari nilai harga terkecil, kemudian menukarnya dengan elemen di posisi pertama. Proses ini diulangi untuk posisi selanjutnya hingga seluruh data harga dan nama menu yang terkait telah terurut secara ascending (kecil ke besar). Pemilihan Selection Sort didasarkan pada efisiensi pertukaran data yang lebih sedikit dibandingkan Bubble Sort, sehingga cocok untuk pengurutan daftar menu yang bersifat statis.
# Source Code
<img width="471" height="345" alt="Screenshot 2026-05-04 224703" src="https://github.com/user-attachments/assets/cf2fe81a-4dba-497b-875f-8fab0e80ba77" />
# penjelasan kode
1. Fungsi Utama: selection_sort_geprek(harga, menu)
Fungsi ini adalah "otak" dari pengurutan data.  

n = len(harga): Program menghitung jumlah data yang ada dalam list harga.  

for i in range(n): Loop luar untuk menentukan posisi urutan (dimulai dari posisi 0 sampai akhir).  

min_idx = i: Program mengasumsikan elemen di posisi i adalah yang terkecil untuk sementara.  

for j in range(i + 1, n): Loop dalam ini memindai sisa list untuk mencari apakah ada harga yang lebih kecil dari harga[min_idx].  

if harga[j] < harga[min_idx]: Jika ditemukan harga yang lebih murah, maka posisi terkecil (min_idx) diperbarui ke posisi j.  

2. Proses Pertukaran (Swapping)
Bagian ini sangat krusial karena program melakukan dua pertukaran sekaligus:  

harga[i], harga[min_idx] = harga[min_idx], harga[i]: Menukar posisi harga terkecil yang ditemukan ke posisi depan.  

menu[i], menu[min_idx] = menu[min_idx], menu[i]: PENTING! Program juga menukar posisi nama menu agar nama geprek tetap sesuai dengan harganya dan tidak tertukar dengan menu lain.  

3. Fungsi main()
Fungsi ini bertugas menyiapkan data dan menampilkan hasil ke layar.  

Input Data: Membuat list menu_geprek (berisi teks) dan harga_geprek (berisi angka).  

Tampilan Awal: Menampilkan daftar menu sesuai urutan asli saat diinput (masih berantakan).  

Pemanggilan Fungsi: Baris selection_sort_geprek(...) memerintahkan program untuk memproses pengurutan.  

Tampilan Akhir: Menampilkan hasil yang sudah rapi dari harga termurah ke termahal.  

Format : <18 dan : <15: Ini digunakan untuk mengatur jarak spasi agar tampilan daftar di terminal terlihat sejajar dan rapi.  

4. if __name__ == "__main__":
Baris ini memastikan bahwa fungsi main() akan langsung dijalankan secara otomatis ketika file Python tersebut dieksekusi.
