# Project 3: Renewable energy consumption by the US Electric Power Sector

**Find any issues?** Report to us:

- Rheeya Uppaal <uppaal@wisc.edu>
- Isha Padmanaban <ipadmanaban@wisc.edu>
- Dakota Sullivan <dsullivan8@wisc.edu>

## Learning Objectives

This project measures your ability to:
- Import a module and use its functions
- Write functions
- Use default arguments when calling functions
- Avoid hardcoding
- Work with the index of a row of data

**Please go through [lab-p3](https://github.com/msyamkumar/cs220-s22-projects/tree/main/lab-p3) before working on this project.** The lab introduces some useful techniques necessary for this project.

## Description

In this project, you'll analyze data of about five different renewable energy sources consumed by the US commercial power industry between 2015 and 2020. In other words, this is the amount of renewable energy that was used to generate electricity that was sold to consumers. The dataset we will analyze is truncated and modified from [here](https://www.eia.gov/totalenergy/data/browser/xls.php?tbl=T10.02C&freq=m) published by [U.S. Energy Information Administration](https://www.eia.gov/totalenergy/data/monthly/index.php).

You'll get practice calling functions from the `project` module, which we've provided, and practice writing your own functions.

Start by downloading `project.py`, `test.py`, `questions.py` and `energy.csv`. Double check that these files don't get renamed by your browser (by running `ls` in the terminal from your `p3` project directory). 

You'll do all your work in a new `main.ipynb` notebook that you'll create also in `p3` project directory and hand in when you're done (please do not write your functions in a separate file). You'll test as usual by running `python test.py` (or similar, depending on your laptop setup). 
Note: If you do not recall how to create a new notebook file, please follow the steps in Segment 4 Task 4.1 in [lab-p1](https://github.com/msyamkumar/cs220-s22-projects/tree/main/lab-p1).

The first cell should contain and only contain information like this:
```python
# project: p3
# submitter: NETID1
# partner: NETID2
# hours: ????
```

We won't explain how to use the `project` module here (the code is in the `project.py` file).  Refer to [lab-p3](https://github.com/msyamkumar/cs220-s22-projects/tree/main/lab-p3) to understand how inspection process works and use `help` function to learn about various functions inside `project.py`. Feel free to take a look at the `project.py` code, if you are curious about how it works.

To get you started, here's what the beginning of your new `main.ipynb` should look like:

![Image of main.ipynb with import](images/import.jpg)

This project consists of writing code to answer 20 questions.  **If you're answering a particular question in a cell in your notebook, you need to put a comment in the cell so we know what you're answering.** For example, if you're answering question 13, the first line of your cell should contain `#q13` (or `#Q13`). We encourage you to copy the actual question as well, like this: 

`#Q1: What is the index of Solar Energy?`

## Dataset

The data looks like this:

index|energy type|2015|2016|2017|2018|2019|2020
------|------|------|------|------|------|------|------|
1|Conventional Hydroelectric Power|2307.717|2458.721|2752.024|2650.608|2552.636|2581.291
3|Solar Energy|227.901|327.712|485.742|575.854|634.613|802.317
4|Wind Energy|1775.705|2093.728|2340.784|2479.897|2632.354|2998.142
5|Wood Energy|243.857|224.407|229.324|221.063|200.524|185.145
7|Biomass Energy|524.879|505.069|509.541|496.085|448.137|423.513

This table lists 5 different renewable energy sources, and the amount of energy from each of these sources that was consumed by the US commercial power industry in each of the years between 2015 and 2020. The units used here are trillions of Btu (British thermal units).

The dataset is in the `energy.csv` file which you downloaded. Alternatively, you can open `energy.csv` file, to look at the same data and to verify answers to simple questions.

## Requirements

You **may not** hardcode indices in your code. For example, if we ask how much Wood Energy was consumed in 2020, you could obtain the answer with this code: `get_consumption(get_idx("Wood Energy"), 2020)`.  If you don't use `get_idx` and instead use `get_consumption(5, 2020)`, we'll **manually deduct** points from your `test.py` score during code review.

For some of the questions, we'll ask you to write (then use) a function to compute the answer.  If you compute the answer **without** creating the function we ask you to write, we'll **manually deduct** points from your `test.py` score when recording your final grade, even if the way you did it produced the correct answer.

## Incremental Coding and Testing
You should always strive to do incremental coding. Incremental coding enables you to avoid challenging bugs. Always write a few lines of code and then test those lines of code, before proceeding to write further code. You can use `print` function call for testing intermediate step outputs. Once you are done with your verification, make sure to remove the `print` function calls. **You should never use `print` function call to print answer to a question.** This is because `test.py` does not recognize `print` function call output. You should only display the output. That is, you can specify a variable name or directly display a function call's output.

We also recommend you to do incremental testing: solve a question and run auto-grader script `test.py`, to verify that you get a PASS for that particular question, before proceeding to the next.

## Questions and Functions


### #Q1: What is the index of Solar Energy?


### #Q2: How much of the Wood Energy was consumed by the US electric power sector in 2020?

Your answer should just be a number (without any units at the end). You **should not** hardcode the ID of "Wood Energy". You must call the appropriate function to determine the ID.

---

### #Q3: How much Conventional Hydroelectric Power was consumed by the US electric power sector in 2015?

Hint: instead of repeatedly calling `project.get_idx("Solar Energy")` (or similar) for each question, you may wish to make these calls once at the beginning of your notebook and save the results in variables, something like this:

```python
hydroelectric_idx = project.get_idx("Conventional Hydroelectric Power")
solar_idx = project.get_idx("Solar Energy")
...
```

---

### Function 1: `year_max(year)`

This function will compute the maximum amount of energy consumed by the US electric power sector from a single renewable energy source in the given year. Copy and paste it directly into your notebook.  

```python
def year_max(year):
    # grab the consumption of each energy source in the given year
    hydroelectric_consumption = project.get_consumption(project.get_idx("Conventional Hydroelectric Power"), year)
    solar_consumption = project.get_consumption(project.get_idx("Solar Energy"), year)
    wind_consumption = project.get_consumption(project.get_idx("Wind Energy"), year)
    wood_consumption = project.get_consumption(project.get_idx("Wood Energy"), year)    
    biomass_consumption = project.get_consumption(project.get_idx("Biomass Energy"), year)

    # use built-in max function to get the maximum of the five values
    return max(hydroelectric_consumption, solar_consumption, wind_consumption, wood_consumption, biomass_consumption)
```

### #Q4: In 2017, what was the largest amount of energy consumed by the US electric power sector from a single renewable energy source?

Use `year_max` to answer this.

### #Q5: What was the the largest amount of energy consumed by the US electric power sector from a single renewable energy source between 2015 and 2020?
Use year_max to answer this. The bounds here are inclusive. Meaning you should consider the years 2015 and 2020 for your calculation.

Hint: Recall that we can use `max()` function to compute maximum of some values. Look at the lab examples where you used `max()` function.

---

### Function 2: `energy_min(source)`

We'll help you start this one, but you need to fill in the rest yourself.

```python
def energy_min(source):
    source_idx = project.get_idx(source)    
    y15 = project.get_consumption(source_idx, 2015)
    y16 = project.get_consumption(source_idx, 2016)
    # grab the consumptions from other years

    # use the min function (similar to the max function)
    # to get the minimum across the six years
    # and return that value
```

This function should compute the minimum energy consumed by the US electric power sector from the given renewable energy source, considering consumption in all six years.

### #Q6: What was the minimum amount of Solar Energy consumed by the US electric power sector in a single year?

Use your `energy_min` function.

### #Q7: What was the minimum amount of Wind Energy consumed by the US electric power sector in a single year?

Use your `energy_min` function.

---

### Function 3: `energy_avg(energy_source)`

This function should compute the average energy consumed by the US electric power sector from the given energy source across the six years in the dataset.

Hint: start by copy/pasting `energy_min` and renaming your copy to `energy_avg`.  Instead of computing the minimum of `y15`, `y16`, etc., compute the average of these by adding them together, then dividing by six. **You may hardcode 6 for the purpose of this average computation**.

### #Q8: How much Biomass Energy was consumed by the US electric power sector on average between 2015 and 2020?

Use your `energy_avg` function.

### #Q9: How much Conventional Hydroelectric Power was consumed by the US electric power sector on average between 2015 and 2020?

Use your `energy_avg` function.

### #Q10: Relative to its 6 year average, how much more Wind Energy was consumed by the US electric power sector in 2019?

Use your `energy_avg` function. We want you to calculate 2019 consumption as a proportion of the average, and report a percentage between 0 and 100, with no percent sign.  

For example, if the average was 10, and a certain year consumption was 13, the answer is 30. You do not need to round your answer. 

---

### Function 4: `year_sum(year)`

This function should compute the total renewable energy consumption of the US electric power sector (over the five sources) in a given year.

You can start from the following code:

```python
def year_sum(year = 2015):
     pass # TODO: replace this line with your code
```

### #Q11: How much renewable energy was consumed by the US electric power sector in 2015?

Use the default argument (your call to `year_sum` should not pass any argument). **If you do not use default arguments, you will lose points.**

### #Q12: How much renewable energy was consumed by the US electric power sector in 2019?

---

### Function 5: `change_per_year(energy, start_year, end_year)`

It is clear from looking at the dataset that the consumption of some renewable energy sources (like Solar Energy) by the US electric power sector is trending upwards, while some (like Wood Energy) are trending downwards. It would be interesting to find the *average* increase/decrease in energy consumption per year, for these energy sources.

This function should return the average increase/decrease in consumption (could be positive if there's an increase, negative if there???s a decrease) over the period from start_year to end_year for the given energy source (example energy source: "Solar Energy").

You can start with the following code snippet:

```python
def change_per_year(energy, start_year = 2015, end_year = 2020):
     pass # TODO: replace this line with your code
```

We're not asking you to do anything complicated here; you just need to compute the difference in consumption between the last year and the first year, then divide by the number of elapsed years. Recall that you created a similar function in the lab.


### #Q13: How much has the consumption of Wood Energy by the US electric power sector changed per year (on average) from 2015 to 2020?

Use the default arguments (your call to `change_per_year` should only pass one argument explicitly). **If you do not use the default arguments and instead pass more than one argument explicitly, you will lose points.**

### #Q14: How much has the consumption of Wind Energy by the US electric power sector changed per year (on average) from 2017 to 2020?

Use the same function `change_per_year` to answer this. **As with Q13, if you explicitly pass more arguments than necessary, you will lose points.**

---

### Function 6: `find_threshold_year(energy, threshold)`

We saw from calling `change_per_year` that the consumption of some renewable energy sources by the US electric power sector is increasing rapidly. However, the consumption of some other renewable energy sources is also shrinking. It will be interesting to estimate when the consumption of these energy sources will reach certain thresholds.

Write a function named `find_threshold_year` to estimate the year when the consumption of a given energy source by the US electric power sector crosses a given threshold. Find the average change in consumption over the six years (using `change_per_year`), and assuming that the energy consumption keeps decreasing at the same rate, compute the year when this energy will become lower than the threshold.

**Note**: You may find that the year when the consumption crosses the threshold is not a whole number. For instance, you may find that the consumption of Biomass Energy by the US electric power sector goes below a threshold of 100 (trillion Btu) in 2038.42. Of course, a fractional number doesn't make much sense in this context, so in this case you need to round up the number to 2039.

In order to round up the numbers, you may use the function `math.ceil` from the `math` module. You can refer to the [official documentation](https://docs.python.org/3/library/math.html). You can also take a look at [this example](https://www.geeksforgeeks.org/python-math-ceil-function/). Before using the function, remember to import `math` module. 

You must import math module in the same cell (top of your notebook) where you imported project. If your import is somewhere else, **we'll manually deduct points**.
Go back to the input cell where you imported project and add the below import statement.

```python
import math
```

`find_threshold_year` function **must invoke** `change_per_year` function. **We'll manually deduct points** if you don't invoke `change_per_year`.

If you find it challenging to write this function, you can start with the following code snippet:

```python
def find_threshold_year(energy, threshold = 0):
    pass
     # TODO: compute the average change in consumption from 2015 to 2020
     # TODO: compute the difference between threshold and consumption in 2020
     # TODO: compute the number of years it will take from 2020 to reach threshold
     # TODO: add that number of years to 2020 to compute threshold year
     # TODO: use math.ceil() to round it up.
```

If you find any of this confusing, feel free to attend office hours, to discuss with a TA / peer mentor.

### #Q15: In which year is the consumption of Wood Energy by the US electric power sector estimated to reach 100 trillion Btu?

### #Q16: In which year is the consumption of Biomass Energy by the US electric power sector estimated to reach 200 trillion Btu?

### #Q17: In which year is the consumption of Biomass Energy by the US electric power sector estimated to be less than the consumption of Wood Energy in 2015?

Do **not** hardcode the consumption of Wood Energy to answer this. Hint: Q17 is very similar to Q15 and Q16, but you'll need an extra call to `get_consumption`.

---

### Function 7: `find_overtake_year(energy1, energy2)`

We previously saw that the consumption of some energy sources by the US electric power sector is growing. But we also saw that some energy sources are growing faster than others. Similarly, the consumption of some energy sources are shrinking much faster than others. Just like we estimated when some energy sources will shrink to zero, it will be interesting to estimate when some energy sources will overtake others in their consumption.

Write a function named `find_overtake_year` to estimate the year when the consumption of energy source `energy1` by the US power sector will exceed the consumption of energy source `energy2`. To do this, find the average change in consumption over the six years for both energy sources, and assume that this does not change for either energy source. Extrapolate from this data to estimate when `energy1` will overtake `energy2`.

Hint 1: You will need to use `math.ceil()` once again to get you answer rounded up.

Hint 2: Focus on the difference in energy consumption between the two energy sources, and just like `find_threshold_year`, estimate when this crosses the threshold 0.

`find_overtake_year` function **must invoke** `change_per_year` function. **We'll manually deduct points** if you don't invoke `change_per_year`.

You can start with the following code snippet:

```python
def find_overtake_year(energy1, energy2):
    pass
    # TODO: compute the average change in consumption for both energy sources from 2015 to 2020.
    # TODO: calculate the difference in change rate, aka the relative change rate
    # TODO: compute the intial difference between consumption of energy1 and energy2 in 2020.    
    # TODO: at the relative change rate you computed, how many years will it take for the gap to close?
    # TODO: take the absolute value of this number and add it to 2020 to get the overtake year
    # TODO: use math.ceil() to round it up.

```

### #Q18: In which year will the consumption of Solar Energy by the US electric power sector overtake Conventional Hydroelectric Power?
Use `find_overtake_year`. Save the answer to this question as a variable - you'll use it in Q19.

### #Q19: Estimate how much Solar Energy will be consumed in the year that you found in Q18.
Be sure to use the variable you defined in Q18! **Do not hardcode the answer.** We'll manually deduct points if you hardcode.  

Hint: We know the consumption of Solar Energy in 2020. We know the average change in consumption per year for Solar Energy. If we assume that the consumption changes the same amount each year between 2020 and the year you found in Q18, we can calculate the total change across that time interval. Then, we add that total change to the starting point (2020 consumption).  

### #Q20: What is the increase in the unit market share for Solar Energy from 2018 to 2019?
Your answer should be a percentage from 0.0 to 100.0. You can find the definition of unit market share [here](https://en.wikipedia.org/wiki/Market_share#Construction).

You will find one of the earlier functions you wrote useful for computing the market share. Look for it! You must invoke the appropriate prior function applicable for this calculation. **We'll manually deduct points** if you don't invoke the function you previously defined.

Hint: It may also help to do this problem on paper first - it involves some math.

------------------------------

## IMPORTANT: Submission instructions
- Review [Grading Rubric](https://github.com/msyamkumar/cs220-s22-projects/tree/main/p3/Rubric.MD), to ensure that you don't lose points during code review.
- Please remember to **`Kernel->Restart and Run All`** to check for errors, save your notebook, then run the **`test.py`** script one more time before submitting the project.
    - To keep your code concise, please remove your own testing code that does not influence the correctness of answers.
    - __If you are unable to solve a question and have partial code that is causing an error__ when running test.py, please __comment out the lines in the cell for that question.__ Failing to do so will cause the auto-grader to fail when you submit your file and give you 0 points even if you have some questions correctly answered.
    - Make sure that all the fields in the header cell are correctly populated, including **submitter** and **partner**.
    - Make sure that you have #q1, #q2, etc., as comments in the cells that answer each of the 20 questions.
- Follow the same steps as prior projects to turn in main.ipynb to the course website. If required, review those steps.
- It is your responsibility to make sure that your project clears auto-grader tests on our testing system. 
	- Approximately 4 hours after you submit your program, auto-grader test results will become available. Make sure to use **View Submissions** to check the auto-grader test results.

------------------------------
