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


- *Fungsionalitas*
  
#(built-in)

![Screenshot 2024-04-30 200314](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/e3deae6e-9e0c-40a0-814a-9742bddf17d4)

1. **`import os`**: Modul `os` memberikan alat untuk berinteraksi dengan sistem operasi, seperti mengelola file dan direktori, mengakses variabel lingkungan, dan menjalankan perintah shell.

2. **`import math`**: Modul `math` menyediakan fungsi matematika dasar, seperti perhitungan akar kuadrat, sinus, kosinus, dan logaritma.

#(external)

![Screenshot 2024-04-30 200327](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/25c8f224-9ff0-4cf0-b1af-6d9f216558dd)

1. **`import mysql.connector`**: Ini memungkinkan koneksi dan manipulasi database MySQL dari Python.

2. **`from pwinput import pwinput`**: Ini memungkinkan input password yang aman.

3. **`from prettytable import PrettyTable`**: Ini digunakan untuk membuat dan mencetak tabel yang rapi di konsol.

-Class Node

![Screenshot 2024-04-30 201040](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/5369419c-2d10-4b1d-97c6-67045fe9a31d)

Fungsi kelas “Node”. Setiap node dalam linked list akan memiliki atribut “data” untuk menyimpan nilai dan atribut “next” untuk menunjukkan ke node berikutnya dalam linked list.

-Class LinkedList

#(fungsi def init)

![Screenshot 2024-04-30 201718](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/1f5cddab-3a67-43f0-9359-14588cd4d2b3)

*Class LinkedList adalah salah satu struktur data yang yang terdiri dari node-node yang terhubung satu sama lain. Dalam Class LinkedList, fungsi def init dan self berperan sebagai konstruktor untuk membuat instance dari class tersebut

*Nantinya setiap method dalam linked list akan memiliki parameter self. Dengan menggunakan parameter self kita dapat mengakses atribut-atribut yang ada pada Class LinkedList

#(fungsi def append)

![Screenshot 2024-04-30 201923](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/e22d9551-7a9d-45bb-a292-a5c5b2ce7518)

* Method ini berfungsi untuk menambahkan node baru di bagian akhir linked list. Method kemudian akan membuat istance baru dari class Node dan menyimpan data pada node tersebut.

#(fungsi def display)

![Screenshot 2024-04-30 202740](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/3070f24c-6cf9-4969-9766-cb8904df2ad8)

* ini berfungsi untuk menampilkan seluruh data-data yang berada di dalam database yang kemudian tersusun di dalam table berkat bantuan dari library prettytable.

#(fungsi def getitem)

![Screenshot 2024-04-30 202952](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/03d2744b-3265-4506-ba6c-208f3723457b)

* biar bisa langsung pakai list[index] macam array biasanya

#(fungsi def iter (self))

![Screenshot 2024-04-30 203433](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/0dfe31b9-356f-4215-b06f-b052fe38ff72)

* biar bisa pakai for loop 

#(fungsi def len (self))

![Screenshot 2024-04-30 203628](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/fbeb5a35-ebf5-4899-826b-6db9b291093a)

* biar bisa pakai len()


-Class MySQLHandler

#(def init)

![Screenshot 2024-04-30 203955](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/1d4f35fe-fa94-43b5-9378-f7ccd01a1fc9)

1.Kelas MySQLHandler merupakan kerangka kerja untuk mengelola koneksi dan operasi database MySQL.

2.Fungsi __init__ digunakan untuk menginisialisasi objek MySQLHandler dengan informasi koneksi yang diberikan.

#(def connect)

![Screenshot 2024-04-30 204550](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/3dae24f0-f212-4d7d-8b22-f698845abf07)

* Fungsi connect(self) dalam kelas MySQLHandler bertujuan untuk membuat koneksi ke server MySQL menggunakan informasi yang telah diberikan saat objek MySQLHandler diinisialisasi.

#(def execute)

![Screenshot 2024-04-30 205318](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/17db4168-583e-4f5f-9744-7bb84999d383)

* Fungsi execute dalam sebuah kelas yang berhubungan dengan database, biasanya digunakan untuk mengeksekusi perintah SQL ke dalam database yang terhubung.

#(def fetchall)

![Screenshot 2024-04-30 205510](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/0917aa5d-85f8-4292-8957-5051d4cb9fb5)

* Fungsi fetchall digunakan dalam koneksi basis data untuk mengambil semua baris hasil dari sebuah query yang dieksekusi.

#(def fetchone)

![Screenshot 2024-04-30 205750](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/4b0933e0-6a3c-4e00-a2d7-4138e8bb03cf)

* Fungsi fetchone dalam koneksi basis data digunakan untuk mengambil satu baris hasil dari sebuah query yang dieksekusi. 

#(def description)

![Screenshot 2024-04-30 205928](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/1f865fb8-a911-4b1e-8885-a3b4d2382838)

* Fungsi description biasanya digunakan untuk mengembalikan deskripsi kolom dari hasil query.

#(def commit)

![Screenshot 2024-04-30 210301](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/52782cf3-a4f0-42a8-b07c-fa0bd9419281)

* Fungsi commit dalam konteks basis data digunakan untuk menyimpan perubahan yang telah dilakukan dalam transaksi ke dalam basis data secara permanen.

#(def close)

![Screenshot 2024-04-30 210447](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/2ff52fa5-2b3e-446e-b897-73565368f478)

* Fungsi close dalam konteks koneksi basis data digunakan untuk menutup koneksi atau kursor yang telah dibuka.


-Class Admin

#(def login)

![Screenshot 2024-04-30 210720](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/df251f4b-9253-403e-b9b9-adc7fb88c82f)

* Kelas `Admin` adalah representasi dari administrator dalam sebuah sistem atau aplikasi. Admin memiliki akses dan kekuatan lebih dalam mengelola sistem dibandingkan pengguna biasa. Ini dapat mencakup atribut seperti username, password, role, email, dan metode untuk mengelola sistem, seperti menambah, menghapus, atau memperbarui informasi pengguna dan data lainnya.

*Fungsi Login adalah program yang digunakan untuk menampilkan perintah terkait login sebelum masuk ke dalam aplikasi, di dalamnya terdapat percabangan(if, elif, else) yang digunakan untuk mengeksekusi kode tertentu hanya jika kondisi tersebut terpenuhi.

1.Membersihkan Layar: Fungsi clear() dipanggil untuk membersihkan layar konsol sebelum tampilan login dimulai.

2.Input Username: Pengguna diminta untuk memasukkan username mereka.

3.Query Database: Fungsi execute digunakan untuk menjalankan perintah SQL yang mencari admin dengan username yang cocok dalam tabel admin.

4.Pengecekan Username: Jika admin dengan username tersebut ditemukan dalam database, pengguna diminta untuk memasukkan password mereka.

5.Validasi Password: Password yang dimasukkan oleh pengguna dibandingkan dengan password yang disimpan dalam database. Jika cocok, pengguna berhasil masuk ke sistem dan menu admin ditampilkan. Jika tidak, pesan kesalahan ditampilkan.

6.Tindakan untuk Username Tidak Terdaftar: Jika admin dengan username yang dimasukkan tidak ditemukan dalam database, pesan kesalahan ditampilkan.


#(def profil)

![Screenshot 2024-04-30 213910](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/0183a3c8-a277-49fb-8d85-de6f05b2b911)

Fungsi `profil` digunakan untuk menampilkan profil admin saat ini beserta jabatan dan hak akses yang dimilikinya. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Query Database**: Fungsi `execute` digunakan untuk menjalankan perintah SQL yang mencari admin dengan ID admin yang sedang aktif dalam tabel admin.

2. **Pengolahan Data**: Jika data admin ditemukan dalam database, informasi admin disimpan dalam variabel `admin_data`.

3. **Tampilan Profil**: Informasi admin, seperti username, ID, dan jabatan, ditampilkan ke layar.

4. **Hak Akses**: Hak akses admin ditampilkan berdasarkan jabatan. Berbagai aksi yang dapat dilakukan oleh admin ditampilkan dengan warna yang sesuai.


#(def menu)

![Screenshot 2024-04-30 214449](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/902725e4-eb36-41e5-a0f0-e493d7d4a32b)

![Screenshot 2024-04-30 214808](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/22bb43e2-d7ee-48b5-807f-daaad7ff84ca)

![Screenshot 2024-04-30 215526](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/ba3f2288-af21-4f5a-aac1-a4f71f23a9ba)

![Screenshot 2024-04-30 215643](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/2541406d-6adb-469c-86e2-34425123941d)

![Screenshot 2024-04-30 220010](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/a3e9bbb6-e9ab-4599-858d-040453ada25b)

![Screenshot 2024-04-30 221312](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/415cc76d-824c-4e5c-87d1-c0eaa57e089f)

![Screenshot 2024-04-30 221348](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/1f55d7d4-5bfd-4707-9a15-272eb72a60fd)

![Screenshot 2024-04-30 221409](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/5a8455ab-fa6a-4170-a37d-da994e80eb76)

![Screenshot 2024-04-30 221435](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/21465ca6-bbf0-4a9a-a02e-ae6b5f5a9e83)

![Screenshot 2024-04-30 221453](https://github.com/PA-B23-KELOMPOK3/PA-B23-KELOMPOK3/assets/144904706/5893813a-6003-4e1e-bdba-000aede6ec09)


Fungsi `menu` adalah bagian dari sistem yang bertanggung jawab untuk menampilkan menu utama admin, memungkinkan mereka untuk memilih dan melakukan berbagai tindakan terkait manajemen sistem. Berikut adalah penjelasan singkat tentang fungsi ini:

1. **Tampilan Menu Utama**: Fungsi `choices` digunakan untuk menampilkan pilihan menu utama kepada admin. Admin dapat memilih dari berbagai opsi, seperti melihat profil, mengelola lowongan, mengelola user, mengelola perusahaan, mengelola lamaran, atau keluar dari sistem.

2. **Pilihan Profil Admin**: Jika admin memilih opsi "Profil", fungsi `profil` dari kelas `Admin` dipanggil untuk menampilkan profil admin saat ini. Admin juga diberikan opsi untuk mengedit data profilnya.

3. **Pilihan Kelola Lowongan**: Jika admin memilih opsi "Kelola Lowongan", mereka dapat memilih untuk melihat, mengurutkan, mencari, atau mengelola lowongan pekerjaan yang ada dalam sistem.

4. **Pilihan Kelola User**: Admin dapat memilih opsi "Kelola User" untuk melihat, mengurutkan, mencari, atau menghapus pengguna (user) dalam sistem.

5. **Pilihan Kelola Perusahaan**: Admin dapat memilih opsi "Kelola Perusahaan" untuk melihat, mengurutkan, mencari, atau menghapus perusahaan yang terdaftar dalam sistem.

6. **Pilihan Kelola Lamaran**: Admin dapat memilih opsi "Kelola Lamaran" untuk melihat, mengurutkan, mencari, atau menghapus lamaran pekerjaan yang telah diajukan oleh pengguna.

7. **Keluar dari Menu**: Admin dapat memilih opsi "Keluar" dari menu utama untuk keluar dari sistem.





