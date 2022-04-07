# Student Rubric for P10

## General deductions
- -5 for hardcoding answers. Max -5 per question.   
- -3 for hardcoding indices (max deduction for 4+ violations: -10)  
- -1 per instance of displaying excessive irrelevant information or test code (max deductions for 5+ violations: -5)
- -3 if they use any "advanced" stuff like `pandas` (the only modules that can be imported are `csv`, `namedtuple`, `json` and `os`)   
- -3 for each instance of not using a required function (max deductions for 4+ violations: -10)   
- -3 if the students loop through a dictionary to get the value of a key instead of just accessing that key's value (max deductions for 4+ violations: -10)  
- -1 to -3 for incorrect logic. Logic incorrectness depends on how different written code is from what is asked in the project description for some segment (function, question, data structure etc.)   
- -1 for the project if bad coding practices are used. Refer to [Coding Style Requirements](https://github.com/msyamkumar/cs220-s22-projectDesign/tree/p10-saurabh/p10#coding-style-requirements) to understand few instances of bad coding practice
- Do not deduct from a question if it has already failed the autograder   

## P10 specific guidelines:
-3 if '\\' or '/' are hardcoded instead of using `os.path.join()` in obtaining any answer    

## Required functions and data structures:      
```python
# functions
list_files_in(directory) # returns a list
get_mapping(mapping_file_path): # returns a dict
get_comment_data(comment_file) # returns a dict
get_videos(video_data, mapping_data) # returns a dict
bucketize(attribute, videos) # returns a dict

#variables
comment_paths # list from Q3
channel_paths # list from Q4
channel_dict # dict from Q6
comments # dict for Q7
comment_buckets # dict for Q12
videos # dict for Q13
channel_buckets # dict for Q17
```

## Q1       
-5 if `list_files_in()` from lab is not used          
-2 if files begining with '.' are not excluded          
-1 if files are not sorted          

## Q2
-2 if answer from Q1 or `list_files_in()` is not used         
-3 if `os.path.join()` is not used.         
-2 if paths are not relative to `main.ipynb` (ensure that your directory structure is as per the [requirements](https://github.com/msyamkumar/cs220-s22-projectDesign/tree/p10-saurabh/p10#requirements)      

## Q3           
-2 if Q2 answer is not used        
-1 if the answer is not stored in a variable `comment_paths`         

## Q4           
-2 if Q2 answer is not used           
-1 if the answer is not stored in a variable        

## `get_mapping()`          
-5 if `get_mapping()` is not created (deduct only once)         
-3 if `get_mapping()` is not used or defined as per specification        
-3 if `get_mapping()` assumes some relative path like `data/`   
-3 if `get_mapping()` results are not stored to variables       

## Q5           
-3 if path has hardcoded slashes   
-3 if `get_mapping` is not used  

## Q6           
-1 if `channel_paths` is not used to get paths of all `channel_ids` json files     
-3 if try/except block is not used to catch **only** `JSONDecodeErrors`         
-1 if `channel_dict` isn't defined     

## Comment namedtuple object:       
-2 if any of the attributes are not utilized properly to create `Comment` object        

## `get_comment_data()` function:       
-5 if `get_comment_data()` is not created (deduct only once)        
-3 if `get_comment_data()` is not used (deduct per instance of it not being used where required)        
-3 if `get_comment_data()` is not defined as per specification      
-3 if column indices are hardcoded  


## Q7
-3 if `get_comment_data` isn't used  
No requirement to save this result to a variable

## `comments` data structure:      
-2 if `comments` is not defined   
-1 if `comment_paths` is not used              
-3 if `get_comment_data()` is not used (deduct per instance of it not being used where required)           
-4 if `get_comment_data()` is redefined (deduct only once)

## Q8, Q9, Q10, Q11            
-2 if `comments` dict is not used           
-1 if indices are used instead of named attributes to access values from `Comment` namedtuple objects 

## comment_buckets data structure:   
-5 if `comment_buckets` is not created (deduct only once)   
-2 if `comment_buckets` is not used or defined as per specification (deduct only once)          
-1 to -3 if there's an error in bucketizing logic    

## Q12
refer to `comment_buckets` guidelines    

## get_videos() and videos:       
-5 if `get_videos` is not defined  
-2 if `get_videos` does not meet spec (For example, if they assume the relative path is `data/` or they hardcode file names)  

-5 if `videos` is not created (deduct only once)   
-2 if `videos` is not used (deduct per instance of it not being used where required)            
-2 if `videos` is not defined as per specification (deduct only once)

## Q13
refer to `videos` guidelines        

## Q14
refer to `videos` guidelines   
-3 if control structures (loops or if statements) are used      

## Q15
refer to `videos` guidelines        
-2 if videos with ratings disabled are not ignored      

## Q16
refer to `videos` guidelines

## bucketize() function:
-5 if `bucketize()` is not created (deduct only once)        
-2 if `bucketize()` is not used (deduct per instance of it not being used where required)        
-3 if `bucketize()` is not defined as per specification      
-3 if `bucketize()` is called more than once for same attribute instead of saving the output to a variable          

## Q17
refer to `bucketize()` guidelines       
-2 if `videos` is not used as data      
-2 if `channel_buckets` is not defined        

## Q18
refer to `bucketize()` guidelines         
-2 if `videos` is not used as data  
-2 if `channel_buckets` is not used          

## Q19
-3 if they make a *redundant* call to `get_videos`, `bucketize`, etc.

## Q20
-3 if they make a *redundant* call to `get_videos`, `bucketize`, etc.
