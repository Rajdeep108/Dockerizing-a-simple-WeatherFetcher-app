from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Web scraping function to get weather data
def get_london_weather():
    url = 'https://www.bbc.com/weather/2643743'  # London Weather page
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape temperature and weather condition
        temperature = soup.find('span', class_='wr-value--temperature--c').get_text(strip=True)
        condition = soup.find('div', class_='wr-day__title').get_text(strip=True)

        return {
            'temperature': temperature,
            'condition': condition
        }
    else:
        return {
            'temperature': 'N/A',
            'condition': 'Failed to fetch weather data'
        }

@app.route('/')
def home():
    weather = get_london_weather()
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
