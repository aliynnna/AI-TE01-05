class Agent:
    def __init__(self, nama):
        self.nama = nama

    def kerja(self, input_data):
        raise NotImplementedError

    def __call__(self, input_data):
        return self.kerja(input_data)


class Peneliti(Agent):
    def kerja(self, topik):
        print(f"[{self.nama}] mencari info tentang: {topik}")
        return f"Fakta: {topik} adalah sistem di mana beberapa agent bekerja sama."


class Penulis(Agent):
    def kerja(self, fakta):
        print(f"[{self.nama}] menulis draft...")
        return f"Ringkasan -> {fakta}"


class Reviewer(Agent):
    def kerja(self, draft):
        print(f"[{self.nama}] memeriksa draft...")
        if "Ringkasan" in draft:
            return draft + " (DISETUJUI)"
        return draft + " (DITOLAK)"


peneliti = Peneliti("Peneliti")
penulis = Penulis("Penulis")
reviewer = Reviewer("Reviewer")

# --- Jalankan ---
topik = input("Masukkan topik: ")   # kamu ketik: multi agent system
hasil = reviewer(penulis(peneliti(topik)))
print("\nHasil akhir:", hasil)
