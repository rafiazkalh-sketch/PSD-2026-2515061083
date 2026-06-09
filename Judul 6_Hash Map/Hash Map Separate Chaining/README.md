# 📞 Sistem Manajemen Kontak Pelanggan (Hash Map dengan Separate Chaining)

Proyek ini adalah aplikasi simulasi penyimpanan data kontak telepon pelanggan berbasis **Hash Map** menggunakan teknik **Separate Chaining** (Linked List) untuk menangani tabrakan data (*collision resolution*). Program ditulis menggunakan Python dan dijalankan secara interaktif melalui terminal/CLI.

---

## 📖 Deskripsi Studi Kasus
Dalam sistem basis data, pencarian data kontak berdasarkan ID pelanggan dituntut untuk berjalan sangat cepat tanpa harus memeriksa seluruh isi database satu per satu. Program ini memanfaatkan konsep *Hash Map* untuk langsung memetakan ID Pelanggan ke slot memori (*bucket/slot*) tertentu yang sudah disediakan.

Setiap data disimpan sebagai sebuah **NodeKontak** yang berisi:
* `id_pelanggan` (*Key* berbentuk integer)
* `nama_kontak` (*Value* berbentuk string)
* `next` (*Pointer* memori untuk menyambungkan rantai data)

### 💥 Solusi Terhadap Collision (Tabrakan Data)
Karena ukuran tabel dibatasi (`size = 10`), sistem menggunakan fungsi hash dengan rumus matematika:
$$\text{Indeks} = \text{ID Pelanggan} \pmod{10}$$

Ketika dua ID pelanggan yang berbeda memiliki digit terakhir yang sama—misalnya ID **1** dan ID **11**—keduanya akan menghasilkan indeks slot yang sama, yaitu slot **[1]**. Fenomena ini disebut **Collision**. 

Untuk mengatasinya, program ini menerapkan **Separate Chaining**. Alih-alih data lama tertimpa atau hilang, sistem akan membuat rantai *Linked List* di slot tersebut. Data baru akan otomatis diantrekan bersambung dengan data lama di slot memori yang sama.

---

## 🧠 Struktur Blok Kode & Logika Program

Program ini terbagi secara modular ke dalam tiga bagian utama:

1. **`class NodeKontak`**: Berfungsi sebagai cetak biru elemen data (*node*) penyimpan informasi kontak sekaligus pointer penghubung rantai memori.
2. **`class BukuKontakHashMap`**: Berfungsi sebagai otak sistem manajemen data yang mengatur operasi tabel hash:
   * `fungsi_hash`: Menghitung penempatan slot indeks menggunakan operasi modulo.
   * `tambah_kontak` (*Insert/Update*): Memasukkan kontak baru ke awal rantai *Linked List* di slot indeksnya, atau memperbarui nama jika ID pelanggan sudah terdaftar.
   * `cari_kontak` (*Search*): Melacak nama pelanggan dengan langsung melompati indeks hasil kalkulasi hash dan menelusuri rantai *Linked List* di dalamnya.
   * `hapus_kontak` (*Delete*): Memutuskan rantai *Linked List* pada node target dan menyambungkan kembali pointer sebelum dan sesudahnya agar memori tetap konsisten.
   * `tampilkan_buku_kontak` (*Display*): Memvisualisasikan matriks isi seluruh slot memori dari indeks 0 hingga 9.
3. **`def main()`**: Mengatur alur antarmuka menu interaktif (Menu 1-5) di terminal yang dilengkapi dengan pembatas error (*try-except ValueError*) agar aplikasi tidak rusak saat menerima input tidak valid.

---

## 🚀 Skenario Pengujian Sistem (Output Terminal)

Untuk melihat keandalan logika *Separate Chaining* dalam menangani tabrakan data secara visual, lakukan input acak berikut:

1. **Menu 1**: Masukkan ID `1`, Nama: `Andi` *(Masuk ke Slot 1)*
2. **Menu 1**: Masukkan ID `11`, Nama: `Budi` *(Terjadi collision, Budi dirantai bersama Andi di Slot 1)*
3. **Menu 1**: Masukkan ID `2`, Nama: `Citra` *(Masuk ke Slot 2)*

### Visualisasi Tampilan Memori (Menu 4):
```text
=== STATUS MEMORI HASH TABLE (SEPARATE CHAINING) ===
Slot [0]: KOSONG
Slot [1]: (ID: 11, Nama: Budi) -> (ID: 1, Nama: Andi) -> END
Slot [2]: (ID: 2, Nama: Citra) -> END
Slot [3]: KOSONG
...
