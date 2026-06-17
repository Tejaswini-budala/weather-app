import requests
import tkinter as tk

API_KEY = "your_api_key"

def get_weather():
    city = city_entry.get()

    if city == "":
        city_label.config(text="Enter a city")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        city_name = data["name"]
        temp = int(data["main"]["temp"] - 273.15)
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        city_label.config(text=city_name)
        temp_label.config(text=f"{temp}°C")
        condition_label.config(text=condition.title())
        extra_label.config(text=f"Humidity: {humidity}%")

    else:
        city_label.config(text="City not found")
        temp_label.config(text="")
        condition_label.config(text="")
        extra_label.config(text="")

# 🎨 Window
root = tk.Tk()
root.title("Weather App")
root.geometry("350x500")
root.configure(bg="#0f2027")  # deep dark

# 🌈 Top Section (like gradient feel using color contrast)
top_frame = tk.Frame(root, bg="#203a43", height=200)
top_frame.pack(fill="x")

title = tk.Label(top_frame, text="Weather",
                 font=("Helvetica", 20, "bold"),
                 bg="#203a43", fg="white")
title.pack(pady=15)

city_entry = tk.Entry(top_frame,
                      font=("Helvetica", 14),
                      justify="center",
                      bd=0)
city_entry.pack(ipady=5, padx=40)

search_btn = tk.Button(top_frame,
                       text="Search",
                       font=("Helvetica", 12, "bold"),
                       bg="#2ecc71",
                       fg="white",
                       bd=0,
                       padx=20,
                       command=get_weather)
search_btn.pack(pady=10)

# 📱 Main Weather Display
main_frame = tk.Frame(root, bg="#0f2027")
main_frame.pack(expand=True)

city_label = tk.Label(main_frame,
                      text="Enter City",
                      font=("Helvetica", 18),
                      bg="#0f2027",
                      fg="white")
city_label.pack(pady=10)

temp_label = tk.Label(main_frame,
                      text="",
                      font=("Helvetica", 50, "bold"),
                      bg="#0f2027",
                      fg="#f1c40f")
temp_label.pack()

condition_label = tk.Label(main_frame,
                           text="",
                           font=("Helvetica", 16),
                           bg="#0f2027",
                           fg="lightgray")
condition_label.pack(pady=5)

extra_label = tk.Label(main_frame,
                       text="",
                       font=("Helvetica", 12),
                       bg="#0f2027",
                       fg="gray")
extra_label.pack(pady=5)

# ▶️ Run
root.mainloop()
