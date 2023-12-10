import json
import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import cm
from matplotlib.colors import Normalize
from . import parser, cleaner


def extract_skills(filename):
    with open(filename, "r", encoding="utf8") as file:
        data = json.load(file)

    all_skills = []

    for vacancy in data:
        skills = vacancy.get("навыки", [])
        all_skills.extend(skills)

    return all_skills


def main(query):
    filename = parser.parse_hh(query)
    all_skills = Counter(extract_skills(filename))
    most_common_skills = all_skills.most_common(30)

    with open("hh_parser/most_common_skills.txt", "w", encoding="utf-8") as f:
        for i in most_common_skills:
            f.write(": ".join(list(map(lambda x: str(x), i))) + "\n")

    skills, counts = zip(*most_common_skills)

    norm = Normalize(vmin=min(counts), vmax=max(counts))
    colors = [cm.viridis_r(norm(i)) for i in counts]

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.barh(skills, counts, color=colors)

    ax.set_xlabel("Количество упоминаний")
    ax.set_title("Самые востребованные навыки в вакансиях")
    ax.invert_yaxis()
    plt.tight_layout()

    plt.savefig(f"static/results/{query}_skills.jpg", format="jpg")
    plt.close()

    cleaner.del_file("hh_parser/most_common_skills.txt")
    cleaner.del_file("hh_parser/vacancies.json")

    return (query, most_common_skills, f"results/{query}_skills.jpg")
