rak_buku = [
    ["Kosong", "Kosong"], 
    ["Kosong", "Kosong"], 
    ["Kosong", "Kosong"]
]

def main():
    while True:
        print("\n" + "="*30)
        print("   SISTEM MANAJEMEN RAK BUKU")
        print("="*30)
        print("1. Lihat Semua Rak")
        print("2. Simpan Buku Baru")
        print("3. Keluar")
        
        pilih = input("Pilih Menu (1-3): ")

        if pilih == "1":
            print("\nSTATUS RAK SAAT INI:")
            for i in range(3):
                print(f"Rak Index {i} : {rak_buku[i]}")

        elif pilih == "2":
            try:
                baris = int(input("\nPilih Nomor Rak (0-2): "))
                kolom = int(input("Pilih Nomor Slot (0-1): "))

                if 0 <= baris <= 2 and 0 <= kolom <= 1:
                    judul = input("Masukkan Judul Buku: ")
                    rak_buku[baris][kolom] = judul
                    print(f"✅ Berhasil! '{judul}' disimpan di Rak {baris} Slot {kolom}.")
                else:
                    print("❌ GAGAL: Indeks di luar jangkauan! (Gunakan Rak 0-2 & Slot 0-1)")
            
            except ValueError:
                print("❌ GAGAL: Masukkan harus berupa angka!")

        elif pilih == "3":
            print("Selesai. Sampai jumpa!")
            break
        else:
            print("❌ Pilihan menu tidak tersedia.")

if __name__ == "__main__":
    main()