import collections
from collections import namedtuple

PASS = "PASS"
TEXT_FORMAT = "text"  # question type when expected answer is a str, int, float, or bool
TEXT_FORMAT_NAMEDTUPLE = "text namedtuple"  # question type when expected answer is a namedtuple
TEXT_FORMAT_UNORDERED_LIST = "text list_unordered"  # question type when the expected answer is a list where the order does *not* matter
TEXT_FORMAT_ORDERED_LIST = "text list_ordered"  # question type when the expected answer is a list where the order does matter
TEXT_FORMAT_ORDERED_LIST_NAMEDTUPLE = "text list_ordered namedtuple"  # question type when the expected answer is a list of namedtuples where the order does matter
TEXT_FORMAT_SPECIAL_ORDERED_LIST = "text list_special_ordered"  # question type when the expected answer is a list where order does matter, but with possible ties. All tied elements are put in a list, where internal order does not matter.
TEXT_FORMAT_DICT = "text dict"  # question type when the expected answer is a dictionary
TEXT_FORMAT_LIST_DICTS_ORDERED = "text list_dicts_ordered"  # question type when the expected answer is a list of dicts where the order does matter
PNG_FORMAT = "png"  # use when the expected answer is an image
HTML_FORMAT = "html"
FILE_FORMAT = "file"
FILE_JSON_FORMAT = "file json"

Question = collections.namedtuple("Question", ["number", "weight", "format"])

questions = [
    Question(number=1, weight=1, format=TEXT_FORMAT_UNORDERED_LIST),
    Question(number=2, weight=1, format=TEXT_FORMAT),
    Question(number=3, weight=1, format=TEXT_FORMAT),
    Question(number=4, weight=1, format=TEXT_FORMAT_UNORDERED_LIST),
    Question(number=5, weight=1, format=TEXT_FORMAT_UNORDERED_LIST),
    Question(number=6, weight=1, format=TEXT_FORMAT_UNORDERED_LIST),
    Question(number=7, weight=1, format=TEXT_FORMAT_UNORDERED_LIST),
    Question(number=8, weight=1, format=TEXT_FORMAT),
    Question(number=9, weight=1, format=TEXT_FORMAT_UNORDERED_LIST),
    Question(number=10, weight=1, format=TEXT_FORMAT_ORDERED_LIST),
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
    "1": ['Brooklyn', 'Bronx', 'Queens', 'Staten Island', 'Manhattan'],
    "2": 152,
    "3": 252,
    "4": ['CBG CtyBGd HelpsHaiti rm#1:1-4',
          'CBG Helps Haiti Room#2.5',
          'CBG Helps Haiti Rm #2',
          'CBG# 4Tiny room w/ huge window/AC',
          'CBG Helps Haiti Rm #3',
          'CBG HelpsHaiti #5 Suite'],
    "5": ['Cozy studio/kitchen, bathroom',
             'Big Kitchen, Beautiful Bathroom',
             'JFK Studio Flat with Kitchen and Private bathroom',
             'Pvt Room W/Pvt Bathroom; NO KITCHEN!',
             "2 Bedrooms & 2 Bathrooms Apt in Hell's Kitchen",
             'Family Room/Kitchen/Shared Bathroom',
             'Private room w/ bathroom & kitchen!',
             '2BR- Private Kitchen + Bathroom-20min to Manhattan',
             'Cozy studio w/kitchen & bathroom. Great location',
             'PRIVATE BATHROOM  AND KITCHEN AREA',
             '2 Bedrooms PRIVATE BATHROOM AND KITCHEN',
             'The printing studio bedroom with garden in Bedstuy  !!Brooklyn. Historic neighborhood close to everything ! Full kitchen bathroom BBQ and porch at your disposal. Learn to print !!',
             '2 bedroom 1 bathroom kitchen and living area',
             'Private Studio w/Bathroom & Kitchenette',
             'Beautiful Private Bed & Bathroom (no kitchen)',
             'Suite nearJFK with private bathroom and kitchen',
             'Work Friendly, Private Bathroom and Kitchen',
             'Back bedroom next to kitchen and bathroom',
             'Private room with shared bathroom and kitchen',
             'Cozy Room, kitchen bathroom & Patio Brooklyn NY',
             'Private Large Bedroom Apt w/ Bathroom (NO KITCHEN)',
             'Two Bedrooms with Four Beds, Bathroom, Kitchenette'],
    "6": ['Elias', 'Leisa', 'Elisa'],
    "7": ['26785',
          '31994',
          '166172',
          '195233',
          '699472',
          '3474320'],
    "8": 2.2159641752458334,
    "9": ['391948',
          '6072842',
          '7026258',
          '8482165',
          '10685496',
          '13040683'],
    "10": [301, 300, 285, 281, 279, 279, 273, 265, 229],
    "11": 357,
    "12": 75,
    "13": 100,
    "14": 93.10344827586206,
    "15": 0.15472762967118855,
    "16": 0.22369125775160625,
    "17": 'Cobble Hill',
    "18": 9.649122807017543,
    "19": 3.847418612298586,
    "20": 30
}
