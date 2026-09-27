import json
import os

PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(PATH, "data.json")


def loadData():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    return[]


def saveData(upDateData):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(upDateData, file, indent=4, ensure_ascii=False)

def clear_terminal():
    
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



addSave = loadData()