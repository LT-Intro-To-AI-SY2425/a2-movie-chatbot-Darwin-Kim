# Assignment 2 - Write UP

## Description
This assignment is about learning and applying the while loop and iterating through multiple lists at a time.  We also will discuss how we match things in chatbots in order to extract what a user is trying to find.  Next assignment we will work with data bases and how we can extract information from them.

## What to complete
1. Go through the notes.py file w/ Mr. Berg
2. Complete `a2.py`, Mr. Berg will walk everyone through the process
3. Make sure you pass all asserts in `a2.py`
4. Complete the reflection problems below
5. Push your code to github for grading

## Reflection Questions
1. What was difficult for you while completing the match function?

The last statement was pretty hard, but I'd say the others were relatively easy

2. Explain how you could use the match function for extracting information from a movie database.

if you figured out a way to decide what the pattern would be, then this function would allow you to compare the pattern and the source to extract only the relavent information

Example:

 - The question ["when", "was", "the", "movie", "Jaws", "written?"] is inputted, either manually by writing it into the code itself or 
   via the input() function. 

 - The code removes any punctuation, turning "written?" into "written" using an unwritten code to stop confusion in later stages due to
   failure to recognize the keyword with a ? at the end, then somehow recognizes that the words ["when", "Jaws", "written"] are relavent using code that has not been written (could use a list of words that are considered keywords, or maybe a list of words that are not usually relavent)

 - it extracts those words using the pattern: ["_", "was", "the", "movie", "_", "_"]

 - The code looks at the list ["when", "Jaws", "written"] and uses that list, now devoid of unnecessary words, to look up the correct
   information in its database using more code that has not yet been written. 
   
   The code would probably work by recognizing a series of keywords that allow it to decide which items in its database are relavent. Recognizing the word "Jaws", allowing the code to ignore all items in the database not related to the movie Jaws, then recognizing the word "date", meaning the code would ignore all items currently being considered that are not written in a date format, and then finally narrowing it down to one final answer using the word "written", which clarifies what date you are looking for in relation to the movie Jaws. it would decide when it was done by constantly checking how many strings were in the list of relavent items, and if it did not ever reach a singular value it would return something along the lines of "more information needed".