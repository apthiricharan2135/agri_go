import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agri_go.settings')
django.setup()
from recommendation.models import Crop
def insert_data():
    crop_list = [
        {
            "name": "Paddy (Rice)",
            "soil_type": "clay",
            "water_requirement": "high",
            "season": "monsoon",
            "budget_range": 20000,
            "advantages": "High market demand; grows well in water-logged areas.",
            "cultivation_process": "1. Nursery raising. 2. Transplanting. 3. Weeding. 4. Harvesting.",
            "yield_tips": "Maintain water level consistently during the first 2 months."
        },
        {
            "name": "Wheat",
            "soil_type": "loamy",
            "water_requirement": "medium",
            "season": "winter",
            "budget_range": 12000,
            "advantages": "Stable price; lower pest risk in winter.",
            "cultivation_process": "1. Field preparation. 2. Sowing in rows. 3. 4-6 irrigations.",
            "yield_tips": "Ensure the first irrigation happens at the 'Crown Root' stage."
        },
        {
            "name": "Bajra (Millet)",
            "soil_type": "sandy",
            "water_requirement": "low",
            "season": "summer",
            "budget_range": 7000,
            "advantages": "Extremely drought-resistant; low input cost.",
            "cultivation_process": "1. Direct sowing. 2. Minimal fertilization. 3. Harvest in 90 days.",
            "yield_tips": "Do not overwater; it prefers dry conditions."
        },
        {
            "name": "Groundnut",
            "soil_type": "sandy",
            "water_requirement": "medium",
            "season": "monsoon",
            "budget_range": 15000,
            "advantages": "Good for soil health (Nitrogen fixation); high oil value.",
            "cultivation_process": "1. Seed treatment. 2. Sowing. 3. Gypsum application. 4. Harvesting.",
            "yield_tips": "Ensure the soil is loose for easy 'pegging' of the nuts."
        },
        {
            "name": "Cotton",
            "soil_type": "black",
            "water_requirement": "medium",
            "season": "monsoon",
            "budget_range": 25000,
            "advantages": "Very high commercial value (Cash crop).",
            "cultivation_process": "1. Sowing after first rain. 2. Pest management. 3. Picking cotton bolls.",
            "yield_tips": "Watch out for Pink Bollworm pests during flowering."
        }
    ]

    for crop_data in crop_list:
        Crop.objects.get_or_create(**crop_data)
        print(f"Successfully added: {crop_data['name']}")

if __name__ == "__main__":
    insert_data()