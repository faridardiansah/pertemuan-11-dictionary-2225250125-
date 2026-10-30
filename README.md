# Pertemuan 11 - Dictionary/Map

**Nama:** Farid Ardiansah  
**NIM:** 2225250125  
**Kelas:** 3E

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value dalam Python. Program ini bertujuan untuk memahami cara menyimpan, mencari, menambahkan, memperbarui, dan menampilkan data mahasiswa serta menghitung rata-rata nilai.

## Struktur Data

Program menggunakan dictionary `data_mahasiswa` dengan struktur sebagai berikut:

- **Key utama:** NIM mahasiswa, seperti A001, A002, dan A003.
- **Value:** Dictionary yang berisi nama, kelas, dan nilai mahasiswa.
- **Nama:** Menyimpan nama mahasiswa.
- **Kelas:** Menyimpan kelas mahasiswa.
- **Nilai:** Menyimpan nilai mahasiswa dalam bentuk angka.

Contoh struktur data:

```python
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78}
}
```

## Cara Menjalankan

1. Buka folder proyek menggunakan VS Code.
2. Buka terminal.
3. Jalankan perintah berikut:

```bash
python3 praktik/data_mahasiswa.py
```

4. Program akan menampilkan hasil pencarian, penambahan, pembaruan, rekap data mahasiswa, dan rata-rata nilai.

## Test Case

| No | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Cari NIM A003 | Data Citra ditampilkan | Data Citra ditampilkan | Berhasil |
| 2 | Cari NIM A999 | Data tidak ditemukan | Data tidak ditemukan | Berhasil |
| 3 | Ubah nilai A002 menjadi 82 | Nilai berubah menjadi 82 | Nilai berubah menjadi 82 | Berhasil |
| 4 | Tambahkan mahasiswa A006 | Data A006 tersedia | Data A006 tersedia | Berhasil |
| 5 | Tampilkan data menggunakan items() | Semua data ditampilkan | Semua 6 data ditampilkan | Berhasil |
| 6 | Hitung rata-rata nilai | Rata-rata 85.17 | Rata-rata 85.17 | Berhasil |

## Refleksi

Kesalahan yang dapat terjadi saat menggunakan dictionary adalah mengakses key yang tidak tersedia menggunakan tanda kurung siku `[]`. Kesalahan tersebut menyebabkan `KeyError`.

Contohnya:

```python
print(data_mahasiswa["A999"])
```

Kesalahan ini dapat diperbaiki menggunakan metode `get()` agar program tidak mengalami error.

```python
print(data_mahasiswa.get("A999", "Data tidak ditemukan"))
```

Dengan menggunakan `get()`, program akan menampilkan pesan "Data tidak ditemukan" apabila NIM tidak tersedia.

Melalui latihan ini, saya memahami penggunaan dictionary dalam
