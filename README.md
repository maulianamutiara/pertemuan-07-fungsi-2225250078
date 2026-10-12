# Pertemuan 07 - Fungsi Python

**Nama:** Mauliana Mutiara  
**NIM:** 2225250078  
**Kelas:** 3A

## Tujuan

Pada pertemuan 7 ini, saya belajar tentang fungsi dalam Python, mulai dari cara membuat fungsi, menggunakan parameter, memakai `return`, sampai memahami scope variabel. Saya juga mencoba membuat beberapa program sederhana dan menggabungkan fungsi ke dalam program matematika.

## Cara Menjalankan Program

Program dibuat menggunakan Python di VS Code. Untuk menjalankan salah satu latihan, buka terminal pada folder utama, kemudian masukkan perintah berikut.

Contoh menjalankan latihan salam:

```bash
python latihan/01_salam.py
```

Untuk menjalankan program utilitas matematika:

```bash
python praktik/utilitas_matematika.py
```

Jika perintah `python` tidak bisa digunakan, saya dapat mencoba perintah `python3`.

## Struktur Fungsi

1. `salam(nama, kelas)` digunakan untuk menampilkan salam dan kelas.
2. `luas_persegi_panjang(p, l)` digunakan untuk menghitung luas persegi panjang.
3. `jumlah_n(n)` digunakan untuk menjumlahkan bilangan dari 1 sampai n.
4. `statistik(data)` digunakan untuk menentukan nilai minimum, maksimum, dan rata-rata.
5. `demo(x)` digunakan untuk mempelajari perbedaan scope variabel.
6. `luas_segitiga(a, t)` digunakan untuk menghitung luas segitiga.
7. `faktorial(n)` digunakan untuk menghitung faktorial bilangan.
8. `tampilkan_menu()` digunakan untuk menampilkan pilihan operasi.
9. `main()` digunakan untuk mengatur jalannya program utama.

Fungsi perhitungan menggunakan `return` agar hasilnya dapat digunakan kembali dalam proses lain. Variabel lokal digunakan untuk menyimpan data yang diperlukan selama fungsi berjalan.


## Hasil Pengujian

Berikut beberapa hasil yang digunakan untuk menguji program.

| Pengujian | Input | Hasil |
|---|---|---|
| Luas persegi panjang | 8 dan 5 | 40 |
| Jumlah bilangan | n = 10 | 55 |
| Statistik sederhana | 70, 80, 65, 90, 75 | Min = 65, maks = 90, rata-rata = 76 |
| Luas segitiga | Alas 10, tinggi 6 | 30.0 |
| Faktorial | n = 5 | 120 |
| Faktorial | n = 0 | 1 |

Hasil tersebut merupakan hasil yang diharapkan dari pengujian. Status akhir disesuaikan dengan hasil setelah program dijalankan di VS Code.

## Refleksi

Dari latihan ini, saya jadi lebih memahami cara menggunakan fungsi untuk membuat program. Menurut saya, fungsi cukup membantu karena rumus tidak perlu ditulis berulang kali. Saya juga belajar bahwa `return` berbeda dengan `print`, karena nilai dari `return` masih bisa digunakan untuk perhitungan lain.

Pada latihan scope, saya memahami bahwa variabel di dalam fungsi tidak selalu bisa digunakan langsung dari luar fungsi. Melalui praktik ini, saya juga berlatih menggunakan perulangan, percabangan, dan parameter dalam satu program.
