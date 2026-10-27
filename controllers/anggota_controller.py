import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.selected_id = None

        # Binding Tombol Form
        if hasattr(self.view, 'btn_simpan'):
            self.view.btn_simpan.configure(command=self.simpan_data)

        if hasattr(self.view, 'btn_update'):
            self.view.btn_update.configure(command=self.perbarui_data)

        if hasattr(self.view, 'btn_hapus'):
            self.view.btn_hapus.configure(command=self.hapus_data)

        # Binding Event Klik Baris Tabel
        self.view.tabel.bind("<<TreeviewSelect>>", self.pada_baris_diklik)

        # Muat Data Awal dari Database
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()

        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(
                anggota.get('id_anggota', anggota.get('id', '')),
                anggota['nama'],
                anggota['alamat']
            ))

    def pada_baris_diklik(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            data = self.view.tabel.item(selected_item[0])['values']
            if data:
                self.selected_id = data[0]

                self.view.entry_id.delete(0, 'end')
                self.view.entry_id.insert(0, str(data[0]))

                self.view.entry_nama.delete(0, 'end')
                self.view.entry_nama.insert(0, str(data[1]))

                self.view.entry_alamat.delete(0, 'end')
                self.view.entry_alamat.insert(0, str(data[2]))

    def bersihkan_form(self):
        self.selected_id = None
        self.view.entry_id.delete(0, 'end')
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data anggota.")

    def perbarui_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data anggota dari tabel terlebih dahulu!")
            return

        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.update_anggota(self.selected_id, nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data anggota.")

    def hapus_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data anggota dari tabel terlebih dahulu!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data anggota ini?")
        if konfirmasi:
            berhasil = self.model.delete_anggota(self.selected_id)

            if berhasil:
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data anggota.")

    def run(self):
        self.view.mainloop()