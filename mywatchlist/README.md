 # Tugas 3 PBP
 
 Muhammad Faris Umar Rahman
 2106702402
 
 
**Jelaskan perbedaan antara JSON, XML, dan HTML!**

 HTML digunakan untuk tampilan user interface. Sedangkan JSON dan XML untuk men-deliver data. JSON sendiri merupakan representasi object, sedangkan XML adalah sebuah markup language yang menggunakan struktur tag untuk merepresantasikan item data
 
**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
 
 Dalam pengimplementasian platform terkadang kita membutuhkan data yang dinamis untuk ditampilkan. Sehingga untuk perlu mengganti data dalam tampilan, kita tidak perlu memperbaiki tampilan, cukup melakukan update data dan mendeliver data tersebut
 
 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 1. Melakukan command `python manage.py startapp mywatchlist` untuk menginisiasi aplikasi
 2. Menambahkan aplikasi mywatchlist ke dalam list installed apps yang ada di settings.py serta mengatur urls.py
 3. Menambahkan atribut yang dibutuhkan pada models.py
 4. Menambahkan folder fixtures dan file JSON yang berisi data-data tersebut
 5. Menambahkan fungsi pada views.py, dan melengkapi fungsi2 tersebut (show_watchlist, show_xml, show_json, show_xml_by_id, show_json_by_id)
 6. Menambahkan path fungsi2 yg ada di views.py, ke dalam list urlpatterns yang ada di urls.
 7. Push ke github, isi secret actions, lalu cek workflow tersebut berhasil untuk memastikan deployment berhasil

**Screenshot Postman**
![Screenshot (304)](https://user-images.githubusercontent.com/92006646/191585033-9f424257-b033-4ace-9c21-643baa79147e.png)
![Screenshot (306)](https://user-images.githubusercontent.com/92006646/191585042-9b8a3091-9202-4ea6-a2e3-567a53da0c71.png)
![Screenshot (305)](https://user-images.githubusercontent.com/92006646/191585044-8f860c2e-2f69-48a8-b429-be4ed438476f.png)
