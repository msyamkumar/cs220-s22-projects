# Project 6: Airbnb

## Corrections/ Clarifications
3/7, 9:00AM: Made several updates:
- Removed backticks from `find_room_names` TODO comments to prevent confusion with quotes
- `secondary_word_in_found_rooms` should return a float between 0 and 100.
- Q6: Anagrams are case-insensitive
- Q7: Brooklyn is a neighborhood group
- Q9: Added warning about Excel dates
- Q17: Runtime is expected to be ~5 seconds. 

**Find any issues?** Report to us:

- Yiwu Zhong ([yzhong52@wisc.edu](mailto:yzhong52@wisc.edu))
- Isha Padmanaban ([ipadmanaban@wisc.edu](mailto:ipadmanaban@wisc.edu))
- Dakota Sullivan ([dsullivan8@wisc.edu](mailto:dsullivan8@wisc.edu))

## Announcements

* **IMPORTANT**: Starting with project p6, resubmissions will **not be allowed**. It is important that you review the grading rubric prior to submission of your project, to make sure you won't lose any points during code review.
* Remember you must begin each cell with the comment #Q1, #Q2, etc. This comment is read by test.py to identify which question is being answered.  **We recommend copying the entire question line as a comment into your notebook.**
* To view grader comments for previous projects, please go to the project submission page and select the graded project and click view submission.
* For P5 regrade requests, please fill in the Grading Issues form which can he found [here](https://www.msyamkumar.com/cs220/s22/surveys.html). Regrade requests must be received within 1-week after release of project grades on Canvas.

## Learning Objectives

In this project, you will demonstrate how to

* access and utilize data in CSV files
* process real world datasets
* use string methods and sorting function / method to order data

**Please go through [lab-p6](https://github.com/msyamkumar/cs220-s22-projects/tree/main/lab-p6) before working on this project.** The lab introduces some useful techniques related to this project.

## Introduction

Data Science can help us understand user behavior on online platform services. This project is about the rooms in Airbnb. Since 2008, guests and hosts have used Airbnb to expand on traveling possibilities and present more unique, personalized way of experiencing the world. `airbnb.csv` has data of nearly 50,000 listings on Airbnb from New York City, NY from the year 2019. This file includes all a lot of information about the hosts, geographical availability of the listings, and other necessary metrics to make predictions and draw conclusions. You will be using various string manipulation methods that come with Python as well as creating some of your own functions to solve the problems posed. Happy coding!

## Directions

Start the project by downloading `airbnb.csv`, `test.py` and `questions.py`. Create a `main.ipynb` file to start answering the following questions. There is no `project.py` this week, use the code from the lab to access the data. Remember to use the `#qN` format as you have for previous projects, and don't forget to add details about the submitter and partner just like in previous projects.

**Important:** 
- You are expected to use the `cell` function you wrote in lab-p6 for all data accesses. You will **lose points** if you access data through other means. You should define this function before q1.
- You should not use concepts / modules that are yet to be covered in this course; for example: you should not use dictionary data structure and modules like pandas. **We'll manually deduct points** accordingly, if you don't follow the provided directions.

The first cell should contain only contain information like this:
```python
# project: p6
# submitter: NETID1
# partner: NETID2
# hours: ????
```
All import statements should be in the second cell. **You will also need to read in the CSV data; use the cells that we made in [lab-p6](https://github.com/msyamkumar/cs220-s22-projects/tree/main/lab-p6) to do so.** Complete this before q1.

---

### #Q1: What unique neighborhood groups are included in the Airbnb dataset?

Generate a Python list containing the different neighborhood groups (`neighborhood_group`). The order doesn't matter but make sure that your answer doesn't contain duplicate entries. If you are unsure about removing duplicates, refer task 4.5 in lab-p6.

It is a good idea to run the test with `python test.py`, after answering every question. If you did Q1 correctly, it should look like this:

```
Summary:
  Test 1: PASS
  Test 2: not found
  Test 3: not found
  Test 4: not found
  Test 5: not found
  Test 6: not found
  Test 7: not found
  Test 8: not found
  Test 9: not found
  Test 10: not found
  Test 11: not found
  Test 12: not found
  Test 13: not found
  Test 14: not found
  Test 15: not found
  Test 16: not found
  Test 17: not found
  Test 18: not found
  Test 19: not found
  Test 20: not found

TOTAL SCORE: 5.00%
```

---

### #Q2: What is the average price of rooms in the Airbnb dataset?

The price of each room can be found in the `price` column. Your answer should be rounded down and returned as an integer.

### #Q3: How many rooms are in the neighborhood of Inwood?

You can find the value Inwood in the `neighborhood` column.

---

### `find_room_names` function:

We require you to complete the below function to answer the next several questions (this is a requirement, and you will **lose points** if you do not implement this function):

```python
def find_room_names(phrase):
    """
    Returns a list of all the room names that contain the substring (case insensitive match)
    passed as an argument to the paramenter `phrase`. 
    """
    pass
    # TODO: create a list
    # TODO: Ignore rooms that do not have data entry for name, as indicated by a value of None.
    # TODO: check if the room name string contains phrase (case insensitive match)
    # TODO: if so, add these room names to the list (the room names should not be modified)
    # TODO: return your list of room names
```

### #Q4: Find all room names that contains string "CBG".

Your answer should be in the form of a Python list. You should use the `find_room_names` function to answer this question.

### #Q5: Find all room names that contain both "kitchen" and "bathroom".

You should use the `find_room_names` function to answer this question. Your answer should be in the form of a Python list. If the room name has a word which contains "bathroom", such as "bathroombath", include it in your answer.

---

### #Q6: Which host names are anagrams of the word "aisle"?

For reference, an anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all of the original letters exactly once. (Read more here: https://en.wikipedia.org/wiki/Anagram). An example of this would be the words "listen" and "silent".

**Note:** Your output should be in the form of a Python list. The order doesn't matter but make sure that your answer doesn't contain duplicate entries.

**Important:** Ignore room ids that do not have data entry for `host_name`, as indicated by a value of `None`.  

**Clarification:** We expect matches to be case-insensitive.

**Hint:** Checking whether a single word is an anagram of another word does not require writing a loop. So if you're writing something complicated, review task 3.3 in lab-p6.

---

### #Q7: List all room ids that received more than 400 reviews in the Brooklyn neighborhood group.

**Note:** Your answer should be in the form of a Python list of strings.

**Important:** Ignore room ids that do not have data entry for `number_of_reviews`, as indicated by a value of `None`.

### #Q8: What percentage of rooms in Manhattan neighborhood group are of shared type ("Shared room")?

**Note:** Your answer should be a float value between 0 and 100.

### #Q9: Which shared room ids in Queens neighborhood group received their last review in the year 2016 or earlier?

**Note:** Your answer should be in the form of a Python list of strings.  

**Warning:** If you open the csv in Excel, Excel will try to convert the dates to the MM/DD/YYYY format instead of the expected YYYY-MM-DD format. Do *not* save the csv if you open it in Excel. You must use the YYYY-MM-DD format for this question.

**Important:** Ignore room ids that do not have an entry for `last_review`, as indicated by a value of `None`.

---

### `availability_per_host_name` function:

We require you to complete the below function to answer the next several questions (this is a requirement, and you will **lose points** if you do not implement this function):

```python
def availability_per_host_name(search_host_name, search_neighborhood = None):
    """
    Returns a list of availabilities (availability_365) for the rooms with the 
    specified host_name (case insensitive match) and within the specified neighborhood. 
    If search_neighborhood is None, returns a list of availabilities for all rooms with 
    the specified host_name (case insensitive match).
    """
    pass
    # TODO: create a list
    # TODO: Ignore rooms for which `availability_365` or `host_name` data is missing, as indicated by a value of `None`.
    # TODO: add every availability matching the host_name (cast insensitive match) and neighborhood to the list as an int. If search_neighborhood is None you should consider rooms within every neighborhood.
    # TODO: return your list of availabilities
```

### #Q10: What are the different availabilities of all rooms in the neighborhood "Long Island City" whose host name is "Leo"?

**Note:** Your answer should be a *descending ordered* list.

**Important:** You should use the `availability_per_host_name` function to answer this question.

### #Q11: What is the difference between the most and least availability among all rooms whose host name is "Pauline"?

**Note:** Your answer should be in the form of an integer.

**Important:** You should use the `availability_per_host_name` function to answer this question.

---

### `find_prices_within` function:

We require you to complete the below function to answer the next several questions (this is a requirement, and you will **lose points** if you do not implement this function):  

```python
def find_prices_within(lat_min, lat_max, long_min, long_max):
    """
    Returns a list of prices of all the rooms within the geographical location between and including
    the latitudes lat_min and lat_max and longitudes long_min and long_max.
    """
    pass
    # TODO: create a list
    # Ignore rooms that do not have data entry for `price`, as indicated by a value of `None`.
    # TODO: if the room is in this region, add the price to the list
    # TODO: return the list of prices
```

### #Q12: What is the lowest price room near NYU (40.729 <= latitude <= 40.73, -74.01 <= longitude <= -74.00)??

**Note:** Your answer should be an integer.

**Important:** Use the `find_prices_within` function, then find the minimum. 

### #Q13: What is the median price of the rooms near Columbia University (40.79 <= latitude <= 40.80, -73.96 <= longitude <= -73.95)?

**Note:** Your answer should be an integer.

**Important:** You must copy/paste your median function definition from lab (task 3.4). Otherwise you'll lose points.

**Important:** Use the `find_prices_within` and `median` functions.

### #Q14: What percentage of rooms near Rockerfeller Center (40.749 <= latitude <= 40.75, -73.98 <= longitude <= -73.97) have a price more than $100?

**Note:** Your answer should be a float value between 0 and 100.

**Important:** Use the `find_prices_within` function. 

---

**Hint:** To answer Q15, Q16, and Q17, define a function that takes a neighborhood as argument and computes the average ratio of number of reviews to availability. You will **not** lose points if you do not implement a function here, but it is highly recommended that you do so.

### #Q15: What is the average ratio of the number of reviews to availability in the neighborhood Arrochar?

**Important:** You should ignore rooms that have `availability_365` data of 0. You should also ignore rooms for which the ratio cannot be computed due to missing data.

**Hints:**
1. The denominator is the availability of a room (`availability_365` column).
   The numerator is the number of reviews of a room (`number_of_reviews` column).
2. Be careful! You need to compute the ratio for each room in the given neighborhood, then take the average of those ratios. Simply dividing the sum of reviews by the sum of availability will calculate the wrong answer.
### #Q16: What is the average ratio of the number of reviews to availability in the neighborhood Tompkinsville?

### #Q17: Which neighborhood in the neighborhood group Brooklyn has the highest average ratio of the number of reviews to availability?

**Hints:** 
1. First make a list of all the *unique* neighborhoods in Brooklyn.
2. Then find which of these neighborhoods has the highest average ratio. If you wrote a function for Q15 and Q16 that will be helpful here.
3. If the program is taking too long to execute, make sure you are not running the logic on duplicate neighborhoods. 

**Clarification:** The runtime of this cell is expected to be around 5 seconds. Don't worry about this.

---

### `secondary_word_in_found_rooms` function:

We require you to complete the `secondary_word_in_found_rooms` function to answer the next two questions (this is a requirement, and you will **lose points** if you do not implement this function),

`secondary_word_in_found_rooms` function definition must invoke find_room_names. **We'll manually deduct points** if you don't use `find_room_names`.

```python
def secondary_word_in_found_rooms(find_room_word, secondary_word):
    """
    Returns the percentage of names containing one word find_room_word (case insensitive match)
    that also contains another word secondary_word (case insensitive match).
    Return value is between 0 and 100.
    """    
    # Hint: The denominator is the number of rooms with find_room_word in their name. 
    #       The numerator is the number of rooms that have both find_room_word and secondary_word in their name.
    pass
```

### #Q18: What percentage of rooms whose names contain the word "quiet" also contain the word "clean"?

**Note:** Your answer should be a float value between 0 and 100. You are expected to use the function `secondary_word_in_found_rooms` here.

### #Q19: What percentage of rooms whose names contain the word "sunny" also contain the word "beautiful"?

**Note:** Your answer should be a float value between 0 and 100. You are expected to use the function `secondary_word_in_found_rooms` here.

---
### #Q20: What is the minimum amount of money one needs to spend to stay for 3 days in Queens, and then 4 days in Brooklyn?

Your answer should be in the form of an int. You may assume that you will stay in exactly one room per `neighborhood_group` throughout this trip. You should ignore rooms with missing `availability_365` or `minimum_nights` data. You don't have to worry about the exact dates of the availability. You may assume that if the room is available for the required number of days, it will be available whenever you want it.

**Hints:** 

1. Note that you need to check the `availability_365` as well as the `minimum_nights` of the rooms. You can only stay in a room for 5 days if `availability_365 >= 5` and `minimum_nights <= 5`.
2. total cost = (lowest price in Queens) * 3 + (lowest price in Brooklyn) * 4
3. Consider defining a function to compute lowest price given a neighborhood group with appropriate parameters.

---

------------------------------

## IMPORTANT: Submission instructions
- Review [Grading Rubric](https://github.com/msyamkumar/cs220-s22-projects/blob/main/p6/rubric.md), to ensure that you don't lose points during code review.
- Please remember to **`Kernel->Restart and Run All`** to check for errors, save your notebook, then run the **`test.py`** script one more time before submitting the project.
    - To keep your code concise, please remove your own testing code that does not influence the correctness of answers.
    - __If you are unable to solve a question and have partial code that is causing an error__ when running test.py, please __comment out the lines in the cell for that question.__ Failing to do so will cause the auto-grader to fail when you submit your file and give you 0 points even if you have some questions correctly answered.
    - Make sure that all the fields in the header cell are correctly populated, including **submitter** and **partner**.
    - Make sure that you have #q1, #q2, etc., as comments in the cells that answer each of the 20 questions.
- Follow the same steps as prior projects to turn in main.ipynb to the course website. If required, review those steps.
- It is **your responsibility to make sure that your project clears auto-grader tests on our testing system**.
	- Approximately 4 hours after you submit your program, auto-grader test results will become available. Make sure to use **View Submissions** to check the auto-grader test results.

------------------------------
