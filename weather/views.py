# weather/views.py

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city', 'Kanpur')
    api_key = 'ed19ff5afd5f35a93484ee2047a5feff'  # Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        result = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return Response(result)
    else:
        return Response({"error": "City not found"}, status=404)
