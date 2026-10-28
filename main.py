from controllers.auth_controller import AuthController
from controllers.buku_controller import BukuController
from controllers.anggota_controller import AnggotaController

if __name__ == "__main__":
    app = AuthController()
    app.run()

    # OPSI TESTING (Opsional): 
    # Jika ingin melakukan testing langsung pada AnggotaController atau BukuController 
    # tanpa melalui Login, cukup beri tanda komentar (#) pada 2 baris AuthController di atas 
    # dan hapus tanda komentar pada baris controller yang ingin diuji di bawah ini:

    # app = AnggotaController()
    # app.run()

    # app = BukuController(user_role="admin")
    # app.run()
