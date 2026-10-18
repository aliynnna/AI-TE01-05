from expert_system_core import MedicalExpertSystem

def main():
    system = MedicalExpertSystem()
    print("=" * 45)
    print("  SISTEM PAKAR DIAGNOSIS PENYAKIT UMUM  ")
    print("=" * 45)
    print("Contoh input: demam, batuk, pilek, sakit kepala\n")

    user_input = input("Masukkan gejala yang dialami (pisahkan dengan koma): ")
    if not user_input.strip():
        print("Gejala tidak boleh kosong!")
        return

    symptoms = [s.strip() for s in user_input.split(",")]
    diagnoses = system.diagnose(symptoms)

    print("\n--- HASIL DIAGNOSIS ---")
    if not diagnoses:
        print("Tidak ditemukan diagnosis yang cocok dengan gejala tersebut.")
    else:
        for i, res in enumerate(diagnoses, 1):
            print(f"\n{i}. Kemungkinan: {res['disease']} ({res['confidence']}%)")
            print(f"   Gejala cocok   : {', '.join(res['matched_symptoms'])}")
            print(f"   Saran tindakan : {res['recommendation']}")

if __name__ == "__main__":
    main()