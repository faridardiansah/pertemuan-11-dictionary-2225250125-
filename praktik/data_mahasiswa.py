# Latihan 2: Sistem Data Mahasiswa
# Pertemuan 11 - Dictionary

# Fungsi mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(data, nim):
    return data.get(nim, "Data tidak ditemukan")


# Fungsi menghitung rata-rata nilai
def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0
    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


# Data awal mahasiswa
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


# 1. Pencarian mahasiswa yang tersedia
print("=== Pencarian Mahasiswa ===")
print("NIM A003:", cari_mahasiswa(data_mahasiswa, "A003"))


# 2. Pencarian mahasiswa yang tidak tersedia
print("\n=== Pencarian NIM Tidak Ada ===")
print("NIM A999:", cari_mahasiswa(data_mahasiswa, "A999"))


# 3. Menambahkan mahasiswa baru
print("\n=== Menambahkan Mahasiswa ===")

data_mahasiswa["A006"] = {
    "nama": "Farid",
    "kelas": "A",
    "nilai": 90
}

print("Mahasiswa A006 berhasil ditambahkan")
print(data_mahasiswa["A006"])


# 4. Memperbarui nilai mahasiswa
print("\n=== Memperbarui Nilai ===")

data_mahasiswa["A002"]["nilai"] = 82

print("Nilai A002 berhasil diperbarui")
print(data_mahasiswa["A002"])


# 5. Menampilkan seluruh data mahasiswa
print("\n=== Rekap Data Mahasiswa ===")

for nim, mahasiswa in data_mahasiswa.items():
    print(f"NIM   : {nim}")
    print(f"Nama  : {mahasiswa['nama']}")
    print(f"Kelas : {mahasiswa['kelas']}")
    print(f"Nilai : {mahasiswa['nilai']}")
    print("------------------------")


# 6. Menghitung rata-rata nilai
print("\n=== Rata-Rata Nilai Mahasiswa ===")

rata_rata = rata_rata_nilai(data_mahasiswa)

print(f"Rata-rata nilai: {rata_rata:.2f}")