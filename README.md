# Sistem Manajemen Perpustakaan

Sistem Manajemen Perpustakaan adalah aplikasi berbasis desktop yang dirancang menggunakan arsitektur **Model-View-Controller (MVC)** untuk mengelola data buku, anggota, serta transaksi peminjaman di perpustakaan. Aplikasi ini dilengkapi dengan antarmuka grafis (GUI) modern menggunakan `CustomTkinter`, integrasi basis data MySQL, serta pengujian otomatis (*unit testing*) dan integrasi berkelanjutan (*CI Pipeline*) menggunakan Pytest dan GitHub Actions.

---

## 📁 Struktur Direktori Project (MVC)

Berikut adalah struktur folder dan berkas dalam proyek ini:

```text
Modul3_RPL/
│
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml      # Konfigurasi GitHub Actions CI Pipeline
│
├── controllers/                 # Logika bisnis dan pengontrol alur aplikasi
│   ├── auth_controller.py
│   ├── buku_controller.py
│   └── anggota_controller.py
│
├── models/                      # Komunikasi dengan database & struktur data
│   ├── database.py              # Koneksi ke MySQL Database
│   ├── buku.py
│   └── anggota.py
│
├── views/                       # Antarmuka Pengguna (GUI CustomTkinter)
│   ├── login_view.py
│   ├── main_view.py
│   ├── buku_view.py
│   └── anggota_view.py
│
├── tests/                       # Unit testing menggunakan Pytest
│   ├── test_auth.py
│   ├── test_buku.py
│   └── test_anggota.py
│
├── dist/                        # Direktori output hasil kompilasi (.exe)
│   └── AplikasiPerpustakaan.exe
│
├── main.py                      # Entry point utama aplikasi
├── requirements.txt             # Daftar dependensi & pustaka Python
└── README.md                    # Dokumentasi teknis proyek

🛠️ Panduan Instalasi & Konfigurasi
1. Prasyarat Sistem
Python 3.10 atau versi lebih baru

MySQL Server (melalui Laragon / XAMPP)

Git

2. Kloning Repositori
Buka terminal/PowerShell dan jalankan perintah:
git clone [https://github.com/nayo890/Modul3_RPL.git](https://github.com/nayo890/Modul3_RPL.git)
cd Modul3_RPL

3. Membuat & Mengaktifkan Virtual Environment
# Membuat virtual environment
python -m venv env

# Mengaktifkan di Windows (PowerShell):
.\env\Scripts\Activate.ps1

# Mengaktifkan di Linux/macOS:
source env/bin/activate

4. Instalasi Dependensi
Instal seluruh pustaka yang diperlukan:
pip install -r requirements.txt

🗄️ Konfigurasi Database MySQL
Aktifkan service MySQL pada Laragon atau XAMPP Anda.

Buka alat manajemen basis data seperti phpMyAdmin atau DBeaver.

Buat database baru dengan nama db_perpustakaan:
CREATE DATABASE db_perpustakaan;

4. Sediakan tabel-tabel utama yang diperlukan (buku, anggota, users).

5. Sesuaikan konfigurasi kredensial basis data pada berkas models/database.py jika menggunakan kustomisasi port/password:

Host: localhost

User: root

Password: "" (kosong secara bawaan)

Database: db_perpustakaan

🚀 Cara Menjalankan Aplikasi
Menjalankan Aplikasi Utama (GUI)
Pastikan virtual environment sudah aktif dan service MySQL sedang berjalan, lalu jalankan perintah:
python main.py

Menjalankan Pengujian Otomatis (Unit Test & Linter)
Untuk memverifikasi bahwa seluruh modul dan fungsi berjalan dengan baik:

1. Menjalankan Linter (Flake8):
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics

2. Menjalankan Unit Test (Pytest):
pytest