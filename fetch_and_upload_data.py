# Environmental Monitoring Prototype - Laptop

import subprocess
import requests

# Raspberry Pi settings
RASPBERRY_PI_IP = "RASPBERRY_PI_IP_ADDRESS"
RASPBERRY_PI_USERNAME = "RASPBERRY_PI_USERNAME"

# ThingSpeak settings
THINGSPEAK_API_KEY = "YOUR_THINGSPEAK_API_KEY"
THINGSPEAK_URL = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}"

def fetch_data_from_raspberry_pi():
    # Use SCP to fetch data from the Raspberry Pi
    subprocess.run(
        f"scp {RASPBERRY_PI_USERNAME}@{RASPBERRY_PI_IP}:environmental_data.csv .",
        shell=True,
        check=True
    )

def upload_data_to_thingspeak():
    # Read data from the fetched file and upload to ThingSpeak
    with open("environmental_data.csv", "r") as file:
        lines = file.readlines()

    for line in lines[1:]:  # Skip header
        data = line.strip().split(",")
        temperature, humidity, air_quality, light_intensity = data

        payload = {
            "field1": temperature,
            "field2": humidity,
            "field3": air_quality,
            "field4": light_intensity
        }

        try:
            response = requests.post(THINGSPEAK_URL, data=payload)
            print(f"Data uploaded: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error uploading data: {e}")

def main():
    fetch_data_from_raspberry_pi()
    upload_data_to_thingspeak()

if __name__ == "__main__":
    main()
