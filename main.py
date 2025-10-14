import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--discord', dest='discord', type=str)
parser.add_argument('--api', dest='api', type=str)
ZIPCODE = 92126

if __name__ == '__main__':
    args = parser.parse_args()
    
    try:
        with open('forecast.json') as f:
            yesterday_forecast = json.load(f)
        if yesterday_forecast['daily_will_it_rain'] or yesterday_forecast['daily_chance_of_rain'] > 30:
            requests.post(args.discord, data={
                'content': f"it was predicted to {'rain' if yesterday_forecast['daily_will_it_rain'] else 'not rain'} with a chance of {yesterday_forecast['daily_chance_of_rain']}",
                'username': "WeatherBot"
            })
    except:
        pass


    req = requests.get(f'https://api.weatherapi.com/v1/forecast.json?key={args.api}&q={ZIPCODE}&days=1&aqi=no&alerts=no')
    result = req.json()
    if 'rain' in result['current']['condition']['text'].lower():
        requests.post(args.discord, data={
        'content': 'it rains today!!!',
        'username': "WeatherBot"
    })
    tomorrow = result['forecast']['forecastday'][0]['day']
    
    with open('forecast.json', 'w') as f:
        json.dump(result, f)