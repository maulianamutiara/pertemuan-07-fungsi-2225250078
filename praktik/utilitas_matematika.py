
def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif")

    total = 0
    for i in range(1, n + 1):
        total += i

    return total


def faktorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif")

    hasil = 1
    for i in range(2, n + 1):
        hasil *= i

    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (1-5): ")

        if pilihan == "1":
            try:
                p = float(input("Panjang: "))
                l = float(input("Lebar: "))
                print("Luas persegi panjang =", luas_persegi_panjang(p, l))
            except ValueError:
                print("Input harus berupa angka.")

        elif pilihan == "2":
            try:
                a = float(input("Alas: "))
                t = float(input("Tinggi: "))
                print("Luas segitiga =", luas_segitiga(a, t))
            except ValueError:
                print("Input harus berupa angka.")

        elif pilihan == "3":
            try:
                n = int(input("Masukkan n: "))
                print("Jumlah =", jumlah_n(n))
            except ValueError as e:
                print("Input tidak valid:", e)

        elif pilihan == "4":
            try:
                n = int(input("Masukkan n: "))
                print("Faktorial =", faktorial(n))
            except ValueError as e:
                print("Input tidak valid:", e)

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")


if __name__ == "__main__":
    main()
