import json
from collections import Counter
import matplotlib.pyplot as plt


def extract_skills(filename):
    with open(filename, "r", encoding="utf8") as file:
        data = json.load(file)

    all_skills = []

    for vacancy in data:
        skills = vacancy.get("навыки", [])
        all_skills.extend(skills)

    return all_skills


def main(filename):
    all_skills = Counter(extract_skills(filename))
    most_common_skills = all_skills.most_common(30)

    with open("most_common_skills.txt", "w", encoding="utf-8") as f:
        for i in most_common_skills:
            f.write(": ".join(list(map(lambda x: str(x), i))) + "\n")

    skills, counts = zip(*most_common_skills)

    plt.figure(figsize=(10, 6))
    plt.barh(skills, counts, color="skyblue")
    plt.xlabel("Количество упоминаний")
    plt.ylabel("Навыки")
    plt.title("Самые востребованные навыки в вакансиях")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


main("vacancies.json")
