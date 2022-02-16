TEXT_FORMAT = "text"  # question type when expected answer is a str, int, float, or bool
from collections import namedtuple

Question = namedtuple("Question", ["number", "weight", "format"])

questions = [
    Question(number=1, weight=1, format=TEXT_FORMAT),
    Question(number=2, weight=1, format=TEXT_FORMAT),
    Question(number=3, weight=1, format=TEXT_FORMAT),
    Question(number=4, weight=1, format=TEXT_FORMAT),
    Question(number=5, weight=1, format=TEXT_FORMAT),
    Question(number=6, weight=1, format=TEXT_FORMAT),
    Question(number=7, weight=1, format=TEXT_FORMAT),
    Question(number=8, weight=1, format=TEXT_FORMAT),
    Question(number=9, weight=1, format=TEXT_FORMAT),
    Question(number=10, weight=1, format=TEXT_FORMAT),
    Question(number=11, weight=1, format=TEXT_FORMAT),
    Question(number=12, weight=1, format=TEXT_FORMAT),
    Question(number=13, weight=1, format=TEXT_FORMAT),
    Question(number=14, weight=1, format=TEXT_FORMAT),
    Question(number=15, weight=1, format=TEXT_FORMAT),
    Question(number=16, weight=1, format=TEXT_FORMAT),
    Question(number=17, weight=1, format=TEXT_FORMAT),
    Question(number=18, weight=1, format=TEXT_FORMAT),
    Question(number=19, weight=1, format=TEXT_FORMAT),
    Question(number=20, weight=1, format=TEXT_FORMAT),
]

expected_json = {
    "1": 4.545454545454546,
    "2": 16.25,
    "3": 1.0,
    "4": 0.5,
    "5": 12.222222222222221,
    "6": 30.90909090909091,
    "7": 12.380952380952381,
    "8": 1,
    "9": 8,
    "10": "Flareon",
    "11": "Blastoise",
    "12": "Starly",
    "13": "Draw",
    "14": "Charizard",
    "15": "Pikachu ran away",
    "16": "Magikarp ran away",
    "17": "Forbidden",
    "18": "Forbidden",
    "19": "Arcanine",
    "20": "Forbidden"
}
