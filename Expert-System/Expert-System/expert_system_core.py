def diagnosa(daftar_gejala):
    if "demam" in daftar_gejala and "batuk" in daftar_gejala:
        return ["Indikasi Flu / Infeksi Saluran Pernapasan"]
    return ["Gejala umum, periksakan ke dokter jika berlanjut"]
