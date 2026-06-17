# 🌦️ Weather App using Python (Tkinter GUI)

## 📌 Description

This project is a Weather Application built using Python.
It uses **Tkinter for the graphical user interface (GUI)** and the **OpenWeatherMap API** to fetch real-time weather data.

The application allows users to enter a city name and view weather details in a clean and interactive window.

---

## 🚀 Features

* 🌍 Search weather by city name
* 🌡️ Displays temperature in Celsius
* 💧 Shows humidity
* 🌥️ Displays weather condition
* 🖥️ User-friendly GUI using Tkinter
* ❌ Handles invalid city names

---

## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI)
* requests library
* OpenWeatherMap API
* JSON parsing

---

## 📦 Installation

1. Install Python

2. Install required library:

   ```bash
   pip install requests
   ```

---

## 🔑 API Setup

1. Create an account on OpenWeatherMap
2. Generate your API key
3. Replace in code:

   ```python
   API_KEY = "your_api_key_here"
   ```

---

## ▶️ How to Run

1. Save the file as `weather_app.py`

2. Run the program:

   ```bash
   python weather_app.py
   ```

3. Enter city name in the GUI window and click **Search**

---

## 🧠 How It Works

1. User enters a city name in the GUI
2. Clicks the search button
3. Program sends a request to the API
4. API returns data in JSON format
5. Data is parsed and displayed in the GUI

---

## 📸 Sample Output

```
City: Chennai
Temperature: 30°C
Condition: Clear Sky
Humidity: 70%
```

---

## ⚠️ Notes

* Internet connection is required
* API key may take a few minutes to activate
* Enter valid city name
* Tkinter comes pre-installed with Python

---

## 🔮 Future Improvements

* 🌤️ Add weather icons
* 📅 5-day forecast
* 📍 Auto location detection
* 🎨 Advanced UI design

---

