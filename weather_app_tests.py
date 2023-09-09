import unittest
import requests
import os
import actual


class Test_Actual_Weather(unittest.TestCase):

    def test_weather_data_storage(self):
        # Test if the file exists
        self.assertTrue(os.path.exists('ACTUAL.txt'))

    def test_weather_api_request(self):
        # Make a request to the weather API
        api_key = 'cd4259afc066461f96e40d56cdc6fe76'
        lat = 60.3954
        lon = 25.6605
        api_urlw = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
        response = requests.get(api_urlw)
        self.assertEqual(response.status_code, 200)  # Check if the request was successful

        dataw = response.json()
        self.assertIn('main', dataw)  # Check if the 'main' key exists in the response
        self.assertIn('temp', dataw['main'])  # Check if 'temp' exists in 'main'
        self.assertIn('wind', dataw)  # Check if the 'wind' key exists in the response
        self.assertIn('speed', dataw['wind'])  # Check if 'speed' exists in 'wind'
        self.assertIn('humidity', dataw['main'])  # Check if 'humidity' exists in 'main'   


