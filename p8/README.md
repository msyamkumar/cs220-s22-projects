# Project 8: Going to the Movies

## Clarifications/Corrections

**Find any issues?** Report to us:
- Rheeya Uppaal [uppaal@wisc.edu](mailto:uppaal@wisc.edu)
- Isha Padmanaban [ipadmanaban@wisc.edu](mailto:ipadmanaban@wisc.edu)
- Dakota Sullivan [dsullivan8@wisc.edu](mailto:dsullivan8@wisc.edu)

## Learning Objectives

In this project, you will demonstrate how to:
- Integrate relevant information from various sources (e.g. multiple csv files)  
- Build appropriate data structures for organized and informative presentation (e.g. list of dictionaries)
- Practice good coding style

## Coding Style Requirements

Remember that coding style matters! **We may deduct points for bad coding style.** In addition to the [requirements from p7](https://github.com/msyamkumar/cs220-s22-projects/tree/main/p7#coding-style-requirements), here are several other common bad coding habits to avoid:

- Do not use meaningless names for variables or functions (e.g. `abc = 'Titanic'`. Instead use something like `movie_name = 'Titanic'`).
- Do not write the same code in multiple places. Instead, wrap this code into a function and call that function whenever the code should be used.
- Avoid calling slow functions multiple times within a loop.
- Avoid calling functions that iterate over the entire dataset within a loop; instead, call the function before the loop and store the result in a variable.

## Introduction

In this project and the next, we will be working on the [IMDb Movies Dataset](https://www.imdb.com/interfaces/). We will use Python to discover some cool facts about our favorite movies, actors, and directors.

In this project, you will combine the data from the movie and mapping files into a more useful format. As usual, hand in the `main.ipynb` file (use the `#qN` format).  
Start by downloading the following files: `test.py`, `small_mapping.csv`, `small_movies.csv`, `small_movies_altered.csv`, `mapping.csv`, and `movies.csv`.

**Please go through the [Lab-P8](https://github.com/msyamkumar/cs220-s22-projects/tree/main/lab-p8) before working on this project.** The lab will introduce some useful techniques related to this project.

## The Data

Open `movies.csv` and `mapping.csv` in any spreadsheet viewer, and see what the data looks like.
`movies.csv` has ~33,000 rows and `mapping.csv` has ~84,000 rows. These datasets are very large when compared to `small_movies.csv` and `small_mapping.csv` from [Lab-P8](https://github.com/msyamkumar/cs220-s22-projects/tree/main/lab-p8). For description of the dataset columns, please refer back to [Lab-P8](https://github.com/msyamkumar/cs220-s22-projects/tree/main/lab-p8).

Before we start working with these very large datasets, let us start with some much smaller datasets (`small_movies.csv` and `small_mapping.csv`). In the next project (P9), you will mainly be working with `movies.csv` and `mapping.csv`.

When seen with a good spreadsheet viewer, this is what some of `movies.csv` wil look like:

| title | year            | genres                      | duration | directors                                                           | actors                                       | rating |
| ----  |-----------------|-----------------------------|----------|---------------------------------------------------------------------|----------------------------------------------|--------|
| tt1735898 | 2012  |  "Action, Adventure, Drama" | 127  | nm2782185                                                           | "nm0829576, nm1165110, nm0000234, nm3510471" | 6.1 |
| tt1210166 | 2011  | "Biography, Drama, Sport"   | 133  | nm0587955                                                           | "nm0000093, nm1706767, nm0000450, nm0000705" | 7.6|
| tt0058079 | 1964 | "Horror"                    | 60    | "nm0554924, nm0692414" | "nm0001033, nm0067280, nm0593360, nm0388885" | 3.0 |

However, if you open the raw version of `movies.csv`, you are more likely to see something like this. It's the same data, but is sometimes a little harder to read:
```
title,year,genres,duration,directors,actors,rating
tt1735898,2012,"Action, Adventure, Drama",127,nm2782185,"nm0829576, nm1165110, nm0000234, nm3510471",6.1
tt1210166,2011,"Biography, Drama, Sport",133,nm0587955,"nm0000093, nm1706767, nm0000450, nm0000705",7.6
tt0058079,1964,Horror,60,"nm0554924, nm0692414","nm0001033, nm0067280, nm0593360, nm0388885",3.0
```

# Data Plumbing
A lot of data-science work often involves *plumbing*, the process of
getting messy data into a more useful format.  We have already dealt with
it in passing in lab-p7. Data plumbing is the focus of this project.
We'll develop and test some functions that will be very
helpful in p9:

1. `get_mapping(path)`: this loads a mapping file that can be used to lookup names from IDs
2. `get_raw_movies(path)`: this loads movie data with info represented using IDs
3. `get_movies(movies_path, mapping_path)`: this uses the other two functions to load movie data, then replace the IDs with names

Note - the variable `path` is of type string

---

## Let's Start!

**Important Warnings:**
- **Do not use the method `csv.DictReader` for p8**. Although the required output can be obtained using this method, one of the learning outcomes of this project is to demonstrate your ability to build dictionaries with your own code.  
- Additional import statements beyond those that are stated in the directions are not allowed. For this project, we allow you to use `csv` and `copy` packages (that is, you can use the `import csv` and `import copy` statements in your submission). All import statements should be in the second cell.
- Do **not** hardcode the column indices anywhere in your code. You will **lose points** during code review if you do so. Instead, use `.index()` as you did in P6.
- You should not use concepts / modules that are yet to be covered in this course; for example: you should not use modules like pandas. **We'll manually deduct points** accordingly, if you don't follow the provided directions.

The first cell should contain only contain information like this:
```python
# project: p8
# submitter: NETID1
# partner: NETID2
# hours: ????
```
Make sure to copy/paste the necessary code from the lab.

---

**Requirement:** Write the below function:

```python
def get_mapping(path):
    """
    Converts mapping csv list of lists data into a dict with keys as IDs and values as names.
    """
    # Task 2.2 of Lab-P8 has all the necessary steps to complete this function.
    # You just need to copy/paste the relevant code, identify the input and output of the function.
```

### #Q1: What is returned by `get_mapping("small_mapping.csv")`?

**Requirements:**
- Store the result in a variable for use in subsequent questions
    - Why do we want to store the result in a variable? This can help you avoid calling this time-consuming function in the future.
- **IMPORTANT**: Use the **relative path** as shown in the question. Do not change the argument. Using any other path will lead to **auto-grader failure.**

### #Q2: What is the value associated with the key "nm6525901"?

**Requirement:** Use the dictionary you saved in a variable in Q1.  

### #Q3: What are the values associated with keys that begin with "nm"?

**Requirements:**
- Use the dictionary you saved in a variable in Q1.  
- The answer should be a Python list. The order does not matter.

Hint: Refer back to String methods / sequence operations, if you don't remember those.

### #Q4: Find the keys of the people (keys beginning with "nm") whose last name is "Henson".

**Requirements**:
- Define the below function.
- Use the variable you saved your Q1 answer to answer this question.
- Your code should only consider the keys that begin with "nm".
- Only return names that *end* with the target last name

```python
def get_key_from_last_name(target_lastname):
    """
    Returns a list of keys (ids) of people that have the specified last name (case insensitive match) in your small mapping.
    Your code must only consider the keys that begin with "nm".
    """
    pass

# These are tests. They will do nothing if your implementation is correct.
# If your implementation is wrong, they will throw an AssertionError.
assert get_key_from_last_name('Spencer') == ['nm0818055']
assert get_key_from_last_name('Chan') == ['nm2110418']    
```

We've given you 2 extra tests in the starter code above. After you've finished your implementation of `get_key_from_last_name`, run them. If running this code gives you something called an `AssertionError`, there is an error your solution. You must ensure that the tests run without an `AssertionError`. You'll learn more about `assert` statements soon. For now, all you need to know is that they show an error if you fail our test.

---

Now, let's move on to reading movie files!

**Requirements**:
- Write the below function.
- Ensure you do not hardcode the indices of any columns in the data.

```python
def get_raw_movies(path):
    """
    Converts movies csv list of lists data into a dict with keys as column names and values as corresponding type converted values.
    """
    # Task 2.1 and 2.3c of Lab-P8 have all the necessary steps to complete this function.
    # You just need to copy/paste the relevant code, identify the input and output of the function.
    pass
```
---

### #Q5: What does `get_raw_movies("small_movies.csv")` return?

Refer back to Lab-P8 task 2.3c, for the expected output.

If your answer looks correct, but does not pass `test.py`, make sure that the datatypes are all correct. Also make sure that the actors and directors are in the same order, as here.

**Requirements**:
- Store the answer to Q5 in a variable and use it for Q6 and Q7.
- **Do not** call `get_raw_movies` every time you need data from the movies file. This will lead to auto-grader failure.

To test for column hardcoding, the copy the following code into your notebook and ensure you do not get an error.
```python
assert get_raw_movies("small_movies_altered.csv") == get_raw_movies("small_movies.csv")
```

### #Q6: How many actors does the movie at index 0 have?

**Requirement:** Use the dictionary from Q5.

### #Q7: What is the ID of the first actor listed for the first movie of the dataset?

**Requirement:** Use the dictionary from Q5.

---

You may have noticed that `title`, `directors`, and `actors` are represented by IDs
rather than actual names. To make our data more intuitive, we next need to write a
function that will convert these IDs to names.

**Requirements**:
- Create the below function.
- You must use `get_raw_movies` to load the movie data file.
- You must use `get_mapping` to load the mapping file.

You should begin by copying the outline below:

```python
def get_movies(movies_path, mapping_path):
    """
    Creates a new movies list of dict data by using the mapping dictionary,
    to convert IDs into actual names for title, actors, and directors.
    """
    # Task 3.2 of Lab-P8 has all the necessary steps to complete this function.
    # You just need to copy/paste the relevant code, identify the input and output of the function.
    pass

```

**Requirement:** After you implement your function, call it and store the result as a variable named
`small_movies_data`.

### #Q8: What is `small_movies_data`?

Refer back to Lab-P8 task 3.2, for the expected output.

### #Q9: What is title of the second movie in `small_movies_data`?

### #Q10: Who are all the actors of the first movie in `small_movies_data`?

### #Q11: Who are all the directors of the last movie in `small_movies_data`?

---

Now that you’ve made it this far, your functions must be working pretty well with small
datasets. Next, let's try a much bigger dataset!

**Requirement:** Run the following code to
open the full dataset.

```python
movies = get_movies("movies.csv", "mapping.csv")
```

**Warning**: You are **not** allowed to call `get_movies` more than once for the
`"movies.csv"` file in your notebook. Instead, reuse the `movies` variable, which
is more efficient. Failure to follow this instruction will result in deduction of points.

---

### #Q12: What is the length of `movies`?

### #Q13: What are the contents of the last 2 rows in `movies`?

Your answer should be a list of dictionaries that follows the format below:

```python
[{'title': 'Battle Bots',
  'year': 2018,
  'genres': ['Action', 'Adventure', 'Sci-Fi'],
  'duration': 67,
  'directors': ['Mark Polonia'],
  'actors': ['Danielle Donahue', 'Jeff Kirkendall', 'Marie DeLorenzo'],
  'rating': 1.9},
 {'title': 'Inescapable',
  'year': 2003,
  'genres': ['Drama'],
  'duration': 82,
  'directors': ['Helen Lesnick'],
  'actors': ['Natalie Anderson', 'Tanna Frederick', 'Athena Demos'],
  'rating': 4.2}]
```

---

Now that we have created this data structure `movies`, we can start doing some fun things with the data!
We will continue working on this data structure for the next project (P9) as well.

Let us now use this data structure `movies` to create a search bar like the one in Netflix!
For now, copy the following function to your notebook, **but don't change it in any way**.
This function takes in keywords like a substring of a title, a genre, or the name of a person,
and returns a list of relevant movies with that title, genre, or actor/director.

**Requirement:** Copy and paste this function into your notebook, but do *not* change it.

```python
def find_specific_movies(movies, keyword):
    """
    Given a list of movie dictionaries and a keyword, returns a list of movies that contain the keyword
    in either its title, genre, actors or directors.
    """
    idx = 0
    while idx < len(movies):
        movie = movies[idx]
        # Note: \ enables you split a long line of code into two lines
        if (keyword not in movie['title']) and (keyword not in movie["genres"]) \
        and (keyword not in movie["directors"]) and (keyword not in movie["actors"]):
            movies.pop(idx)
        else:
            idx += 1
    return movies
```

**Warning:** Do **not** call `get_movies` on "movies.csv" more than once in your notebook.

------

### #Q14: List all the movies in the dataset that Greta Gerwig has directed.
Your answer will be a list of dictionaries.

If you try to call `find_specific_movies` with `movies` as an argument, you will see that many entries get deleted. Take a look at the definition of `find_specific_movies` function. Are you able to spot the line of code that changes the `movies` data structure?

This is undesirable, as we need to retain the original data structure. Review the copy functions in the `copy` module and use it to prevent `movies` from being modified.

**Requirements:**
- Use `find_specific_movies` to answer this question.
- Do not change `find_specific_movies`
- Use the `copy` module to pass a copy of `movies` to `find_specific_movies`
- Only include movies where Greta is an actor


**Hint:** `find_specific_movies` returns the movies that are directed or acted by "Greta Gerwig". Make sure to use appropriate loop structures (for/while loop) to retrieve only the movies that are *directed* by "Greta Gerwig".

### #Q15: Which genres of movies did Leonardo DiCaprio ever appear in?

Your answer should be a list of unique strings. Note that we are not specifying whether Leonardo should appear as an actor or director.

**Requirement:** You must use `find_specific_movies` but ensure that `movies` does not get modified.  

---

The function `find_specific_movies` was a good start, but the function has some limitations. For one, it has to
loop through the entire dataset each time it is called, so it is a little slow. But since there are so few genres to deal with, we can optimize our code by bucketizing our movies by genre. This means creating a dictionary where the keys are genres and the values are lists of movies (dictionaries) and storing it in a variable. Then we can simply look up genres in this variable instead of calling `find_specific_movies` each time.


**Requirements:**
- Write the function `bucketize_by_genre` as specified.
	- If a movie falls under multiple genres, it must appear under *all* of these genres in the dictionary.
- You should first call `bucketize_by_genre` on `movies` and store the result in a variable.
- Use this variable for Q16, Q17 and Q18.
- Do *not* call `bucketize_by_genre` on the **same list of movies** more than once.

This function should return a dictionary that maps each genre to a list of all movies with that genre. For instance:
```python
{'Action':
    [{'title': 'They Live',
      'year': 1988,
      'genres': ['Action', 'Horror', 'Sci-Fi'],
      'duration': 94,
      'directors': ['John Carpenter'],
      'actors': ['Roddy Piper', 'Keith David', 'Meg Foster'],
      'rating': 7.3},
   ...],
'Romance': [...list of romance movies],
'Horror': [...list of horror movies],
...
}
```

If you find it challenging to write this function, you can start with the following code snippet:
```python
def bucketize_by_genre(movies):
    """Given a list of movie dictionaries,
    returns a dict in which the key is the genre and
    the value is a list of all movies that contain that genre"""
    #TODO: initialize a dictionary
    #TODO: loop through all movies
    #TODO: loop through all genres in this movie
    #TODO: if this genre is not a key in our dictionary, set the value associated with this genre to an empty list
    #TODO: if we already have this genre in our dictionary, add the movie to the list associated with this genre
```

You can create similar functions for actors and directors as well. You will deal more with such functions
in p9. *Can you figure out why it is **not** a good idea to create a similar function for **substrings** of the title*?

**IMPORTANT WARNING**: do not display the output of `bucketize_by_genre` function. Just store it into a variable and use that for Q16, Q17 and Q18.

### #Q16: List the unique genres present in the `movies` dataset.

Your answer should be a list.

### #Q17: How many Comedy movies do we have in the `movies` dataset?

### #Q18: What is the title of the Drama movie has the highest rating in the `movies` dataset?

### #Q19: List all the genres of movies that Daniel Radcliffe has ever acted in.

*Note:* Daniel Radcliffe has never directed any movies, so you can assume that if his name is mentioned in a movie, he acted in it.

**Requirements**:
- Use `bucketize_by_genre` and `find_specific_movies`
- Answer this question **without any new control structures (loops, if statements)** or you will lose points

**Hint:** You will *not* use the variable you created for Q16-18.

Note that this question is nearly identical to Q15, but quicker to answer because of our bucketizing function.

### #Q20: Which movie genre does the actress Jennifer Aniston play the least?

Your answer should be a string. This code will need control structures (loops, if statements) that finds a minimum.

*Note:* Jennifer Aniston has never directed any movies, so you can assume that if her name is mentioned in a movie, she acted in it.

**Requirements**:
- Use `bucketize_by_genre` and `find_specific_movies`
- To break ties (multiple genres with the same least number of movies), you must consider the last one in the data set.

<!---
**Warning:** Since `small_movies` is
a small dataset, you might have gotten the correct answer without the correct code. In that case, you will lose points during code review.
You can check to see if your code is correct
by running that code in a separate cell on the larger `mapping.csv` dataset. If your code is correct, the answer will not change.
--->

---

## IMPORTANT: Submission instructions
- Review [Grading Rubric](https://github.com/msyamkumar/cs220-s22-projects/blob/main/p8/rubric.md), to ensure that you don't lose points during code review.
- To keep your code concise, **remove your own testing code that does not influence the correctness of answers.** In particular, **remove any code that displays large lists such as `movies`**.
- Please remember to **`Kernel->Restart and Run All`** to check for errors, save your notebook, then run the **`test.py`** script one more time before submitting the project.
    - If you are unable to solve a question and have partial code that is __causing an error__ when running test.py, please __comment out the lines__ in the cell for that question. Failing to do so will cause the auto-grader to fail when you submit your file and give you 0 points even if you have some questions correctly answered.
    - Make sure that all the fields in the header cell are correctly populated, including **submitter** and **partner**.
    - Make sure that you have #q1, #q2, etc., as comments in the cells that answer each of the 20 questions.
- Follow the same steps as prior projects to turn in main.ipynb to the course website. If required, review those steps.
- It is **your responsibility to make sure that your project clears auto-grader tests on our testing system**.
  - Approximately 4 hours after you submit your program, auto-grader test results will become available. Make sure to use **View Submissions** to check the auto-grader test results.
  - We will __not__ accept submissions more than 7 days after the deadline, even for auto-grader errors. A failed auto-grader means a 0.


---
