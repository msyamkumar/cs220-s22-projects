# Student Rubric for P8

## General deductions
- -5 for hardcoding answers. Max -5 per question.   
- -4 for hardcoding indices (max deduction for 3+ violations: -10)  
- Upto -5 for displaying excessive irrelevant information or test code  
- -3 if they use any "advanced" stuff like pandas (the only modules that can be imported are `csv` and `copy`)   
- -2 for each instance of not using a required function (max deductions for 6+ violations: -10)   
- -3 if the students loop through a dictionary to get the value of a key instead of just accessing that key's value (max deductions for 4+ violations: -10)  
- -1 to -3 for incorrect logic. Logic incorrectness depends on how different written code is from what is asked in the project description for some segment (function, question, data structure etc.)   
- Do not deduct from a question if it has already failed the autograder   

## Required functions and data structures:      
```python
get_mapping(path) # returns a dict
get_key_from_last_name(lastname) # returns a list of strings
get_raw_movies(path) # returns a list of dicts
get_movies(movies_path, mapping_path) # returns a
find_specific_movies(movies, keyword) # returns a list
bucketize_by_genre(movies) # returns a list of dict of list of dicts
```

## Q1       
-5 if hardcoded.  
-3 if `get_mapping()` function is not called     
-1 if the result of `get_mapping()` is not assigned to a variable for future use    

## Q2
-5 if answer is hardcoded without working code.  
-1 if the answer from Q1 is not used.     

## Q3
-5 if answer is hardcoded without working code.  
(In this question, looping is allowed, because no specific key is mentioned in the question)  

## Q4
-5 if answer is hardcoded without working code.  
-4 if columns are hardcoded   
-3 if the starter code provided for Q4 is not used.         
-1 if the student didn't check only **last name**  
-1 if the answer from Q1 is not used.     

## Q5
-5 if answer is hardcoded without working code.  
-3 if `get_raw_movies()` is not used  
-5 if `get_raw_movies()` is not created (deduct only once)    
-1 if the result of `get_raw_movies()` is not assigned to a variable for future use   

## Q6
-5 if answer is hardcoded without working code.   
-2 if the result from Q5 is not used and/or `get_raw_movies()` is called again   

## Q7
-5 if answer is hardcoded without working code.   
-2 if the result from Q5 is not used and/or `get_raw_movies()` is called again   

## Q8
-5 if answer is hardcoded without working code.   
-5 if `get_movies()` is not created (deduct only once)  
-1 if `get_movies()` body doesn't contain `get_raw_movies()` function call    
-1 if `get_movies()` body doesn't contain `get_mapping()` function call
-3 if `get_movies()` is not used    
-1 if the result of `get_movies("small_movies.csv", "small_mapping.csv")` is not stored to a variable called `small_movies_data`     

## Q9
-5 if answer is hardcoded without working code.     
-2 if the solution contains anything besides a single access to `small_movies_data`    

## Q10
-5 if answer is hardcoded without working code.     
-2 if the solution contains anything besides a single access to `small_movies_data`   

## Q11
-5 if answer is hardcoded without working code.     
-2 if the solution contains anything besides a single access to `small_movies_data`   

## Q12
-5 if answer is hardcoded without working code.     
-4 if the result of `get_movies("movies.csv", "mapping.csv")` is not assigned to `movies` variable (deduct only once)     
-2 if a loop is used to find the length of `movies` dataset   

## Q13
-5 if answer is hardcoded without working code.     
-3 if `get_movies("movies.csv", "mapping.csv")` is called and/or variable is not reused      
-2 if a loop is used to obtain the contents of last 2 rows of `movies`    

## Q14
-5 if answer is hardcoded without working code.     
-5 if `find_specific_movies()` is changed in any way (deduct only once)     
-3 if `find_specific_movies` is not used    
-3 if `get_movies("movies.csv", "mapping.csv")` is called     
-2 if one of the copy functions from `copy` module is not used and/or `movies` is changed     
-2 if movies where Greta is an actor are not filtered out    

## Q15
-5 if answer is hardcoded without working code.     
-3 if `get_movies("movies.csv", "mapping.csv")` is called     
-2 if the student goes through the whole `movies` dataset instead of using `find_specific_movies`     
-2 if `find_specific_movies` is not called      
-2 if `movies` gets modified  

## Q16
-5 if answer is hardcoded without working code.     
-3 if `get_movies("movies.csv", "mapping.csv")` is called     
-5 if `bucketize_by_genre()` is not created (deduct only once)     
-2 if `bucketize_by_genre` is not used         
-1 if the result of `bucketize_by_genre(movies)` is not assigned to a variable (deduct only once)     

## Q17
-5 if answer is hardcoded without working code.     
-3 if `get_movies("movies.csv", "mapping.csv")` is called     
-3 if `bucketize_by_genre(movies)` is called for this question and/or variable is not reused   
-2 if a loop is used to find the number of Comedy movies    

## Q18
-5 if answer is hardcoded without working code.     
-3 if `get_movies("movies.csv", "mapping.csv")` is called     
-3 if `bucketize_by_genre(movies)` is called for this question and/or variable is not reused       

## Q19
-5 if answer is hardcoded without working code.     
-3 if `get_movies("movies.csv", "mapping.csv")` is called     
-4 if any control structures (loops or `if` statements) are used   
-2 if `bucketize_by_genre` is not used    
-2 if `find_specific_movies` is not used  

## Q20
-5 if answer is hardcoded without working code.     
-3 if `get_movies("movies.csv", "mapping.csv")` is called     
-1 if tie-breaking is not done to prefer the last genre   
-2 if `bucketize_by_genre` is not used    
-2 if `find_specific_movies` is not used    
