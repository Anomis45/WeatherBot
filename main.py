import requests


def get_weather(city: str) -> None:
    api_key = '79d1ca96933b0328e1c7e3e7a26cb347'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,  # Название города
        'units': 'metric',  # Единицы измерения - метрические
        'lang': 'ru',  # Язык ответа
        'appid': api_key  # Ключ API
    }

    try:
        # Выполняем GET-запрос с параметрами
        response = requests.get(base_url, params=params)
        # Проверяем успешность выполнения запроса
        response.raise_for_status()
        # Преобразуем ответ в формат JSON
        weather_data = response.json()

        # Получаем текущую температуру
        temperature = weather_data['main']['temp']
        # Получаем ощущаемую температуру
        temperature_feels = weather_data['main']['feels_like']
        # Получаем скорость ветра
        wind_speed = weather_data['wind']['speed']
        # Получаем описание облачности
        cloud_cover = weather_data['weather'][0]['description']
        # Получаем влажность
        humidity = weather_data['main']['humidity']

        # Выводим собранные данные о погоде
        print(f'Температура воздуха: {temperature}°C\n'
              f'Ощущается как: {temperature_feels}°C\n'
              f'Ветер: {wind_speed} м/с\n'
              f'Облачность: {cloud_cover}\n'
              f'Влажность: {humidity}%')
    # Обрабатываем исключения, связанные с запросом
    except requests.RequestException as e:
        print(f'Ошибка при запросе погоды: {e}')
    # Обрабатываем случаи отсутствия данных в ответе
    except KeyError:
        print(f'Не удалось определить город: {city}')


if __name__ == "__main__":
    city = input('Введите город, в котором хотите узнать погоду: ')
    get_weather(city)


