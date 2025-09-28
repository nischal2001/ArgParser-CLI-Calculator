import requests

API_KEY = "d3f7547936b3726916163c7dac03dcfb".strip()     # strip removes the whitespaces if any 
city = input("Enter city name: ")   # user enters city in Terminal
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


print(repr(API_KEY))
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"\nCity: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
else:
    print("Error:", data.get("message", "Failed to fetch weather"))
