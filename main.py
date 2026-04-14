import json
import os
from functions import kmh_to_ms, ms_to_kmh, compare

FILE = "MyData.json"


def load_data():
    if not os.path.exists(FILE):
        return None
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except:
        return None


def save_data():
    v1 = float(input("Введіть швидкість v1 (км/год): "))
    v2 = float(input("Введіть швидкість v2 (м/с): "))
    lang = input("Введіть мову інтерфейсу: ")

    data = {
        "v1": v1,
        "v2": v2,
        "lang": lang
    }

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Дані збережено в файл {FILE}")


def run(data):
    v1 = data["v1"]
    v2 = data["v2"]

    v1_ms = kmh_to_ms(v1)
    v2_kmh = ms_to_kmh(v2)

    print(f"{v1} км/год = {round(v1_ms, 1)} м/с")
    print(f"{v2} м/с = {round(v2_kmh, 1)} км/год")
    print(compare(v1_ms, v2))


data = load_data()

if data is None:
    save_data()
else:
    run(data)