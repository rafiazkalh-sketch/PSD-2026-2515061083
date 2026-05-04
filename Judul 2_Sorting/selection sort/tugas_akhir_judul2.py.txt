def selection_sort_geprek(harga, menu):
    n = len(harga)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if harga[j] < harga[min_idx]:
                min_idx = j
        
        harga[i], harga[min_idx] = harga[min_idx], harga[i]
        
        menu[i], menu[min_idx] = menu[min_idx], menu[i]

def main():
    menu_geprek = ["Mister Geprek", "Geprek Damdam", "Geprek Lingling", "Geprek Kitha", "Geprek Arsy"]
    harga_geprek = [20000, 14000, 13000, 11000, 10000]

    print(" DAFTAR MENU SEBELUM DIURUTKAN ")
    for i in range(len(menu_geprek)):
        print(f"- {menu_geprek[i]:<18} : Rp {harga_geprek[i]}")

    selection_sort_geprek(harga_geprek, menu_geprek)

    print("\n DAFTAR MENU SETELAH DIURUTKAN (TERMURAH) ")
    for i in range(len(menu_geprek)):
        print(f"{i+1}. {menu_geprek[i]:<15} : Rp {harga_geprek[i]}")

if __name__ == "__main__":
    main()