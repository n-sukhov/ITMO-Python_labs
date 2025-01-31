HH_URL = 'https://api.hh.ru/vacancies'

params = {
    'text': 'Python',
    'area': 1,
    'per_page': 5
}


hh_response = requests.get(HH_URL, params=params)

if hh_response.status_code == 200:
    vacancies = hh_response.json()
    for vacancy in vacancies.get('items', []):
        print(f"Название: {vacancy.get('name')}")
        print(f"Компания: {vacancy.get('employer', {}).get('name')}")
        print(f"Город: {vacancy.get('area', {}).get('name')}")
        print(f"Дата публикации: {vacancy.get('published_at')}")
        print(f"Ссылка: {vacancy.get('alternate_url')}\n")
else:
    print(f"Ошибка выполнения запроса: {hh_response.status_code}")
