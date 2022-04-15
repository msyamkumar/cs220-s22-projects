#===================== DO NOT EDIT THIS BLOCK =================================#
import collections
from collections import namedtuple
import json
import os

PASS = "PASS"
TEXT_FORMAT = "text"  # question type when expected answer is a str, int, float, or bool
NO_RERUN = "no_rerun" #any question involving paths. Do not expect the rerun to match submission
TEXT_NO_RERUN = TEXT_FORMAT + " " + NO_RERUN
TEXT_FORMAT_NAMEDTUPLE = "text namedtuple"  # question type when expected answer is a namedtuple
TEXT_FORMAT_UNORDERED_LIST = "text list_unordered"  # question type when the expected answer is a list where the order does *not* matter
TEXT_FORMAT_ORDERED_LIST = "text list_ordered"  # question type when the expected answer is a list where the order does matter
TEXT_FORMAT_ORDERED_LIST_NO_RERUN = "text list_ordered no_rerun"  # question type when the expected answer is a list where the order does matter and contains paths
TEXT_FORMAT_ORDERED_LIST_NAMEDTUPLE = "text list_ordered namedtuple"  # question type when the expected answer is a list of namedtuples where the order does matter
TEXT_FORMAT_SPECIAL_ORDERED_LIST = "text list_special_ordered"  # question type when the expected answer is a list where order does matter, but with possible ties. All tied elements are put in a list, where internal order does not matter.
TEXT_FORMAT_DICT = "text dict"  # question type when the expected answer is a dictionary
TEXT_FORMAT_LIST_DICTS_ORDERED = "text list_dicts_ordered"  # question type when the expected answer is a list of dicts where the order does matter
PNG_FORMAT = "png"  # use when the expected answer is an image
HTML_FORMAT = "html"
FILE_FORMAT = "file"
FILE_JSON_FORMAT = "file json"

Question = collections.namedtuple("Question", ["number", "weight", "format"])
#===================== DO NOT EDIT THIS BLOCK =================================#


# EDIT THIS: definitions specific to this project
Comment = collections.namedtuple("Comment", ['video_id', 'comment_length', 'author_id', 'likes', 'published_at'])

REQUIRED_FILES = [os.path.join('data', 'channel_ids1.json'),
         os.path.join('data', 'channel_ids2.json'),
         os.path.join('data', 'channel_ids3.json'),
         os.path.join('data', 'channel_ids4.json'),
         os.path.join('data', 'channel_ids5.json'),
         os.path.join('data', 'comment_data1.csv'),
         os.path.join('data', 'comment_data2.csv'),
         os.path.join('data', 'comment_data3.csv'),
         os.path.join('data', 'comment_data4.csv'),
         os.path.join('data', 'comment_data5.csv'),
         os.path.join('data', 'video_data.csv'),
         os.path.join('data', 'video_ids.json'),
         os.path.join('broken_file', 'english_lowercase', 'a_to_m', 'a_to_m.json'),
         os.path.join('broken_file', 'english_lowercase', 'rest.json'),
         os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'A', 'A.json'),
         os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'E.json'),
         os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'rest', 'rest.json'),
         os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'F_to_H.json'),
         os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'I_to_K', 'I', 'I.json'),
         os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'I_to_K', 'rest.json'),
         os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'O.json'),
         os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'M.json'),
         os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'rest', 'rest.json'),
         os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'P_to_Q.json'),
         os.path.join('broken_file', 'english_uppercase', 'R_to_W.json'),
         os.path.join('broken_file', 'english_uppercase', 'rest.json'),
         os.path.join('broken_file', 'non_english', 'korean.json'),
         os.path.join('broken_file', 'non_english', 'rest', 'japanese', 'japanese.json'),
         os.path.join('broken_file', 'non_english', 'rest', 'rest.json'),
         os.path.join('broken_file', 'non_english', 'russian', 'russian.json'),
         os.path.join('broken_file', 'number.json'),
         os.path.join('broken_file', 'special', 'special.json')]

questions = [
    Question(number=1, weight=0.5, format=PNG_FORMAT),
    Question(number=1.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=2, weight=0.5, format=PNG_FORMAT),
    Question(number=2.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=3, weight=0.5, format=PNG_FORMAT),
    Question(number=3.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=4, weight=0.5, format=PNG_FORMAT),
    Question(number=4.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=5, weight=0.5, format=PNG_FORMAT),
    Question(number=5.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=6, weight=0.5, format=PNG_FORMAT),
    Question(number=6.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=7, weight=0.5, format=PNG_FORMAT),
    Question(number=7.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=8, weight=0.5, format=PNG_FORMAT),
    Question(number=8.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=9, weight=0.5, format=PNG_FORMAT),
    Question(number=9.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=10, weight=1, format=TEXT_FORMAT),
    Question(number=11, weight=1, format=TEXT_FORMAT_ORDERED_LIST),
    Question(number=12, weight=0.5, format=PNG_FORMAT),
    Question(number=12.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=13, weight=0.5, format=PNG_FORMAT),
    Question(number=13.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=14, weight=1, format=TEXT_FORMAT_ORDERED_LIST_NO_RERUN),
    Question(number=15, weight=1, format=TEXT_FORMAT_ORDERED_LIST_NO_RERUN),
    Question(number=16, weight=1, format=TEXT_FORMAT_ORDERED_LIST_NO_RERUN),
    Question(number=17, weight=1, format=TEXT_FORMAT_ORDERED_LIST_NO_RERUN),
    Question(number=18, weight=1, format=TEXT_FORMAT),
    Question(number=19, weight=1, format=TEXT_FORMAT),
    Question(number=20, weight=1, format=TEXT_FORMAT_ORDERED_LIST),
]

expected_json = {
        "1.1": True,
        "2.1": True,
        "3.1": True,
        "4.1": True,
        "5.1": True,
        "6.1": True,
        "7.1": True,
        "8.1": True,
        "9.1": True,
        "10": 66,
        "11": 478.6,
        "12.1": True,
        "13.1": True,
        "14": [os.path.join('broken_file', 'special', 'special.json')],
        "15": [os.path.join('broken_file', 'non_english', 'rest', 'japanese', 'japanese.json'),
                os.path.join('broken_file', 'non_english', 'rest', 'rest.json')],
        "16": [os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'O.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'M.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'rest', 'rest.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'P_to_Q.json')],
        "17": [os.path.join('broken_file', 'english_lowercase', 'a_to_m', 'a_to_m.json'),
                os.path.join('broken_file', 'english_lowercase', 'rest.json'),
                os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'A', 'A.json'),
                os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'E.json'),
                os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'rest', 'rest.json'),
                os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'F_to_H.json'),
                os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'I_to_K', 'I', 'I.json'),
                os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'I_to_K', 'rest.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'O.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'M.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'rest', 'rest.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'P_to_Q.json'),
                os.path.join('broken_file', 'english_uppercase', 'R_to_W.json'),
                os.path.join('broken_file', 'english_uppercase', 'rest.json'),
                os.path.join('broken_file', 'non_english', 'korean.json'),
                os.path.join('broken_file', 'non_english', 'rest', 'japanese', 'japanese.json'),
                os.path.join('broken_file', 'non_english', 'rest', 'rest.json'),
                os.path.join('broken_file', 'non_english', 'russian', 'russian.json'),
                os.path.join('broken_file', 'number.json'),
                os.path.join('broken_file', 'special', 'special.json')],
        "18": 18519,
        "19": 'Like it Matters',
        "20": ['ChippyGaming',
                 'Odin J',
                 'A comely black woman',
                 'BadBoyHalo',
                 'Nakatomino Calamari ']
    }

# The following code is used to verify plots. See the p11 solution for how to generate
# plot_points.json
with open("plot_points.json", "r", encoding="utf-8") as fp:
    read_dicts = json.load(fp, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})

def verify_bar(plot_dict, qnum):
    if not 1 <= qnum <= 20:
        print("qnum is invalid")
        return None
    if read_dicts[qnum-1] == {}:
        print("This question has no plot to verify")
        return None
    return read_dicts[qnum-1] == plot_dict

def verify_scatter(x, y, qnum):
    if not 1 <= qnum <= 20:
        print("qnum is invalid")
        return None
    if read_dicts[qnum-1] == {}:
        print("This question has no plot to verify")
        return None
    answer = zip(read_dicts[qnum-1]["x"], read_dicts[qnum-1]["y"])
    input = zip(x, y)
    return sorted(answer) == sorted(input)

def view_plot_data(qnum):
    if not 1 <= qnum <= 20:
        print("qnum is invalid")
        return None
    if read_dicts[qnum-1] == {}:
        print("This question has no plot to verify")
        return None
    return read_dicts[qnum-1]
