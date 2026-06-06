import requests
API_KEY ="your_api_key"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        city_name = data["name"]
        temp = data["main"]["temp"] - 273.15  # Kelvin → Celsius
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        print(f"\nCity: {city_name}")
        print(f"Temperature: {temp:.2f} °C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
    else:
        print("City not found!")
        print(f"Error: {response.status_code}")
        print(f"Error: {response.json()}")
        print(f"URL used: {url}")

city = input("Enter city name: ")
get_weather(city)
