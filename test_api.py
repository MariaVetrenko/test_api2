import requests


def test_google_search_status_code_200():
    response_status_code = requests.get('https://www.google.ru/?hl=ru')
    assert response_status_code.status_code == 200
    print(response_status_code.status_code)


test_google_search_status_code_200()


def test_google_search_contains_text():
    response_contains_text = requests.get(
        'https://www.google.ru/complete/search?q&cp=0&client=gws-wiz-serp&xssi=t&hl=ru&authuser=0'
        '&pq=QA%20AUtomation')
    text = response_contains_text.text
    if text.find("qa automation"):
        print("Contains text")
    else:
        print("Does not contains text")


test_google_search_contains_text()
