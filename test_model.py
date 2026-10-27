#Naila Nurul Lathifah_010
from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("--- 1. MENAMBAHKAN DATA BUKU ---")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke database!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n--- 2. DAFTAR BUKU (SETELAH CREATE) ---")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# 3. Menguji fungsi Update (memperbarui buku)
# Ambil ID buku terakhir yang baru ditambahkan
if daftar_buku:
    target_id = daftar_buku[-1]['id_buku']
    
    print("\n--- 3. MEMPERBARUI DATA BUKU ---")
    model.update_buku(target_id, "Pemrograman Python MVC (Edisi Revisi)", "Guido van Rossum", 2025)
    print(f"Data buku dengan ID {target_id} berhasil diperbarui!")

    # Tampilkan ulang untuk memastikan data berubah
    print("\n--- DAFTAR BUKU (SETELAH UPDATE) ---")
    for buku in model.get_all_buku():
        print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

    # 4. Menguji fungsi Delete (menghapus buku)
    print("\n--- 4. MENGHAPUS DATA BUKU ---")
    model.delete_buku(target_id)
    print(f"Data buku dengan ID {target_id} berhasil dihapus!")

    # Tampilkan ulang untuk memastikan data terhapus
    print("\n--- DAFTAR BUKU (SETELAH DELETE) ---")
    for buku in model.get_all_buku():
        print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")