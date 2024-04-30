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
