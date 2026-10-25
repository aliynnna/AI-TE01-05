import heapq

# Peta rute (semua kunci dan nama dibuat standar huruf kecil di dalam program)
peta_asli = {
    'Rumah': [('Halte', 2), ('Pasar', 5)],
    'Halte': [('Stasiun', 4)],
    'Pasar': [('Kampus', 6)],
    'Stasiun': [('Kampus', 1)],
    'Kampus': []
}

def cari_rute_termurah(peta, awal, tujuan):
    # Buat peta versi huruf kecil agar pencarian fleksibel
    graph = {k.lower(): [(t[0].lower(), t[1]) for t in v] for k, v in peta.items()}
    
    start = awal.lower().strip()
    goal = tujuan.lower().strip()

    # Validasi apakah nama lokasi ada di peta
    if start not in graph or goal not in graph:
        return None, float('inf')

    # Antrean: (total_ongkos, tempat_sekarang, [jalur])
    antrean = [(0, start, [start.capitalize()])]
    sudah_dikunjungi = set()

    while antrean:
        ongkos, tempat, jalur = heapq.heappop(antrean)

        if tempat == goal:
            return jalur, ongkos

        if tempat not in sudah_dikunjungi:
            sudah_dikunjungi.add(tempat)

            for tetangga, tarif in graph.get(tempat, []):
                if tetangga not in sudah_dikunjungi:
                    jalur_baru = list(jalur)
                    jalur_baru.append(tetangga.capitalize())
                    heapq.heappush(antrean, (ongkos + tarif, tetangga, jalur_baru))

    return None, float('inf')


if __name__ == "__main__":
    print("Pilihan lokasi: Rumah, Halte, Pasar, Stasiun, Kampus\n")
    
    awal = input("Masukkan lokasi awal: ")
    tujuan = input("Masukkan lokasi tujuan: ")

    jalur, total_ongkos = cari_rute_termurah(peta_asli, awal, tujuan)

    if jalur:
        print("\n=== HASIL PENCARIAN UCS ===")
        print("Rute Paling Hemat :", " -> ".join(jalur))
        print(f"Total Ongkos      : Rp{total_ongkos}.000")
    else:
        print("\nRute tidak ditemukan atau nama lokasi salah.")
