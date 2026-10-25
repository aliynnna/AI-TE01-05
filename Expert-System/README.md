# 🩺 Rule-Based Expert System (Sistem Pakar)

Repositori/folder ini berisi implementasi **Sistem Pakar (Expert System)** sederhana berbasis aturan (*rule-based*) menggunakan bahasa pemrograman **Python** untuk simulasi diagnosa awal kondisi kesehatan.

---

## 📌 Apa itu Expert System?

Expert System adalah cabang dari Kecerdasan Buatan (AI) yang dirancang untuk **meniru kemampuan pengambilan keputusan seorang pakar manusia** (dalam kasus ini: dokter umum).

Sistem ini bekerja menggunakan metode **Forward Chaining**:
1. **Pengumpulan Fakta:** Menanyakan gejala yang dialami pengguna secara interaktif.
2. **Pencocokan Aturan (*Rule Matching*):** Mencocokkan fakta-fakta tersebut dengan basis pengetahuan (*knowledge base*) menggunakan logika **JIKA ... MAKA ...** (*IF-THEN*).
3. **Penarikan Kesimpulan:** Menghasilkan kemungkinan diagnosa penyakit beserta saran penanganan awal.

---

## 🩺 Alur Gejala dan Diagnosa

Sistem mengevaluasi beberapa gejala berikut:
* Demam tinggi
* Batuk kering
* Hidung tersumbat / pilek
* Sakit tenggorokan
* Sesak napas

Berdasarkan kombinasi jawaban `y` (ya) atau `n` (tidak), sistem dapat mengidentifikasi:
* **Faringitis (Radang Tenggorokan)**
* **Infeksi Saluran Pernapasan Akut (ISPA)**
* **Flu Ringan (Common Cold)**
* **Influenza**
* Kondisi belum terdefinisi jika tidak ada aturan yang cocok

---

## 🚀 Cara Menjalankan

Pastikan **Python 3** sudah terpasang di komputer Anda. Buka terminal di folder ini, lalu jalankan:

```bash
python expert_system.py
