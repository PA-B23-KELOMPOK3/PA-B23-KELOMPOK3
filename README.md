# Project Akhir ASD Kelompok 3
# Program Peluang Kerja Untuk Semua: Membantu Masyarakat Menemukan Pekerjaan Yang Sesuai Dengan Mudah

_Anggota Kelompok:_

*• Joshua Timothy (2309116070)*

*• Aqiyah Zulqiyah (2309116075)*

*• Allya Putri Ditya (2309116078)*

*• Reisya Nurfaris D. A. (2309116102)*

## **Deskripsi Program**

### ⭐️1. Tujuan Program

_Program ini bertujuan untuk membantu masyarakat secara menyeluruh dalam menemukan pekerjaan dengan lebih mudah dan efisien. Kami memahami tantangan yang dihadapi banyak orang dalam mencari pekerjaan dikarenakan proses rekrutmen yang rumit. Dengan menyediakan platform yang mempermudah penelusuran lowongan kerja melalui berbagai filter dan kategori, serta meningkatkan akses informasi dengan detail yang akurat tentang deskripsi pekerjaan dan kualifikasi yang dibutuhkan, kami berharap dapat membantu pencari kerja menemukan pekerjaan yang sesuai dengan minat dan keterampilan mereka._

### ⭐️2. Pengguna Program

_Program ini memiliki beberapa jenis pengguna, dengan peran dan akses yang berbeda:_

      Admin:
      - Memiliki hak istimewa untuk mengelola data lowongan, termasuk:
        a. Menyetujui atau menolak permintaan untuk mengelola lowongan.
        b. Mengelola data pengguna (menambahkan, menghapus, dan mengedit).
        c. Mengelola data perusahaan (menambahkan, menghapus, dan mengedit).
        d. Mengelola data lamaran (menambahkan, menghapus, dan mengedit).
      - Setiap admin memiliki akses ke lowongan yang berbeda.
      
      User/Pelamar:
      - Memiliki hak istimewa untuk:
        a. Mencari lowongan berdasarkan berbagai filter dan kategori.
        b. Mengisi formulir lamaran secara cepat dan mudah.
        c. Melacak status lamaran mereka.
        d. Berkomunikasi dengan perusahaan secara langsung.

      Perusahaan:
      - Memiliki hak istimewa untuk:
        a. Mengedit profil perusahaan mereka.
        b. Melihat semua lamaran yang masuk ke perusahaan mereka.
        c. Menghapus lamaran.
        d. Melihat semua lowongan yang mereka buat.
        e. Menghapus dan mengedit lowongan.
        f. Memasukkan data lowongan baru.

### ⭐️3. Struktur Database

_Database program ini dirancang menggunakan struktur MySQL dengan 5 entitas utama:_

      1. Admin:
         - Atribut:
           - id_admin (primary key)
           - username
           - password
           - jabatan
      
      2. Lamaran:
         - Atribut:
           - id_lamaran (primary key)
           - id_perusahaan (foreign key)
           - id_user (foreign key)
           - id_lowongan (foreign key)
           - sumber_informasi
           - pengalaman_relevan
           - deskripsi
      
      3. Lowongan:
         - Atribut:
           - id_lowongan (primary key)
           - id_perusahaan (foreign key)
           - id_admin (foreign key)
           - klasifikasi
           - tipe
           - deskripsi
           - posisi
           - ketentuan
           - gaji

      4. Perusahaan:
         - Atribut:
           - id_perusahaan (primary key)
           - nama_perusahaan
           - password
           - no_telp
           - email_perusahaan
           - alamat_perusahaan
      
      5. User:
         - Atribut:
           - id_user (primary key)
           - nama
           - password
           - email
           - no_telp
           - pendidikan
           - pengalaman
           - keahlian
           - jenis_kelamin
           - alamat

## Struktur Program

### Halaman Log in
- *Proses Memilih Log in sebagai Admin*
![Flowchart Capstone-Halaman-1 (1)](./res/login2.jpg)

- *Proses Log in sebagai User/Pelamar*
![Flowchart Capstone-Halaman-1 (2)](./res/login3.jpg)

- *Proses Log in sebagai Perusahaan*
![Flowchart Capstone-Halaman-1 (3) (1)](./res/login4.jpg)

- *Proses kembali ke menu sebelumnya*
![Flowchart Capstone-Halaman-1 (3) (2)](./res/login5.jpg)

- *Proses Registrasi akun user atau registrasi akun perusahaan*
![register](./res/(fix)-Login1.jpg)
Jika pengguna belum memiliki akun, program menyediakan opsi registrasi. pengguna menginputkan data-data yang dibutuhkan oleh program sebelum masuk ke dalam menu utama.

- *Proses keluar dari program*
![Flowchart Capstone-Halaman-1 (4) (1)](./res/login7.jpg)

### Halaman Menu Admin
- *Terdapat pilihan melihat profil, mengelola lowongan, user, perusahaan, atau lamaran*
![Flowchart Capstone-Halaman-2 1](./res/(fix)-Admin1.jpg)

Di dalam menu admin, admin mempunyai fitur untuk mengedit dan menghapus pada lowongan,user,perusahaan, atau lamaran. 

- *Untuk melihat/menampilkan profil*
![mengelola lowongan](./res/(fix)-Admin2.jpg)
Pada fitur menampilkan profil, admin dapat mengedit profil admin.

- *Proses mengelola lowongan*
![mengelola user](./res/(fix)-Admin3.jpg)
Pada fitur ini, admin dapat menampilkan profil lowongan yang dipilih untuk dihapus, mengurutkan lowongan, dan juga mencari lowongan menggunakan keyword.

- *Proses mengelola user*
![mengelola perusahaan](./res/(fix)-Admin4.jpg)
Sama halnya dengan fitur lowongan, admin dapat menampilkan profil user yang dipilih untuk dihapus, mengurutkan data user, dan juga mencari user menggunakan keyword.

- *Proses mengelola perusahaan*
![mengelola lamaran](./res/(fix)-Admin5.jpg)
Begitu juga dengan fitur perusahaan, admin dapat menampilkan profil perusahaan yang dipilih untuk dihapus, mengurutkan data perusahaan, dan juga mencari perusahaan menggunakan keyword.

- *Proses mengelola lamaran*
![mengelola lamaran](./res/(fix)-Admin6.jpg)
Terakhir dengan fitur lamaran, admin dapat menampilkan profil lamaran yang dipilih untuk dihapus, mengurutkan data lamaran, dan juga mencari lamaran menggunakan keyword.

- *Proses Admin kembali ke menu log in*

  ![admin kembali ke menu](./res/(fix)-Admin7.jpg)


### Halaman Menu User
- *Pilihan untuk memilih user ingin melihat profil atau melihat daftar lowongan*
![Flowchart Capstone-Halaman-3(1) 1](./res/(fix)-User1.jpg)

- *Menampilkan Profil User*
![Flowchart Capstone-Halaman-3(1) 2](./res/(fix)-User2.jpg)
Pada fitur ini user bisa mengedit profil yang dimiliki user itu sendiri.

- *Proses user melihat list lowongan yang tersedia*
![Flowchart Capstone-Halaman-3(1) 3](./res/(fix)-User3.jpg)
Pada fitur ini, user dapat memilih lowongan yang dinginkan dan dapat mengisi lamaran cepat yang berisi format lamaran yg telah disediakan. Selain itu, user juga dapat melakukan sorting berdasarkan pilihan yg diinginkan dan dapat melakukan searching berdasarkan keyword yg dimasukkan.

- *Proses user memilih kembai ke menu utama*
  
![Flowchart Capstone-Halaman-3(1) 2](./res/(fix)-User4.jpg)

### Halaman Menu Perusahaan
- *Proses memilih melihat daftar lamaran, melihat profil perusahaan, atau mengelola lowongan*
![Flowchart Capstone-Halaman-4 1](./res/(fix)-Perusahaan1.jpg)

Pada halaman menu perusahaan memiliki fitur mengedit menghapus dan melihat data tertentu.

- *Proses melihat daftar lamaran dan menghapus data lamaran*
![daftar lamaran dan menghapus](./res/(fix)-Perusahaan2.jpg)
Pada fitur Lihat lamaran, perusahaan dapat memilih lamaran yang ingin dihapus, dapat mengurutkan daftar lowongan, dan dapat mencari lowongan yang diingin dengan fitur searching.

- *Proses mengedit profil perusahaan*
![melihat daftar lowongan](./res/(fix)-Perusahaan3.jpg)
Pada fitur ini, perusahaan dapat mengedit profil perusahaannya sendiri.

- *Menampilkan seluruh lowongan yang sudah di submit*
![melihat daftar lowongan](./res/(fix)-Perusahaan4.jpg)

- *Proses mengedit profil perusahaan, sorting, dan searching*
![melihat daftar lowongan](./res/(fix)-Perusahaan5.jpg)
Pada fitur ini, perusahaan dapat memilih lowongan yang ingin dihapus atau diedit, dapat mengurutkan berdasarkan pilihannya, dan dapt melakukan pencarian berdasarkan keyword yang ingin diinginkan.

- *Proses perusahaan submit lowongan baru, kembali ke menu sebelumnya*
![perusahaan submit lowongan baru](./res/(fix)-Perusahaan6.jpg)
Pada fitur Submit lowongan baru, perusahaan dapat menambahkan lowongan kerja dalam program namun lowongan baru tersebut tidak bisa langsung ditampilkan, harus disetujui oleh admin terlebih dahulu untuk ditampilkan.

- *Proses perusahaan memilih keluar ke menu log in*
  
![perusahaan keluar ke menu log in](./res/(fix)-Perusahaan7.jpg)


### Fungsionalitas

#### Modul bawaan

```py
import os
import math
```

1. **`import os`**: Modul `os` memberikan alat untuk berinteraksi dengan sistem operasi, seperti mengelola file dan direktori, mengakses variabel lingkungan, dan menjalankan perintah shell.

2. **`import math`**: Modul `math` menyediakan fungsi matematika dasar, seperti perhitungan akar kuadrat, sinus, kosinus, dan logaritma.

#### Modul external

```py
import mysql.connector
from pwinput import pwinput
from prettytable import PrettyTable
```

1. **`import mysql.connector`**: Ini memungkinkan koneksi dan manipulasi database MySQL dari Python.

2. **`from pwinput import pwinput`**: Ini memungkinkan input password yang aman.

3. **`from prettytable import PrettyTable`**: Ini digunakan untuk membuat dan mencetak tabel yang rapi di terminal.

#### Class Node
      
```py
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
```

Fungsi kelas “Node”. Setiap node dalam linked list akan memiliki atribut “data” untuk menyimpan nilai dan atribut “next” untuk menunjukkan ke node berikutnya dalam linked list.


#### Class LinkedList

```py
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
```

Class LinkedList adalah salah satu struktur data yang yang terdiri dari node-node yang terhubung satu sama lain. Dalam Class LinkedList, fungsi def init dan self berperan sebagai konstruktor untuk membuat instance dari class tersebut

Nantinya setiap method dalam linked list akan memiliki parameter self. Dengan menggunakan parameter self kita dapat mengakses atribut-atribut yang ada pada Class LinkedList

- Method append
<ul>

```py
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
```

Method ini berfungsi untuk menambahkan node baru di bagian akhir linked list. Method kemudian akan membuat istance baru dari class Node dan menyimpan data pada node tersebut.

</ul>

- Method display
<ul>

```py
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
```

ini berfungsi untuk menampilkan seluruh data-data yang berada di dalam database yang kemudian tersusun di dalam table.

</ul>

- Method \_\_getitem__
<ul>
      
```py
    def __getitem__(self, index):
        current_index = 0
        current_node = self.head
        while current_node:
            if current_index == index:
                return current_node.data
            current_node = current_node.next
            current_index += 1
        raise IndexError("Index out of range")
```

biar bisa langsung pakai list[index] macam array biasanya

</ul>

- Method \_\_iter__
<ul>

```py
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
```

biar bisa pakai for loop 

</ul>

- Method len
<ul>
      
```py
    def __len__(self):
        return self.length
```

biar bisa pakai len()

</ul>


#### Class MySQLHandler
<ul>

```py
class MySQLHandler:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connect()
```

Class ini merupakan kerangka kerja untuk mengelola koneksi dan operasi database MySQL.
`__init__` digunakan untuk menginisialisasi objek MySQLHandler dengan informasi koneksi yang diberikan.

</ul>

- Method connect
<ul>

```py
    def connect(self):
        self.db = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )
        self.cursor = self.db.cursor()
```

Fungsi `connect(self)` dalam kelas MySQLHandler bertujuan untuk membuat koneksi ke server MySQL menggunakan informasi yang telah diberikan saat objek MySQLHandler diinisialisasi.

</ul>

- Method execute
<ul>

```py
    def execute(self, query, params=None):
        try:
            self.cursor.execute(query, params)
        except:
            print("Terjadi kesalahan saat menjalankan query")
```

Fungsi execute dalam sebuah kelas yang berhubungan dengan database, biasanya digunakan untuk mengeksekusi perintah SQL ke dalam database yang terhubung.

</ul>

- Method fetchall
<ul>

```py
    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except:
            None
```

Method fetchall digunakan dalam koneksi basis data untuk mengambil semua baris hasil dari sebuah query yang dieksekusi.

</ul>

- Method fetchone
<ul>

```py
    def fetchone(self):
        try:
            return self.cursor.fetchone()
        except:
            None
```

Method fetchone dalam koneksi basis data digunakan untuk mengambil satu baris hasil dari sebuah query yang dieksekusi. 

</ul>

- Method description
<ul>

```py
    def description(self):
        return self.cursor.description
```

Fungsi description biasanya digunakan untuk mengembalikan deskripsi kolom dari hasil query.

</ul>

- Method commit
<ul>

```py
    def commit(self):
        self.db.commit()
```

Fungsi commit dalam konteks basis data digunakan untuk menyimpan perubahan yang telah dilakukan dalam transaksi ke dalam basis data secara permanen.

</ul>

- Method close
<ul>

```py
    def close(self):
        self.cursor.close()
        self.db.close()
```

Fungsi close dalam konteks koneksi database digunakan untuk menutup koneksi atau kursor yang telah dibuka.

</ul>


#### Class Admin

- Method login
<ul>
      
```py
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
```

Class `Admin` adalah representasi dari administrator dalam sebuah sistem atau aplikasi. Admin memiliki akses dan kekuatan lebih dalam mengelola sistem dibandingkan pengguna biasa. Ini dapat mencakup atribut seperti username, password, role, email, dan metode untuk mengelola sistem, seperti menambah, menghapus, atau memperbarui informasi pengguna dan data lainnya.

Method login digunakan untuk menampilkan perintah terkait login sebelum masuk ke dalam aplikasi, di dalamnya terdapat percabangan(if, elif, else) yang digunakan untuk mengeksekusi kode tertentu hanya jika kondisi tersebut terpenuhi.

1. **Membersihkan terminal**: Method `clear()` dipanggil untuk membersihkan terminal sebelum tampilan login dimulai.

2. **Input Username**: User diminta untuk memasukkan username mereka.

3. **Query Database**: Method execute digunakan untuk menjalankan perintah SQL yang mencari admin dengan username yang cocok dalam tabel admin.

4. **Pengecekan Username**: Jika admin dengan username tersebut ditemukan dalam database, pengguna diminta untuk memasukkan password mereka.

5. **Validasi Password**: Password yang dimasukkan oleh pengguna dibandingkan dengan password yang disimpan dalam database. Jika cocok, pengguna berhasil masuk ke sistem dan menu admin ditampilkan. Jika tidak, pesan kesalahan ditampilkan.

6. **Kondisi untuk Username Tidak Terdaftar**: Jika admin dengan username yang dimasukkan tidak ditemukan dalam database, pesan kesalahan ditampilkan.

</ul>

- Method profil
<ul>

```py
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
```

Method `profil` digunakan untuk menampilkan profil admin saat ini beserta jabatan dan hak akses yang dimilikinya. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Query Database**: Fungsi `execute` digunakan untuk menjalankan perintah SQL yang mencari admin dengan ID admin yang sedang aktif dalam tabel admin.

2. **Pengolahan Data**: Jika data admin ditemukan dalam database, informasi admin disimpan dalam variabel `admin_data`.

3. **Tampilan Profil**: Informasi admin, seperti username, ID, dan jabatan, ditampilkan ke layar.

4. **Hak Akses**: Hak akses admin ditampilkan berdasarkan jabatan. Berbagai aksi yang dapat dilakukan oleh admin ditampilkan dengan warna yang sesuai.

</ul>

- Method menu
<ul>

```py
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
```

Method `menu` adalah bagian dari sistem yang bertanggung jawab untuk menampilkan menu utama admin, memungkinkan mereka untuk memilih dan melakukan berbagai tindakan terkait manajemen sistem. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Tampilan Menu Utama**: Fungsi `choices` digunakan untuk menampilkan pilihan menu utama kepada admin. Admin dapat memilih dari berbagai opsi, seperti melihat profil, mengelola lowongan, mengelola user, mengelola perusahaan, mengelola lamaran, atau keluar dari sistem.

2. **Pilihan Profil Admin**: Jika admin memilih opsi "Profil", fungsi `profil` dari kelas `Admin` dipanggil untuk menampilkan profil admin saat ini. Admin juga diberikan opsi untuk mengedit data profilnya.

3. **Pilihan Kelola Lowongan**: Jika admin memilih opsi "Kelola Lowongan", mereka dapat memilih untuk melihat, mengurutkan, mencari, atau mengelola lowongan pekerjaan yang ada dalam sistem.

4. **Pilihan Kelola User**: Admin dapat memilih opsi "Kelola User" untuk melihat, mengurutkan, mencari, atau menghapus pengguna (user) dalam sistem.

5. **Pilihan Kelola Perusahaan**: Admin dapat memilih opsi "Kelola Perusahaan" untuk melihat, mengurutkan, mencari, atau menghapus perusahaan yang terdaftar dalam sistem.

6. **Pilihan Kelola Lamaran**: Admin dapat memilih opsi "Kelola Lamaran" untuk melihat, mengurutkan, mencari, atau menghapus lamaran pekerjaan yang telah diajukan oleh pengguna.

7. **Keluar dari Menu**: Admin dapat memilih opsi "Keluar" dari menu utama untuk keluar dari sistem.

</ul>

#### Class User

- Method register
<ul>

```py
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
            sql.commit()
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
```

Method `register` dalam kelas `User` bertujuan untuk memungkinkan pengguna untuk mendaftar ke dalam sistem. Berikut penjelasan singkat tentang fungsi ini:

1. **Input Data**: Pengguna diminta untuk memasukkan informasi pribadi seperti email, password, nama, jenis kelamin, nomor telepon, pendidikan, alamat, pengalaman, dan keahlian.

2. **Validasi Email**: Sistem memeriksa apakah email yang dimasukkan pengguna telah digunakan sebelumnya. Jika belum, proses pendaftaran dilanjutkan; jika sudah, pengguna diminta untuk menggunakan email lain.

3. **Penyimpanan Data**: Informasi yang dimasukkan oleh pengguna disimpan ke dalam tabel user dalam basis data.

4. **Konfirmasi Pendaftaran**: Pengguna diberikan konfirmasi bahwa akun mereka telah berhasil dibuat.

5. **Kembali ke Menu**: Setelah pendaftaran berhasil, pengguna diarahkan kembali ke menu utama.

Ini adalah kerangka umum dari fungsi `register` yang memanfaatkan berbagai fungsi bantuan seperti `inputhandler` (untuk validasi input) dan `choices` (untuk memilih jenis kelamin). Fungsi-fungsi lainnya terkait dengan operasi basis data seperti eksekusi perintah SQL dan manipulasi data yang diperlukan untuk pendaftaran pengguna.

</ul>

- Method login
<ul>

```py
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
```

Method login dalam kelas User bertujuan untuk memungkinkan pengguna untuk masuk ke dalam sistem. Berikut penjelasan lebih detail tentang fungsi ini:

1. Input Data: Pengguna diminta untuk memasukkan email dan password mereka menggunakan fungsi inputhandler. Ini membantu memastikan bahwa input yang dimasukkan sesuai dengan format yang diinginkan.

2. Query Database: Sistem menggunakan perintah SQL untuk mencari pengguna berdasarkan email yang dimasukkan. Ini dilakukan dengan pernyataan SELECT yang mencocokkan email yang dimasukkan pengguna dengan email yang ada dalam tabel user.

3. Validasi Pengguna: Jika email yang dimasukkan oleh pengguna ditemukan dalam database, sistem membandingkan password yang dimasukkan oleh pengguna dengan password yang tersimpan dalam database. Jika keduanya cocok, pengguna dianggap berhasil masuk.

4. Tindakan Setelah Login: Jika login berhasil, pengguna diberikan pesan selamat datang yang mencakup nama pengguna, dan kemudian diarahkan ke menu utama menggunakan fungsi User.menu().

</ul>

- Method profil
<ul>

```py
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
```

Method `profil` dalam kelas `User` bertujuan untuk menampilkan profil pengguna. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Parameter Opsional**: Fungsi ini menerima parameter opsional `user_id`, yang merupakan ID pengguna yang ingin ditampilkan profilnya. Jika tidak ada `user_id` yang diberikan, fungsi akan mencoba menggunakan `user_data` global, yang berisi informasi pengguna yang saat ini login.

2. **Query Database**: Sistem menggunakan perintah SQL untuk mencari pengguna berdasarkan `user_id` yang diberikan atau ID pengguna yang tersimpan dalam `user_data`.

3. **Validasi Pengguna**: Jika pengguna dengan `user_id` yang diberikan ditemukan dalam database, informasi mereka akan ditampilkan. Jika tidak, akan ada pesan yang memberi tahu bahwa pengguna dengan ID tersebut tidak ditemukan.

4. **Menampilkan Profil**: Setelah mendapatkan informasi pengguna dari database, profil pengguna ditampilkan dengan menggunakan data yang ditemukan, seperti nama, jenis kelamin, alamat, email, nomor telepon, pendidikan terakhir, pengalaman, dan keahlian.

</ul>

- Method list
<ul>

```py
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
```

Fungsi `list` dalam kelas `User` bertujuan untuk menampilkan daftar pengguna dalam format yang rapi. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Parameter Opsi**: Fungsi ini menerima beberapa parameter opsional, termasuk `sort_key` untuk menentukan kunci pengurutan, `sort_order` untuk menentukan urutan pengurutan, dan `keyword` untuk pencarian khusus.

2. **Query Database**: Sistem menggunakan perintah SQL untuk mengambil data pengguna dari database. Data ini kemudian diubah menjadi struktur data yang lebih mudah diolah.

3. **Pengurutan dan Pencarian**: Pengguna memiliki opsi untuk mengurutkan daftar pengguna berdasarkan kriteria tertentu, dan juga melakukan pencarian berdasarkan kata kunci yang diberikan.

4. **Menampilkan Data**: Jika ada pengguna yang ditemukan, data mereka ditampilkan menggunakan `PrettyTable` untuk format yang rapi. Setiap baris tabel mencakup nomor urut, nama pengguna, email, dan ID pengguna.

5. **Penanganan Kasus Kosong**: Jika tidak ada pengguna yang ditemukan atau daftar pengguna kosong, pesan yang sesuai dicetak untuk memberi tahu pengguna bahwa tidak ada data yang tersedia untuk ditampilkan.

</ul>

- Method pilih
<ul>

```py
    def pilih():
        global selected_user
        while True:
            idx = inputhandler("Pilih: ", "int")-1
            if idx < len(users):
                selected_user = users[idx]['id_user']
                break
            else:
                print("Nomor tidak valid")
```

Method `pilih` bertujuan untuk memilih satu dari daftar pengguna yang ditampilkan sebagai ID user. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Pemilihan Pengguna**: Pengguna diminta untuk memasukkan nomor yang terkait dengan pengguna yang ingin mereka pilih dari daftar yang ditampilkan.

2. **Validasi Nomor**: Sistem memvalidasi nomor yang dimasukkan oleh pengguna untuk memastikan bahwa nomor tersebut sesuai dengan nomor yang terdaftar dalam daftar pengguna.

3. **Penetapan Pengguna Dipilih**: Jika nomor yang dimasukkan valid, ID pengguna terkait ditetapkan sebagai `selected_user`, yang dapat digunakan untuk operasi lebih lanjut.

4. **Penanganan Kasus Tidak Valid**: Jika nomor yang dimasukkan tidak valid (misalnya, di luar rentang nomor yang tersedia), pesan yang sesuai dicetak untuk memberi tahu pengguna bahwa nomor tersebut tidak valid.

</ul>

- Method menu
<ul>

```py
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
```

Fungsi `menu` dalam kelas `User` bertujuan untuk menyediakan menu interaktif bagi pengguna. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Pemilihan Opsi**: Pengguna diberikan beberapa opsi yang dapat mereka pilih, seperti melihat profil mereka, melihat lowongan pekerjaan yang tersedia, atau keluar dari sistem.

2. **Profil Pengguna**: Jika pengguna memilih opsi "Profil", mereka dapat melihat dan mengedit informasi profil mereka seperti nama, alamat, email, dan lainnya.

3. **Lihat Lowongan**: Jika pengguna memilih opsi "Lihat Lowongan", mereka dapat melihat daftar lowongan pekerjaan yang tersedia. Mereka juga dapat melakukan pencarian, pengurutan, dan melamar lowongan yang mereka minati.

4. **Penanganan Opsi**: Fungsi ini menangani setiap opsi yang dipilih oleh pengguna. Misalnya, jika pengguna memilih untuk melihat profil mereka, fungsi `profil()` akan dipanggil. Jika mereka memilih untuk melihat lowongan, fungsi `Lowongan.list()` akan dipanggil.

5. **Penanganan Kasus Tidak Valid**: Fungsi ini memeriksa apakah opsi yang dipilih oleh pengguna valid. Jika pengguna memasukkan opsi yang tidak valid, pesan yang sesuai dicetak untuk memberi tahu mereka bahwa opsi tersebut tidak valid.

</ul>


#### Class perusahaan

- Method register
<ul>

```py
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
            sql.commit()
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
```

Menthod `register` dalam kelas `Perusahaan` bertujuan untuk memungkinkan perusahaan untuk mendaftar dan membuat akun baru dalam sistem. Berikut adalah penjelasan singkat tentang method ini:

1. **Input Data**: Perusahaan diminta untuk memasukkan email, password, nama perusahaan, nomor telepon, dan alamat perusahaan mereka.

2. **Query Database**: Sistem melakukan pencarian dalam tabel perusahaan menggunakan email yang dimasukkan oleh perusahaan.

3. **Validasi Perusahaan**: Jika email yang dimasukkan belum digunakan, sistem menyimpan informasi perusahaan yang baru didaftarkan ke dalam basis data.

4. **Tindakan Setelah Registrasi**: Setelah berhasil mendaftar, perusahaan diberikan pesan konfirmasi bahwa akun mereka telah berhasil dibuat dan mereka diarahkan ke menu utama perusahaan.

Fungsi ini memungkinkan perusahaan untuk mendaftar dengan mudah dalam sistem, memungkinkan mereka untuk mengakses fitur-fitur dan fungsionalitas yang disediakan. Ini adalah proses penting dalam memungkinkan perusahaan untuk memanfaatkan layanan yang ditawarkan oleh platform.

</ul>

- Method login
<ul>

```py
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
```

Fungsi `login` dalam kelas `Perusahaan` bertujuan untuk memungkinkan perusahaan untuk masuk ke dalam sistem menggunakan akun mereka. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Input Data**: Perusahaan diminta untuk memasukkan email dan password mereka.

2. **Query Database**: Sistem melakukan pencarian dalam tabel perusahaan menggunakan email yang dimasukkan oleh perusahaan.

3. **Validasi Perusahaan**: Jika email yang dimasukkan ditemukan dalam database, sistem membandingkan password yang dimasukkan oleh perusahaan dengan password yang tersimpan dalam database. Jika cocok, perusahaan dianggap berhasil masuk.

4. **Tindakan Setelah Login**: Setelah berhasil login, perusahaan diberikan pesan selamat datang dan diarahkan ke menu utama perusahaan.

Fungsi ini memungkinkan perusahaan untuk masuk ke dalam sistem dengan menggunakan akun mereka, memberikan akses ke berbagai fitur dan fungsionalitas yang tersedia. Ini adalah langkah penting dalam memungkinkan perusahaan untuk mengelola informasi dan melakukan tindakan yang sesuai dengan kebutuhan bisnis mereka.

</ul>

- Method profil
<ul>

```py
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
```

Fungsi `profil` dalam kelas `Perusahaan` bertujuan untuk menampilkan profil perusahaan yang sedang aktif. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Input Parameter Opsional**: Fungsi ini menerima parameter opsional `perusahaan_id`, yang merupakan ID perusahaan yang ingin ditampilkan profilnya. Jika tidak ada ID yang disediakan, fungsi akan mencoba menggunakan data perusahaan yang disimpan dalam variabel `perusahaan_data`.

2. **Query Database**: Jika `perusahaan_id` diberikan, fungsi akan menjalankan query SQL untuk mengambil data perusahaan dari basis data berdasarkan ID tersebut.

3. **Format dan Tampilkan Informasi**: Setelah mendapatkan data perusahaan, fungsi akan memformat informasi tersebut dan menampilkannya ke layar. Ini mencakup nama perusahaan, alamat, email, dan nomor telepon.

Fungsi ini memungkinkan perusahaan untuk melihat informasi profil mereka sendiri atau profil perusahaan lain jika `perusahaan_id` disediakan. Ini membantu perusahaan untuk memeriksa dan memperbarui informasi yang terkait dengan bisnis mereka.

</ul>

- Method list
<ul>

```py
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
```

Fungsi `list` dalam kelas `Perusahaan` bertujuan untuk menampilkan daftar perusahaan yang ada dalam sistem. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Query Database**: Fungsi ini menjalankan query SQL untuk mengambil data perusahaan dari basis data, termasuk ID perusahaan, nama perusahaan, nomor telepon, email, dan alamat.

2. **Penyusunan dan Pengurutan Data**: Setelah mendapatkan data perusahaan, fungsi ini menyusunnya ke dalam linked list `companies`. Data kemudian diurutkan berdasarkan kunci pengurutan yang disediakan (misalnya, `id_perusahaan`, `nama_perusahaan`, dll.) dan urutan pengurutan yang ditentukan (ascending atau descending).

3. **Pencarian Berdasarkan Kata Kunci**: Jika kata kunci pencarian disediakan, fungsi ini akan melakukan pencarian menggunakan algoritma jump search pada data perusahaan.

4. **Tampilkan Informasi**: Setelah data perusahaan disusun dan diurutkan, fungsi ini akan menampilkan informasi perusahaan ke layar. Ini termasuk nama perusahaan, email, ID, dan alamat. Setiap perusahaan ditampilkan dalam format yang mudah dibaca, dengan nomor dan warna yang berbeda untuk membedakan mereka.

Fungsi ini memungkinkan pengguna untuk melihat daftar perusahaan yang terdaftar dalam sistem, memberikan visibilitas tentang perusahaan-perusahaan yang ada.

</ul>

- Method pilih
<ul>

```py
    def pilih():
        global selected_perusahaan
        while True:
            idx = inputhandler("Masukkan nomor urut perusahaan: ", "int")-1
            if idx < len(companies):
                selected_perusahaan = companies[idx]['id_perusahaan']
                break
            else:
                print("Nomor tidak valid")
```

Fungsi `pilih` dalam kelas `Perusahaan` bertujuan untuk memungkinkan pengguna memilih sebuah perusahaan dari daftar perusahaan yang ditampilkan. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Input Pilihan Pengguna**: Pengguna diminta untuk memasukkan nomor urut perusahaan yang ingin mereka pilih dari daftar yang ditampilkan.

2. **Validasi Pilihan**: Sistem memeriksa apakah nomor yang dimasukkan oleh pengguna sesuai dengan nomor perusahaan yang ditampilkan. Jika nomor valid (antara 1 dan jumlah perusahaan yang ditampilkan), perusahaan yang sesuai dipilih.

3. **Penyimpanan Pilihan**: ID perusahaan yang dipilih disimpan dalam variabel `selected_perusahaan` untuk digunakan di bagian lain dari program.

Fungsi ini memastikan bahwa pengguna dapat memilih perusahaan yang tepat dari daftar yang ditampilkan dengan memvalidasi nomor yang dimasukkan dan menyimpan pilihan mereka untuk penggunaan selanjutnya.

</ul>

- Method menu
<ul>

```py
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
                                    sql.commit()
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
                                    sql.commit()
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
                        sql.commit()
                        print(color("Lowongan berhasil disubmit. Silahkan tunggu disetujui admin", "green"))
                    elif pil == '5':
                        clear()
                        break
            
            elif pil == '4':
                clear()
                perusahaan_data = {}
                break
```

Fungsi `menu` dalam kelas `Perusahaan` adalah menu utama yang memungkinkan perusahaan untuk mengelola berbagai aspek dalam sistem. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Menu Pilihan**: Pengguna diberikan opsi untuk memilih dari beberapa tindakan yang dapat dilakukan oleh perusahaan, seperti memeriksa lamaran, melihat profil perusahaan, mengelola lowongan pekerjaan, dan keluar dari menu.

2. **Pilihan Aksi**: Bergantung pada pilihan pengguna, fungsi ini memanggil fungsi terkait atau memproses aksi yang diminta.

3. **Pemrosesan Aksi**: Setiap pilihan memiliki logika yang berbeda untuk memprosesnya. Misalnya, untuk "Cek lamaran", sistem memungkinkan pengguna untuk memilih, mengurutkan, atau mencari lamaran. Untuk "Lihat profil perusahaan", sistem menampilkan profil perusahaan dan memungkinkan pengguna untuk mengedit data. Untuk "Kelola lowongan", sistem memungkinkan perusahaan untuk menambah, mengedit, menghapus, atau melihat lowongan pekerjaan.

4. **Kembali**: Pengguna diberikan opsi untuk kembali ke menu utama setelah menyelesaikan tindakan tertentu.

Fungsi ini memungkinkan perusahaan untuk mengelola berbagai aspek dari akun mereka dalam sistem dengan cara yang terstruktur dan mudah dipahami.

</ul>


#### Class Lowongan

<ul>

```py
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
```

Fungsi `list` dalam kelas `Lowongan` bertujuan untuk menampilkan daftar lowongan pekerjaan sesuai dengan beberapa kriteria tertentu. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Pengaturan Query**: Fungsi ini membangun kueri SQL tergantung pada siapa pengguna yang mengaksesnya dan status lowongan yang ingin ditampilkan. Jika diakses oleh admin, fungsi akan menampilkan semua lowongan dengan status "disetujui" atau "pending". Jika diakses oleh perusahaan, hanya lowongan yang dimiliki oleh perusahaan tersebut yang akan ditampilkan. Jika diakses oleh pengguna umum atau tidak ada pengguna yang masuk, semua lowongan akan ditampilkan.

2. **Eksekusi Kueri**: Setelah kueri dibangun, fungsi menjalankannya dan mengambil hasilnya.

3. **Pengolahan Data**: Hasil kueri diproses untuk membentuk objek data yang sesuai dengan lowongan pekerjaan. Objek-objek ini kemudian dimasukkan ke dalam struktur data yang sesuai, yaitu LinkedList.

4. **Pengurutan dan Pencarian**: Setelah data dimuat, mereka diurutkan dan kemudian dicari jika pengguna memberikan kata kunci pencarian.

5. **Pembentukan Output**: Berdasarkan siapa pengguna yang mengaksesnya, fungsi ini memformat dan menampilkan data lowongan dalam format yang sesuai. Untuk pengguna biasa, tampilan berupa daftar lowongan dengan beberapa detail. Untuk perusahaan, tampilan berupa tabel yang mencakup status setiap lowongan. Untuk admin, tampilan serupa dengan perusahaan tetapi dengan nama perusahaan sebagai tambahan.

Fungsi ini memberikan fleksibilitas dalam menampilkan lowongan pekerjaan yang memungkinkan pengguna, baik perusahaan, admin, atau pengguna umum, untuk melihat dan mengelola lowongan sesuai kebutuhan.

</ul>

- Method lihat
<ul>

```py
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
```

Fungsi `lihat` dalam kelas `Lowongan` bertujuan untuk menampilkan detail lengkap tentang satu lowongan pekerjaan tertentu. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Query Database**: Fungsi ini menjalankan kueri SQL untuk mengambil data lowongan pekerjaan dari basis data berdasarkan ID lowongan yang diberikan.

2. **Pemrosesan Data**: Jika baris data ditemukan, fungsi ini memproses hasil kueri untuk membentuk objek data lowongan pekerjaan.

3. **Pengaturan Tampilan**: Fungsi ini memformat dan menampilkan detail lowongan pekerjaan dalam format yang sesuai. Informasi yang ditampilkan termasuk posisi pekerjaan, klasifikasi, tipe pekerjaan, gaji rata-rata, deskripsi pekerjaan, dan ketentuan. Jika pengguna yang sedang masuk bukan perusahaan, tambahan informasi seperti nama perusahaan dan alamat perusahaan juga ditampilkan. Jika pengguna adalah admin, informasi tambahan seperti ID lowongan, ID perusahaan, dan status persetujuan juga ditampilkan.

4. **Output**: Detail lowongan pekerjaan ditampilkan dalam bentuk teks dengan pewarnaan opsional untuk menyoroti status persetujuan jika diakses oleh admin.

Fungsi ini memungkinkan pengguna untuk melihat semua detail penting tentang lowongan pekerjaan tertentu, termasuk informasi tentang perusahaan yang mempostingnya dan status persetujuannya jika diakses oleh admin.

</ul>

- Method pilih
<ul>

```py
    def pilih():
        global selected_lowongan
        while True:
            idx = inputhandler("Pilih: ", "int")-1
            if idx < len(jobs):
                selected_lowongan = jobs[idx]['id_lowongan']
                break
            else:
                print("Nomor tidak valid")
```

Fungsi `pilih` dalam kelas `Lowongan` bertujuan untuk memungkinkan pengguna memilih lowongan pekerjaan tertentu dari daftar lowongan yang ditampilkan. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Input Pengguna**: Pengguna diminta untuk memasukkan nomor urut lowongan pekerjaan yang ingin mereka pilih.

2. **Validasi Nomor**: Fungsi ini memastikan bahwa nomor yang dimasukkan oleh pengguna valid, yaitu berada dalam rentang nomor urut yang ditampilkan.

3. **Penyimpanan Data**: Jika nomor yang dimasukkan valid, ID lowongan yang sesuai dengan nomor tersebut disimpan dalam variabel `selected_lowongan` untuk digunakan di tempat lain dalam program.

4. **Feedback**: Jika nomor yang dimasukkan tidak valid, pengguna diberi umpan balik bahwa nomor tersebut tidak valid, dan mereka diminta untuk memasukkan nomor yang lain.

Fungsi ini membantu pengguna memilih lowongan pekerjaan tertentu dari daftar yang ditampilkan sehingga mereka dapat melanjutkan dengan tindakan selanjutnya, seperti melihat detail lowongan atau mengambil tindakan terkait.

</ul>


#### Class Lamaran

- Method list
<ul>

```py
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
```

Fungsi `list` dalam kelas `Lamaran` bertujuan untuk menampilkan daftar lamaran pekerjaan. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Parameter Opsional**: Fungsi ini menerima beberapa parameter opsional, seperti `id_perusahaan` (ID perusahaan yang ingin menampilkan lamaran), `sort_key` (kunci pengurutan), `sort_order` (urutan pengurutan), dan `keyword` (kata kunci untuk pencarian).

2. **Query Database**: Berdasarkan parameter yang diberikan, fungsi ini membangun kueri SQL untuk mengambil data lamaran dari database. Jika `id_perusahaan` diberikan, hanya lamaran dari perusahaan tersebut yang akan ditampilkan.

3. **Membangun Struktur Data**: Data yang diambil dari database diubah menjadi struktur data yang lebih mudah diolah, dalam hal ini, menggunakan linked list.

4. **Pengurutan dan Pencarian**: Data lamaran diurutkan berdasarkan kunci pengurutan yang diberikan, dan jika ada, pencarian dilakukan berdasarkan kata kunci yang diberikan.

5. **Output Tampilan**: Jika terdapat lamaran yang cocok dengan kriteria yang diberikan, hasilnya ditampilkan dalam bentuk tabel yang terformat dengan baik menggunakan modul `PrettyTable`. Tabel akan berisi informasi seperti nomor urut, ID lamaran, nama pelamar, nama perusahaan (jika diakses oleh admin), dan posisi pekerjaan yang dilamar.

6. **Umpan Balik**: Jika tidak ada lamaran yang cocok dengan kriteria yang diberikan, pengguna diberi umpan balik bahwa tidak ada lamaran yang dapat ditampilkan.

Fungsi ini memfasilitasi penggunaan informasi lamaran pekerjaan dengan menyediakan tampilan yang terstruktur dan mudah dibaca.

</ul>

- Method pilih
<ul>

```py
    def pilih():
        global selected_lamaran
        while True:
            idx = inputhandler("Pilih: ", "int")-1
            if idx < len(lamarans):
                selected_lamaran = lamarans[idx]['id_lamaran']
                break
            else:
                print("Nomor tidak valid")
```

Fungsi `pilih` dalam kelas `Lamaran` bertujuan untuk memungkinkan pengguna untuk memilih salah satu lamaran pekerjaan dari daftar yang ditampilkan. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Input Pengguna**: Fungsi ini meminta pengguna untuk memasukkan nomor urut dari daftar lamaran yang ditampilkan.

2. **Validasi Input**: Input yang diterima dari pengguna diverifikasi untuk memastikan bahwa nomor yang dimasukkan valid, yaitu berada dalam rentang nomor urut lamaran yang ditampilkan.

3. **Penetapan Lamaran Terpilih**: Jika nomor yang dimasukkan oleh pengguna valid, maka lamaran yang sesuai dengan nomor tersebut akan ditetapkan sebagai lamaran yang dipilih (`selected_lamaran`).

4. **Looping**: Jika nomor yang dimasukkan tidak valid, pengguna akan diberi pesan kesalahan dan diminta untuk memasukkan nomor yang valid lagi. Proses ini akan terus berulang sampai nomor yang valid dimasukkan.

Fungsi ini memastikan bahwa pengguna dapat memilih lamaran pekerjaan dari daftar yang ditampilkan dengan cara yang mudah dan aman.

</ul>

- Method lihat
<ul>

```py
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
```

Fungsi `lihat` dalam kelas `Lamaran` bertujuan untuk menampilkan detail lengkap dari sebuah lamaran pekerjaan. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Input Parameter**: Fungsi ini menerima parameter `id_lamaran`, yang merupakan ID unik dari lamaran pekerjaan yang ingin dilihat.

2. **Query Database**: Fungsi ini menjalankan sebuah query SQL untuk mengambil data lengkap terkait dengan lamaran pekerjaan yang memiliki ID sesuai dengan yang diberikan.

3. **Pemrosesan Data**: Data yang diambil dari database diorganisir ke dalam bentuk sebuah dictionary menggunakan nama kolom sebagai kunci dan nilai-nilai dari baris yang sesuai sebagai nilainya.

4. **Tampilan Informasi**: Informasi dari lamaran pekerjaan tersebut ditampilkan kepada pengguna, termasuk nama pelamar, jenis kelamin, alamat, email, nomor telepon, sumber informasi, pengalaman relevan, dan deskripsi tambahan. Jika pengguna yang mengakses adalah seorang admin, informasi tambahan seperti ID lamaran, ID user, ID perusahaan, dan ID lowongan juga ditampilkan.

Fungsi ini memungkinkan pengguna untuk melihat detail lengkap dari sebuah lamaran pekerjaan, termasuk informasi yang relevan seperti data pelamar, informasi kontak, pengalaman, dan deskripsi tambahan.

</ul>

- Method submit
<ul>

```py
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
        sql.commit()
        
        print("Lamaran berhasil disubmit. Silahkan cek email anda secara berkala")
```

Fungsi `submit` dalam kelas `Lamaran` bertujuan untuk memungkinkan pengguna untuk mengirimkan lamaran pekerjaan. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Input Penggunaan Informasi**: Pengguna diminta untuk memilih sumber informasi dari mana mereka mengetahui lowongan pekerjaan yang mereka lamar. Pilihan sumber informasi termasuk "Dari aplikasi ini", "Iklan di internet", "Diberitahu kerabat", atau "Lainnya".

2. **Input Penggunaan Pengalaman Relevan**: Pengguna diminta untuk memasukkan pengalaman relevan mereka terkait dengan pekerjaan yang dilamar. Input ini divalidasi untuk memastikan panjangnya berada dalam rentang yang sesuai.

3. **Input Penggunaan Deskripsi**: Pengguna diminta untuk memberikan deskripsi tambahan tentang diri mereka atau alasan mereka tertarik dengan pekerjaan tersebut. Deskripsi ini juga divalidasi untuk memastikan panjangnya berada dalam rentang yang sesuai.

4. **Query Database**: Setelah pengguna memasukkan informasi yang diperlukan, fungsi ini menjalankan sebuah pernyataan SQL untuk memasukkan data lamaran ke dalam basis data, termasuk ID perusahaan, ID user, ID lowongan, sumber informasi, pengalaman relevan, dan deskripsi.

5. **Pesan Konfirmasi**: Pengguna diberikan pesan konfirmasi bahwa lamaran mereka berhasil disubmit, dan mereka diarahkan untuk memeriksa email mereka secara berkala untuk pembaruan selanjutnya.

Fungsi ini memberikan pengguna cara yang jelas dan terstruktur untuk mengajukan lamaran pekerjaan dan memastikan bahwa informasi yang diberikan divalidasi sebelum dimasukkan ke dalam sistem.

</ul>

#### Function inputhandler

```py
def inputhandler(prompt, inputtype="str", max=None, min=None):
    while True:
        try:
            if inputtype == "str":
                userinput = input(prompt).strip()
            elif inputtype == "int":
                userinput = int(input(prompt))
            elif inputtype == "digit":
                userinput = input(prompt)
                if not userinput.isdigit():
                    print("Input hanya bisa berupa angka\n")
                    continue
            elif inputtype == "pw":
                userinput = pwinput(prompt).strip()
            elif inputtype == "nospecial":
                userinput = input(prompt).strip()
                if any(char in "!@#$%^&*()+=[]{};:'\"<>,.?/~`" for char in userinput):
                    print("Input tidak boleh mengandung karakter spesial\n")
                    continue
            
            # jika parameter max dipakai (gak kosong) dan panjang input lebih dari max
            if max is not None and len(str(userinput)) > max:
                print(f"Input terlalu panjang. Maksimum panjang adalah {max} karakter.\n")
                continue
            
            if min is not None and len(str(userinput)) < min:
                print(f"Input terlalu pendek. Minimum panjang adalah {min} karakter.\n")
                continue
            
            if '\t' in userinput or '\\' in userinput:
                print("Input tidak boleh mengandung tab atau '\\'\n")
                continue

            return userinput
        except KeyboardInterrupt:
            print("Terdeteksi interupsi\n")
        except ValueError:
            print("Input hanya bisa berupa integer\n")
        except:
            print(f"Apa lah dia\n")
```

Fungsi `inputhandler` digunakan untuk memvalidasi input pengguna sesuai dengan tipe data dan batasan panjang yang diberikan. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Parameter**:
   - `prompt`: Pesan yang akan ditampilkan kepada pengguna sebagai prompt.
   - `inputtype`: Tipe data yang diharapkan dari input pengguna. Default-nya adalah string (`"str"`).
   - `max`: Batas maksimum panjang input yang diperbolehkan.
   - `min`: Batas minimum panjang input yang diperbolehkan.

2. **Validasi Input**:
   - Fungsi ini menggunakan loop `while True` untuk terus meminta input dari pengguna sampai input yang valid diberikan.
   - Bergantung pada `inputtype`, input pengguna diambil dengan menggunakan fungsi `input()`, `int()`, atau `pwinput()` (untuk input password).
   - Input string di-strip dari spasi di awal dan akhir.
   - Jika `inputtype` adalah `"digit"`, input akan divalidasi untuk memastikan bahwa hanya terdiri dari digit angka.
   - Setelah mendapatkan input, panjangnya diperiksa menggunakan parameter `max` dan `min`. Jika panjang input tidak memenuhi kriteria, pesan kesalahan akan ditampilkan, dan loop akan melanjutkan hingga input yang valid diberikan.

3. **Penanganan Eksepsi**:
   - Fungsi ini menangani beberapa jenis eksepsi yang mungkin terjadi, seperti `KeyboardInterrupt` dan `ValueError`, dengan memberikan pesan kesalahan yang sesuai.
   - Untuk setiap jenis eksepsi selain yang sudah ditentukan, pesan umum "Apa lah dia" akan ditampilkan.

4. **Pengembalian Nilai**:
   - Setelah input yang valid diterima, nilai input tersebut dikembalikan ke pemanggil fungsi.

Fungsi ini membantu dalam memastikan bahwa input pengguna sesuai dengan harapan dan memenuhi persyaratan yang diberikan sebelum diproses lebih lanjut.

### Function clear

```py
def clear():
    print('\n'*40)
    print('\033[H')
```

Fungsi `clear()` bertujuan untuk membersihkan layar konsol dengan cara menampilkan 40 baris kosong di layar, diikuti dengan perintah untuk mengatur kursor ke posisi awal pada layar konsol menggunakan kode escape `\033[H`.

Penjelasan kode escape `\033[H`:
- `\033`: Ini adalah kode escape yang digunakan untuk menunjukkan bahwa karakter khusus akan diikuti.
- `[H`: Ini adalah kode ANSI untuk mengatur kursor ke posisi awal pada layar konsol. Saat kode ini dieksekusi, kursor akan dipindahkan ke koordinat baris 1, kolom 1 pada layar konsol.

Dengan melakukan ini, layar konsol akan terlihat bersih dan tampilan baru dapat dimulai dari posisi awal.

### Function edit

```py
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
    sql.commit()
```

Fungsi `edit()` bertujuan untuk mengizinkan pengguna mengedit data dalam database dengan memasukkan input baru. Berikut adalah penjelasan untuk setiap bagian dari fungsi ini:

1. **Parameter**:
   - `table`: Nama tabel yang akan diedit.
   - `old_data`: Data yang sudah ada sebelum diedit.
   - `fields`: Daftar bidang yang dapat diedit beserta batasan dan tipe data.

2. **Proses Edit**:
   - Pertama, layar konsol dibersihkan menggunakan fungsi `clear()`.
   - Pengguna diberi tahu bahwa mereka dapat mengosongkan input untuk menggunakan data lama jika mereka tidak ingin mengubahnya.
   - Selanjutnya, pengguna diminta untuk memasukkan nilai baru untuk setiap bidang yang ingin diedit.
   - Data lama ditampilkan diikuti dengan prompt untuk memasukkan data baru.
   - Jika bidang memiliki tipe khusus seperti `tipe_choices` atau `kelamin_choices`, pengguna diberi pilihan menggunakan fungsi `choices()`.
   - Data baru yang dimasukkan oleh pengguna kemudian divalidasi menggunakan fungsi `inputhandler()` untuk memastikan sesuai dengan batasan dan tipe data yang ditentukan.
   - Setiap bidang yang diubah disimpan dalam daftar `updates`.
   - Setelah semua bidang diperiksa, sebuah query SQL UPDATE dibuat dengan menggunakan data baru yang dimasukkan oleh pengguna.
   - Query tersebut kemudian dieksekusi untuk mengubah data di database.
   - Layar konsol kembali dibersihkan dan pengguna diberi tahu bahwa data telah berhasil diubah.

3. **Penggunaan**:
   - Fungsi ini digunakan untuk memfasilitasi proses pengeditan data dalam database, baik untuk pengguna, perusahaan, atau lowongan pekerjaan, tergantung pada tabel yang ditentukan dalam parameter `table`.

Fungsi ini memungkinkan pengguna untuk secara interaktif mengedit data dalam database dengan memasukkan nilai baru untuk bidang-bidang yang dipilih.

### Function quicksort

```py
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
```

Fungsi `quicksort()` mengimplementasikan algoritma quicksort untuk mengurutkan sebuah daftar (list) berdasarkan nilai-nilai elemennya. Berikut adalah penjelasan singkat tentang bagaimana fungsi ini bekerja:

1. **Pemahaman Dasar Quicksort**:
   - Quicksort adalah algoritma pengurutan yang bekerja dengan cara membagi daftar menjadi dua bagian, lalu mengurutkan setiap bagian tersebut secara terpisah.
   - Proses ini terus berlanjut secara rekursif sampai daftar kosong atau hanya memiliki satu elemen.

2. **Parameter Fungsi**:
   - `arr`: Daftar (list) yang akan diurutkan.
   - `key`: Kunci (opsional) untuk menentukan kriteria pengurutan berdasarkan suatu atribut dalam elemen daftar. Jika tidak ditentukan, maka pengurutan dilakukan berdasarkan nilai langsung dari elemen.
   - `order`: Urutan pengurutan, apakah ascending ('asc') atau descending ('desc'). Default-nya adalah descending.

3. **Proses Quicksort**:
   - Fungsi ini memeriksa panjang daftar. Jika panjangnya 1 atau kurang, maka daftar tersebut sudah dianggap terurut.
   - Jika panjangnya lebih dari 1, maka:
     - Fungsi memilih sebuah elemen "pivot" dari daftar tersebut (biasanya diambil dari tengah-tengah daftar).
     - Daftar dibagi menjadi tiga bagian: elemen-elemen yang lebih kecil dari pivot, elemen-elemen yang sama dengan pivot, dan elemen-elemen yang lebih besar dari pivot.
     - Proses ini dilakukan menggunakan pemahaman list (list comprehension) untuk memisahkan elemen-elemen berdasarkan kriteria pivot.
     - Selanjutnya, pemisahan ini dilakukan secara rekursif untuk setiap bagian daftar yang lebih kecil dan lebih besar dari pivot.
     - Elemen-elemen yang telah terurut dari kedua bagian tersebut digabungkan kembali bersama dengan elemen-elemen yang sama dengan pivot.
     - Hasil akhirnya adalah daftar yang terurut.

4. **Penanganan Kunci (Key)**:
   - Jika `key` ditentukan, maka pemisahan elemen-elemen dilakukan berdasarkan nilai dari atribut yang diberikan oleh `key`.
   - Jika `key` adalah fungsi, maka nilai-nilai dari elemen akan dievaluasi dengan menggunakan fungsi tersebut sebelum dibandingkan.
   - Jika `key` adalah sebuah string, maka pemisahan akan dilakukan berdasarkan nilai dari atribut yang memiliki nama tersebut dalam setiap elemen.

Fungsi ini dapat digunakan untuk mengurutkan daftar berdasarkan nilai-nilai elemennya, baik secara ascending maupun descending, dengan atau tanpa menggunakan kunci (key) untuk menentukan kriteria pengurutan.

### Function jumpsearch

```py
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
```

Fungsi `jumpsearch` mengimplementasikan algoritma pencarian Jump Search untuk mencari keyword dalam suatu daftar `entries`. Berikut adalah penjelasan singkat tentang cara kerja fungsi ini:

1. **Pra-Pemrosesan Data**:
   - Daftar `entries` dipecah menjadi kata-kata individual dan diindeks menggunakan nomor entri aslinya.
   - Setiap kata dikonversi menjadi huruf kecil dan dipecah berdasarkan spasi.
   - Setiap kata bersama dengan indeks entri aslinya ditambahkan ke dalam daftar tuple `items`.

2. **Pengurutan Data**:
   - Daftar `items` diurutkan berdasarkan kata-kata secara alfabetis menggunakan algoritma quicksort. Pengurutan dilakukan untuk mempermudah pencarian nantinya.

3. **Inisialisasi Variabel**:
   - Variabel `result` digunakan untuk menyimpan indeks entri yang cocok dengan kata kunci.
   - Variabel `step` dihitung sebagai akar kuadrat dari panjang `items` dan digunakan sebagai langkah untuk melakukan pencarian.

4. **Pencarian**:
   - Kata kunci dipecah menjadi kata-kata individual.
   - Setiap kata kunci dicocokkan secara bergantian dengan kata-kata dalam `items`.
   - Algoritma mencari lokasi di mana kata kunci dapat ditemukan atau kemungkinan di mana kata kunci harus ditempatkan dalam daftar yang telah diurutkan.

5. **Penghilangan Duplikat**:
   - Setelah pencarian selesai, indeks entri yang ditemukan disimpan dalam himpunan (`set`) untuk menghilangkan duplikat.
   - Daftar `entries` kemudian dibuat ulang berdasarkan indeks entri yang unik tersebut.
   - Hanya entri yang cocok dengan kata kunci yang akan dikembalikan.

Fungsi ini memberikan hasil pencarian dari daftar `entries` yang sesuai dengan kata kunci yang diberikan, dengan menghilangkan duplikat dan mengembalikan entri yang cocok.

### Function color

```py
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
```

Fungsi `color` digunakan untuk memberi warna pada teks menggunakan kode ANSI escape. Berikut adalah penjelasan singkat tentang cara kerja fungsi ini:

1. **Daftar Kode Warna ANSI**:
   - Fungsi ini memiliki daftar yang memetakan nama warna ke kode ANSI escape yang sesuai. Setiap warna memiliki kode ANSI yang berbeda.

2. **Pengecekan Validitas Warna**:
   - Sebelum menerapkan warna pada teks, fungsi memeriksa apakah nama warna yang diberikan valid atau tidak. Jika warna yang diberikan tidak terdaftar dalam daftar warna yang didukung, fungsi akan mengembalikan pesan kesalahan.

3. **Penerapan Warna**:
   - Setelah memastikan bahwa nama warna yang diberikan valid, fungsi mengambil kode ANSI escape yang sesuai untuk warna tersebut.
   - Kemudian, teks yang diberikan dikelilingi dengan kode ANSI escape warna yang sesuai untuk memberi efek warna.
   - Akhirnya, teks yang telah diwarnai bersama dengan kode reset ANSI (untuk mengembalikan warna ke nilai default) dikembalikan sebagai output dari fungsi.

Fungsi ini memungkinkan untuk memberi warna pada teks dengan mudah hanya dengan menentukan nama warna yang diinginkan.

### Function choices

```py
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
```

Fungsi `choices` digunakan untuk menampilkan opsi pilihan ke pengguna dan meminta mereka untuk memilih. Berikut adalah penjelasan singkat tentang cara kerja fungsi ini:

1. **Menampilkan Opsi Pilihan**:
   - Fungsi ini menerima daftar opsi pilihan sebagai argumen. Setiap opsi ditampilkan di layar bersama dengan nomor urutannya.

2. **Input dan Validasi Pilihan**:
   - Setelah menampilkan opsi pilihan, fungsi meminta pengguna untuk memasukkan nomor opsi yang mereka pilih.
   - Kemudian, fungsi menggunakan `inputhandler` untuk memvalidasi masukan pengguna. Jika masukan tidak berupa angka atau berada di luar jangkauan nomor opsi yang tersedia, fungsi akan memberikan pesan kesalahan dan meminta pengguna untuk memasukkan kembali pilihan mereka.

3. **Pengembalian Nilai**:
   - Setelah pengguna memilih opsi yang valid, fungsi mengembalikan opsi tersebut.
   - Fungsi juga memiliki argumen opsional `re` yang menentukan jenis pengembalian nilai:
     - Jika `re` disetel ke `'num'`, maka fungsi akan mengembalikan nomor opsi yang dipilih.
     - Jika `re` disetel ke `'opt'`, maka fungsi akan mengembalikan opsi yang dipilih.

Fungsi ini memungkinkan pengguna untuk memilih opsi dari daftar opsi yang diberikan dengan mudah dan memastikan bahwa pilihan mereka valid.

### Function banner

```py
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
```

Fungsi `banner` digunakan untuk membuat teks menjadi bagian dari sebuah banner dengan garis pemisah di sekelilingnya. Berikut adalah penjelasan singkat tentang cara kerja fungsi ini:

1. **Parameter Masukan**:
   - Fungsi menerima satu parameter, yaitu `text`, yang merupakan teks yang ingin dimasukkan ke dalam banner.

2. **Panjang Banner**:
   - Panjang banner ditetapkan sebagai 65 karakter.

3. **Perhitungan Padding**:
   - Panjang teks yang diberikan sebagai parameter diukur.
   - Padding dihitung sebagai selisih antara panjang banner dan panjang teks.
   - Padding dibagi menjadi dua bagian: padding kiri dan padding kanan.

4. **Membuat Banner**:
   - Karakter `'='` digunakan untuk membuat garis pemisah.
   - Padding kiri dan padding kanan digunakan untuk menentukan jumlah karakter `'='` yang akan ditempatkan sebelum dan sesudah teks, sehingga teks berada di tengah banner.

5. **Pengembalian Nilai**:
   - Fungsi mengembalikan teks yang telah dimasukkan ke dalam banner dengan garis pemisah di sekelilingnya.

Dengan menggunakan fungsi ini, pengguna dapat dengan mudah membuat teks mereka menonjol di dalam banner dengan garis pemisah yang konsisten di sekitarnya.

### Function login

```py
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
```

Fungsi `login` bertujuan untuk memberikan opsi kepada pengguna untuk masuk ke dalam sistem dengan peran yang berbeda-beda. Berikut penjelasan singkat tentang cara kerja fungsi ini:

1. **Tampilan Menu Login**:
   - Fungsi ini mencetak menu login menggunakan fungsi `banner`, yang menampilkan pilihan untuk login sebagai admin, user, atau menggunakan akun perusahaan.

2. **Pemilihan Opsi**:
   - Pengguna diminta untuk memilih opsi login sesuai dengan peran yang dimilikinya.
   - Jika pengguna memilih untuk login sebagai admin, fungsi akan memanggil fungsi `Admin.login()`.
   - Jika pengguna memilih untuk login sebagai user, fungsi akan memanggil fungsi `User.login()`.
   - Jika pengguna memilih untuk login menggunakan akun perusahaan, fungsi akan memanggil fungsi `Perusahaan.login()`.
   - Jika pengguna memilih untuk kembali, fungsi akan mengakhiri proses login dengan memecahkan loop.

Dengan menggunakan fungsi `login`, pengguna diberikan kemudahan untuk memilih peran mereka dalam sistem dan masuk ke dalam akun yang sesuai dengan peran tersebut.

### Function register

```py
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
```

Fungsi `register` digunakan untuk memberikan opsi kepada pengguna untuk mendaftar akun baru, baik sebagai pengguna (user) maupun perusahaan. Berikut adalah penjelasan singkat tentang cara kerja fungsi ini:

1. **Tampilan Menu Registrasi**:
   - Fungsi ini mencetak menu registrasi menggunakan fungsi `banner`, yang menampilkan pilihan untuk mendaftar sebagai pengguna atau perusahaan.

2. **Pemilihan Opsi**:
   - Pengguna diminta untuk memilih opsi registrasi sesuai dengan jenis akun yang ingin mereka buat.
   - Jika pengguna memilih untuk mendaftar sebagai pengguna, fungsi akan memanggil fungsi `User.register()` untuk memulai proses registrasi pengguna.
   - Jika pengguna memilih untuk mendaftar sebagai perusahaan, fungsi akan memanggil fungsi `Perusahaan.register()` untuk memulai proses registrasi perusahaan.
   - Jika pengguna memilih untuk kembali, fungsi akan mengakhiri proses registrasi dengan memecahkan loop.

Dengan menggunakan fungsi `register`, pengguna diberikan opsi untuk membuat akun baru sesuai dengan jenis akun yang mereka inginkan.

### sql,user data,admin data,perusahaan data

```
sql = MySQLHandler('root', '', 'localhost', 'lowongankerja')

# predefine untuk pas login biar gak error
user_data = {}
admin_data = {}
perusahaan_data = {}
```

mendefinisikan variabel `sql` yang merupakan instance dari kelas `MySQLHandler`. 

Variabel `sql` digunakan untuk berinteraksi dengan database MySQL. Dalam inisialisasi `MySQLHandler`, memberikan parameter seperti nama pengguna (`'root'`), kata sandi (`''`), host (`'localhost'`), dan nama database (`'lowongankerja'`). Ini menunjukkan bahwa Anda terhubung ke server MySQL yang berjalan pada komputer lokal Anda dan mengakses basis data bernama `'lowongankerja'`.

Setelah itu, mendefinisikan beberapa variabel global, yaitu `user_data`, `admin_data`, dan `perusahaan_data`, yang awalnya kosong (`{}`). Variabel-variabel ini kemungkinan besar akan digunakan untuk menyimpan data pengguna, admin, dan perusahaan setelah mereka berhasil login. 

### Bagian menu utama

```py
os.system('') # entah kenapa kalau gak pakai ini warna teksnya gak muncul di beberapa device

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

```
Loop `while True` membuat program berjalan secara terus-menerus hingga kondisi di dalamnya tidak terpenuhi lagi. Di setiap iterasi dari loop ini, program akan membersihkan layar terminal, menampilkan judul program dengan menggunakan fungsi `banner`, dan menampilkan pilihan menu untuk pengguna.

Pengguna dapat memilih antara tiga opsi:
1. **Login**: Jika pengguna memilih opsi ini, fungsi `login()` akan dipanggil untuk memungkinkan pengguna masuk ke dalam sistem.
2. **Register**: Jika pengguna memilih opsi ini, fungsi `register()` akan dipanggil untuk memungkinkan pengguna membuat akun baru di dalam sistem.
3. **Keluar**: Jika pengguna memilih opsi ini, program akan keluar dari loop `while True` dan berhenti.

Setelah pengguna memilih salah satu dari tiga opsi tersebut, program akan mengevaluasi pilihan pengguna dan menjalankan fungsi yang sesuai dengan pilihan tersebut. Proses ini akan berulang terus menerus selama pengguna tidak memilih untuk keluar dari program.

## CARA PENGGUNAAN

### Halaman Depan
Ketika program dijalankan, akan muncul tampilan opsi untuk login bagi yang sudah mempunyai akun, registrasi bagi yang belum mempunyai akun dan keluar untuk menghentika program.
![halamanawal](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144436692/2e5f8ecc-762d-44ef-97c1-1a56b6febb2b)

- Login

Jika memilih login, maka program akan menyediakan 3 opsi role yaitu admin, user dan Perusahaan. Pada opsi nomor 4, program akan kembali ke halaman utama.
![opsilogin](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144436692/35452d64-28d1-4867-892e-bf240b4e9715)

- Registrasi

Bagi User maupun Perusahaan yang belum memiliki akun, program menyediakan menu registrasi agar terdaftar dalam program lowongan kerja ini.
![regist](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144436692/3b3975ac-cec6-4117-9843-595c4eb9131f)

Dalam menu registrasi, terdapat registrasi untuk user dan perusahaan
![pilihanregist](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144436692/ef93fc15-df64-4c27-a6ca-aae1db704a85)

Contoh, ini adalah proses Registrasi user. Program meminta user untuk menginput data yang diperlukan untuk melengkapi profil.
![prosesregistrasi](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144436692/9f555675-068f-470b-bc16-2365413702b4)

Jika data yang diinputkan Valid, program langsung mengarahkan ke menu halaman utama user.
![registberhasil](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144436692/81d8f733-89b2-490a-b6a2-ac452b936b5f)

- Keluar
  
Untuk menghentikan program, pilih keluar.
![keluar](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144436692/87e482e4-1187-43bd-b8d2-0377cab3dd07)


- Login Gagal

Jika pengguna menginputkan email atau password atau keduanya yang salah, program akan menampilkan pemberitahuan seperti dibawah ini.

![logingagal](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144436692/01762b7b-1812-4c9e-aaf2-8bebcd3be6c3)


