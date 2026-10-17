from expert_system_core import diagnosa

if __name__ == "__main__":
    print("=== SISTEM PAKAR DIAGNOSIS PENYAKIT (CLI) ===")
    gejala_input = []
    daftar = [("demam", "Demam tinggi?"), ("batuk", "Batuk?"), ("sesak", "Sesak napas?")]
    for k, t in daftar:
        if input(f"{t} (y/n): ").strip().lower() == 'y':
            gejala_input.append(k)
    print("\nHasil:", diagnosa(gejala_input))
