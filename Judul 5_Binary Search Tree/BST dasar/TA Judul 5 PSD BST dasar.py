class NodeBuku: 
    def __init__(self, id_buku, judul): 
        self.id_buku = id_buku      
        self.judul = judul          
        self.left = None 
        self.right = None 

class KategoriBukuBST: 
    def __init__(self): 
        self.root = None 

    def _tambah_node(self, root, id_buku, judul): 
        if root is None: 
            return NodeBuku(id_buku, judul) 
        
        # Jika ID baru lebih kecil, belok kiri
        if id_buku < root.id_buku: 
            root.left = self._tambah_node(root.left, id_buku, judul) 
        # Jika ID baru lebih besar, belok kanan
        elif id_buku > root.id_buku: 
            root.right = self._tambah_node(root.right, id_buku, judul) 
        return root 

    def tambah_buku(self, id_buku, judul): 
        self.root = self._tambah_node(self.root, id_buku, judul) 

    def _cari_node(self, root, id_buku): 
        if root is None: 
            return None 
        if root.id_buku == id_buku: 
            return root 
        if id_buku < root.id_buku: 
            return self._cari_node(root.left, id_buku) 
        return self._cari_node(root.right, id_buku) 

    def cari_buku(self, id_buku): 
        return self._cari_node(self.root, id_buku) 

    def katalog_inorder(self, root): 
        if root is None: 
            return 
        self.katalog_inorder(root.left) 
        print(f"[{root.id_buku}: {root.judul}]", end=" -> ") 
        self.katalog_inorder(root.right)

    def struktur_preorder(self, root): 
        if root is None: 
            return 
        print(f"[{root.id_buku}: {root.judul}]", end=" -> ") 
        self.struktur_preorder(root.left) 
        self.struktur_preorder(root.right) 

    def arsip_postorder(self, root): 
        if root is None: 
            return 
        self.arsip_postorder(root.left) 
        self.arsip_postorder(root.right) 
        print(f"[{root.id_buku}: {root.judul}]", end=" -> ") 

    def id_terkecil(self, root): 
        if root is None: 
            return "Perpustakaan Kosong" 
        current = root 
        while current.left is not None: 
            current = current.left 
        return f"ID: {current.id_buku} (Buku: {current.judul})" 

    def id_terbesar(self, root): 
        if root is None: 
            return "Perpustakaan Kosong" 
        current = root 
        while current.right is not None: 
            current = current.right 
        return f"ID: {current.id_buku} (Buku: {current.judul})" 

    def total_buku(self, root): 
        if root is None: 
            return 0 
        return 1 + self.total_buku(root.left) + self.total_buku(root.right) 

    def total_nilai_id(self, root): 
        if root is None: 
            return 0 
        return root.id_buku + self.total_nilai_id(root.left) + self.total_nilai_id(root.right) 


def main(): 
    perpus = KategoriBukuBST() 
    pilih = 0 
    
    while pilih != 10: 
        print(" SIMULATOR KATALOG PERPUSTAKAAN BST ") 
        print("menu:")
        print("1. Daftarkan Buku Baru (Insert)") 
        print("2. Lacak Posisi Buku Berdasarkan ID (Search)") 
        print("3. Tampilkan Katalog Terurut ID (Inorder)") 
        print("4. Tampilkan Struktur Hierarki Rak (Preorder)") 
        print("5. Tampilkan Alur Deteksi Arsip (Postorder)") 
        print("6. Lihat Buku dengan ID Paling Kecil (Min)") 
        print("7. Lihat Buku dengan ID Paling Besar (Max)") 
        print("8. Hitung Total Koleksi Buku (Count Nodes)") 
        print("9. Hitung Total Nilai ID Buku (Sum Nodes)") 
        print("10. Keluar Sistem") 
        
        try: 
            pilih = int(input("Pilih Menu: ")) 
        except ValueError: 
            print("Pesan Error: Input menu harus berupa angka!") 
            continue 
            
        if pilih == 1: 
            try: 
                id_buku = int(input("Masukkan Kode ID Buku (Angka): ")) 
                judul = input("Masukkan Judul Buku: ") 
                perpus.tambah_buku(id_buku, judul) 
                print(f"Sukses: Buku '{judul}' berhasil disimpan di rak.") 
            except ValueError: 
                print("Pesan Error: ID Buku wajib berupa angka!") 
                
        elif pilih == 2: 
            try: 
                id_buku = int(input("Masukkan ID Buku yang dicari: ")) 
                buku = perpus.cari_buku(id_buku) 
                if buku: 
                    print(f"Hasil: Buku Ditemukan! Judulnya: '{buku.judul}'.") 
                else: 
                    print("Hasil: Buku Tidak Ditemukan di rak manapun.") 
            except ValueError: 
                print("Pesan Error: Input ID harus berupa angka!") 
                
        elif pilih == 3: 
            print("Katalog Sesuai Urutan ID (Inorder):\n") 
            perpus.katalog_inorder(perpus.root) 
            print("SELESAI") 
            
        elif pilih == 4: 
            print("Struktur Penempatan Node Rak (Preorder):\n") 
            perpus.struktur_preorder(perpus.root) 
            print("SELESAI") 
            
        elif pilih == 5: 
            print("Urutan Pemrosesan Arsip Belakang (Postorder):\n") 
            perpus.arsip_postorder(perpus.root) 
            print("SELESAI") 
            
        elif pilih == 6: 
            print(f"Buku ID Terendah -> {perpus.id_terkecil(perpus.root)}") 
            
        elif pilih == 7: 
            print(f"Buku ID Tertinggi -> {perpus.id_terbesar(perpus.root)}") 
            
        elif pilih == 8: 
            print(f"Jumlah Total Koleksi Buku Saat Ini: {perpus.total_buku(perpus.root)} buku.") 
            
        elif pilih == 9: 
            print(f"Hasil Akumulasi Nilai ID Buku: {perpus.total_nilai_id(perpus.root)}") 
            
        elif pilih == 10: 
            print("Sistem Perpustakaan Dimatikan. baayy") 
        else: 
            print("Pilihan tidak valid! Silakan pilih menu 1-10.") 

if __name__ == "__main__": 
    main()