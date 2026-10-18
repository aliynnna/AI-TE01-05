from medical_knowledge_base import DISEASE_RULES

class MedicalExpertSystem:
    def __init__(self):
        self.rules = DISEASE_RULES

    def diagnose(self, user_symptoms):
        normalized_symptoms = [s.strip().lower() for s in user_symptoms]
        results = []

        for disease, data in self.rules.items():
            rule_symptoms = set(data["symptoms"])
            matched = rule_symptoms.intersection(normalized_symptoms)
            confidence = (len(matched) / len(rule_symptoms)) * 100

            if confidence > 0:
                results.append({
                    "disease": disease,
                    "confidence": round(confidence, 2),
                    "matched_symptoms": list(matched),
                    "recommendation": data["recommendation"]
                })

        # Urutkan berdasarkan tingkat kecocokan tertinggi
        results.sort(key=lambda x: x["confidence"], reverse=True)
        return results