# Student Rubric for P5

## General deductions
-3 for every instance where they hardcode the value of `project.count()`  
-5 for hardcoding. Max -5 per question.  
-3 if they use any "advanced" stuff like lists, dictionaries or modules like pandas

## Required functions:
```python
get_month(date) # returns an int
get_day(date) # returns an int
get_year(date) # returns an int
format_damage(damage) # returns an int
get_number_of_days(start_date, end_date) # returns an int
deadliest_in_range(year1, year2) # returns an index, which is an int
```

## Q1
-5 if hardcoded.

## Q2
-2 if they reverse-engineer the name of the hurricane.

## Q3
-3 if they hardcode the index.

## Q4
-3 if they don't cover all possible cases.
For example, they only cover "SaLLy" and "SALly".

## Q5, Q6
-4 if their search target hardcodes any specific index or mph  
No requirements for initial index.  


## Q7
-3 if they don't write and use `format_damage` OR  
(-2 if `format_damage` doesn't take in a damage string OR doesn't return an `int` OR is incorrectly named)  
The -3 deduction takes precedence.  
No requirement to check lowercase suffixes

## Q8
-3 if they don't use or redefine `format_damage`  
-2 if they don't round to 2 decimal places  
No deduction if they look for both 'G' and 'g'.  
No deduction for not rounding.
No requirements for initial index.  


## Q9
-4 if their search target hardcodes any specific index or mph  
-1 if they don't break ties by preferring first entry  
No requirements for initial index.  

## Q10
-2 if they don't use or redefine `format_damage`  
-4 if their search target hardcodes any specific index or mph  
No requirement for default index.

## Q11
-1 if they initialize minimum value to any positive number (should be `None`, `0`, or negative value)  \
-2 if they don't use `get_year`  
-1 if they don't break ties by preferring the later entry (probably should use `<=` or `=>`)  \
No requirements for initial index.  


## Q12
-2 if they hardcoded the wrong years  
-2 if they don't use or redefine `format_damage`  
-3 if they don't use `deadliest_in_range` correctly  
-5 if they hardcoded the index in any way  
No requirements for initial index.  
No tiebreaking requirement for `deadliest_in_range`  

## Q13
-2 if they hardcoded the wrong years, expected `(1901, 2000)`  
-5 if they hardcoded the index in any way  
-3 if they don't use `deadliest_in_range` correctly or if they redefine it  
No requirements for initial index.  

## Q14
-3 if they don't use `deadliest_in_range` correctly or if they redefine it  
No requirements for initial index.  

## Q15
-1 if they initialize minimum value to any positive number (should be `None`, `0`, or negative value)  \
No requirements for initial index.

## Q16
-1 if they don't use `get_year` *somewhere*, probably in `get_year_total`  
No deduction for not using `get_year_total`  

## Q17
No deduction for not using `get_decade_total`

## Q18
-1 if they initialize minimum value to any positive number (should be `None`, `0`, or negative value)  \
-1 if they don't break ties by preferring later entries (probably using `<=` or `>=`)

## Q19
-2 if they don't use `get_month`

## Q20
-1 if they initialize minimum value to any positive number (should be `None`, `0`, or negative value)  \
-2 for not using `get_number_of_days` correctly  
No requirements for initial index.  
No tiebreaking requirement.
