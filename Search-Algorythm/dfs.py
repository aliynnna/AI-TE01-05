# Denah tempat dan isinya
tempat = {
    'Ruang Tamu': ['Kamar Tidur', 'Dapur'],
    'Kamar Tidur': ['Lemari Baju'],
    'Lemari Baju': ['Baju'],
    'Dapur': ['Kulkas'],
    'Kulkas': ['Kue']
}

# Ketik barang yang dicari (misal ketik: Kue atau Baju)
yang_dicari = input("Mau cari apa? ")

# Tumpukan DFS (dimulai dari pintu masuk)
tumpukan = ['Ruang Tamu']
ketemu = False

while tumpukan:
    # Ciri khas DFS: ambil yang paling atas / terakhir masuk (.pop())
    lokasi = tumpukan.pop()
    print("Membuka:", lokasi)

    # Cek apakah lokasinya pas dengan barang yang dicari
    if lokasi.lower() == yang_dicari.lower():
        print(f"Hore! '{lokasi}' berhasil ditemukan!")
        ketemu = True
        break

    # Masukkan isi ruangan ke tumpukan untuk ditelusuri sampai mentok
    for isi in tempat.get(lokasi, []):
        tumpukan.append(isi)

if not ketemu:
    print(f"Barang '{yang_dicari}' tidak ada di mana pun.")
