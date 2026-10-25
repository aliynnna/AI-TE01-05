def tanya_gejala(pertanyaan):
    while True:
        jawaban = input(f"Apakah Anda mengalami {pertanyaan}? (y/n): ").strip().lower()
        if jawaban in ['y', 'n']:
            return jawaban == 'y'
        print("Input salah! Harap ketik 'y' untuk ya atau 'n' untuk tidak.\n")

def diagnosa():
    print("=" * 50)
    print("   SISTEM PAKAR DIAGNOSA AWAL KESEHATAN (AI)   ")
    print("=" * 50)
    print("Silakan jawab pertanyaan di bawah ini dengan jujur.\n")

    # 1. Mengumpulkan fakta gejala melalui input pengguna
    demam = tanya_gejala("demam tinggi")
    batuk = tanya_gejala("batuk kering")
    pilek = tanya_gejala("hidung tersumbat / pilek")
    sakit_tenggorokan = tanya_gejala("sakit tenggorokan saat menelan")
    sesak_napas = tanya_gejala("sesak napas / dada terasa berat")

    print("\n" + "=" * 50)
    print("                  HASIL DIAGNOSA                  ")
    print("=" * 50)

    # 2. Basis Aturan (Knowledge Base) & Penarikan Kesimpulan (Inference Engine)
    if demam and batuk and sesak_napas:
        hasil = "Infeksi Saluran Pernapasan Akut (ISPA)"
        saran = "Gejala tergolong serius karena ada sesak napas. Segera periksakan diri ke dokter/IGD."
    
    elif demam and sakit_tenggorokan and not sesak_napas:
        hasil = "Faringitis (Radang Tenggorokan)"
        saran = "Istirahat cukup, hindari gorengan atau minuman dingin, dan minum air hangat."

    elif demam and pilek and batuk:
        hasil = "Influenza"
        saran = "Konsumsi obat pereda flu/demam, perbanyak istirahat total, dan minum air putih."

    elif pilek and batuk and not demam:
        hasil = "Flu Ringan / Common Cold"
        saran = "Jaga tubuh tetap hangat, konsumsi vitamin C, dan istirahat yang cukup."

    elif not (demam or batuk or pilek or sakit_tenggorokan or sesak_napas):
        hasil = "Kondisi Sehat"
        saran = "Tidak ada gejala penyakit yang terdeteksi. Pertahankan pola hidup sehat!"

    else:
        hasil = "Gejala Tidak Cocok dengan Basis Aturan Kami"
        saran = "Kombinasi gejala Anda membutuhkan evaluasi medis lebih mendalam oleh dokter."

    print(f"Hasil Analisis : {hasil}")
    print(f"Saran Medis    : {saran}")
    print("=" * 50)

if __name__ == "__main__":
    diagnosa()
