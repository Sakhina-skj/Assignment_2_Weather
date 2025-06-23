## 🌦️ Weather API with Django + OpenWeatherMap + HTML/CSS

### 🔧 Project Summary

This project is a **simple and powerful Weather App** built using:

* **Django 4.2**
* **Django REST Framework**
* **OpenWeatherMap API**
* **HTML + CSS + JavaScript frontend**
* Optional: **Redis + Channels** (for WebSocket real-time use cases)

Users can enter any city name and instantly get real-time weather data like:

* 🌡️ Temperature (in °C)
* 💧 Humidity (in %)
* 🌤️ Weather Description (e.g., "clear sky")

---

## 🚀 Features

* ✅ Simple, mobile-friendly weather form
* ✅ Fetches data from OpenWeatherMap using API
* ✅ Shows data dynamically with JavaScript
* ✅ Django REST Framework backend
* ✅ Can be extended with WebSockets using Redis & Channels
* ✅ Clean code and folder structure for full-stack developers

---

## 📁 Folder Structure

```
weather-api-project/
├── weatherapi/             # Django project
├── weather/                # Django app
│   └── views.py            # Contains API + frontend views
├── templates/
│   └── index.html          # HTML frontend
├── static/
│   └── style.css           # CSS styles
├── db.sqlite3              # Default database
└── manage.py
```

---

## ⚙️ Setup Instructions

### 1. 📦 Clone the repository / Create project folder

```bash
git clone <repo-url>
cd weather-api-project
```

Or manually create folders if starting fresh.

---

### 2. 🐍 Create a Virtual Environment

```bash
python -m venv env
env\Scripts\activate   # For Windows
```

---

### 3. 🔧 Install Required Packages

```bash
pip install django==4.2 djangorestframework requests django-cors-headers channels channels-redis psycopg2-binary
```

---

### 4. 🔑 Get OpenWeatherMap API Key

* Sign up at 👉 [https://openweathermap.org/api](https://openweathermap.org/api)
* Copy your free API key
* Replace the line in `weather/views.py`:

```python
api_key = 'your_api_key_here'
```

---

### 5. 🔌 Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. 🖥️ Run the Development Server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 🌐 How It Works

* User enters a city name in the input field
* JavaScript makes a GET request to `/api/weather/?city=CityName`
* Django fetches weather data from OpenWeatherMap API
* Response is shown as formatted weather details on screen

---

## 🧪 Sample API Test

```
GET http://127.0.0.1:8000/api/weather/?city=Kanpur
```

Sample Output:

```json
{
  "city": "Kanpur",
  "temperature": 33.7,
  "humidity": 42,
  "description": "clear sky"
}
```

---

## 📦 Optional: Use Redis for Real-Time (Channels)

To enable real-time updates via WebSocket:

* Install Redis via Memurai / WSL / Docker
* Configure `ASGI`, `CHANNEL_LAYERS`, etc.

*(Skip this step if you just want basic HTTP weather API.)*

---

## ✨ Future Improvements

* Save weather search history in DB
* Add dark mode UI
* Graphical weather icons
* Geo-location based search
* Deploy on Render / Railway

---

## 👨‍💻 Author

**Khushi Jalan**

* Web Developer


