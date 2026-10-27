import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from models.buku_model import BukuModel

from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

def test_get_all_buku_berhasil():
    model = BukuModel()

    # Mock koneksi dan cursor database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    
    # Menyiapkan dummy data yang seolah-olah dikembalikan dari database
    dummy_data = [
        {"id_buku": 1, "judul": "Buku A", "penulis": "Penulis A", "tahun_terbit": 2020},
        {"id_buku": 2, "judul": "Buku B", "penulis": "Penulis B", "tahun_terbit": 2021}
    ]
    mock_cursor.fetchall.return_value = dummy_data
    model.conn.cursor.return_value = mock_cursor

    # Panggil fungsi get_all_buku()
    hasil = model.get_all_buku()

    # Verifikasi hasil kembalian
    assert hasil == dummy_data
    assert isinstance(hasil, list)
    assert len(hasil) == 2
    
    # Verifikasi cursor execute & fetchall dipanggil
    mock_cursor.execute.assert_called_once()
    mock_cursor.fetchall.assert_called_once()