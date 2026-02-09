from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
    return render(request, 'recommendation/home.html')

def recommend(request):
    if request.method == "POST":
        #Capture data from the form
        soil = request.POST.get('soil_type')
        water = request.POST.get('water')
        season = request.POST.get('season')
        budget = request.POST.get('budget')

        #Filter the MySQL database
        matching_crops = Crop.objects.filter(
            soil_type=soil,
            water_requirement=water,
            season=season,
            budget_range__lte=budget
        )

        return render(request, 'recommendation/results.html', {'crops': matching_crops})
    
    return render(request, 'recommendation/home.html')