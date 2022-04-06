# Project 10: Analyzing Youtube Comments


## Corrections/Clarifications


None yet.

**Find any issues?** Report to us:

- Saurabh Kulkarni <skulkarni27@wisc.edu>

## Learning Objectives

In this project, you will demonstrate your ability to:

- read and write files
- use dictionaries in advanced ways
- handle errors using try/except
- create a custom type

## Coding Style Requirements

Remember that coding style matters! **We might deduct points for bad coding style.** Here is a list of coding style requirements:

- Do not use meaningless names for variables or functions (e.g. uuu = "my name").
- Do not write the exact same code in multiple places. Instead, wrap this code into a function and call that function whenever the code should be used.
- Do not call unnecessary functions.
- Avoid using slow functions multiple times within a loop.
- Avoid inappropriate use of data structures. For example, using a for loop to search for a corresponding value in a dictionary with a given key instead of using `dictname[key]` directly.
- Don't name variables or functions as python keywords or built-in functions. Bad example: str = "23".
- Don't define multiple functions with the same name or define multiple versions of one function with different names. Just keep the best version.
- Put all `import` commands together at the second cell of `main.ipynb`, the first cell should be submission information (netid and etc).
- Do not leave in irrelevant output or test code that we didn't ask for

**Warning:** Do **not** use `csv.DictReader` to read the csv files. It may cause errors with the autograder due to version compatibility issues. It would be safest for you to use a function like `process_csv` that we have been working with in the past, to parse csv files.

## Setup
**Step 1:** Create a `p10` directory

**Step 2:** Download [`data.zip`](https://github.com/msyamkumar/cs220-s22-projects/tree/main/p10/data.zip ) to `p10` and extract it the same way you did in lab. The `data.zip` for P10 is slightly different from Lab 10's, so do *not* simply copy over your lab data.

**Step 3:** Download `test.py` and `questions.py` to your `p10` directory from Step 1.

**Step 4:** Create a `main.ipynb` in the same location, which contains your p10 solution.

**Step 5:** Add the following cell to the top of your notebook, and fill out the information:

```python
# project: p10
# submitter: NETID1
# partner: NETID2
# hours: ????
```

## Introduction

In this project, you'll be analyzing comments from trending YouTube videos. We have gathered data from the [trending](https://www.youtube.com/feed/trending) videos on each day of the first two weeks of October 2021. In total, we managed to collect nearly 1 million comments from the 493 videos that were trending over these two weeks. However, that made the dataset too unwieldy, so in this project, we will be analyzing a representative sample of (merely) 200,000 comments.


This data is still quite messy! You'll face the following challenges:

* Data is spread across multiple files.
* Some files will be CSVs, others JSONs.
* The files may be missing values or may be too corrupt to parse.


In p10, you'll write code to clean up the data, representing everything as namedtuple objects (you'll create a new type for these).  In p11, you'll analyze your clean data.

For this project, you'll create a new `main.ipynb` and answer questions in the usual format. **Please go through the [lab-p10](https://github.com/msyamkumar/cs220-s22-projects/tree/main/lab-p10) before working on this project.** In the lab, you will make helper functions and learn some useful techniques related to this project.

You may only use the following import statements:
```python
import os
import csv
import json
from collections import namedtuple
# you may use from style of import to import JSONDecodeError
```


### #Q1: What are the names of the files present in the `data` directory?

Your answer should be a list of filenames sorted in alphabetical order.  

**Requirements:**
- Use the `list_files_in` function you wrote in lab
  - It must sort your answer and exclude files that begin with a period (".")

### #Q2: What are the *paths* of all the files in the `data` directory?

Your answer should be a list of relative paths sorted in alphabetical order.

**Requirements:**
- Use the `list_paths_in` function you wrote in lab
  - Use `os.path.join()`. Do not hardcode slashes ("\\" or "/")
  - The paths must be relative to where your `main.ipynb` is
- Store the return value of `list_paths_in` into a variable and use it for Q3 and Q4.

**WARNING**: *DO NOT* use absolute paths such as `C:\\Desktop\\CS220\\p10`. **You may only use relative paths in this project**. Otherwise, all of the tests will fail and **you will get a 0**.

---

We see that there are five json files titled `channel_ids1.json`, `channel_ids2.json`, etc., followed by five csv files titled `comment_data1.csv`, `comment_data2.csv`, etc., followed by the two files `video_data.csv` and `video_ids.json`.

In this project, we will read in the data that is stored in each of these files and parse them. Now would be a great time to open these files with a Text Editor, or Jupyter Notebook, to see what data is stored in each of them. For now, note that the five `channel_ids` json files store data in the same format. Similarly, the five `comment_data` csv files store data in the same format.


### #Q3: What are the paths of all the files whose name contains `comment_data` in our `data` directory?

Your answer should be a list sorted in alphabetical order.

**Requirements:**
- Do not invoke `list_paths_in` function again
  - Instead use the variable from Q2 to answer this question
- Store this list in a variable called `comment_paths`


### #Q4: What are the paths of all the files whose name contains `channel_ids` in our `data` directory?

Your answer should be a list sorted in alphabetical order.

**Requirements:**
- Do not invoke `list_paths_in` function again
  - Instead use the variable from Q2 to answer this question
- Store this list in a variable called `channel_paths`



----

### Function requirement:

Copy the following function over directly from your lab. You will also need to copy the `read_json` function.

```python
def get_mapping(pathname):
    """
    Given a path called pathname, load the json data at the path and return the loaded json data.
    If a json.JSONDecodeError is thrown, an empty dictionary is returned.
    """
    # TODO: copy this over from your lab
```

### #Q5: What is the name of the channel with the ID `UCNye-wNBqNL5ZzHSJj3l8Bg`?

This channel ID is in the `data` directory within the file `channel_ids1.json`. You may use this in your code.

**Requirement**:

- Use `get_mapping`
- Do not hardcode slashes ('/' or '\\') in your path
    - *Warning*: if you do not follow this, your code will not clear auto-grader.

### #Q6: How many channels do we have in the entire dataset?

Use `get_mapping` to read all `channel_ids` json files and combine them into a **single dictionary**. Your answer should be an `int`.

**Requirements:**
- Use `channel_paths`
- Use the function `get_mapping`, to generate mapping for each channel path
- Populate a new dict called `channel_dict`, mapping channel ID to the channel name
  - `channel_dict` should store the mapping for all the channel IDs in all the channel paths

----


### Data Structure Requirement:

You will need to create a `namedtuple` to represent a `Comment`. This should have the following attributes...

- `video_id`
- `comment_length`
- `author_id`
- `likes`
- `published_at`

... where `video_id`, `author_id`, and`published_at` are strings, and `comment_length` and `likes` are ints. These attributes will exactly match the name of a column in the CSV header.

**Note**: We introduced namedtuples in "Objects & Tuples" lecture. If required, please review the lecture examples before you create your `Comment` namedtuple.

### Function requirement:

Now, parse the `comment_data` files and make `Comment` objects out of them. You should define a function `get_comment_data` that takes in the path of a csv file as its input and returns a dict mapping comment IDs to Comment objects. Some starter code is given for you.

**Requirements:** 
- Simply **ignore** any row that has a cell with an empty string. (See below description)
- `comment_length` and `likes` field should be of type `int` when you create `Comment` object instance.


```python
# You will need process_csv in order to complete get_comment_data.
# If you already copy/pasted it from lab, please ignore this copy.
def process_csv(filename):
    exampleFile = open(filename, encoding="utf-8")  
    exampleReader = csv.reader(exampleFile) 
    exampleData = list(exampleReader)        
    exampleFile.close()  
    return exampleData 

def get_comment_data(comment_file):
    csv_data = process_csv(comment_file)
    header = csv_data[0] 
    # TODO: if required, use a print function call to display header or alternatively, take a look at the comments csv file
    comment_rows = csv_data[1:]
    comment_id_idx = header.index("comment_id")
    video_id_idx = header.index("video_id")
    # TODO: Get the indices for the other columns
    # TODO: Iterate over comment_rows
    # TODO:   Ignore rows with missing data. That is, ignore any row that has a cell with an empty string.
    # TODO:   Create Comment object instance (custom type created with namedtuple)
    # TODO:   Add each Comment to a dict with its comment ID as a key and Comment object reference as value
    # TODO: return the dict of Comments
```

**Warning:** While you may assume that each attribute of `Comment` has a corresponding column in `comment_file`, you may not hardcode the column indices. Use `.index()` instead (as seen in the above starter code).

**Note:** There are a few 'bad' rows in the dataset with missing values. The missing values are represented as **empty strings**. Here are a few examples of bad rows in `comment_data1.csv`:

```python
['UgxKBGVZtGDsKz402o94AaABAg', 'CVsldjBMb3I', '', 'UCkeRlDhi8ew8bLJ_KJzYVHA', '0', '2021-10-07 14:23:49']
['Ugxit0CxKFdQSGHBQVZ4AaABAg', 'Ht9v8YLy-O4', '', 'UCrZ9OYz2o7_YlcYuu58O3IA', '0', '2021-10-28 20:49:46']
['UgxqInn43ZA8HICsaCN4AaABAg', 'ymXnK6UX5zE', '34', '', '0', '2021-10-10 09:39:07']
```

The first two comments are missing their `comment_length`, and the third comment is missing its `author_id`. 

### #Q7: What is the Comment object with comment ID `UgygOezB4Mvd5o6FgAt4AaABAg`?

This comment is in the `data` directory within the file `comment_data1.csv`. You may use this in your code.

**Requirements:** 
- Use the function `get_comment_data`
- Do not hardcode slashes ('/' or '\\') in your path
   - *Warning*: if you do not follow this, your code will not clear auto-grader.

---

## Data Structure Requirement

The following code will construct a complete dictionary of comments by [update](https://www.programiz.com/python-programming/methods/dictionary/update)'ing the dictionary with the `Comment` objects from each file in `comment_paths`. You may use this code to solve q8!

```python
comments = {}
for file in comment_paths:
    comments.update(get_comment_data(file))
```

...

**Oops!** It is likely that you ran into a `ValueError` or `IndexError` when you tried to read all the `comment_data` files. This is because just like with the json files, some of the csv files are also corrupted. Luckily for us, corrupted csv files are a lot easier to deal with than corrupted json files.

In most cases, when a csv file is corrupted, only a few rows will be affected, so we can identify the bad rows and skip just those rows. For example, here are a few bad rows from `comment_data3.csv`:

```python
['Ugxb6qba6ktwyHNzbaR4AaABAg', '0', '24', 'Mi personaje favorito siempre será bobby :(', '2021-10-21 02:16:30']
['UgyCZjll63l7jsHFQyN4AaABAg.9TZNB2bVMfv9Tb7_hNKE7i', 'CznrNHHeF8k', '16', 'UCH2a2z0wCNMnFzufc-_iszQ', '2021-10-17 15:25:42']
```

Can you tell what makes these rows broken? Count the number of elements.

Go back and modify `get_comment_data` so that it skips rows that don't have the expected number of elements. You should also handle when the row has incorrect data - that is when `int` conversion fails. For handling this, you should use the appropriate try / except block.

**Requirements:**
- Use the above code snippet to construct the `comments` dictionary.
- Modify `get_comment_data` to handle bad rows (incorrect fields and incorrect values, that is when `int` conversion fails).
  - Do *not* redefine `get_comment_data`

**Hint:** If you have implemented `get_comment_data` correctly, you should have 199970 comments in `comments`.

### #Q8: What is the length of the comment with ID `UgztIaGfqFoiGvbOdfp4AaABAg`?

Your answer should be an int.

**Requirements:**
- Use the `comments` dict that you just made

---

Now, let us do something interesting with the data we have collected so far!

### #Q9: What percentage of comments are at most 140 characters long?
Your answer should be a float between 0 and 100.

### #Q10: What is the author ID of the comment that has the highest number of likes?

There is a unique comment with the highest number of likes. So, you don't have to worry about any ties here.


### #Q11: What is the most popular hour for publishing comments?

Your answer should be an int representing the hour of the day. 

*Hint*: String slicing may be useful here.

**Requirements:**
- Use `comments` to get the information you need

----

### Data structure requirement:

Bucketize the `comments` data by creating a **dict** mapping video IDs to a **list of comment IDs** corresponding to that video ID. Call this dict `comment_buckets`. For example, the corresponding value for the video id `'tzU2P1JfEJM'` should be...

```python
['UgxKqI14hrfBma9f3uB4AaABAg',
 'UgyMSyCv7WhVdwJpWnJ4AaABAg',
 'Ugw68NEB_-Vxr5f_YGF4AaABAg',
 'UgxJr7cNBJ8Zjq7eAsR4AaABAg',
 'UgxS5IAKmwhRv43v1Il4AaABAg',
 'UgwhwKsREQFqoN1b_fZ4AaABAg',
 'Ugw7JMAm90LTx5IkZE54AaABAg',
 'UgxCseCYDTshrTjOH3x4AaABAg',
 'UgziOHldack2REfF2jZ4AaABAg.9SyorZ4dLxM9T5JWpB34L1',
 'UgyPX0LDQi6DoNrYfT14AaABAg',
 ...]
```
### #Q12: How many comments does the video with ID `A8rrr_w8rfk` have?

**Requirement:** Use `comment_buckets`.

----

Finally, we are ready to read the remaining `video_ids.json` and `video_data.csv` files! As usual, it is recommended that you open these files manually and see how the data is stored before attempting to parse them with Python.

### Function and data structure requirement:
Copy over your `get_videos` function from lab. There's *two* modifications you need to make.

1) Add a `channel_name` to each video. This can be found by looking up the video's `channel_id` in `channel_dict`. Use appropriate indexing operation to find `channel_id` for every video.

2) Add a list of `comments` for each video which is a list of comment IDs for that video. This can be found by looking up the video's `video_id`  in `comment_buckets`.

Define `videos` as the result of calling `get_videos` on `video_data.csv` and `video_ids.json` (both in the `data` directory).

Ensure the following test passes:

```python
sample = ['UgzgwN2JXxjTN4mR5954AaABAg.9TPxukUd20g9TQLnJi3RFU', 'UgzvogxMg82Kj0aW84x4AaABAg']
for s in sample:
    assert s in videos['fkMW60W180E']['comments']
```

### #Q13: What is the video with ID `fkMW60W180E`?

Your output should be a **dict** that contains all the attributes of a video as specified by the lab. A video should *not* include its original `video_id` or `channel_id` (we instead added `title` and `channel_name`).

**Requirement:** Use the `videos` data structure you just made.

---

We can now use the two data structures `videos` and `comments` we have created to analyze our dataset. We will be doing far more interesting things with this data in p11, but for now, let us get acquainted with the data structures we have created so far.

### #Q14: What is the title of the video with ID `gF69voHU_ys`?

**Requirements:**
- Use the `videos` data structure you just made.
- Do not use any control structures (loops, if statements)


### #Q15: Among the videos with more than 1 million views, what is the title of the video with the highest likes to views ratio?

There is a unique video with the highest ratio, so you don't have to worry about tiebreaking.

**Requirements:**
- Ignore the videos with ratings disabled
- Use the `videos` data structure


### #Q16: What is the author ID of the most liked comment under the video titled 'Giving Away My Beard For Charity!'?

There is only one video with such a title. There is a unique comment with the highest number of likes, so you don't have to worry about any ties here.  

**Requirements:**

  - Use the `videos` and `comments` data structures
    - *Warning*: make sure to not accidentally overwrite your `comments` data structure, while iterate over `videos.`

---

### Function requirement:

The `bucketize` function takes in the name of an attribute (such as `channel_name`, `category`, `tags`, etc.) along with a dict of videos and returns a dict that maps the unique values of that attribute to a list of **video IDs** (**warning:** do not use the entire video dictionary) with that unique value. If a video has multiple values for a certain attribute (i.e. that attribute is a list), its ID must appear in the lists for *all* those values.

You should set your global variable `videos` as the default value for the list that `bucketize` takes.


```python
def bucketize(attribute, videos=videos):
  #TODO: This is very similar to bucketize from the last project
```

Use the following to test your function:
```python
category_dict = bucketize('category')
assert category_dict['Pets & Animals'] == ['Hz_DslzN2IA', 'AwvyrO_yM4c']
```

**Requirement:** Remember not to call `bucketize` on the same attribute more than once. You will **lose points** if you call this function unnecessarily.


### #Q17: Which video titles were produced by the "Corridor Crew" channel?

Your output should be a list of video titles.

**Requirements:**
- Use `bucketize`, and store the result to `channel_buckets`
- Use `videos` for data

### #Q18: What are the top 5 channels that have the most total comments on their videos?

Your output should be a list of 5 channel names sorted in **decreasing order of the number of comments on their videos**.

**Requirements:**
- Use the variable `channel_buckets`
- Use `videos` for data


### #Q19: List all the unique video titles which have Minecraft tags.

Your output should be a **list** of video titles. Note that a Minecraft tag is not just a tag that says 'minecraft'. It is any tag that **contains the substring 'minecraft'**, such as the tag 'minecraft funny'.

**Requirements:**
- Use `bucketize`, and store the result to `tag_buckets`
- Use `videos` for data

*Have a look at these titles. Some of them don't have anything to do with Minecraft! Why do you think that is?*


### #Q20: List the titles of the 5 shortest videos.

Your output should be a list of 5 video titles sorted in increasing order of their durations.

**Requirements:**
- Use `videos`

**Hint:** The durations of the videos are in 'hh:mm:ss' format. So, simple string comparison will allow you to sort the videos by their duration. A `lambda` may come in handy, but is not required.

------------------------------

## IMPORTANT: Submission instructions

- Review the [grading rubric](https://github.com/msyamkumar/cs220-s22-projects/blob/main/p10/rubric.md), to ensure that you don't lose points during code review.
- Please remember to **`Kernel->Restart and Run All`** to check for errors, save your notebook, then run the **`test.py`** script one more time before submitting the project.
    - To keep your code concise, please remove your own testing code that does not influence the correctness of answers.
    - __If you are unable to solve a question and have partial code that is causing an error__ when running test.py, please __comment out the lines in the cell for that question.__ Failing to do so will cause the auto-grader to fail when you submit your file and give you 0 points even if you have some questions correctly answered.
    - Make sure that all the fields in the header cell are correctly populated, including **submitter** and **partner**.
    - Make sure that you have #q1, #q2, etc., as comments in the cells that answer each of the 20 questions.
- Follow the same steps as prior projects to turn in main.ipynb to the course website. If required, review those steps.
- It is **your responsibility to make sure that your project clears auto-grader tests on our testing system**.
  - Approximately 4 hours after you submit your program, auto-grader test results will become available. Make sure to use **View Submissions** to check the auto-grader test results.  
  - We will not accept submissions after 7 days, even for autograder issues. This will result in a 0.
