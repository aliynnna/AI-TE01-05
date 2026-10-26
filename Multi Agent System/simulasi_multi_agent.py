class Agent:
    def __init__(self, nama):
        self.nama = nama

    def kerja(self, data):
        raise NotImplementedError

    def __call__(self, data):
        return self.kerja(data)


class Peneliti(Agent):
    BASIS_DATA = {
        "ayam": "ayam adalah unggas yang dipelihara untuk diambil daging dan telurnya.",
        "multi agent system": "multi agent system adalah sistem di mana beberapa agent bekerja sama.",
        "python": "python adalah bahasa pemrograman yang mudah dibaca dan serbaguna.",
    }

    def kerja(self, data):
        topik = data["topik"]
        print(f"[{self.nama}] mencari info tentang: {topik}")
        data["fakta"] = self.BASIS_DATA.get(topik.lower())  # None kalau tidak ada
        return data


class Penulis(Agent):
    def kerja(self, data):
        print(f"[{self.nama}] menulis draft...")
        if data["fakta"] is None:
            data["draft"] = f"Ringkasan -> tidak ada data tentang {data['topik']}"
        else:
            data["draft"] = f"Ringkasan -> {data['fakta']}"
        return data


class Reviewer(Agent):
    def kerja(self, data):
        print(f"[{self.nama}] memeriksa draft...")
        topik = data["topik"].lower()
        draft = data["draft"].lower()

        if data["fakta"] is None:
            data["status"] = "DITOLAK (fakta tidak ditemukan)"
        elif topik not in draft:
            data["status"] = "DITOLAK (draft tidak sesuai topik)"
        else:
            data["status"] = "DISETUJUI"
        return data


peneliti = Peneliti("Peneliti")
penulis = Penulis("Penulis")
reviewer = Reviewer("Reviewer")

while True:
    topik = input("\nMasukkan topik (ketik 'keluar' untuk berhenti): ")
    if topik.lower() == "keluar":
        break

    data = {"topik": topik}
    data = reviewer(penulis(peneliti(data)))
    print("\nHasil akhir:", data["draft"], "|", data["status"])
