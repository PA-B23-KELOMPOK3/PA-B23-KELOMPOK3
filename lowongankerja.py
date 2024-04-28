# built-in
import os
os.system("")
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

class Admin:
    def login():
        global admin_data
        while True:
            username = inputhandler("username: ")
            cursor.execute(f"select * from admin where username = '{username}'")
            row = cursor.fetchone()
            columns = [column[0] for column in cursor.description]

            if row:
                admin_data = dict(zip(columns, row))
                while True:
                    password = inputhandler("password: ", "pw")
                    if password == admin_data["password"]:
                        Admin.menu()
                        return
                    else:
                        print(color("Password salah\n","red"))
            else:
                admin_data = {}
                print(color("Username tidak terdaftar\n", "red"))
            
    def profil():
        print(f"\n{admin_data['username']}")
        print(f"ID: {admin_data['id_admin']}")

    def menu():
        global admin_data
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
                while True:
                    Admin.profil()
                    pil = choices([
                        "Edit data",
                        "Keluar"
                    ])
                    if pil == '1':
                        None
                    elif pil == '2':
                        break
                    else:
                        print("Pilihan tidak valid")
            elif pil == '2':
                status = 'all'
                while True:
                    # status yang kiri itu nama parameter, yang kanan variable
                    Lowongan.list(status=status)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "List berdasarkan status",
                        "Kembali"
                    ])
                    if pil == '1':
                        Lowongan.pilih()
                        while True:
                            if job["id_admin"] is not None:
                                pil = choices([
                                    "Kembali",
                                    color("Hapus lowongan", "red")
                                ])
                                if pil == '1':
                                    break
                                elif pil == '2':
                                    None
                            else:
                                pil = choices([
                                    "Setujui",
                                    "Kembali",
                                    color("Hapus lowongan", "red")
                                ])
                                if pil == '1':
                                    cursor.execute(f"UPDATE lowongan SET id_admin = {admin_data['id_admin']} WHERE id_lowongan = {job['id_lowongan']}")
                                    db.commit()
                                    clear()
                                    print(color("Lowongan berhasil disetujui", "green"))
                                    break
                                elif pil == '2':
                                    break
                                elif pil == '3':
                                    None
                    elif pil == '2':
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
                    elif pil == '3':
                        None
                    elif pil == '4':
                        print("Pilih status")
                        status = choices([
                            "all",
                            "disetujui",
                            "pending",
                        ],"opt")
                    elif pil == '5':
                        break

                        
            elif pil == '3':
                sort_key = "nama"
                sort_order = "asc"
                while True:
                    User.list(sort_key=sort_key, sort_order=sort_order)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Kembali"
                    ])
                    if pil == '1':
                        User.pilih()
                        while True:
                            pil = choices([
                                "Kembali",
                                color("Hapus user", "red")
                            ])
                            if pil == '1':
                                break
                            elif pil == '2':
                                None
                        break
                    
                    elif pil == '2':
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
                        
                    elif pil == '3':
                        None
                    elif pil == '4':
                        break
                        
            elif pil == '4':
                sort_key = "id_perusahaan"
                sort_order = "desc"
                while True:
                    Perusahaan.list(sort_key=sort_key, sort_order=sort_order)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Kembali"
                    ])
                    if pil == '1':
                        Perusahaan.pilih()
                        while True:
                            pil = choices([
                                "Kembali",
                                color("Hapus perusahaan", "red")
                            ])
                            if pil == '1':
                                break
                            elif pil == '2':
                                None
                        
                    elif pil == '2':
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
                    elif pil == '3':
                        None
                    elif pil == '4':
                        break

            
            elif pil == '5':
                sort_key = 'id_lamaran'
                sort_order = 'desc'
                while True:
                    Lamaran.list(sort_key=sort_key, sort_order=sort_order)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Kembali"
                    ])
                    if pil == '1':
                        Lamaran.pilih()
                        while True:
                            pil = choices([
                                "Kembali",
                                color("Hapus lamaran", "red")
                            ])
                            if pil == '1':
                                break
                            elif pil == '2':
                                None

                    elif pil == '2':
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
                    elif pil == '3':
                        None
                    elif pil == '4':
                        break

            
            elif pil == '6':
                admin_data = {}
                break
        
    
class User:
    def login():
        global user_data
        print("\nLogin user")
        while True:
            email = inputhandler("email: ")
            cursor.execute(f"SELECT * FROM user WHERE email = '{email}'")
            row = cursor.fetchone()
            columns = [column[0] for column in cursor.description]

            if row:
                user_data = dict(zip(columns, row))
                while True:
                    password = inputhandler("password: ", "pw")
                    if password == user_data["password"]:
                        clear()
                        print(f"Selamat datang {user_data['nama']}!")
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

        cursor.execute(f"SELECT * FROM user WHERE id_user = {user_id}")
        row = cursor.fetchone()
        if not row:
            print("User dengan ID tersebut tidak ditemukan")
            return

        columns = [column[0] for column in cursor.description]
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
    
    def list(sort_key="id_user", sort_order='asc'):
        global users
        global user
        cursor.execute("select * from user")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        users = LinkedList()

        # ubah data tiap user jadi dictionary
        for row in rows:
            # bikin dictionary dari row data pakai nama kolom
            row_data = dict(zip(columns, row))
            # append dictionary ke list
            users.append(row_data)
        
        users = quicksort(users, sort_key, sort_order)

        # PrettyTable for perusahaan_data
        table = PrettyTable(["#", "Nama", "Email", "ID"])

        for i, user in enumerate(users, start=1):
            table.add_row([color(i, 'orange'), user['nama'], user['email'], user['id_user']])
        
        print(table)
        
    def pilih():
        while True:
            idx = inputhandler("Pilih: ", "int")-1
            if idx < len(users):
                User.profil(users[idx]['id_user'])
                break
            else:
                print("Nomor tidak valid")

    def menu():
        while True:
            pil = choices([
                "Profil",
                "Lihat Lowongan",
                "Keluar"
            ])
            if pil == '1':
                while True:
                    User.profil()
                    pil = choices([
                        "Edit Data",
                        "Keluar"
                    ])
                    if pil == '1':
                        None
                    elif pil == '2':
                        break
                    else:
                        print("Pilihan tidak valid")
            elif pil == '2':
                sort_key = "id_lowongan"
                sort_order = "desc"
                while True:
                    Lowongan.list(status="disetujui", sort_key=sort_key, sort_order=sort_order)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Kembali"
                    ])
                    if pil == '1':
                        Lowongan.pilih()
                        while True:
                            pil = choices([
                                "Lamaran cepat",
                                "Kembali"
                            ])
                            if pil == '1':
                                Lamaran.submit()
                                break
                            elif pil == '2':
                                break
                            else:
                                print(color("Pilihan tidak valid\n", "red"))
                    elif pil == '2':
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
                    elif pil == '3':
                        None
                    elif pil == '4':
                        break
            elif pil == '3':
                global user_data
                user_data = {}
                break

class Perusahaan:
    def login():
        global perusahaan_data
        print("\nLogin menggunakan akun perusahaan")
        while True:
            email = inputhandler("email: ")
            cursor.execute(f"select * from perusahaan where email_perusahaan = '{email}'")
            row = cursor.fetchone()
            columns = [column[0] for column in cursor.description]

            if row:
                perusahaan_data = dict(zip(columns, row))
                while True:
                    password = inputhandler("password: ", "pw")
                    if password == perusahaan_data["password"]:
                        Perusahaan.menu()
                        return
                    else:
                        print("password salah")
            else:
                perusahaan_data = {}
                print("email gak terdaftar")

    def profil(perusahaan_id=None):
        global perusahaan_data
        print(perusahaan_data)
        # jaga-jaga
        if perusahaan_id is None:
            if not perusahaan_data:
                print("Tidak ada perusahaan yang terdaftar. Silakan login terlebih dahulu.")
                return
            else:
                perusahaan_id = perusahaan_data['id_perusahaan']
        print("id", perusahaan_id)

        cursor.execute(f"SELECT * FROM perusahaan WHERE id_perusahaan = {perusahaan_id}")
        row = cursor.fetchone()
        columns = [column[0] for column in cursor.description]
        perusahaan_data = dict(zip(columns, row))

        print(f"\n{color(perusahaan_data['nama_perusahaan'], 'cyan')}")
        print(f"alamat: {perusahaan_data['alamat_perusahaan']}")
        print(f"email: {perusahaan_data['email_perusahaan']}")
        print(f"nomor telepon: {perusahaan_data['no_telp']}")

    def list(sort_key='id_perusahaan', sort_order='desc'):
        global companies
        global perusahaan
        
        cursor.execute("select * from perusahaan")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        companies = LinkedList()

        # ubah datanya jadi dictionary
        for row in rows:
            # bikin dictionary dari row data pakai nama kolom
            row_data = dict(zip(columns, row))
            companies.append(row_data)
        
        companies = quicksort(companies, sort_key, sort_order)

        for i, perusahaan in enumerate(companies, start=1):
            print(f"[{color(i, 'orange')}] {color(perusahaan['nama_perusahaan'], 'cyan')}")
            print(f"    {perusahaan['email_perusahaan']}")
            print(f"    ID: {perusahaan['id_perusahaan']}")
            print('-'*30)
    
    def pilih():
        while True:
            idx = inputhandler("Masukkan nomor urut perusahaan: ", "int")-1
            if idx < len(companies):
                Perusahaan.profil(companies[idx]['id_perusahaan'])
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
                sort_key = 'id_lamaran'
                sort_order = 'desc'
                while True:
                    Lamaran.list(sort_key=sort_key, order=sort_order)
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Kembali"
                    ])
                    if pil == '1':
                        Lamaran.pilih()
                        while True:
                            pil = choices([
                                "Kembali",
                                color("Hapus lamaran", "red")
                            ])
                            if pil == '1':
                                break
                            elif pil == '2':
                                None
                    elif pil == '2':
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
                    elif pil == '3':
                        None
                    elif pil == '4':
                        break

            elif pil == '2':
                while True:
                    Perusahaan.profil()
                    pil = choices([
                        "Edit data",
                        "Kembali"
                    ])
                    if pil == '1':
                        None
                    elif pil == '2':
                        break
                    else:
                        print("Pilihan tidak valid")
            elif pil == '3':
                while True:
                    Lowongan.list()
                    pil = choices([
                        "Pilih",
                        "Urutkan",
                        "Cari",
                        "Submit Lowongan Baru",
                        "Kembali"
                    ])
                    if pil == '1':
                        Lowongan.pilih()
                        while True:
                            pil = choices([
                                "Edit",
                                "Kembali",
                                color("Hapus user", "red")
                            ])
                            if pil == '1':
                                None
                            if pil == '2':
                                break
                            elif pil == '3':
                                None
                            
                    elif pil == '2':
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
                    elif pil == '3':
                        None
                    elif pil == '4':
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

                        cursor.execute(f"insert into lowongan values (NULL, '{perusahaan_data['id_perusahaan']}', NULL, '{klasifikasi}', '{tipe}', '{deskripsi}', '{posisi}', '{ketentuan}', '{gaji}')")
                        db.commit()
                        print("berhasil keknya")
                    elif pil == '5':
                        break
            
            elif pil == '4':
                perusahaan_data = {}
                break
            else:
                print("Pilihan tidak valid")

class Lowongan:
    def list(id_perusahaan=None, status='all', sort_key='id_lowongan', sort_order='desc'):
        global jobs
        global job
        if id_perusahaan is not None:
            cursor.execute(f"SELECT * FROM lowongan INNER JOIN perusahaan ON lowongan.id_perusahaan = perusahaan.id_perusahaan INNER JOIN admin ON lowongan.id_admin = admin.id_admin WHERE id_perusahaan = {id_perusahaan}")
        elif not perusahaan_data:
            if status == "all":
                cursor.execute("select * from lowongan INNER JOIN perusahaan ON lowongan.id_perusahaan = perusahaan.id_perusahaan LEFT JOIN admin ON lowongan.id_admin = admin.id_admin")
            elif status == "disetujui":
                cursor.execute("select * from lowongan INNER JOIN perusahaan ON lowongan.id_perusahaan = perusahaan.id_perusahaan INNER JOIN admin ON lowongan.id_admin = admin.id_admin")
            elif status == "pending":
                cursor.execute("select * from lowongan INNER JOIN perusahaan ON lowongan.id_perusahaan = perusahaan.id_perusahaan WHERE lowongan.id_admin IS NULL")
        else:
            cursor.execute(f"select * from lowongan LEFT JOIN admin ON lowongan.id_admin = admin.id_admin where id_perusahaan = {perusahaan_data['id_perusahaan']}")

        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        jobs = LinkedList()

        # Populate jobs list regardless of conditions
        for row in rows:
            row_data = dict(zip(columns, row))
            jobs.append(row_data)

        jobs = quicksort(jobs, sort_key, sort_order)

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


    def lihat(id_lowongan):
        global jobs
        global job
        for job in jobs:
            if job['id_lowongan'] == id_lowongan:
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
        print("Gaada")

    def pilih():
        while True:
            idx = inputhandler("Pilih: ", "int")-1
            if idx < len(jobs):
                Lowongan.lihat(jobs[idx]['id_lowongan'])
                break
            else:
                print("Nomor tidak valid")
    

class Lamaran:
    def list(id_perusahaan=None, sort_key='id_lamaran', sort_order='desc'):
        global lamarans
        if id_perusahaan:
            query = f"SELECT lamaran.*, user.*, perusahaan.*, lowongan.posisi FROM lamaran JOIN user ON lamaran.id_user = user.id_user JOIN lowongan ON lamaran.id_lowongan = lowongan.id_lowongan JOIN perusahaan ON lamaran.id_perusahaan = perusahaan.id_perusahaan WHERE perusahaan.id_perusahaan = {id_perusahaan}"
        else:
            query = "SELECT lamaran.*, user.*, perusahaan.*, lowongan.posisi FROM lamaran JOIN user ON lamaran.id_user = user.id_user JOIN lowongan ON lamaran.id_lowongan = lowongan.id_lowongan JOIN perusahaan ON lamaran.id_perusahaan = perusahaan.id_perusahaan"

        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        lamarans = LinkedList()

        # ubah datanya jadi dictionary
        for row in rows:
            # bikin dictionary dari row data pakai nama kolom
            row_data = dict(zip(columns, row))
            lamarans.append(row_data)

        lamarans = quicksort(lamarans, sort_key, sort_order)
        
        table = PrettyTable(["No", "ID Lamaran", "Pelamar", "Perusahaan", "Posisi"])
        table.align["Posisi"] = "l" 

        for i, lamaran in enumerate(lamarans, start=1):
            table.add_row([i, lamaran['id_lamaran'], lamaran['nama'], lamaran['nama_perusahaan'], lamaran['posisi']])

        print(table)
    
    def pilih():
        while True:
            idx = inputhandler("Pilih: ", "int")-1
            if idx < len(lamarans):
                Lamaran.lihat(lamarans[idx]['id_lamaran'])
                break
            else:
                print("Nomor tidak valid")

    def lihat(id_lamaran=None):
        cursor.execute(f"SELECT lamaran.*, user.*, perusahaan.*, lowongan.posisi FROM lamaran JOIN user ON lamaran.id_user = user.id_user JOIN lowongan ON lamaran.id_lowongan = lowongan.id_lowongan JOIN perusahaan ON lamaran.id_perusahaan = perusahaan.id_perusahaan WHERE id_lamaran = {id_lamaran}")
        row = cursor.fetchone()
        columns = [column[0] for column in cursor.description]
        lamaran_data = dict(zip(columns, row))
        
        if not perusahaan_data:
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

        pengalaman_relevan = inputhandler("\nPegalaman relevan:\n", max=500)
        deskripsi = inputhandler("\nDeskripsi:\n", max=1500)

        cursor.execute(f"insert into lamaran values (NULL, {job['id_perusahaan']}, {user_data['id_user']}, {job['id_lowongan']}, '{sumber}', '{pengalaman_relevan}', '{deskripsi}')")
        db.commit()
        
        print("Lamaran berhasil disubmit. Silahkan cek email anda secara berkala")

# Global functions
def clear():
    os.system("cls")

def quicksort(arr, key, order='desc'):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2][key]
        less = [x for x in arr if x[key] < pivot]
        equal = [x for x in arr if x[key] == pivot]
        greater = [x for x in arr if x[key] > pivot]

        if order == 'desc':
            return quicksort(greater, key, order) + equal + quicksort(less, key, order)
        else:
            return quicksort(less, key, order) + equal + quicksort(greater, key, order)

# handle inputs
def inputhandler(prompt, inputtype="str", max=None):
    while True:
        try:
            if inputtype == "str":
                userinput = input(prompt)
            elif inputtype == "int":
                userinput = int(input(prompt))
            elif inputtype == "digit":
                userinput = input(prompt)
                if not userinput.isdigit():
                    print("Input hanya bisa berupa angka\n")
                    continue
            elif inputtype == "pw":
                userinput = pwinput(prompt)
            
            if max is not None and len(str(userinput)) > max:
                print(f"Input terlalu panjang. Maksimum panjang adalah {max} karakter.\n")
                continue
                
            return userinput
        except KeyboardInterrupt:
            print("Terdeteksi interupsi\n")
        except ValueError:
            print("Input hanya bisa berupa integer\n")
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
        choice = inputhandler("Masukkan pilihan: ", "digit")
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

# connect
db = mysql.connector.connect(
    user = 'root',
    password = '',
    host = 'localhost',
    database = 'lowongankerja'
)
cursor = db.cursor()

# predefine untuk pas login biar gak error
user_data = {}
admin_data = {}
perusahaan_data = {}

# Login
def login():
    while True:
        print(f"\n{banner('LOGIN')}")
        pil = choices([
            "Login admin",
            "Login user",
            "Login menggunakan akun perusahaan"
        ])

        if pil == '1':
            Admin.login()
        elif pil == '2':
            User.login()
        elif pil == '3':
            Perusahaan.login()
        
#Regist

#main
while True:
    print(f"\n{banner('PROGRAM LOWONGAN KERJA UNTUK SEMUA')}")
    pil = choices([
        "Login",
        "Register",
        "Keluar"
    ])

    if pil == '1':
        login()
    elif pil == '2':
        None #belum ada 
    elif pil == '3':
        break
    
