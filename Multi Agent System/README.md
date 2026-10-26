# Contoh Sederhana Multi-Agent System

Proyek ini adalah contoh sederhana **multi-agent system** dengan Python. Beberapa agent bekerja secara berurutan (pipeline), dan keluaran dari satu agent menjadi masukan bagi agent berikutnya.

## Deskripsi

Ada tiga agent dengan peran berbeda:

| Agent | Peran | Masukan | Keluaran |
|-------|-------|---------|----------|
| `Peneliti` | Mencari informasi tentang suatu topik | Topik (string) | Teks fakta |
| `Penulis` | Menyusun draft ringkasan dari fakta | Fakta | Teks ringkasan |
| `Reviewer` | Memeriksa draft dan memberi keputusan | Draft | Draft + status `(DISETUJUI)` atau `(DITOLAK)` |

Semua agent mewarisi kelas dasar `Agent` yang memiliki atribut `nama` dan method `kerja()`. Method `kerja()` di kelas dasar sengaja dibiarkan kosong (`NotImplementedError`) sehingga wajib diimplementasikan oleh setiap subkelas.

## Alur Kerja

```
Topik --> [Peneliti] --> Fakta --> [Penulis] --> Draft --> [Reviewer] --> Hasil Akhir
```

1. `Peneliti` menerima topik dan menghasilkan fakta.
2. `Penulis` mengubah fakta menjadi ringkasan.
3. `Reviewer` memeriksa apakah draft mengandung kata `Ringkasan`. Jika ya, draft disetujui; jika tidak, ditolak.

## Struktur Kode

```python
class Agent:            # Kelas dasar (abstrak)
class Peneliti(Agent):  # Mencari fakta
class Penulis(Agent):   # Menulis draft
class Reviewer(Agent):  # Memeriksa draft
```

Bagian eksekusi membuat instance setiap agent lalu menjalankannya secara berurutan dalam sebuah loop:

```python
hasil = "multi agent system"
for agent in [peneliti, penulis, reviewer]:
    hasil = agent.kerja(hasil)
```

## Prasyarat

- Python 3.6 atau lebih baru (menggunakan f-string)
- Tidak membutuhkan library tambahan

## Cara Menjalankan

```bash
python main.py
```

> Ganti `main.py` dengan nama file skrip Anda.

## Contoh Keluaran

```
[Peneliti] mencari info tentang: multi agent system
[Penulis] menulis draft...
[Reviewer] memeriksa draft...

Hasil akhir: Ringkasan -> Fakta: multi agent system adalah sistem di mana beberapa agent bekerja sama. (DISETUJUI)
```

## Cara Menambah Agent Baru

1. Buat kelas baru yang mewarisi `Agent`.
2. Implementasikan method `kerja()`.
3. Tambahkan instance-nya ke dalam daftar pada loop eksekusi.

Contoh:

```python
class Penerjemah(Agent):
    def kerja(self, teks):
        print(f"[{self.nama}] menerjemahkan teks...")
        return f"{teks} (diterjemahkan)"

penerjemah = Penerjemah("Penerjemah")

for agent in [peneliti, penulis, reviewer, penerjemah]:
    hasil = agent.kerja(hasil)
```

## Catatan

Kode ini hanya simulasi untuk pembelajaran. Agent tidak benar-benar mencari informasi di internet atau menggunakan model AI. Untuk sistem nyata, isi method `kerja()` dapat diganti dengan pemanggilan API LLM, pencarian web, atau logika lain.

## Pengembangan Lanjutan

- Menghubungkan agent dengan LLM (misalnya melalui API)
- Menambahkan alur revisi: jika `Reviewer` menolak, draft dikembalikan ke `Penulis`
- Menjalankan agent secara paralel atau asinkron
- Menambahkan memori bersama antar agent

## Lisensi

Bebas digunakan untuk keperluan belajar.
