# Student Rubric for P11

## General deductions
- -5 for hardcoding answers. Max -5 per question.   
- -3 for hardcoding indices (max deduction for 4+ violations: -10)  
- -1 per instance of displaying excessive irrelevant information or test code (max deductions for 5+ violations: -5)
- -3 if they use any "advanced" stuff like `numpy` (the only modules that can be imported are `csv`, `namedtuple`, `json`, `os`, `copy`, `matplotlib`, `pandas`, `datetime` and our own `questions`). `pandas` can only be used in the given plot functions.     
- -3 for each instance of not using a required function (max deductions for 4+ violations: -10)   
- -3 if the students loop through a dictionary to get the value of a key instead of just accessing that key's value (max deductions for 4+ violations: -10)  
- -1 to -3 for incorrect logic. Logic incorrectness depends on how different written code is from what is asked in the project description for some segment (function, question, data structure etc.)   
- -1 for the project if bad coding practices are used. Refer to [Coding Style Requirements](https://github.com/msyamkumar/cs220-s22-projects/tree/main/p10#coding-style-requirements) to understand few instances of bad coding practice
- Do not deduct from a question if it has already failed the autograder   

## P11 specific guidelines:
-3 if '\\' or '/' are hardcoded instead of using `os.path.join()` in obtaining any answer or absolute paths (such as, `C://ms//CS220//p11` are used instead of relative paths)    
-2 for each instance of not using named access (like comment.video_id) for namedtuples (max -5)  
-5 for the whole project if they look at `data` files again instead of `videos` or `comments`
## Required data structures and functions:

```python   
#from p10:
read_json(path)
get_mapping(pathname)
Comment
get_comment_data(comment_file)
bucketize(attribute, videos)
plot_dict(d, label="Please Label Me!!!")
process_csv(filename)
list_files_in(pathname)
list_paths_in(pathname)
get_videos(data_file, video_mapping_file)
comments
videos

#for p11:
process_duration(duration_str) # 5 minute time interval   
scatter(x, y, xlabel, ylabel) # makes a scatter plot    
sort_comments_by_published_time(video_title) # sorted list of comments      
time_delta(start, end): # float representing time difference      
get_all_paths_in(directory) # list of files     
```     

## Q1       
-3 if `videos` is modified  
-3 if any one of `process_duration` or `bucketize` is not used          
-1 if the output of `bucketize` is not stored in a variable called `duration_buckets`     
-1 if `plot_dict` is not used     
-1 if the vertical axis is not labelled "number of videos"   

## Q2
-1 if the variable from Q1 (`duration_buckets`) is not used        
-3 if `plot_dict` is not used     
-1 if the vertical axis is not labelled "average views"    

## Q3                  
-3 if `plot_dict` is not used (do not deduct twice)     
-1 if the vertical axis is not labelled "views"    

## Q4           
-3 if `scatter` function from lab-p11 is not used             
-1 if the horizontal axis is not labelled "views" or vertical axis is not labelled "likes"              

## Q5         
-3 if `scatter` function from lab-p11 is not used (do not deduct twice)                
-1 if the horizontal axis is not labelled "views" or vertical axis is not labelled "likes"              

## Q6           
-3 if `scatter` function from lab-p11 is not used (do not deduct twice)                 
-1 if the horizontal axis is not labelled "views" or vertical axis is not labelled "engagement"  

## Q7
-3 if `scatter` function from lab-p11 is not used (do not deduct twice)                         
-1 if the horizontal axis is not labelled "views" or vertical axis is not labelled "engagement"   

## Q8     
-3 if `scatter` function from lab-p11 is not used (do not deduct twice)                 
-1 if the horizontal axis is not labelled "comment length" or vertical axis is not labelled "likes"

## Q9
-3 if `scatter` function from lab-p11 is not used (do not deduct twice)          
-1 if the horizontal axis is not labelled "comment length" or vertical axis is not labelled "likes"   

## sort_comments_by_published_time(video_title):    
Follow the instructions mentioned in function description     

## Q10
-3 if `sort_comments_by_published_time` is not used   
-1 if the argument to `sort_comments_by_published_time` isn't "If I lose a boss fight, the video ends 2 (Genshin Impact)"  
-1 if `sort_comments_by_published_time` doesn't return a list of comment_ids  

## Q11
-2 if `sort_comments_by_published_time` is not used   
-1 if the title argument to `sort_comments_by_published_time` is incorrect        

## Q12    
-3 if `scatter` function from lab-p11 is not used (do not deduct twice)     
-3 if `time_delta` function is not used           
-1 if the horizontal axis is not labelled "days after video was published" or vertical axis is not labelled "likes"      

## Q13
-3 if `scatter` function from lab-p11 is not used (do not deduct twice)         
-3 if `time_delta` function is not used (do not deduct twice)  
&nbsp;&nbsp;&nbsp;&nbsp;They may have reused delta data from Q12. Do not deduct in this case   
-1 if the horizontal axis is not labelled "days after video was published" or vertical axis is not labelled "length of comments"      

## get_all_paths_in(directory):     
-4 if the function is not recursive       
-2 if the returned value is not sorted         
-1 if files beginning with '.' are not excluded by checking for them        

## Q14, Q15, Q16:
-2 if the path names are hardcoded instead of using `os.path.join()`   
&nbsp;&nbsp;&nbsp;&nbsp;They may have used `list_paths_in`. Do not deduct in this case, unless `list_paths_in` hardcodes slashes.   

## Q17
-1 if the answer to Q17 is not saved to a variable called `all_broken_paths`    

## Q18
-2 if `get_mapping` is not used     
-1 if variable, `all_broken_paths` from Q17 is not used   
-1 if all the mappings from files in `all_broken_paths` are not stored in `broken_mapping`           

## Q19
-2 if `broken_mapping` from Q18 is not used            

## Q20
-2 if `broken_mapping` from Q18 is not used     
