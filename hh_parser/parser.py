import os
import json
import requests
import time
from .parser_url import parse_url


def take_skills(v, url):
    key_skills = v.get("key_skills")
    if key_skills and len(key_skills) > 0:
        return key_skills
    else:
        return parse_url(url)


def getPage(name="Python", page=0):
    """
    Создаем метод для получения страницы со списком вакансий.
    Аргументы:
        page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
    """

    params = {"text": f"NAME:{name}", "area": 1, "page": page, "per_page": 5}

    req = requests.get("https://api.hh.ru/vacancies", params)
    data = req.content.decode()
    req.close()
    return data


def parse_hh(name="Python"):
    res_data = []

    for page in range(0, 20):
        js_obj = json.loads(getPage(name, page))

        for v in js_obj["items"]:
            vacancy_data = {
                "название": v.get("name", "Нет данных"),
                "ссылка": v.get("alternate_url", "Нет данных"),
                "навыки": take_skills(v, v.get("alternate_url")),
                "зарплата": v.get("salary", "Нет данных"),
                "формат_работы": v.get("employment", {}).get("name", "Нет данных"),
                "удаленная_работа": v.get("accept_remote", False),
                "требования": v.get("snippet").get("requirement", "Нет данных"),
                "обязанности": v.get("snippet").get("responsibility", "Нет данных"),
            }
            res_data.append(vacancy_data)

            if (js_obj["pages"] - page) <= 1:
                break

    filename = "hh_parser/vacancies.json"

    with open(filename, mode="a", encoding="utf8") as f:
        f.write(json.dumps(res_data, ensure_ascii=False) + "\n")

    return filename
