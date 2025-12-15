import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()   # reads .env file and loads the variables into the os.environ dictionary

#Retrieve the API key from environment variables
api_key = os.getenv("API_KEY")  # fetch the value of API_KEY

# simple test to check if the API key is loaded correctly
if api_key:
    print(f"API Key loaded successfully. length:",len(api_key))
    # Optionally, you can print the first and last few characters for verification
    print("Preview:", api_key[:4] + "..." + api_key[-4:])
else:
    print("API Key not found. Please set the API_KEY environment variable.")    
    

city = "London"

url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}
 
response = requests.get(url, params=params)

# checkif the request was successful
if response.status_code == 200:
    data = response.json()
    # Extract the useful information
    city_name = data["name"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"].capitalize()
    humidity = data["main"]["humidity"]
    country = data["sys"]["country"]
    
    # Print in a nice formatted way
    print("\n" + "="*40)
    print(f"Weather in {city_name}, {country}")
    print("="*40)
    print(f"Temperature: {temp}°C")
    print(f"Feels like:  {feels_like}°C")
    print(f"Conditions:  {description}")
    print(f"Humidity:    {humidity}%")
    print("="*40)
else:
    print(f"\nError! Status code: {response.status_code}")
    print("Response text:", response.text)


# Interactive part - ask user for city
print("\nWant to check another city?")
user_city = input("Enter city name (or 'quit' to exit): ").strip()

if user_city.lower() != "quit" and user_city:
    # Reuse the same logic with user_city instead of "London"
    params["q"] = user_city
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        country = data["sys"]["country"]
        
        print("\n" + "="*40)
        print(f"Weather in {city_name}, {country}")
        print("="*40)
        print(f"Temperature: {temp}°C")
        print(f"Feels like:  {feels_like}°C")
        print(f"Conditions:  {description}")
        print(f"Humidity:    {humidity}%")
        print("="*40)
    else:
        print(f"Could not find weather for '{user_city}'. Check spelling or try again.")