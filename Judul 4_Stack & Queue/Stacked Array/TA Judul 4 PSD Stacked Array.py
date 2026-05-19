class StackArray: 
    def __init__(self, max_size=100): 
        self.MAX = max_size 
        self.st = [None] * self.MAX 
        self.top_idx = -1 
 
    def is_empty(self): 
        return self.top_idx == -1 
 
    def is_full(self): 
        return self.top_idx == self.MAX - 1 
 
    def push(self, x): 
        if self.is_full(): 
            print("Riwayat penuh, tidak bisa memuat halaman baru.") 
            return 
        self.top_idx += 1 
        self.st[self.top_idx] = x 
        print(f"Membuka halaman: {x}") 
 
    def pop(self): 
        if self.is_empty(): 
            print("Tidak ada riwayat halaman sebelumnya (Tombol Back Mati).") 
            return 
        print(f"Kembali dari halaman: {self.st[self.top_idx]}") 
        self.top_idx -= 1 
 
    def peek(self): 
        if self.is_empty(): 
            print("Browser kosong, belum membuka halaman apapun.") 
            return 
        print(f"Halaman aktif saat ini: {self.st[self.top_idx]}") 
 
    def display(self): 
        if self.is_empty(): 
            print("Riwayat kunjungan kosong.") 
            return 
        print("\n--- DAFTAR RIWAYAT KUNJUNGAN ---") 
        for i in range(self.top_idx, -1, -1): 
            print(f"- {self.st[i]}") 
        print("-----------------------------------------------------") 

def main(): 
    browser_history = StackArray() 
    pilih = 0 
    while pilih != 5: 
        print("\n=== SIMULATOR TOMBOL BACK BROWSER ===") 
        print("1. Buka Halaman Baru (Push)") 
        print("2. Klik Tombol Kembali / Back (Pop)") 
        print("3. Lihat Halaman Aktif (Peek)") 
        print("4. Tampilkan Semua Riwayat (Display)") 
        print("5. Keluar") 
        try: 
            pilih = int(input("Pilih Menu: ")) 
        except ValueError: 
            print("Input harus berupa angka!") 
            continue 
            
        if pilih == 1: 
            val = input("Masukkan Nama/URL Web (Contoh: google.com): ") 
            browser_history.push(val) 
        elif pilih == 2: 
            browser_history.pop() 
        elif pilih == 3: 
            browser_history.peek() 
        elif pilih == 4: 
            browser_history.display() 
        elif pilih == 5: 
            print("Simulator ditutup.") 
        else: 
            print("Pilihan menu tidak tersedia!") 
 
if __name__ == "__main__": 
    main()