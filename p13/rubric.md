# Student Rubric for P13

## General deductions
- -5 for hardcoding answers. Max -5 per question.   
- -3 for hardcoding indices (max deduction for 4+ violations: -10)  
- -1 per instance of displaying excessive irrelevant information or test code (max deductions for 5+ violations: -5)
- -3 if they use any "advanced" (the only modules that can be imported are `sqlite3`, `os`, `requests`, `pandas`, `math`, `matplotlib`, and `questions`.         
- -3 for each instance of not using a required function (max deductions for 4+ violations: -10)   
- -3 if the students loop through a dictionary to get the value of a key instead of just accessing that key's value (max deductions for 4+ violations: -10)  
- -1 to -3 for incorrect logic. Logic incorrectness depends on how different written code is from what is asked in the project description for some segment (function, question, data structure etc.)   
- -1 for the project if bad coding practices are used. Refer to [Coding Style Requirements](https://github.com/msyamkumar/cs220-s22-projectDesign/tree/p13-refresh/p13#coding-style-requirements) to understand few instances of bad coding practice     
- Do not deduct from a question if it has already failed the autograder   

## P13 specific guidelines:
-3 if a Pandas operation is used to extract data instead of an SQL query (unless permitted, such as in Q11 and Q12)     
-2 if .loc is used on a pandas DataFrame to hardcode an index (instead use .iloc appropriately) (max deductions for 5+ violations: -10)     

## Required data structures and functions:

```python   
#for p13:
download(filename, url) # downloads url and saves contents to filename    

# from lab p13
bar_plot(df, x, y)
scatter_plot(df, x, y)
plot_horizontal_bar(df, x)
plot_pie(df, x, y, title=None)

get_regression_coeff(df, x, y)
plot_regression_line(df, x, y)

rankings # DataFrame storing data from QSrankings.json    
```     

## `download(filename, url)`     
-3 if function is not created     

## rankings data structure:
-0 if `pd.read_json()` is used to download and save "QSrankings.json" instead of `download()` function (i.e. both ways are allowed)           

## Q1
-2 if any column other than `institution_name` and `international_students` is included in the DataFrame  
-1 if more than first 10 rows are displayed         
-1 if any year apart from `2020` is used  

## Q2
-2 if any column other than `institution_name` and `reputation` is included in the DataFrame      
-2 if rows are not in descending order of `reputation` or ties are not broken in alphabetical order of `institution_name`       
-1 if more than first 10 rows are displayed         
-1 if any year apart from `2019` is used    

## Q3
-2 if any column other than `country` and `num_of_institutions` is included in the DataFrame      
-2 if rows are not in descending order of `num_of_institutions` or ties are not broken in alphabetical order of `country`       
-1 if more than first 10 rows are displayed        
-1 if any year apart from `2020` is used      

## Q4       
-2 if any column other than `country` and `num_of_institutions` is included in the DataFrame      
-2 if rows are not in descending order of `num_of_institutions` or ties are not broken in alphabetical order of `country`         
-1 if more than first 10 rows are displayed      
-1 if any year apart from `2020` is used        

-3 if given `bar_plot` function is not used     
-1 if x-axis label is not `country` or y-axis label is not `num_of_institutions`  
-1 if the DataFrame created is not assigned to a variable called `num_institutions`     

## Q5       
-2 if any column other than `country` and `total_score` is included in the DataFrame      
-2 if rows are not in descending order of `total_score`           
-1 if more than first 10 rows are displayed     
-1 if any year apart from `2019` is used       
-1 if the DataFrame created is not assigned to a variable called `top_total_score`      

## Q6     
-3 if `bar_plot` function is not used     
-2 if `top_total_score` DataFrame from Q5 is not used     
-1 if x-axis label is not `country` or y-axis label is not `total_score`

## Q7       
-2 if any column other than `institution_name` and `international_score` is included in the DataFrame      
-2 if rows are not in descending order of `international_score`       
-1 if more than first 10 rows are displayed     
-1 if any year apart from `2020` or any country apart from `United States` is used       

## Q8     
-2 if any column other than `citations_per_faculty` and `overall_score` is used for the plot            
-1 if any year apart from `2018` is used        
-1 if x-axis label is not `citations_per_faculty` or y-axis label is not `overall_score`      
-2 if `scatter_plot` function is not used       

## Q9   
-2 if any column other than `academic_reputation` and `employer_reputation` is used for the plot            
-1 if any year apart from `2019` or any country apart from `United States` is used        
-1 if x-axis label is not `academic_reputation` or y-axis label is not `employer_reputation`      
-2 if `scatter_plot` function is not used       

## Q10     
-2 if any column other than `international_students` and `faculty_student_score` is used for the plot            
-1 if any year apart from `2020` is used        
-1 if x-axis label is not `international_students` or y-axis label is not `faculty_student_score`      
-2 if `scatter_plot` function is not used          

## Q11   
-2 if any column other than `international_students` and `overall_score` is used for the plot            
-1 if any year apart from `2020` is used
-1 if more than top 100 institutions are included in the calculations     
-2 if correlations of countries apart from `United States` or `United Kingdom` are calculated             
-3 if any `Pandas` operations apart from `.corr`, `.loc` and `.iloc` are used     

## Q12
-2 if any column other than `citations_per_international` and `overall_score` is used for the plot            
-1 if any year apart from `2019` is used         
-3 if any `Pandas` operations apart from `.corr`, `.loc` and `.iloc` are used     

## Q13     
-2 if any column other than `country` and `sum_intl_citations` is included in the DataFrame      
-2 if rows are not in descending order of `sum_intl_citations`      
-1 if more than first 15 rows are displayed     
-1 if any year apart from `2019` is used       

## Q14             
-2 if any column other than `country` and `avg_intl_citations` is included in the DataFrame      
-2 if rows are not in descending order of `avg_intl_citations`       
-1 if any year apart from `2019` is used       

## Q15
-2 if any column other than `country`, `institution_name` and `max_intl_citations` is included in the DataFrame      
-2 if rows are not in descending order of `max_intl_citations`        
-1 if any year apart from `2020` is used        
-2 if `HAVING` clause is not used as specified in the requirement to omit rows with missing `max_intl_citations` values          

## Q16   
-2 if any column other than `country`, `avg_citations` and `avg_intl_faculty` is used for the plot                 
-1 if institutions other than those ranked top 50 are considered        
-1 if any year apart from `2018` is used              
-1 vertical axis label is not `country`         
-2 if legend is not present in the graph              
-2 if `plot_horizontal_bar` function is not used                  

## Q17                  
-2 if any column other than `overall_score` and `rank` is used for the plot               
-1 if any year apart from `2020` is used   
-2 if `plot_regression_line` function is not used     
-1 if x-axis label is not `overall_score` or y-axis label is not `rank`             

## Q18
-2 if any column other than `inverse_overall_score` and `rank` is used for the plot               
-1 if any year apart from `2020` is used   
-2 if `plot_regression_line` function is not used         
-1 if x-axis label is not `inverse_overall_score` or y-axis label is not `rank`                 

## Q19
-2 if `get_regression_coeff` function is not used to get the regression coefficients        
-2 if the equation `y = m * x + b` is not used to find the rank of the institution with `overall_score` of 72                 

## Q20   
-2 if `num_institutions` from Q4 is not used          
-1 if title of the plot is not `Number of institutions`           
-2 if `plot_pie` function from lab is not used        
-1 if any year apart from `2020` is used      
