# Environmental Monitoring Prototype - Raspberry Pi

import Adafruit_DHT
import requests
import time

# Sensor settings
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
AIR_QUALITY_PIN = 0
LIGHT_SENSOR_PIN = 18

# ThingSpeak settings
THINGSPEAK_API_KEY = "YOUR_THINGSPEAK_API_KEY"
THINGSPEAK_URL = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}"

def read_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

def read_air_quality():
    # Function to read air quality from the MQ-135 sensor
    # Add implementation based on the Raspberry Pi GPIO library or ADC converter used
    pass

def read_light_intensity():
    # Function to read light intensity from the LDR sensor
    # Add implementation based on the Raspberry Pi GPIO library or ADC converter used
    pass

def main():
    while True:
        humidity, temperature = read_temperature_humidity()
        air_quality = read_air_quality()
        light_intensity = read_light_intensity()
        
        data = {
            "field1": temperature,
            "field2": humidity,
            "field3": air_quality,
            "field4": light_intensity
        }
        
        try:
            response = requests.post(THINGSPEAK_URL, data=data)
            print(f"Data uploaded: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error uploading data: {e}")
        
        time.sleep(300)  # 5 minutes interval for data collection

if __name__ == "__main__":
    main()
