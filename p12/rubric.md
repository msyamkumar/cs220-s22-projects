# Student Rubric for P12

## General deductions
- -5 for hardcoding answers. Max -5 per question.   
- -3 for hardcoding indices (max deduction for 4+ violations: -10)  
- -1 per instance of displaying excessive irrelevant information or test code (max deductions for 5+ violations: -5)
- -3 if they use any "advanced" stuff like `numpy` (the only modules that can be imported are `json`, `os`, `requests`, `pandas`, `bs4` and `BeautifulSoup`.         
- -3 for each instance of not using a required function (max deductions for 4+ violations: -10)   
- -3 if the students loop through a dictionary to get the value of a key instead of just accessing that key's value (max deductions for 4+ violations: -10)  
- -1 to -3 for incorrect logic. Logic incorrectness depends on how different written code is from what is asked in the project description for some segment (function, question, data structure etc.)   
- -1 for the project if bad coding practices are used. Refer to [Coding Style Requirements](https://github.com/msyamkumar/cs220-s22-projectDesign/tree/p12-refresh/p12#coding-style-requirements) to understand few instances of bad coding practice  ???     
- Do not deduct from a question if it has already failed the autograder   

## P12 specific guidelines:
-3 if conditional statements or loops are used to go through a pandas DataFrame (unless permitted) instead of boolean indexing (max deductions for 7+ violations: -20)                            
-2 if .loc is used on a pandas DataFrame to hardcode an index (instead use .iloc appropriately) (max deductions for 5+ violations: -10)     

## Required data structures and functions:

```python   
#for p12:
download(filename, url) # downloads url and saves contents to filename    
parse_html(filename) # returns data from html file  

rankings # DataFrame storing data from rankings.json    
institutions_df
```     

## `download(filename, url)`     
-3 if function is not created

## rankings data structure:
-0 if `pd.read_json()` is used to download and save "rankings.json" instead of `download()` function (i.e. both ways are allowed)           

## Q1, Q2, Q3						
-2 if incorrect column is used (anything apart from `Country`, `World Rank`, `Institution` for respective questions)           
-1 if the output for Q3 is not stored in a variable called `uw_madison`    

## Q4   		                    					
-1 if `uw_madison` from Q3 is not used   
-2 if the year being checked for is not `2021-2022`   
-2 if `loc` is used  

## Q5         
-1 if `uw_madison` from Q3 is not used                         

## Q6           
-2 if the year being checked for is not `2020-2021` in boolean indexing  

## Q7    
-1 if the row containing the best German institution is not stored in a variable called `german_best`  
-2 if `loc` is used  

## Q8     
-2 if `german_best` from Q7 is not used to find all `USA` institutions with a `World Rank` better than that of `german_best`       
-2 if the year being checked for is not `2019-2020`    

## Q9   
-2 if the highest rank institution is not found specifically from `Quality of Education Rank`  
-2 if the year being checked for is not `2021-2022`   
-2 if `loc` is used

## Q10     
-2 if the top 5 highest rank institutions are not found specifically from `Research Performance Rank`   
-2 if the year being checked for is not `2020-2021`        

## Q11   
-1 if the solution DataFrame is not stored in a variable called `institutions_df`       
  
## Q12     
-2 if the difference in rankings is not between the years `2019-2020` and `2021-2022`     
-1 if `institutions_df` is not used   
   
## Q13     
-2 if the difference in rankings is not between the years `2019-2020` and `2021-2022`     
-1 if `institutions_df` is not used       
-2 if absolute difference is not considered     
-2 if `loc` is used

## Q14    
-2 if `institutions_df` from Q11 is not used     

## Q15
-2 if `.sort_values()` is not used to find top 10 institutions in terms of `Alumni Employment Ranking`  
-2 if the year being checked for is not `2020-2021`   
-2 if `loc` is used  

## Q16   
-2 if the years being considered are not `2019-2020` and `2021-2022`  
-2 if `loc` is used  

## Q17
-2 if the year being checked for is not `2020-2021`   
-1 if output is not a list    

## Q18
-2 if output is not a list of column names from `2019-2020.html`            
-0 for hardcoding indices or html tags (i.e. no deductions for hardcoding indices or html tags)     

## Q19
-2 if `parse_html()` function from lab-p12 is not used          

## Q20   
-2 if the data from parsing `2019-2020.html`, `2020-2021.html` and `2021-2022.html` files is not stored to a file called `my_rankings.json`    
