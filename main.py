import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--discord', dest='discord', type=str)
parser.add_argument('--api', dest='api', type=str)
ZIPCODE = 92126

if __name__ == '__main__':
    args = parser.parse_args()
    
    req = requests.get(f'https://api.weatherapi.com/v1/forecast.json?key={args.api}&q={ZIPCODE}&days=1&aqi=no&alerts=no')
    result = req.json()
    today = result['forecast']['forecastday'][0]['day']
    if today['daily_will_it_rain'] or today['daily_chance_of_rain'] > 30:
        requests.post(args.discord, data={
            'content': f"it is predicted to {'rain' if today['daily_will_it_rain'] else 'not rain'} today with a chance of {today['daily_chance_of_rain']}%.",
            'username': "WeatherBot"
        })
