# Project Akhir ASD Kelompok 3
# Program Peluang Kerja Untuk Semua: Membantu Masyarakat Menemukan Pekerjaan Yang Sesuai Dengan Mudah

_Anggota Kelompok:_

*• Joshua Timothy (2309116070)*

*• Aqiyah Zulqiyah (2309116075)*

*• Allya Putri Ditya (2309116078)*

*• Reisya Nurfaris D. A. (2309116102)*

## **Deskripsi Program**

### 🪐1. Tujuan Program

_Program ini bertujuan untuk membantu masyarakat secara menyeluruh dalam menemukan pekerjaan dengan lebih mudah dan efisien. Kami memahami tantangan yang dihadapi banyak orang dalam mencari pekerjaan dikarenakan proses rekrutmen yang rumit. Dengan menyediakan platform yang mempermudah penelusuran lowongan kerja melalui berbagai filter dan kategori, serta meningkatkan akses informasi dengan detail yang akurat tentang deskripsi pekerjaan dan kualifikasi yang dibutuhkan, kami berharap dapat membantu pencari kerja menemukan pekerjaan yang sesuai dengan minat dan keterampilan mereka._

### ☀️2. Pengguna Program

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
- *Proses Memilih Masuk/Mendaftar sebagai user*
  ![Flowchart Capstone-Halaman-1 (1) (2) (3)](https://github.com/aqiyahzh/nyoba/assets/144746779/91e5ea95-909e-4f04-a9a7-69590e930f5e)

- *Proses Meilih Log in sebagai Admin*
![Flowchart Capstone-Halaman-1 (1)](https://github.com/aqiyahzh/nyoba/assets/144746779/d734b9ca-6547-403f-b77a-71ea46495cd0)

- *Proses Log in sebagai User/Pelamar*
![Flowchart Capstone-Halaman-1 (2)](https://github.com/aqiyahzh/nyoba/assets/144746779/cdfc1841-2496-4be9-bb3f-0efe02ada18e)

- *Proses Log in sebagai Perusahaan*
![Flowchart Capstone-Halaman-1 (3) (1)](https://github.com/aqiyahzh/nyoba/assets/144746779/54cc4561-38f7-4ca8-86a8-bee3d07cc416)

- *Proses kembali ke menu sebelumnya*
![Flowchart Capstone-Halaman-1 (3) (2)](https://github.com/aqiyahzh/nyoba/assets/144746779/52a9ad5b-fc95-485b-8ec5-ae889982bdfd)

- *Proses Registrasi*
![register](https://github.com/aqiyahzh/nyoba/assets/144746779/961bb501-5aab-489c-9a12-a142409f4aae)

- *Proses keluar dari program*
![Flowchart Capstone-Halaman-1 (4) (1)](https://github.com/aqiyahzh/nyoba/assets/144746779/06ddb02c-e02a-45f3-ac0b-94e379918378)


### Halaman Menu Admin
- *Proses memilih mengelola lowongan, user, perusahaan, atau lamaran*
![Flowchart Capstone-Halaman-2 1](https://github.com/aqiyahzh/nyoba/assets/144746779/8d1f4c8d-703a-4912-b01b-77faea39caa3)

- *Proses mengelola lowongan*
![mengelola lowongan](https://github.com/aqiyahzh/nyoba/assets/144746779/bd519e18-62a2-4b4b-a1ad-cdc217b3c321)

- *Proses mengelola user*
![mengelola user](https://github.com/aqiyahzh/nyoba/assets/144746779/4c696743-7755-44b4-bd37-c166f77782d6)

- *Proses mengelola perusahaan*
![mengelola perusahaan](https://github.com/aqiyahzh/nyoba/assets/144746779/f86b0398-c96f-4fde-8adb-0fa8e938d564)

- *Proses mengelola lamaran*
![mengelola lamaran](https://github.com/aqiyahzh/nyoba/assets/144746779/5d7a5b96-0e09-4302-877f-7dbd831e75e4)

- *Proses Admin kembali ke menu log in*
![admin kembali ke menu](https://github.com/aqiyahzh/nyoba/assets/144746779/008a2e35-ae5a-4694-b02f-8b52fbb60dae)


### Halaman Menu User
- *Proses user memilih lowongan*
![Flowchart Capstone-Halaman-3(1) 1](https://github.com/aqiyahzh/nyoba/assets/144746779/f47e689e-e87b-4040-8f68-1891aa22474e)

- *Proses user mengisi lamaran cepat dan di bawahnya keluar kemenu sebelumnya*
![Flowchart Capstone-Halaman-3(1) 2](https://github.com/aqiyahzh/nyoba/assets/144746779/a450209b-3499-43df-9713-65561a2582da)

- *Proses user memilih keluar ke menu log in*
![Flowchart Capstone-Halaman-3(1) 3](https://github.com/aqiyahzh/nyoba/assets/144746779/d21848f3-4094-44d7-820d-e5492ca8e6d5)


### Halaman Menu Perusahaan
- *Proses memilih melihat profil perusahaan, lihat lamaran atau lihat lowongan*
![Flowchart Capstone-Halaman-4 1](https://github.com/aqiyahzh/nyoba/assets/144746779/47a8f297-4e39-45e7-b7b8-fa85303602dc)

- *Proses perusahaan mengedit profil perusahaan*
![perusahaan mengeidt profil](https://github.com/aqiyahzh/nyoba/assets/144746779/8c00fc45-d787-42cf-a439-ef1c700c07a7)

- *Proses melihat daftar lamaran dan menghapus data lamaran*
![daftar lamaran dan menghapus](https://github.com/aqiyahzh/nyoba/assets/144746779/8aeeaa32-3f5e-4ba8-b35b-24aac530516b)

- *Proses melihat daftar lowongan, memilih lowongan untuk dihapus atau diedit*
![melihat daftar lowongan](https://github.com/aqiyahzh/nyoba/assets/144746779/c7ed6778-1973-4a49-aa84-44a19485bfd1)

- *Proses perusahaan submit lowongan baru, kembali ke menu sebelumnya*
![perusahaan submit lowongan baru](https://github.com/aqiyahzh/nyoba/assets/144746779/6a2edf1b-2882-48b7-b59d-f3a053bda12c)

- *Proses perusahaan memilih keluar ke menu log in*
![perusahaan keluar ke menu log in](https://github.com/aqiyahzh/nyoba/assets/144746779/0358dc29-4a0f-4dac-8f22-4d9e7a340547)
