# Tugas 4 PBP
 
 Muhammad Faris Umar Rahman - 
 2106702402
 
**Link tautan ke aplikasi heroku:**
 
 https://tugas2pbpfaris.herokuapp.com/todolist/login/

 
 
**Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?**

 CSRF atau Cross Site Request Forgery merupakan sebuah proteksi pada elemen form yang berfungsi untuk memastikan form diisi dari domain yang terpercaya. Jika tidak ada potongan tersebut, maka serangan bisa saja terjadi.
 
**Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.**
 
Ya bisa. Kita bisa menggunakan label+input untuk memasukkan data, dan juga button untuk mensubmit data tersebut

 **Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**
 
Data yang diisikan oleh user di dalam HTML form, akan melalui perintah form.save pada views.py. Selanjutnya data form tersebut akan disimpan dalam bentuk model yang telah kita definisikan ke dalam database. Selanjutnya saat template HTML membutuhkan data tersebut, data dipanggil dari database
 
**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
 1. Melakukan command `python manage.py startapp todolist` untuk menginisiasi aplikasi
 2. Menambahkan aplikasi todolist ke dalam list installed apps yang ada di settings.py serta mengatur urls.py
 3. Menambahkan kelas Task serta atribut sesuai yang dibutuhkan pada models.py
 4. Membuat fungsi login, register, logout pada views.py. Lalu menambahkan route fungsi tersebut pada urls.py. Serta menambahkan template HTML nya
 5. Membuat HTML utama (todolist.html) yang sesuai dibutuhkan
 6. Membuat forms.py untuk mengatur data yang diinput user. Mengaitkan kelas yang ada di forms.py, ke fungsi create_task (views.py), serta mengatur HTML create-task
 7. Melakukan routing pada urls.py
 8. Push ke github, isi secret actions, lalu cek workflow tersebut berhasil untuk memastikan deployment berhasil
 9. Melakukan create akun dan create task pada aplikasi yang sudah dideploy
