# Student Rubric for P6

## General deductions
-2 for every instance where they don't use the `cell()` function to access a value in airbnb.csv (max deduction for 3+ violations: -5)  
-5 for hardcoding answers. Max -5 per question.  
-4 for hardcoding indexes (max deduction for 3+ violations: -10)  
-3 if they use any "advanced" stuff like dictionaries or modules like pandas  
-2 for each instance of not using a required function (max deductions for 6+ violations: -10)  
Do not deduct from a question if it has already failed the autograder  

## Required functions:
```python
find_room_names(phrase) # returns a list
availability_per_host_name(search_host_name, search_neighborhood = None) # returns a list
find_prices_within(lat_min, lat_max, long_min, long_max) # returns a list
secondary_word_in_found_rooms(find_room_word, secondary_word) # returns a float
```

## Q1
-5 if hardcoded.  
-2 if they don't use `cell()` to access column values

## Q2
-5 if answer is hardcoded without working code.  
-2 if they don't use `cell()` to access column values

## Q3
-3 if they hardcode the indices of rooms which are in Inwood neighborhood.  
-2 if they don't use `cell()` to access column values

## Q4, Q5
-3 if they don't cover all possible cases (case-insensitive match).  
-4 if their search hardcodes any specific index  
-2 if `find_room_names` is not used.   
-2 if they don't use `cell()` to access column values

## Q6
-4 if their search hardcodes any specific index   
-2 if they don't use `cell()` to access column values  

## Q7
-4 if their search hardcodes any specific index   
-2 if they don't use `cell()` to access column values  

## Q8
-2 if they don't use `cell()` to access column values  
-2 if any of the values used is wrong even if the answer is correct (for example, they used "Brooklyn" instead of "Manhattan")  

## Q9
-2 if they don't use `cell()` to access column values  
-4 if their search hardcodes any specific index  

## Q10
-2 if they don't use `cell()` to access column values  
-3 if they don't use `availability_per_host_name()` function  

## Q11
-4 if they hardcode the most or least availability  
-3 if they don't use `availability_per_host_name()` function  

## Q12
-3 if they don't use `find_prices_within()` function  
-1 if the arguments to `find_prices_within()` function are incorrect  

## Q13
-3 if they don't use `find_prices_within()` function  
-2 if they don't develop a `median` function from lab-p6 practice to find median  
-1 if the arguments to `find_prices_within()` function are incorrect  

## Q14
-3 if they don't use `find_prices_within()` function  
-1 if the arguments to `find_prices_within()` function are incorrect  

## Q15, Q16
-2 if they found the average of ratios for wrong neighborhood but got the correct answer  
-5 if they hardcode the answer  
-2 if the logic is incorrect (for example, if they added all the `number_of_reviews` and divided by the sum of `availability_365`  

## Q17
-5 if they hardcode the answer  

## Q18
-2 if `secondary_word_in_found_rooms` doesn't invoke `find_room_names()` in its body  
-3 if `secondary_word_in_found_rooms` is not used  

## Q19
-3 if `secondary_word_in_found_rooms` is not used  

## Q20
-5 if they hardcoded the answer  
