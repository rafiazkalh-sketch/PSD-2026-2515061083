class NodeKontak: 
    def __init__(self, id_pelanggan, nama_kontak): 
        self.id_pelanggan = id_pelanggan    
        self.nama_kontak = nama_kontak      
        self.next = None 
 
class BukuKontakHashMap: 
    def __init__(self, size=10): 
        self.SIZE = size 
        self.table = [None] * self.SIZE 
 
    def fungsi_hash(self, id_pelanggan): 
        return (id_pelanggan % self.SIZE + self.SIZE) % self.SIZE 
 
    def tambah_kontak(self, id_pelanggan, nama_kontak): 
        indeks = self.fungsi_hash(id_pelanggan) 
        current = self.table[indeks] 
        
        while current is not None: 
            if current.id_pelanggan == id_pelanggan: 
                current.nama_kontak = nama_kontak 
                return 
            current = current.next 
            
        new_node = NodeKontak(id_pelanggan, nama_kontak) 
        new_node.next = self.table[indeks] 
        self.table[indeks] = new_node 
 
    def cari_kontak(self, id_pelanggan): 
        indeks = self.fungsi_hash(id_pelanggan) 
        current = self.table[indeks] 
        
        while current is not None: 
            if current.id_pelanggan == id_pelanggan: 
                return current 
            current = current.next 
        return None 
 
    def hapus_kontak(self, id_pelanggan): 
        indeks = self.fungsi_hash(id_pelanggan) 
        current = self.table[indeks] 
        prev = None 
        
        while current is not None: 
            if current.id_pelanggan == id_pelanggan: 
                if prev is None: 
                    self.table[indeks] = current.next 
                else: 
                    prev.next = current.next 
                return True 
            prev = current 
            current = current.next 
        return False 
 
    def tampilkan_buku_kontak(self): 
        print("\n STATUS MEMORI HASH TABLE (SEPARATE CHAINING) ") 
        for i in range(self.SIZE): 
            print(f"Slot [{i}]: ", end="") 
            current = self.table[i] 
            if current is None:
                print("KOSONG")
            else:
                while current is not None: 
                    print(f"(ID: {current.id_pelanggan}, Nama: {current.nama_kontak}) -> ", end="") 
                    current = current.next 
                print("END") 
 

def main(): 
    buku_telepon = BukuKontakHashMap(size=10) 
    pilih = 0 
    
    while pilih != 5: 
        print(" SIMULATOR DATA KONTAK HASH MAP ") 
        print("1. Simpan Kontak Baru (Insert)") 
        print("2. Cari Nama Kontak Berdasarkan ID (Search)") 
        print("3. Hapus Kontak Pelanggan (Delete)") 
        print("4. Lihat Visualisasi Memori Tabel (Display)") 
        print("5. Keluar Sistem") 
        
        try: 
            pilih = int(input("Pilih Menu: ")) 
        except ValueError: 
            print("Pesan Error: Input harus berupa angka!") 
            continue 
            
        if pilih == 1: 
            try: 
                id_pelanggan = int(input("Masukkan ID Pelanggan (Angka): ")) 
                nama = input("Masukkan Nama Pelanggan: ") 
                buku_telepon.tambah_kontak(id_pelanggan, nama) 
                print(f"Sukses: Kontak '{nama}' berhasil disimpan.") 
            except ValueError: 
                print("Pesan Error: ID Pelanggan harus berupa angka!") 
                
        elif pilih == 2: 
            try: 
                id_pelanggan = int(input("Masukkan ID Pelanggan yang dicari: ")) 
                hasil = buku_telepon.cari_kontak(id_pelanggan) 
                if hasil: 
                    print(f"Hasil: Data Ditemukan! ID {id_pelanggan} adalah milik: '{hasil.nama_kontak}'") 
                else: 
                    print("Hasil: ID Pelanggan tidak ditemukan.") 
            except ValueError: 
                print("Pesan Error: ID harus berupa angka!") 
                
        elif pilih == 3: 
            try: 
                id_pelanggan = int(input("Masukkan ID Pelanggan yang akan dihapus: ")) 
                if buku_telepon.hapus_kontak(id_pelanggan): 
                    print(f"Sukses: Data pelanggan ID {id_pelanggan} telah dihapus.") 
                else: 
                    print("Gagal: ID Pelanggan tidak ditemukan, tidak ada data dihapus.") 
            except ValueError: 
                print("Pesan Error: ID harus berupa angka!") 
                
        elif pilih == 4: 
            buku_telepon.tampilkan_buku_kontak() 
            
        elif pilih == 5: 
            print("Sistem Buku Kontak Dimatikan. baayy") 
        else: 
            print("Pilihan tidak valid! Silakan pilih menu 1-5.") 

if __name__ == "__main__": 
    main()