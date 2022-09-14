# Readme Tugas 2
Muhammad Faris Umar Rahman

2106702402

**- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;**

Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan penjelasan keterkaitan antar berkas:
![urls py](https://user-images.githubusercontent.com/92006646/190192358-903607aa-8321-404c-bb1d-6fd8f6cccb83.jpg)

**- Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Virtual environment dipertimbangkan menjadi _best practice_ dalam pembuatan aplikasi web berbasis Django. Hal ini disebabkan karena penggunaan virtual environment mengurangi terjadinya konflik _dependencies_. Walaupun, tanpa virtual environment pun, pembuatan aplikasi web berbasis Django tetap bisa dilakukan

**- Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**
1. Implementasi untuk pembuatan fungsi tersebut, yaitu mengambil semua objek atau data yang ada di model, lalu data tersebut dimasukkan ke suatu dictionary yang nantinya akan direturn bersama dengan berkas html yang kita inginkan
2. Memanggil fungsi yang sudah dibuat tersebut di dalam urls.py dengan menggunakan fungsi path
3. Menjalankan perintah `python manage.py makemigrations`, `python manage.py migrate`, dan `python manage.py loaddata initial_wishlist_data.json` untuk membuat skema migrasi, menerapkan skema migrasi, serta memasukkan data tersebut ke database lokal. Barulah date tersebut akan berjalan melalui models,py, views.py hingga sampai ke html
4. Karena sudah terdapat file `dpl.yml`, untuk melakukan deploy tinggal menambahkan API Key Heroku dan App Name ke dalam variable repository secret, lalu melakukan re-run pada actions yang gagal
