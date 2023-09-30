from bs4 import BeautifulSoup as Bs
import requests

BASE_URL = "https://www.weather-forecast.com/locations/{}/forecasts/latest"
city = input('Hi. Which city would you like to observe? ')
page = requests.get(BASE_URL.format(city))
soup = Bs(page.text, 'html.parser')


def info():
    brief_info = soup.find('p', class_='large-loc')
    print('####    ', f'{city} informations'.upper(), '  ####')
    print(brief_info.text)
    print('#' * 100)


def weather_next_three_days():
    weather_info = soup.select_one(
        'body > main > section:nth-child(3) > div > div > div.b-forecast__overflow > div > table > '
        'thead > tr.b-forecast__table-description.b-forecast__hide-for-small.days-summaries.js-day'
        '-summary > td:nth-child(2) > p > span')
    print('#' * 5, f'\t Next three days weather in {city} \t', '#' * 5)
    print(weather_info.text)
    print('#' * 100)


def weather_next_4_to_7_days():
    weather_info = soup.select_one('body > main > section:nth-child(3) > div > div > div.b-forecast__overflow > '
                                   'div > table > thead > '
                                   'tr.b-forecast__table-description.b-forecast__hide-for-small.days-summaries'
                                   '.js-day-summary > td:nth-child(3) > p')
    print('#' * 5, f'\t Next 4 to 7 days weather in {city} \t', '#' * 5)
    print(weather_info.text)
    print('#' * 100)


def weather_next_7_to_10_days():
    weather_info = soup.select_one('body > main > section:nth-child(3) > div > div > div.b-forecast__overflow >'
                                   'div > table > thead > '
                                   'tr.b-forecast__table-description.b-forecast__hide-for-small.days'
                                   '-summaries.js-day-summary > td:nth-child(4) > p')
    print('#' * 5, f'\t Next 7 to 10 days weather in {city} \t', '#' * 5)
    print(weather_info.text)
    print('#' * 100)


def weather_next_10_to_12_days():
    weather_info = soup.select_one('body > main > section:nth-child(3) > div > div > div.b-forecast__overflow > div > '
                                   'table > thead > '
                                   'tr.b-forecast__table-description.b-forecast__hide-for-small.days-summaries.js-day'
                                   '-summary > td:nth-child(5) > p')
    print('#' * 5, f'\t Next 10 to 12 days weather in {city} \t', '#' * 5)
    print(weather_info.text)
    print('#' * 100)
