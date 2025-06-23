## 🌦️ Django Weather API using OpenWeatherMap

### 🔧 Project Summary

This project is a simple but effective **Django-based REST API** that allows users to fetch **real-time weather data** for any city using the **OpenWeatherMap API**.

It is designed to be easily integrated with mobile apps, frontend frameworks (React, Angular, etc.), or other systems that consume weather data.

---

## 🚀 Features

* ✅ Built with **Django 4.2** and **Django REST Framework**
* ✅ Fetches weather data using **OpenWeatherMap API**
* ✅ City name passed as a **query parameter**
* ✅ Returns JSON response with:

  * 🌡️ Temperature (°C)
  * 💧 Humidity (%)
  * 🌥️ Weather description
* ✅ Modular, scalable, and production-ready backend

---

## 📁 Folder Structure

```
weather-api-project/
├── weatherapi/             # Django project
├── weather/                # Django app with API logic
│   └── views.py            # API endpoint
├── manage.py               # Django CLI
└── db.sqlite3              # Default SQLite database
```

---

## ⚙️ Setup Instructions

### 1. 📦 Clone or Create Project Folder

If cloning:

```bash
git clone <repo-url>
cd weather-api-project
```

Or create a fresh Django project manually.

---

### 2. 🐍 Create Virtual Environment

```bash
python -m venv env
env\Scripts\activate   # Windows
```

---

### 3. 🔧 Install Dependencies

```bash
pip install django==4.2 djangorestframework requests django-cors-headers
```

Add installed apps in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'weather',
]
```

Also add middleware:

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
```

---

### 4. 🔑 Configure Your API Key

Sign up at 👉 [https://openweathermap.org/api](https://openweathermap.org/api)

Copy your API key and update this line in `weather/views.py`:

```python
api_key = 'your_openweathermap_api_key'
```

---

### 5. 🔧 Create and Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. ▶️ Run Server

```bash
python manage.py runserver
```

---

## 📡 How to Use the API

### Endpoint

```
GET /api/weather/?city=CityName
```

### Example:

```
http://127.0.0.1:8000/api/weather/?city=Delhi
```

### Sample Output:

```json
{
  "city": "Delhi",
  "temperature": 34.2,
  "humidity": 48,
  "description": "clear sky"
}
```

If an invalid city is passed:

```json
{
  "error": "City not found"
}
```

---

## 🔧 Sample `views.py` Snippet

```python
@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city', 'Kanpur')
    api_key = 'your_api_key_here'
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
```

---

## 🔐 Optional: Redis + Channels Support

If you're planning to expand to real-time functionality:

* Install Redis
* Set up Django Channels + `channels-redis`

*Not required for basic weather API functionality.*

---

## 🧠 Future Scope

* Add database logging for query history
* Enable user-based API usage and limits
* Add unit tests & API documentation (Swagger/Postman)
* Enable Geo-location & language support

---

## 👨‍💻 Author

**Khushi Jalan**

> Django Developer | API Integrator | Cybersecurity & AI Enthusiast
