def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return pos

def main():
    print(" SISTEM PENCARIAN PRESENSI MAHASISWA ")
    try:
        n = int(input("Masukkan jumlah mahasiswa yang hadir: "))
    except ValueError:
        print("Input tidak valid!")
        return
    
    arr = []
    print("Masukkan NIM Mahasiswa (urutkan dari yang terkecil):")
    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Mahasiswa ke-{i+1}: "))
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid!")

    print(f"Data Presensi Terdaftar: {arr}")
    
    try:
        target = int(input("Cari NIM Mahasiswa: "))
        pos = binary_search(arr, n, target)
        
        if pos != -1:
            print(f"HASIL: NIM {target} terverifikasi hadir di indeks {pos}")
        else:
            print(f"HASIL: NIM {target} TIDAK ditemukan.")
    except ValueError:
        print("Input NIM tidak valid!")

if __name__ == "__main__":
    main()