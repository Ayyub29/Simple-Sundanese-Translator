# Simple Sundanese Translator
Simple Sundanese to Bahasa Indonesia translator using Pattern Matching

## Latar Belakang
Pada suatu hari, ada mahasiswa bernama Riyugan yang baru pindah ke Bandung. Pada awalnya dia mengalami kesulitan untuk bersosialisai dengan lingkungan sekitar karena orang-orang di lingkungannya yang baru hanya berbicara dalam bahasa Sunda. Beruntungnya Riyugan punya teman dari kampung halamannya, yaitu Anda, untuk diminta membuat penerjemah sederhana dari Bahasa Sunda ke Bahasa Indonesia begitu pula sebaliknya untuk memudahkan dirinya bersosialisasi dengan lingkungan barunya di Bandung.

## Spesifikasi
Buatlah dalam bahasa pemrograman Python, program penerjemah sederhana yang memanfaatkan algoritma String Matching (Knuth-Morris-Pratt(KMP), Boyer-Moore(BM), dan Regex), dengan spesifikasi sebagai berikut.
1. Program mampu membaca kata atau kalimat yang akan diterjemahkan.
2. Program akan membaca file eksternal yang berisi vocabulary Bahasa Sunda - Bahasa Indonesia (file sudah disiapkan dalam repository).
3. Program akan melakukan penerjemahan secara perkata (untuk contoh akan ditampilkan di bawah).
4. Program dapat memilih mau "Bahasa Sunda ke Bahasa Indonesia" atau "Bahasa Indonesia ke Bahasa Sunda".
5. Pada saat penerjemahan "Bahasa Sunda ke Bahasa Indonesia", program mampu mengenali kata yang tidak memiliki arti (stopwords), seperti "teh" sehingga dapat diabaikan saat penerjemahan.
6. Pada saat penerjemahan "Bahasa Indonesia ke Bahasa Sunda", program mampu menambahkan kata untuk penekanan kalimat, seperti "teh".
7. Program dapat menampilkan hasil terjemahan.

## Contoh Kasus Uji
```
Sunda - Indonesia
Sunda : nami abdi Riyugan
Indonesia : nama saya Riyugan
```

```
Sunda - Indonesia
Sunda : abdi teh sanes jalma Bandung
Indonesia : saya bukan orang Bandung
```

```
Sunda - Indonesia
Sunda : anjeun sumping ti mana?
Indonesia : kamu tiba dari mana?
```

```
Indonesia - Sunda
Indonesia : nama saya Riyugan
Sunda : nami abdi Riyugan
```

```
Indonesia - Sunda
Indonesia : nama adik kamu siapa?
Sunda : nami rai anjeun teh saha?
```

```
Indonesia - Sunda
Indonesia : saya tidak bisa bahasa Sunda
Sunda : abdi henteu tiasa bahasa Sunda
```

### Prerequisites

Sebelum menjalankan Program, anda harus memiliki beberapa program berikut:
1. Phyton 3.5/ 3.6 /3.7
    Download : https://www.python.org/downloads/

2. Xampp 
    Download : https://www.apachefriends.org/download.html

3. nltk module
    how to install : https://www.nltk.org/install.html
    data install : http://www.nltk.org/data.html

4. Web browser
    Saya sangat menyarankan untuk menggunakan Peramban Bawaan (Microsoft Edge, Firefox, Safari) untuk menjalankan aplikasi ini.

### How to use

Untuk dapat menjalankan aplikasi, anda perlu mengikuti langkah-langkah berikut:
1. Ekstrak isi file (.zip) ini ke folder xampp/htdocs
2. Buka Xampp lalu jalankan Apache
3. Buka browser, lalu kunjungi laman localhost/path/main.php
4. Ikuti petunjuk yang tersedia pada laman

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - The IDE used
* [Google Chrome](https://www.google.com/chrome/?brand=CHBD&gclid=Cj0KCQjws_r0BRCwARIsAMxfDRjP5lga30im11-ODArhKSfgI7lrAffLHFLVjksk5bJpscnCwxcf2qEaAoJnEALw_wcB&gclsrc=aw.ds) - The IDE used

## Authors

* **Muhammad Ayyub Abdurrahman** - *Initial work* - [PurpleBooth](https://github.com/Ayyub29)

## License

This project is licensed under the STEI ITB

## Demo Penggunaan
https://youtu.be/UZmpbc69Z6c

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
