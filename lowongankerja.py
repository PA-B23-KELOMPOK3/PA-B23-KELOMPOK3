# built-in
import os
import math

# external
import mysql.connector
from pwinput import pwinput
from prettytable import PrettyTable

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # biar bisa langsung pakai list[index] macam array biasanya
    def __getitem__(self, index):
        current_index = 0
        current_node = self.head
        while current_node:
            if current_index == index:
                return current_node.data
            current_node = current_node.next
            current_index += 1
        raise IndexError("Index out of range")
    
    # biar bisa pakai for loop 
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    # biar bisa pakai len()
    def __len__(self):
        return self.length

class MySQLHandler:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connect()

    def connect(self):
        self.db = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )
        self.cursor = self.db.cursor()

    def execute(self, query, params=None):
        try:
            self.cursor.execute(query, params)
        except:
            print("Terjadi kesalahan saat menjalankan query")

    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except:
            None
    
    def fetchone(self):
        try:
            return self.cursor.fetchone()
        except:
            None
    
    def description(self):
        return self.cursor.description
    
    def commit(self):
        self.db.commit()

    def close(self):
        self.cursor.close()
        self.db.close()

class Admin:
    def login():
        clear()
        global admin_data
        print("Login admin")
        while True:
            username = inputhandler("username: ")
            sql.execute(f"select * from admin where username = '{username}'")
            row = sql.fetchone()

            if row:
                columns = [column[0] for column in sql.description()]
                admin_data = dict(zip(columns, row))
                while True:
                    password = inputhandler("password: ", "pw")
                    if password == admin_data["password"]:
                        clear()
                        print(color("Berhasil login\n", "green"))
                        Admin.menu()
                        return
                    else:
                        print(color("Password salah\n","red"))
            else:
                admin_data = {}
                print(color("Username tidak terdaftar\n", "red"))
            
    def profil():
        global admin_data
        sql.execute(f"SELECT * FROM admin WHERE id_admin = '{admin_data['id_admin']}'")
        row = sql.fetchone()
        if row:
            columns = [column[0] for column in sql.description()]
            admin_data = dict(zip(columns, row))

        print(f"\n{admin_data['username']}")
        print(f"ID: {admin_data['id_admin']}")
        print(f"Jabatan: {admin_data['jabatan']}")
        print("Hak akses: ")
        if admin_data['jabatan'] == 'admin1':
            print(color("  Hapus user", "green"))
            print(color("  Hapus perusahaan", "green"))
            print(color("  Hapus lowongan", "green"))
            print(color("  Hapus lamaran", "green"))
            print(color("  Setujui request lowongan", "green"))
        elif admin_data['jabatan'] == 'admin2':
            print(color("  Hapus user", "red"))
            print(color("  Hapus perusahaan", "red"))
            print(color("  Hapus lowongan", "green"))
            print(color("  Hapus lamaran", "green"))
            print(color("  Setujui request lowongan", "green"))
        elif admin_data['jabatan'] == 'admin3':
            print(color("  Hapus user", "red"))
            print(color("  Hapus perusahaan", "red"))
            print(color("  Hapus lowongan", "red"))
            print(color("  Hapus lamaran", "red"))
            print(color("  Setujui request lowongan", "green"))

    def menu():
        global admin_data
        # untuk pas keluar dari profil perusahaan/user
        global perusahaan_data
        global user_data
        while True:
            pil = choices([
                "Profil",
                "Kelola Lowongan",
                "Kelola User",
                "Kelola Perusahaan",
                "Kelola Lamaran",
                "Keluar"
            ])
            if pil == '1':
                clear()
                while True:
                    Admin.profil()
                    pil = choices([
                        "Edit data",
                        "Keluar"
                    ])
                    if pil == '1':
                        fields = {
                            "Username": ("username", 50),
                            "Password": ("password", 8)
                        }
                        edit('admin', admin_data, fields)

                    elif pil == '2':
                        clear()
                        break
                    else:
                        print("Pilihan tidak valid")
            elif pil == '2':
                clear()
                status = 'all'
                sort_key = 'id_lowongan'
                sort_order = 'desc'
                keyword = None
                while True:
                    # status yang kiri itu nama parameter, yang kanan variable
                    if keyword:
                        print(f"Hasil untuk '{keyword}'")
                    if status != 'all':
                        print("Status:", status)
                    Lowongan.list(status=status, sort_key=sort_key, sort_order=sort_order, keyword=keyword)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "List berdasarkan status",
                        "Kembali"
                    ])
                    if pil == '1':
                        Lowongan.pilih()
                        clear()
                        while True:
                            Lowongan.lihat(selected_lowongan)
                            if job["id_admin"] is not None:
                                pil = choices([
                                    "Kembali",
                                    color("Hapus lowongan", "red")
                                ])
                                if pil == '1':
                                    clear()
                                    break
                                elif pil == '2':
                                    if admin_data['jabatan'] != 'admin3':
                                        if inputhandler(f"Apakah anda yakin ingin menghapus lowongan ini? [{color('y', 'orange')}/{color('n', 'orange')}]: ").lower() == 'y':
                                            sql.execute(f"delete from lowongan where id_lowongan = {job['id_lowongan']}")
                                            # sql.commit()
                                            clear()
                                            print("Berhasil menghapus lowongan.")
                                            break
                                        else:
                                            clear()
                                    else:
                                        clear()
                                        print(color("Anda tidak memiliki hak akses untuk menghapus data ini.\n", "red"))
                            else:
                                pil = choices([
                                    "Setujui",
                                    "Kembali",
                                    color("Hapus lowongan", "red")
                                ])
                                if pil == '1':
                                    sql.execute(f"UPDATE lowongan SET id_admin = {admin_data['id_admin']} WHERE id_lowongan = {job['id_lowongan']}")
                                    # sql.commit()
                                    clear()
                                    print(color("Lowongan berhasil disetujui", "green"))
                                    break
                                elif pil == '2':
                                    clear()
                                    break
                                elif pil == '3':
                                    if admin_data['jabatan'] != 'admin3':
                                        if inputhandler(f"Apakah anda yakin ingin menghapus lowongan ini? [{color('y', 'orange')}/{color('n', 'orange')}]: ").lower() == 'y':
                                            sql.execute(f"delete from lowongan where id_lowongan = {job['id_lowongan']}")
                                            # sql.commit()
                                            clear()
                                            print("Berhasil menghapus lowongan.")
                                            break
                                    else:
                                        clear()
                                        print(color("Anda tidak memiliki hak akses untuk menghapus data ini.\n", "red"))
                    elif pil == '2':
                        clear()
                        print("\nUrut berdasarkan:")
                        key = choices([
                            "Posisi",
                            "Klasifikasi",
                            "ID lowongan",
                            "Rata-rata gaji"
                        ])
                        if key == '1':
                            sort_key = "posisi"
                        elif key == '2':
                            sort_key = "klasifikasi"
                        elif key == '3':
                            sort_key = "id_lowongan"
                        elif key == '4':
                            sort_key = "gaji"
                        
                        print("\nUrutan:")
                        order = choices(["Ascending", "Descending"])
                        if order == '1':
                            sort_order = "asc"
                        elif order == '2':
                            sort_order = "desc"
                        clear()
                    elif pil == '3':
                        keyword = inputhandler("Masukkan keyword: ")
                        clear()
                    elif pil == '4':
                        print("Pilih status")
                        status = choices([
                            "all",
                            "disetujui",
                            "pending",
                        ],"opt")
                        clear()
                    elif pil == '5':
                        clear()
                        break

                        
            elif pil == '3':
                clear()
                sort_key = "nama"
                sort_order = "asc"
                keyword = None
                while True:
                    if keyword:
                        print(f"Hasil untuk '{keyword}'")
                    User.list(sort_key=sort_key, sort_order=sort_order, keyword=keyword)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Kembali"
                    ])
                    if pil == '1':
                        User.pilih()
                        clear()
                        while True:
                            User.profil(selected_user)
                            pil = choices([
                                "Kembali",
                                color("Hapus user", "red")
                            ])
                            if pil == '1':
                                clear()
                                break
                            elif pil == '2':
                                if admin_data['jabatan'] == 'admin1':
                                    if inputhandler(f"Apakah anda yakin ingin menghapus user ini? [{color('y', 'orange')}/{color('n', 'orange')}]: ").lower() == 'y':
                                        sql.execute(f"delete from user where id_user = {user_data['id_user']}")
                                        # sql.commit()
                                        clear()
                                        print("Berhasil menghapus user.")
                                        break
                                    else:
                                        clear()
                                else:
                                    clear()
                                    print(color("Anda tidak memiliki hak akses untuk menghapus data ini.\n", "red"))
                        # supaya gak ke-overwrite jadi akun user
                        user_data ={}
                    
                    elif pil == '2':
                        clear()
                        print("\nUrut berdasarkan:")
                        key = choices(["Nama user", "ID User"])
                        if key == '1':
                            sort_key = "nama"
                        elif key == '2':
                            sort_key = "id_user"
                        
                        print("\nUrutan:")
                        order = choices(["Ascending", "Descending"])
                        if order == '1':
                            sort_order = "asc"
                        elif order == '2':
                            sort_order = "desc"
                        clear()
                    elif pil == '3':
                        keyword = inputhandler("Masukkan keyword: ")
                        clear()
                    elif pil == '4':
                        clear()
                        break
                        
            elif pil == '4':
                clear()
                sort_key = "id_perusahaan"
                sort_order = "desc"
                keyword = None
                while True:
                    Perusahaan.list(sort_key=sort_key, sort_order=sort_order, keyword=keyword)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Kembali"
                    ])
                    if pil == '1':
                        Perusahaan.pilih()
                        clear()
                        while True:
                            Perusahaan.profil(selected_perusahaan)
                            pil = choices([
                                "Kembali",
                                color("Hapus perusahaan", "red")
                            ])
                            if pil == '1':
                                clear()
                                break
                            elif pil == '2':
                                if admin_data['jabatan'] == 'admin1':
                                    if inputhandler(f"Apakah anda yakin ingin menghapus perusahaan ini? [{color('y', 'orange')}/{color('n', 'orange')}]: ").lower() == 'y':
                                        sql.execute(f"delete from perusahaan where id_perusahaan = {perusahaan_data['id_perusahaan']}")
                                        # sql.commit()
                                        print("Berhasil menghapus perusahaan.")
                                        clear()
                                        break
                                    else:
                                        clear()
                                else:
                                    clear()
                                    print(color("Anda tidak memiliki hak akses untuk menghapus data ini.\n", "red"))
                        # supaya gak ke-overwrite jadi akun perusahaan
                        perusahaan_data = {}
                        
                    elif pil == '2':
                        clear()
                        print("\nUrut berdasarkan:")
                        key = choices([
                            "Nama perusahaan",
                            "Alamat perusahaan",
                            "ID perusahaan"
                        ])
                        if key == '1':
                            sort_key = "nama_perusahaan"
                        elif key == '2':
                            sort_key = "alamat_perusahaan"
                        elif key == '3':
                            sort_key = "id_perusahaan"
                        
                        print("\nUrutan:")
                        order = choices(["Ascending", "Descending"])
                        if order == '1':
                            sort_order = "asc"
                        elif order == '2':
                            sort_order = "desc"
                        clear()
                    elif pil == '3':
                        keyword = inputhandler("\nMasukkan keyword: ")
                        clear()
                    elif pil == '4':
                        clear()
                        break

            
            elif pil == '5':
                clear()
                sort_key = 'id_lamaran'
                sort_order = 'desc'
                keyword = None
                while True:
                    Lamaran.list(sort_key=sort_key, sort_order=sort_order, keyword=keyword)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Kembali"
                    ])
                    if pil == '1':
                        Lamaran.pilih()
                        clear()
                        while True:
                            Lamaran.lihat(selected_lamaran)
                            pil = choices([
                                "Kembali",
                                color("Hapus lamaran", "red")
                            ])
                            if pil == '1':
                                break
                            elif pil == '2':
                                if admin_data['jabatan'] != 'admin3':
                                    if inputhandler(f"Apakah anda yakin ingin menghapus lamaran ini? [{color('y', 'orange')}/{color('n', 'orange')}]: ").lower() == 'y':
                                        sql.execute(f"delete from lamaran where id_lamaran = {lamaran_data['id_lamaran']}")
                                        # sql.commit()
                                        clear()
                                        print("Berhasil menghapus lamaran.")
                                        break
                                    else:
                                        clear()
                                        break
                                else:
                                    clear()
                                    print(color("Anda tidak memiliki hak akses untuk menghapus data ini.\n", "red"))

                    elif pil == '2':
                        clear()
                        print("\nUrut berdasarkan:")
                        key = choices([
                            "Nama pelamar",
                            "Nama perusahaan",
                            "Posisi pekerjaan",
                            "ID lamaran",
                            "ID user",
                            "ID perusahaan",
                            "ID lowongan"
                        ])
                        if key == '1':
                            sort_key = "nama"
                        elif key == '2':
                            sort_key = "nama_perusahaan"
                        elif key == '3':
                            sort_key = "posisi"
                        elif key == '4':
                            sort_key = "id_lamaran"
                        elif key == '5':
                            sort_key = "id_user"
                        elif key == '6':
                            sort_key = "id_perusahaan"
                        elif key == '7':
                            sort_key = "id_lowongan"
                        
                        print("\nUrutan:")
                        order = choices(["Ascending", "Descending"])
                        if order == '1':
                            sort_order = "asc"
                        elif order == '2':
                            sort_order = "desc"
                        print(sort_key, sort_order)
                        clear()
                    elif pil == '3':
                        keyword = inputhandler("\nMasukkan keyword: ")
                        clear()
                    elif pil == '4':
                        clear()
                        break

            
            elif pil == '6':
                clear()
                admin_data = {}
                break
        
    
class User:
    def register():
        global user_data
        sql.execute("select email from user")
        emails = [row[0] for row in sql.fetchall()]
        email = inputhandler("Masukkan email anda: ", min=11, max=25)
        if email not in emails:
            password = inputhandler("Masukkan password: ", "pw", min=1, max=8)
            nama = inputhandler("Masukkan nama anda: ", min=1, max=25)
            print("Pilih jenis kelamin anda:")
            jenis_kelamin = choices(["Laki-laki", "Perempuan"], "opt")
            no_telp = inputhandler("Masukkan nomor telepon anda: ", "digit", min=10, max=15)
            pendidikan = inputhandler("Masukkan pendidikan terakhir anda: ", min=2, max=25)
            alamat = inputhandler("Masukkan alamat anda: ", min=11, max=30)
            pengalaman = inputhandler("Masukkan pengalaman anda: ", min=5, max=500)
            keahlian = inputhandler("Masukkan keahlian anda: ", min=5, max=80)
            sql.execute(f"insert into user values(NULL, '{nama}', '{password}', '{email}', '{no_telp}', '{pendidikan}', '{pengalaman}', '{keahlian}', '{jenis_kelamin}', '{alamat}')")
            # sql.commit()
            sql.execute(f"SELECT * FROM user WHERE id_user = {sql.cursor.lastrowid}")
            row = sql.fetchone()
            columns = [column[0] for column in sql.description()]
            user_data = dict(zip(columns, row))
            clear()
            print(color("Akun berhasil dibuat", "green"))
            User.menu()
        else:
            clear()
            print(color("Email sudah dipakai. Silahkan gunakan email lain\n", "red"))
    def login():
        global user_data
        print("\nLogin user")
        while True:
            email = inputhandler("email: ")
            sql.execute(f"SELECT * FROM user WHERE email = '{email}'")
            row = sql.fetchone()
            columns = [column[0] for column in sql.description()]

            if row:
                user_data = dict(zip(columns, row))
                while True:
                    password = inputhandler("password: ", "pw")
                    if password == user_data["password"]:
                        clear()
                        print(color(f"Selamat datang {user_data['nama']}!\n", "green"))
                        User.menu()
                        return
                    else:
                        print("Password salah")
            else:
                user_data = {}
                print("Email tidak terdaftar")

    def profil(user_id=None):
        global user_data
        
        # jaga-jaga
        if user_id is None:
            if not user_data:
                print("Tidak ada pengguna yang terdaftar. Silakan login terlebih dahulu.")
                return
            user_id = user_data.get('id_user')

        sql.execute(f"SELECT * FROM user WHERE id_user = {user_id}")
        row = sql.fetchone()
        if not row:
            print("User dengan ID tersebut tidak ditemukan")
            return

        columns = [column[0] for column in sql.description()]
        user_data = dict(zip(columns, row))

        print(f"\n{user_data['nama']}")
        if admin_data:
            print(f"{user_data['id_user']}")
        print(f"Jenis kelamin: {user_data['jenis_kelamin']}")
        print(f"Alamat: {user_data['alamat']}")
        print(f"Email: {user_data['email']}")
        print(f"Nomor telepon: {user_data['no_telp']}")
        print(f"\nPendidikan terakhir: {user_data['pendidikan']}")
        print(f"Pengalaman:\n{user_data['pengalaman']}")
        print(f"Keahlian:\n{user_data['keahlian']}")
    
    def list(sort_key="id_user", sort_order='asc', keyword=None):
        global users
        global user
        sql.execute("select u.nama, u.email, u.id_user from user as u")
        rows = sql.fetchall()
        columns = [column[0] for column in sql.description()]
        users = LinkedList()

        # ubah data tiap user jadi dictionary
        for row in rows:
            # bikin dictionary dari row data pakai nama kolom
            row_data = dict(zip(columns, row))
            # append dictionary ke list
            users.append(row_data)
        
        users = quicksort(users, sort_key, sort_order)
        if keyword:
            users = jumpsearch(users, keyword)

        if len(users) > 0:
            # PrettyTable for perusahaan_data
            table = PrettyTable(["#", "Nama", "Email", "ID"])

            for i, user in enumerate(users, start=1):
                table.add_row([color(i, 'orange'), user['nama'], user['email'], user['id_user']])
            
            print(table)
        else:
            print("Tidak ada user untuk ditampilkan")
        
    def pilih():
        global selected_user
        while True:
            idx = inputhandler("Pilih: ", "int")-1
            if idx < len(users):
                selected_user = users[idx]['id_user']
                break
            else:
                print("Nomor tidak valid")

    def menu():
        global user_data
        while True:
            pil = choices([
                "Profil",
                "Lihat Lowongan",
                "Keluar"
            ])
            if pil == '1':
                clear()
                while True:
                    User.profil()
                    pil = choices([
                        "Edit Data",
                        "Keluar"
                    ])
                    if pil == '1':
                        fields = {
                            "Nama": ("nama", 25),
                            "Jenis kelamin": ("jenis_kelamin", 10),
                            "Alamat": ("alamat", 30),
                            "Email": ("email", 25),
                            "Password": ("password", 8),
                            "Nomor telepon": ("no_telp", 15),
                            "Pendidikan": ("pendidikan", 30),
                            "Pengalaman": ("pengalaman", 500),
                            "Keahlian": ("keahlian", 80)
                        }
                        edit('user', user_data, fields)

                    elif pil == '2':
                        clear()
                        break
                    else:
                        print("Pilihan tidak valid")
            elif pil == '2':
                clear()
                sort_key = "id_lowongan"
                sort_order = "desc"
                keyword = None
                while True:
                    Lowongan.list(status="disetujui", sort_key=sort_key, sort_order=sort_order, keyword=keyword)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Kembali"
                    ])
                    if pil == '1':
                        Lowongan.pilih()
                        clear()
                        Lowongan.lihat(selected_lowongan)
                        while True:
                            pil = choices([
                                "Lamaran cepat",
                                "Kembali"
                            ])
                            if pil == '1':
                                clear()
                                Lamaran.submit()
                                clear()
                                break
                            elif pil == '2':
                                clear()
                                break
                    elif pil == '2':
                        clear()
                        # 'Waktu ditambahkan' itu pakai ID hehe
                        print("\nUrut berdasarkan:")
                        key = choices([
                            "Posisi",
                            "Klasifikasi",
                            "Waktu ditambahkan",
                            "Rata-rata gaji"
                        ])
                        if key == '1':
                            sort_key = "posisi"
                        elif key == '2':
                            sort_key = "klasifikasi"
                        elif key == '3':
                            sort_key = "id_lowongan"
                        elif key == '4':
                            sort_key = "gaji"
                        
                        print("\nUrutan:")
                        order = choices(["Ascending", "Descending"])
                        if order == '1':
                            sort_order = "asc"
                        elif order == '2':
                            sort_order = "desc"
                        clear()
                    elif pil == '3':
                        keyword = inputhandler("Keyword: ")
                        clear()
                    elif pil == '4':
                        clear()
                        break
            elif pil == '3':
                clear()
                user_data = {}
                break

class Perusahaan:
    def register():
        global perusahaan_data
        sql.execute("select email_perusahaan from perusahaan")
        emails = [row[0] for row in sql.fetchall()]
        email = inputhandler("Masukkan email perusahaan anda: ", min=11, max=50)
        if email not in emails:
            password = inputhandler("Masukkan password: ", "pw", min=1, max=8)
            nama_perusahaan = inputhandler("Masukkan nama perusahaan: ", min=1, max=25)
            no_telp = inputhandler("Masukkan nomor telepon perusahaan: ", "digit", min=10, max=15)
            alamat = inputhandler("Masukkan alamat perusahaan: ", min=11, max=30)
            sql.execute(f"insert into perusahaan values(NULL, '{nama_perusahaan}', '{password}', '{no_telp}', '{email}', '{alamat}')")
            # sql.commit()
            sql.execute(f"SELECT * FROM perusahaan WHERE id_perusahaan = {sql.cursor.lastrowid}")
            row = sql.fetchone()
            columns = [column[0] for column in sql.description()]
            perusahaan_data = dict(zip(columns, row))
            clear()
            print(color("Akun berhasil dibuat", "green"))
            Perusahaan.menu()
        else:
            clear()
            print(color("Email sudah dipakai. Silahkan gunakan email lain\n", "red"))
    def login():
        global perusahaan_data
        print("\nLogin menggunakan akun perusahaan")
        while True:
            email = inputhandler("email: ")
            sql.execute(f"select * from perusahaan where email_perusahaan = '{email}'")
            row = sql.fetchone()
            columns = [column[0] for column in sql.description()]

            if row:
                perusahaan_data = dict(zip(columns, row))
                while True:
                    password = inputhandler("password: ", "pw")
                    if password == perusahaan_data["password"]:
                        clear()
                        print(color("Berhasil login!\n", "green"))
                        Perusahaan.menu()
                        return
                    else:
                        print("password salah")
            else:
                perusahaan_data = {}
                print("email gak terdaftar")

    def profil(perusahaan_id=None):
        global perusahaan_data
        
        if perusahaan_id is None:
            # jaga-jaga
            if not perusahaan_data:
                print("Tidak ada perusahaan yang terdaftar. Silakan login terlebih dahulu.")
                return
            else:
                perusahaan_id = perusahaan_data['id_perusahaan']

        sql.execute(f"SELECT * FROM perusahaan WHERE id_perusahaan = {perusahaan_id}")
        row = sql.fetchone()
        columns = [column[0] for column in sql.description()]
        perusahaan_data = dict(zip(columns, row))

        print(f"\n{color(perusahaan_data['nama_perusahaan'], 'cyan')}")
        print(f"alamat: {perusahaan_data['alamat_perusahaan']}")
        print(f"email: {perusahaan_data['email_perusahaan']}")
        print(f"nomor telepon: {perusahaan_data['no_telp']}")

    def list(sort_key='id_perusahaan', sort_order='desc', keyword=None):
        global companies
        global perusahaan
        
        sql.execute('''
            select p.id_perusahaan, p.nama_perusahaan, p.no_telp, p.email_perusahaan, p.alamat_perusahaan
            from perusahaan as p
        ''')
        rows = sql.fetchall()
        columns = [column[0] for column in sql.description()]
        companies = LinkedList()

        # ubah datanya jadi dictionary
        for row in rows:
            # bikin dictionary dari row data pakai nama kolom
            row_data = dict(zip(columns, row))
            companies.append(row_data)
        
        companies = quicksort(companies, sort_key, sort_order)
        if keyword:
            companies = jumpsearch(companies, keyword)

        if len(companies) > 0:
            for i, perusahaan in enumerate(companies, start=1):
                print(f"[{color(i, 'orange')}] {color(perusahaan['nama_perusahaan'], 'cyan')}")
                print(f"    {perusahaan['email_perusahaan']}")
                print(f"    ID: {perusahaan['id_perusahaan']}")
                print('-'*30)
        else:
            print("Tidak ada perusahaan untuk ditampilkan")
    
    def pilih():
        global selected_perusahaan
        while True:
            idx = inputhandler("Masukkan nomor urut perusahaan: ", "int")-1
            if idx < len(companies):
                selected_perusahaan = companies[idx]['id_perusahaan']
                break
            else:
                print("Nomor tidak valid")

    def menu():
        global perusahaan_data
        while True:
            pil = choices([
                "Cek lamaran",
                "Lihat profil perusahaan",
                "Kelola lowongan",
                "Keluar"
            ])
            if pil == '1':
                clear()
                sort_key = 'id_lamaran'
                sort_order = 'desc'
                keyword = None
                while True:
                    Lamaran.list(sort_key=sort_key, sort_order=sort_order, keyword=keyword)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Kembali"
                    ])
                    if pil == '1':
                        Lamaran.pilih()
                        clear()
                        Lamaran.lihat(selected_lamaran)
                        while True:
                            pil = choices([
                                "Kembali",
                                color("Hapus lamaran", "red")
                            ])
                            if pil == '1':
                                clear()
                                break
                            elif pil == '2':
                                if inputhandler(f"Apakah anda yakin ingin menghapus lamaran ini? [{color('y', 'orange')}/{color('n', 'orange')}]: ").lower() == 'y':
                                    sql.execute(f"delete from lamaran where id_lamaran = {lamaran_data['id_lamaran']}")
                                    # sql.commit()
                                    print("Berhasil menghapus lamaran.")
                                    break
                                else:
                                    clear()
                    elif pil == '2':
                        clear()
                        print("\nUrut berdasarkan:")
                        key = choices([
                            "Nama pelamar",
                            "Posisi pekerjaan",
                            "Waktu melamar"
                        ])
                        if key == '1':
                            sort_key = "nama"
                        elif key == '2':
                            sort_key = "posisi"
                        elif key == '3':
                            sort_key = "id_lamaran"
                        
                        print("\nUrutan:")
                        order = choices(["Ascending", "Descending"])
                        if order == '1':
                            sort_order = "asc"
                        elif order == '2':
                            sort_order = "desc"
                        clear()
                    elif pil == '3':
                        keyword = inputhandler("Masukkan keyword: ")
                        clear()
                    elif pil == '4':
                        clear()
                        break

            elif pil == '2':
                clear()
                while True:
                    Perusahaan.profil()
                    pil = choices([
                        "Edit data",
                        "Kembali"
                    ])
                    if pil == '1':
                        fields = {
                            "Nama perusahaan": ("nama_perusahaan", 50),
                            "Email perusahaan": ("email_perusahaan", 50),
                            "Password": ("password", 8),
                            "Alamat perusahaan": ("alamat_perusahaan", 255),
                        }
                        edit('perusahaan', perusahaan_data, fields)
                    elif pil == '2':
                        clear()
                        break
                    
            elif pil == '3':
                clear()
                sort_key = 'id_lowongan'
                sort_order = 'desc'
                keyword = None
                while True:
                    Lowongan.list(sort_key=sort_key, sort_order=sort_order, keyword=keyword)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Submit Lowongan Baru",
                        "Kembali"
                    ])
                    if pil == '1':
                        Lowongan.pilih()
                        clear()
                        while True:
                            Lowongan.lihat(selected_lowongan)
                            pil = choices([
                                "Edit",
                                "Kembali",
                                color("Hapus lowongan", "red")
                            ])
                            if pil == '1':
                                fields = {
                                    "Posisi pekerjaan": ("posisi", 50),
                                    "Klasifikasi pekerjaan": ("klasifikasi", 100),
                                    "Tipe pekerjaan": ("tipe", 15, 'tipe_choices'),
                                    "Deskripsi": ("deskripsi", 500),
                                    "Ketentuan": ("ketentuan", 500),
                                    "gaji": ("gaji", 11, 'int')
                                }
                                edit('lowongan', job, fields)
                            if pil == '2':
                                clear()
                                break
                            elif pil == '3':
                                if inputhandler(f"Apakah anda yakin ingin menghapus lowongan ini? [{color('y', 'orange')}/{color('n', 'orange')}]: ").lower() == 'y':
                                    sql.execute(f"delete from lowongan where id_lowongan = {job['id_lowongan']}")
                                    # sql.commit()
                                    clear()
                                    print("Berhasil menghapus lowongan.")
                                    break
                                else:
                                    clear()
                            
                    elif pil == '2':
                        clear()
                        print("\nUrut berdasarkan:")
                        key = choices([
                            "Posisi",
                            "Klasifikasi",
                            "Waktu ditambahkan",
                            "Rata-rata gaji"
                        ])
                        if key == '1':
                            sort_key = "posisi"
                        elif key == '2':
                            sort_key = "klasifikasi"
                        elif key == '3':
                            sort_key = "id_lowongan"
                        elif key == '4':
                            sort_key = "gaji"
                        
                        print("\nUrutan:")
                        order = choices(["Ascending", "Descending"])
                        if order == '1':
                            sort_order = "asc"
                        elif order == '2':
                            sort_order = "desc"
                        clear()
                    elif pil == '3':
                        keyword = inputhandler("Masukkan keyword: ")
                        clear()
                    elif pil == '4':
                        clear()
                        posisi = inputhandler("Posisi pekerjaan: ", max=50)
                        klasifikasi = inputhandler("Klasifikasi pekerjaan: ", max=100)
                        tipe = choices([
                            "Full time",
                            "Paruh waktu",
                            "Kontrak"
                        ], 'opt')
                        deskripsi = inputhandler("Deskripsi pekerjaan: ", max=500)
                        ketentuan = inputhandler("ketentuan pekerjaan: ", max=500)
                        gaji = inputhandler("Gaji pekerjaan: ", "int", 11)

                        sql.execute(f"insert into lowongan values (NULL, '{perusahaan_data['id_perusahaan']}', NULL, '{klasifikasi}', '{tipe}', '{deskripsi}', '{posisi}', '{ketentuan}', '{gaji}')")
                        clear()
                        # sql.commit()
                        print(color("Lowongan berhasil disubmit. Silahkan tunggu disetujui admin", "green"))
                    elif pil == '5':
                        clear()
                        break
            
            elif pil == '4':
                clear()
                perusahaan_data = {}
                break
            
class Lowongan:
    def list(id_perusahaan=None, status='all', sort_key='id_lowongan', sort_order='desc', keyword=None):
        global jobs
        global job
        # admin
        if id_perusahaan is not None:
            sql.execute(
                f'''
                SELECT lowongan.*, p.id_perusahaan, p.nama_perusahaan, p.no_telp, p.email_perusahaan, p.alamat_perusahaan, a.id_admin, a.username
                FROM lowongan 
                INNER JOIN perusahaan AS p ON lowongan.id_perusahaan = p.id_perusahaan
                INNER JOIN admin AS a ON lowongan.id_admin = a.id_admin 
                WHERE id_perusahaan = {id_perusahaan}
                '''
            )
        # admin/user
        elif not perusahaan_data:
            if status == "all":
                sql.execute(
                    '''
                    select lowongan.*, p.id_perusahaan, p.nama_perusahaan, p.no_telp, p.email_perusahaan, p.alamat_perusahaan, a.id_admin, a.username
                    from lowongan
                    INNER JOIN perusahaan AS p ON lowongan.id_perusahaan = p.id_perusahaan 
                    LEFT JOIN admin AS a ON lowongan.id_admin = a.id_admin
                    '''
                )
            elif status == "disetujui":
                sql.execute(
                    '''
                    select lowongan.*, p.id_perusahaan, p.nama_perusahaan, p.no_telp, p.email_perusahaan, p.alamat_perusahaan, a.id_admin, a.username
                    from lowongan 
                    INNER JOIN perusahaan AS p ON lowongan.id_perusahaan = p.id_perusahaan 
                    INNER JOIN admin AS a ON lowongan.id_admin = a.id_admin
                    '''
                )
            elif status == "pending":
                sql.execute(
                    '''
                    select lowongan.*, p.id_perusahaan, p.nama_perusahaan, p.no_telp, p.email_perusahaan, p.alamat_perusahaan
                    from lowongan 
                    INNER JOIN perusahaan AS p ON lowongan.id_perusahaan = p.id_perusahaan 
                    WHERE lowongan.id_admin IS NULL
                    '''
                )
        # perusahaan
        else:
            sql.execute(
                f'''
                select lowongan.*, a.id_admin, a.username
                from lowongan 
                LEFT JOIN admin AS a ON lowongan.id_admin = a.id_admin 
                where id_perusahaan = {perusahaan_data['id_perusahaan']}
                '''
            )

        rows = sql.fetchall()
        columns = [column[0] for column in sql.description()]
        jobs = LinkedList()

        # Populate jobs list regardless of conditions
        for row in rows:
            row_data = dict(zip(columns, row))
            jobs.append(row_data)

        jobs = quicksort(jobs, sort_key, sort_order)
        if keyword:
            jobs = jumpsearch(jobs, keyword)

        if len(jobs) > 0:
            if user_data:
                # Output for user
                for i, job in enumerate(jobs, start=1):
                    print(f"[{color(i, 'orange')}] {color(job['posisi'], 'cyan')}")
                    print(f"    {job['nama_perusahaan']}")
                    print(f"    {job['klasifikasi']}")
                    print('-'*30)
            elif perusahaan_data:
                # PrettyTable for perusahaan_data
                table = PrettyTable(["#", "ID", "Posisi", "Tipe", "Status"])
                table.align["Posisi"] = "l" 

                for i, job in enumerate(jobs, start=1):
                    if job['id_admin'] is not None:
                        status = color("Disetujui", "green")
                    else:
                        status = color("Pending", "yellow")
                    table.add_row([i, job['id_lowongan'], job['posisi'], job['tipe'], status])
                
                print(table)
            else:
                # PrettyTable for admin
                table = PrettyTable(["#", "ID", "Posisi", "Perusahaan", "Status"])
                table.align["Posisi"] = "l" 

                for i, job in enumerate(jobs, start=1):
                    if job['id_admin'] is not None:
                        status = color("Disetujui", "green")
                    else:
                        status = color("Pending", "yellow")
                    table.add_row([i, job['id_lowongan'], job['posisi'], job['nama_perusahaan'], status])
            
                print(table)
        else:
            print("Tidak ada lowongan untuk ditampilkan")


    def lihat(id_lowongan):
        global jobs
        global job

        sql.execute(f"SELECT * FROM lowongan INNER JOIN perusahaan ON lowongan.id_perusahaan = perusahaan.id_perusahaan LEFT JOIN admin on lowongan.id_admin = admin.id_admin WHERE id_lowongan = '{id_lowongan}'")
        row = sql.fetchone()
        if row:
            columns = [column[0] for column in sql.description()]
            job = dict(zip(columns, row))

        print(f"\n{color(job['posisi'], 'cyan')}")
        if not perusahaan_data:
            print(f"{job['nama_perusahaan']}")
            print(f"Alamat: {job['alamat_perusahaan']}")
        print(f"Klasifikasi: {job['klasifikasi']}")
        print(f"Tipe: {job['tipe']}")
        print(f"Rata-rata gaji: {job['gaji']}")
        print(f"\nDeskripsi:\n{job['deskripsi']}")
        print(f"\nKetentuan:\n{job['ketentuan']}")
        if admin_data:
            print(f"\nID lowongan: {job['id_lowongan']}")
            print(f"ID perusahaan: {job['id_lowongan']}")
            if job['id_admin'] is not None:
                print(f"Disetujui oleh: {job['username']} ({job['id_admin']})")
            else:
                print(color("Menunggu persetujuan", "yellow"))
        return

    def pilih():
        global selected_lowongan
        while True:
            idx = inputhandler("Pilih: ", "int")-1
            if idx < len(jobs):
                selected_lowongan = jobs[idx]['id_lowongan']
                break
            else:
                print("Nomor tidak valid")
    
class Lamaran:
    def list(id_perusahaan=None, sort_key='id_lamaran', sort_order='desc', keyword=None):
        global lamarans
        query = f'''
                SELECT lamaran.*, user.nama, perusahaan.nama_perusahaan, lowongan.posisi 
                FROM lamaran 
                JOIN user ON lamaran.id_user = user.id_user 
                JOIN lowongan ON lamaran.id_lowongan = lowongan.id_lowongan 
                JOIN perusahaan ON lamaran.id_perusahaan = perusahaan.id_perusahaan 
                '''
        if perusahaan_data:
            id_perusahaan = perusahaan_data['id_perusahaan']

        if id_perusahaan:
            query += f"WHERE perusahaan.id_perusahaan = {id_perusahaan}"

        sql.execute(query)
        rows = sql.fetchall()
        columns = [column[0] for column in sql.description()]
        lamarans = LinkedList()

        # ubah datanya jadi dictionary
        for row in rows:
            # bikin dictionary dari row data pakai nama kolom
            row_data = dict(zip(columns, row))
            lamarans.append(row_data)

        lamarans = quicksort(lamarans, sort_key, sort_order)
        if keyword:
            lamarans = jumpsearch(lamarans, keyword)

        if len(lamarans) > 0:
            if perusahaan_data:
                table = PrettyTable(["No", "ID Lamaran", "Pelamar", "Posisi"])
                table.align["Posisi"] = "l" 

                for i, lamaran in enumerate(lamarans, start=1):
                    table.add_row([i, lamaran['id_lamaran'], lamaran['nama'], lamaran['posisi']])

                print(table)
            else:
                table = PrettyTable(["No", "ID Lamaran", "Pelamar", "Perusahaan", "Posisi"])
                table.align["Posisi"] = "l" 

                for i, lamaran in enumerate(lamarans, start=1):
                    table.add_row([i, lamaran['id_lamaran'], lamaran['nama'], lamaran['nama_perusahaan'], lamaran['posisi']])

                print(table)
        else:
            print("Tidak ada lamaran untuk ditampilkan")
    
    def pilih():
        global selected_lamaran
        while True:
            idx = inputhandler("Pilih: ", "int")-1
            if idx < len(lamarans):
                selected_lamaran = lamarans[idx]['id_lamaran']
                break
            else:
                print("Nomor tidak valid")

    def lihat(id_lamaran=None):
        global lamarans
        global lamaran_data
        sql.execute(f'''
            SELECT lamaran.*, user.*, perusahaan.*, lowongan.posisi 
            FROM lamaran 
            JOIN user ON lamaran.id_user = user.id_user 
            JOIN lowongan ON lamaran.id_lowongan = lowongan.id_lowongan 
            JOIN perusahaan ON lamaran.id_perusahaan = perusahaan.id_perusahaan 
            WHERE id_lamaran = {id_lamaran}
        ''')
        row = sql.fetchone()
        columns = [column[0] for column in sql.description()]
        lamaran_data = dict(zip(columns, row))
        
        if admin_data:
            print(f"Nama perusahaan: {lamaran_data['nama_perusahaan']}")
            print(f"Posisi: {lamaran_data['posisi']}")
            print(f"Nama Pelamar: {color(lamaran_data['nama'], 'cyan')}")
        else:
            print(f"{color(lamaran_data['nama'], 'cyan')}")
        print(f"Jenis Kelamin: {lamaran_data['jenis_kelamin']}")
        print(f"Alamat: {lamaran_data['alamat']}")
        print(f"Email: {lamaran_data['email']}")
        print(f"Nomor Telepon: {lamaran_data['no_telp']}")
        print(f"\nSumber informasi: {lamaran_data['sumber_informasi']}")
        print(f"Pengalaman relevan:\n{lamaran_data['pengalaman_relevan']}")
        print(f"\n{lamaran_data['deskripsi']}")

        if admin_data:
            print(f"ID lamaran: {lamaran_data['id_lamaran']}")
            print(f"ID user: {lamaran_data['id_user']}")
            print(f"ID perusahaan: {lamaran_data['id_perusahaan']}")
            print(f"ID lowongan: {lamaran_data['id_lowongan']}")

    def submit():
        print("Sumber Informasi")
        sumber = choices([
            'Dari aplikasi ini',
            'Iklan di internet',
            'Diberitahu kerabat',
            'Lainnya'
        ], 'opt')

        pengalaman_relevan = inputhandler("\nPegalaman relevan:\n", min=10, max=500)
        deskripsi = inputhandler("\nDeskripsi:\n", min=10, max=1500)

        sql.execute(f"insert into lamaran values (NULL, {job['id_perusahaan']}, {user_data['id_user']}, {job['id_lowongan']}, '{sumber}', '{pengalaman_relevan}', '{deskripsi}')")
        # sql.commit()
        
        print("Lamaran berhasil disubmit. Silahkan cek email anda secara berkala")

# Global functions

# mindahin output jadi ke kiri atas (mirip os.system('cls') tapi gak beneran ngehapus)
def clear():
    print('\n'*40)
    print('\033[H')

def edit(table, old_data, fields):
    clear()
    print(color("(Kosongkan untuk menggunakan data lama)", 'blue'))
    updates = [] 
    for prompt, (field, max, *inputtype) in fields.items():
        print(f"\n{color(f'{prompt} lama', 'purple')}: {old_data[field]}")
        if inputtype:
            inputtype = inputtype[0]
        else:
            inputtype = 'str'

        if inputtype == 'tipe_choices':
            new_data = choices([
                "Full time",
                "Paruh waktu",
                "Kontrak"
            ], 'opt')
        elif inputtype == 'kelamin_choices':
            new_data = choices([
                "Laki-laki",
                "Perempuan"
            ], 'opt')
        else:
            new_data = inputhandler(f"{color(f'{prompt} baru', 'yellow')}: ", inputtype, max=max)

        if new_data:
            updates.append(f"{field} = '{new_data}'")

    query = f"update {table} set "
    query += ", ".join(updates)
    query += f" where id_{table} = {old_data[f'id_{table}']}"
    if updates != []:
        sql.execute(query)
    clear()
    print(color("Data berhasil diubah", "green"))
    # sql.commit()

def quicksort(arr, key=None, order='desc'):
    if len(arr) <= 1:
        return arr
    else:
        if key:
            # akses pivot value pakai key function kalau memang dipakai
            if callable(key):
                pivot_value = key(arr[len(arr) // 2])  # pakai key function ke tuple
                less = [x for x in arr if key(x) < pivot_value]
                equal = [x for x in arr if key(x) == pivot_value]
                greater = [x for x in arr if key(x) > pivot_value]
            else:
                pivot_value = arr[len(arr) // 2][key]  # ekstrak pakai key biasa kalau key-nya string
                less = [x for x in arr if x[key] < pivot_value]
                equal = [x for x in arr if x[key] == pivot_value]
                greater = [x for x in arr if x[key] > pivot_value]
        else:
            pivot = arr[len(arr) // 2]
            less = [x for x in arr if x < pivot]
            equal = [x for x in arr if x == pivot]

        if order == 'desc':
            return quicksort(greater, key, order) + equal + quicksort(less, key, order)
        else:
            return quicksort(less, key, order) + equal + quicksort(greater, key, order)

# custom jumpsearch pakai list dict dan bisa nyari per-kata
def jumpsearch(entries, keyword):
    # pecah entries per-kata jadi items, bikin list tuple yang isinya index entry sama items, cth: [(0: hi), (0: guys), (1: hello)]
    items = []
    for idx, entry_dict in enumerate(entries):
        for key, entry in entry_dict.items():
            for item in str(entry).lower().split():  # lower() = ubah ke lowercase. split() =  misah string jadi array
                items.append((idx, item))

    # urutkan items
    quicksort(items, key=lambda x: x[1])

    result = []
    step = int(math.sqrt(len(items)))  # size untuk step, pakai akar dari panjang items
    
    # pecah keyword per-kata
    # strip() = hapus spasi di awal dan akhir
    targets = keyword.lower().strip().split()
    for target in targets:
        for i in range(len(items)):
            current_index = i
            if current_index < len(items):
                current_item = items[current_index][1]
            else:
                break
            
            # maju sampai current_item lebih besar dari target
            while current_item < target and current_index < len(items) - step:
                current_index += step
                if current_index < len(items):
                    current_item = items[current_index][1]
                else:
                    break
            
            # mundur 1 langkah sampai current_item kurang atau sama dengan target
            while current_item >= target and current_index >= 0:
                if current_item == target:
                    result.append(items[current_index][0])
                current_index -= 1
                if current_index >= 0 and current_index < len(items):
                    current_item = items[current_index][1]
                else:
                    break
    
    # hilangin duplikat, return semua entry yang cocok
    return [entries[i] for i in set(result)]

def execute_query():
    try:
        None
    except:
        None
# handle inputs
def inputhandler(prompt, inputtype="str", max=None, min=None):
    while True:
        try:
            if inputtype == "str":
                userinput = input(prompt).strip()
            elif inputtype == "int":
                userinput = int(input(prompt))
            elif inputtype == "digit":
                userinput = input(prompt).strip()
                if not userinput.isdigit():
                    print("Input hanya bisa berupa angka\n")
                    continue
            elif inputtype == "pw":
                userinput = pwinput(prompt).strip()
            
            # jika parameter max dipakai (gak kosong) dan panjang input lebih dari max
            if max is not None and len(str(userinput)) > max:
                print(f"Input terlalu panjang. Maksimum panjang adalah {max} karakter.\n")
                continue
            
            if min is not None and len(str(userinput)) < min:
                print(f"Input terlalu pendek. Minimum panjang adalah {min} karakter.\n")
                continue
                
            return userinput
        except KeyboardInterrupt:
            print("Terdeteksi interupsi\n")
        except ValueError:
            print("Input hanya bisa berupa integer\n")
        except mysql.connector.errors.ProgrammingError:
            print("wahyu kontol\n")
        except Exception as error:
            print(f"Apa lah dia {error}\n")
        

# warnain teks
def color(text, color_name):
    # ANSI color escape
    color_codes = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'orange': '\033[38;5;208m'
    }

    # cek color_name valid atau nggak
    if color_name.lower() not in color_codes:
        raise KeyError(f"Warna {color_name} gak didukung. Cuman ini yang ada: {', '.join(color_codes.keys())}")

    # aplikasikan warna ke teks
    color_code = color_codes[color_name.lower()]
    reset_code = '\033[0m'  # ANSI escape untuk reset ke default
    colored_text = f"{color_code}{text}{reset_code}"

    return colored_text

# Handle choices (pilihan)
# re = 'num': ouputnya angka optionnya
# re = 'opt': ouputnya teks optionnya
def choices(options, re='num'):
    for idx, option in enumerate(options, start=1):
        print(f"[{color(idx, 'orange')}] {option}")
    while True:
        choice = inputhandler("\nMasukkan pilihan: ", "digit")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            if re == 'num':
                return choice
            elif re == 'opt':
                return options[int(choice)-1]
        else:
            print(color("Pilihan tidak valid", "red"))

# buat bikin banner (judul) biar serasi
def banner(text):
    # definisikan panjang banner
    banner_length = 65
    text_length = len(text)
    # hitung berapa karakter '=' yang diperlukan
    padding = banner_length - text_length
    # dibagi jadi dua untuk kanan kiri
    left_padding = padding // 2
    right_padding = padding - left_padding
    # tinggal dikalikan pakai jumlah kanan kiri
    return f"{'=' * left_padding} {text} {'=' * right_padding}"

# Login
def login():
    clear()
    while True:
        print(f"\n{banner('LOGIN')}")
        pil = choices([
            "Login admin",
            "Login user",
            "Login menggunakan akun perusahaan",
            "Kembali"
        ])

        if pil == '1':
            Admin.login()
        elif pil == '2':
            User.login()
        elif pil == '3':
            Perusahaan.login()
        elif pil == '4':
            break
        
#Regist
def register():
    clear()
    while True:
        print(f"\n{banner('REGISTRASI')}")
        pil = choices([
            "Registrasi akun user",
            "Registrasi akun perusahaan",
            "Kembali"
        ])

        if pil == '1':
            clear()
            User.register()
        elif pil == '2':
            clear()
            Perusahaan.register()
        elif pil == '3':
            break

sql = MySQLHandler('root', '', 'localhost', 'lowongankerja')

# predefine untuk pas login biar gak error
user_data = {}
admin_data = {}
perusahaan_data = {}

#main
os.system("") # entah kenapa kalau gak pakai ini warna teksnya gak muncul di beberapa device

while True:
    clear()
    print(f"\n{banner('PROGRAM LOWONGAN KERJA UNTUK SEMUA')}")
    pil = choices([
        "Login",
        "Register",
        "Keluar"
    ])

    if pil == '1':
        login()
    elif pil == '2':
        register()
    elif pil == '3':
        break
    
