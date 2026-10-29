import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from views.buku_view import BukuView

class LoginController:
    def __init__(self, view: LoginView):
        self.view = view
        self.model = UserModel()

        # Hubungkan tombol login di LoginView ke fungsi autentikasi
        self.view.btn_login.configure(command=self.proses_login)

    def proses_login(self):
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan Password tidak boleh kosong!")
            return

        # Cek autentikasi ke database melalui UserModel
        user = self.model.autentikasi(username, password)

        if user:
            messagebox.showinfo("Sukses", f"Selamat datang, {user['username']}!")
            
            # 1. Tutup jendela LoginView
            self.view.destroy()

            # 2. Impor BukuController di dalam metode untuk menghindari Circular Import
            from controllers.buku_controller import BukuController
            
            # 3. Buka BukuController dengan menyertakan role pengguna
            app = BukuController(user_role=user['role'])
            app.run()
        else:
            messagebox.showerror("Error", "Username atau Password salah!")