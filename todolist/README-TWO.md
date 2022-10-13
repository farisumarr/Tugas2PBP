# Tugas 6 PBP
 
 Muhammad Faris Umar Rahman - 
 2106702402
 
**Link tautan ke aplikasi heroku:**

 https://tugas2pbpfaris.herokuapp.com/todolist/login/
 
**Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**

Dalam asynchronous programming bisa melakukan multiple request secara bersamaan (multithread process). Sedangkan synchronous hanya 1 request di 1 waktu (single thread process)

**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

Paradigma Event-Driven Programming merupakan sebuah paradigma programming dimana flow atau alurnya diatur oleh event yang dilakukan oleh user.
Contoh penerapannya, melalui fitur add task. Dimana fungsi add task baru dijalankan ketika user menekan tombol add task

**Jelaskan penerapan asynchronous programming pada AJAX.**

Asynchronous programming pada Ajax, menjadikan user tidak perlu me-refresh halaman webpage untuk mengupdate data.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. Membuat fungsi yang mereturn json, lalu diroute di urls.py
2. Membuat html todolist dalam ajax dengan data yang dilakukan asynchronous function
3. Membuat fungsi yang mengembalikan html todolist ajax pada views.py
4. Membuat fungsi pada views.py untuk menghandle data baru
5. Lalu membuat fungsi asynchronous untuk mengambil data serta melakukan refresh
6. Menambahkan kelas modal untuk form
7. Membuat button serta fungsi asynchronous untuk menambahkan data
8. Lalu merouting untuk penambahan data tersebut di views dan urls
