# 🍚 Mbak Kos AI
## Smart Meal Planner Berbasis Large Language Model untuk Mahasiswa dan Anak Kos


## 1. Deskripsi Project

Mbak Kos AI merupakan chatbot berbasis Large Language Model (LLM) yang dibuat untuk membantu mahasiswa dan anak kos dalam menentukan pilihan makanan sehari-hari berdasarkan kondisi keuangan dan bahan makanan yang tersedia.

Ide project ini berangkat dari permasalahan sederhana yang sering dialami mahasiswa yang tinggal sendiri, yaitu sulit menentukan menu makanan yang murah, mudah dibuat, tetapi tetap sesuai dengan kondisi yang ada. Banyak mahasiswa memiliki keterbatasan seperti budget makan yang terbatas, bahan makanan seadanya, serta alat masak yang sederhana.

Melalui chatbot ini, pengguna dapat memberikan informasi seperti budget makan, bahan yang tersedia, atau kondisi tertentu seperti sedang akhir bulan. Sistem kemudian akan memberikan rekomendasi menu yang sesuai dengan kebutuhan pengguna.

Mbak Kos AI tidak hanya berfungsi sebagai chatbot resep makanan, tetapi juga sebagai asisten pengatur pola makan sederhana untuk anak kos. Sistem memiliki beberapa mode rekomendasi agar hasil yang diberikan lebih sesuai dengan kondisi pengguna.

Mode yang tersedia:

### Normal Mode
Mode standar untuk memberikan rekomendasi menu berdasarkan bahan yang tersedia dan budget pengguna.

### Quick Cooking Mode
Mode untuk pengguna yang membutuhkan makanan dengan proses memasak cepat dan langkah sederhana.

### Akhir Bulan Survival Mode
Mode yang membantu pengguna ketika memiliki budget terbatas dengan memprioritaskan penggunaan bahan yang sudah tersedia.

### Anti Mubazir Mode
Mode yang membantu pengguna mengolah bahan makanan tersisa agar dapat digunakan kembali dan mengurangi makanan yang terbuang.


Project ini menggunakan API Large Language Model dari Groq dengan model:

```
openai/gpt-oss-120b
```

Aplikasi dibangun menggunakan Python dan Streamlit sehingga chatbot dapat digunakan melalui tampilan web sederhana.


---

# 2. Fitur Aplikasi

## 2.1 Chatbot Berbasis LLM

Pengguna dapat berinteraksi dengan chatbot menggunakan bahasa sehari-hari tanpa harus menggunakan format input tertentu.

Contoh:

```
Saya punya telur, kentang, dan wortel
```

Chatbot akan memahami bahan yang diberikan kemudian memberikan rekomendasi menu yang sesuai.


---

## 2.2 Deteksi Bahan Makanan

Sistem memiliki database bahan makanan yang digunakan untuk mengenali berbagai variasi penyebutan bahan.

Contoh:

Input pengguna:

```
Saya punya indomie dan telor
```

Sistem akan mengenali:

```
mie instan
telur
```

Fitur ini dibuat agar pengguna dapat memasukkan bahan menggunakan bahasa yang biasa digunakan sehari-hari.


---

## 2.3 Rekomendasi Berdasarkan Budget

Pengguna dapat memasukkan batas pengeluaran makanan.

Contoh:

```
Budget saya 10000
```

Kemudian chatbot akan menyesuaikan rekomendasi makanan agar tetap berada dalam batas budget yang diberikan.


---

## 2.4 Mode Rekomendasi Menu

Chatbot memiliki beberapa mode yang dapat dipilih pengguna sesuai kebutuhan.

| Mode | Fungsi |
|---|---|
| Normal Mode | Memberikan rekomendasi menu sehari-hari |
| Quick Cooking Mode | Memberikan menu dengan waktu memasak lebih singkat |
| Akhir Bulan Survival Mode | Fokus pada menu hemat dengan budget terbatas |
| Anti Mubazir Mode | Membantu memanfaatkan bahan makanan sisa |


---

## 2.5 Streaming Response

Jawaban chatbot ditampilkan secara bertahap menggunakan fitur streaming dari Groq API.

Fitur ini membuat proses interaksi terasa lebih natural karena pengguna tidak perlu menunggu seluruh jawaban selesai dibuat.


---

## 2.6 Conversation History

Sistem menyimpan riwayat percakapan selama penggunaan sehingga chatbot dapat mempertahankan konteks pembicaraan sebelumnya.


---

# 3. Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama |
| Streamlit | Membuat tampilan chatbot berbasis web |
| Groq API | Menghubungkan aplikasi dengan Large Language Model |
| GPT OSS 120B | Model AI yang digunakan |
| JSON | Menyimpan database bahan makanan dan history chat |
| python-dotenv | Mengelola API key secara aman |


---

# 4. Struktur Folder Project

```
MbakKos-AI/

│
├── app.py
│   └── Mengatur tampilan aplikasi menggunakan Streamlit,
│       input pengguna, sidebar, dan tampilan chat
│
├── chatbot.py
│   └── Mengatur proses utama chatbot seperti koneksi API,
│       deteksi bahan, history, dan pengiriman prompt
│
├── prompt.py
│   └── Berisi system prompt yang mengatur karakter,
│       aturan, dan batasan chatbot
│
├── food_database.json
│   └── Database bahan makanan, variasi nama bahan,
│       dan harga acuan
│
├── requirements.txt
│   └── Daftar library Python yang diperlukan
│
├── .env
│   └── Menyimpan API key Groq
│
├── .gitignore
│   └── Mengatur file yang tidak ikut di-upload ke GitHub
│
└── README.md
    └── Dokumentasi project
```


---

# 5. Cara Menjalankan Program


## 5.1 Clone Repository

Clone repository melalui terminal:

```bash
git clone https://github.com/username/MbakKos-AI.git
```

Masuk ke folder project:

```bash
cd MbakKos-AI
```


---

## 5.2 Membuat Virtual Environment

Buat virtual environment:

```bash
python -m venv venv
```

Aktifkan virtual environment.


Windows:

```bash
venv\Scripts\activate
```


Git Bash:

```bash
source venv/Scripts/activate
```


---

## 5.3 Install Library

Install seluruh library yang dibutuhkan:

```bash
pip install -r requirements.txt
```


---

## 5.4 Konfigurasi API Key

Buat file:

```
.env
```

Kemudian masukkan API Key Groq:

```
GROQ_API_KEY=API_KEY_ANDA
```

API key tidak ditulis langsung pada kode untuk menjaga keamanan.


---

## 5.5 Menjalankan Aplikasi

Jalankan:

```bash
streamlit run app.py
```

Setelah berhasil dijalankan, aplikasi dapat diakses melalui browser:

```
http://localhost:8501
```


---

# 6. Contoh Tampilan dan Percakapan

## Screenshot Tampilan Aplikasi

Tambahkan screenshot hasil running aplikasi pada bagian ini.

Contoh:

```
assets/screenshot.png
```


![Mbak Kos AI](assets/screenshot.png)


---

## Contoh Percakapan


### Input Pengguna

```
Saya punya telur, kentang, wortel, dan brokoli
```


### Output Mbak Kos AI

```
🍳 Omelet Kentang Sayur Hemat

Bahan:
- telur
- kentang
- wortel
- brokoli


Cara Masak:
1. Potong bahan menjadi ukuran kecil.
2. Campurkan bahan dengan telur.
3. Masak menggunakan wajan.


Estimasi Biaya:
Rp ...
```


---

# 7. Penjelasan Struktur Program


## app.py

File ini bertanggung jawab terhadap bagian tampilan aplikasi.

Pekerjaan yang dilakukan:

- membuat tampilan chatbot menggunakan Streamlit
- membuat sidebar pengaturan
- menyediakan pilihan mode chatbot
- menerima input pengguna
- menampilkan hasil percakapan
- mengatur session state agar percakapan tetap tersimpan selama aplikasi berjalan


---

## chatbot.py

File ini merupakan bagian utama dari sistem chatbot.

Pekerjaan yang dilakukan:

- melakukan koneksi dengan Groq API
- mengirimkan pesan pengguna ke model LLM
- mengatur conversation history
- melakukan deteksi bahan makanan dari input pengguna
- mengambil informasi harga bahan dari database
- mengatur proses streaming response
- menangani error ketika API mengalami gangguan


---

## prompt.py

File ini digunakan untuk menentukan perilaku chatbot.

Pekerjaan yang dilakukan:

- membuat karakter Mbak Kos AI
- menentukan gaya bahasa chatbot
- menentukan format jawaban
- membuat aturan budget makanan
- membuat batasan agar chatbot tetap fokus pada topik makanan


---

## food_database.json

File ini berfungsi sebagai database sederhana bahan makanan.

Data yang disimpan:

- nama bahan makanan
- variasi penyebutan bahan
- harga acuan bahan


Database ini membantu chatbot mengenali input pengguna yang menggunakan bahasa sehari-hari.


---

# 8. Pembagian Jobdesk Pengerjaan


## Pengembangan Konsep dan Perancangan Sistem

Pekerjaan yang dilakukan:

- menentukan ide chatbot dengan tema asisten makanan hemat anak kos
- melakukan identifikasi masalah yang dialami mahasiswa terkait pengaturan makanan
- menentukan fitur utama chatbot
- merancang konsep mode chatbot seperti Normal Mode, Quick Cooking Mode, Survival Mode, dan Anti Mubazir Mode
- menentukan alur interaksi antara pengguna dengan chatbot


---

## Perancangan Prompt dan Perilaku Chatbot

Pekerjaan yang dilakukan:

- menyusun system prompt untuk mengatur karakter chatbot
- menentukan batasan topik yang dapat dijawab chatbot
- mengatur format keluaran rekomendasi menu
- membuat aturan agar chatbot tidak memberikan harga yang tidak tersedia
- mengatur chatbot agar menyesuaikan jawaban berdasarkan budget pengguna


---

## Pengembangan Sistem Backend Chatbot

Pekerjaan yang dilakukan:

- melakukan implementasi koneksi Python dengan Groq API
- mengatur penggunaan model `openai/gpt-oss-120b`
- membuat sistem conversation history
- membuat fungsi deteksi bahan makanan berdasarkan database
- membuat sistem penyimpanan history percakapan
- menambahkan error handling ketika terjadi kegagalan API


---

## Pengembangan Tampilan Aplikasi

Pekerjaan yang dilakukan:

- membuat tampilan chatbot menggunakan Streamlit
- membuat tampilan sidebar untuk pengaturan mode dan informasi pengguna
- menghubungkan tampilan dengan sistem backend chatbot
- membuat tampilan percakapan agar lebih mudah digunakan


---

## Pengujian dan Evaluasi Sistem

Pekerjaan yang dilakukan:

- melakukan pengujian input bahan makanan
- menguji respon chatbot pada berbagai kondisi budget
- menguji setiap mode chatbot
- melakukan pengecekan apakah chatbot memberikan rekomendasi sesuai batasan yang telah dibuat
- melakukan perbaikan ketika ditemukan error


---

# 9. Penggunaan AI Assistant

Dalam proses pembuatan project ini, AI assistant digunakan sebagai alat bantu dalam proses pengembangan.

Bagian yang dibantu oleh AI:

- membantu memberikan referensi struktur project Python
- membantu proses debugging ketika terdapat error pada implementasi API
- membantu menyusun beberapa bagian kode awal
- membantu melakukan evaluasi terhadap desain sistem chatbot


Bagian yang dikerjakan secara mandiri:

- menentukan konsep dan tema chatbot
- menentukan fitur yang ingin dikembangkan
- menentukan kebutuhan pengguna
- merancang alur penggunaan chatbot
- menentukan mode rekomendasi makanan
- melakukan implementasi dan pengujian aplikasi
- melakukan revisi sistem berdasarkan hasil testing


Penggunaan AI assistant dilakukan sebagai pendukung dalam proses pengembangan, sedangkan keputusan desain, pengujian, dan pengembangan fitur dilakukan secara mandiri.


---

# 10. Keamanan API Key

API Key Groq tidak ditulis langsung pada source code.

API Key disimpan menggunakan file:

```
.env
```

File tersebut dimasukkan ke dalam:

```
.gitignore
```

sehingga informasi sensitif tidak ikut masuk ke repository GitHub.


---

# Author

Nama:
Indy Nailuvar - 3324600037


Mata Kuliah:
Large Language Model


Project:
Mbak Kos AI
