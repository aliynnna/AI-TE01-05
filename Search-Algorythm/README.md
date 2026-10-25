# 🔍 Graph Search Algorithms (BFS, DFS, & UCS)

Repositori ini berisi implementasi algoritma penelusuran graf (*Graph Search Algorithms*) dasar menggunakan bahasa pemrograman **Python**:
* **Breadth-First Search (BFS)**
* **Depth-First Search (DFS)**
* **Uniform Cost Search (UCS)**

---

## 📌 Rangkuman Konsep Tiga Algoritma

| Algoritma | File | Prinsip Utama | Struktur Data | Hasil Akhir |
|---|---|---|---|---|
| **BFS** | `bfs.py` | Melebar per lapis dari simpul terdekat | *Queue* (FIFO) via `deque` | Menjamin **langkah/belokan paling sedikit** |
| **DFS** | `dfs.py` | Menyelam sedalam mungkin sampai mentok | *Stack* (LIFO) via list `.pop()` | Jalur pertama yang ketemu (bisa lebih panjang) |
| **UCS** | `ucs.py` | Memilih rute dengan akumulasi biaya terkecil | *Priority Queue* via `heapq` | Menjamin **total ongkos/jarak termurah** |

---

## 💡 Penjelasan Masing-Masing File

### 1. Breadth-First Search (`bfs.py`)
* Menggunakan antrean barisan biasa: siapa yang masuk duluan akan diperiksa lebih awal.
* Cocok untuk graf tanpa bobot jalan (*unweighted graph*) saat mencari rute terdekat.

### 2. Depth-First Search (`dfs.py`)
* Menggunakan sistem tumpukan: data yang terakhir masuk akan diproses lebih dulu.
* Menuntaskan satu lorong cabang sampai ke ujung buntu (*backtracking*) sebelum melirik cabang lainnya.

### 3. Uniform Cost Search (`ucs.py`)
* Memperhitungkan bobot atau tarif di setiap ruas jalan.
* Menggunakan `heapq` (Priority Queue) untuk selalu mengevaluasi rute dengan total ongkos termurah terlebih dahulu, bukan sekadar jumlah belokan.

---

## 🚀 Cara Menjalankan

Pastikan **Python 3** sudah terpasang di komputer Anda. Buka terminal pada folder ini dan jalankan perintah berikut:

1. **Menjalankan BFS:**
   ```bash
   python bfs.py
2. **Menjalankan DFS:**
   python dfs.py
4. **Menjalankan UCF:**
   python ucs.py
