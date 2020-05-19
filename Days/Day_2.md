# Daily Coding Exercises

###  Day 2 - File IO
Now that you have reviewed some of the basics with printing and formatting we will move on
to file input and output. The code should be written in a file named  ```day2_python_exercises.py``` in the Scripts directory

File IO is very important in research. Most of the scripts you will write are going to have
at least one file that is used as input and at least one file for output.  

Tips when naming files:
- Stay consistent in you naming convention.
- Use descriptive file names (input.csv vs FEHM_Model_Calibration_Data.csv).
- When you have multiple files being output use a file number at the end of the name.
Example: Moisture_Data_1.csv, Moisture_Data_2.csv etc.
- Do not use spaces in your file names.
- Include the extension (generally it will be a *.csv or *.txt extension)

Now time for some code. The process will be the same as yesterday. Type out the code provided 
and try to determine what the output will be. Do not copy and paste. There will be a few short
challenges in the comments, this will help you think about what you've learned and apply it.
Good luck!

#### Code Part 1
```python
import re

# When working in Windows the filepath slashes are flipped
# Example path in Windows. Note that there are two back slashes. This is because a backslash is the escape
# character and is used to represent other test items (\t for tab, \n for new line etc.)
windows_example_filepath = "Data\\test.csv"

# Simple variables to find the file
working_directory = "../Data/"
file_name = "Day_2_data.txt"

# Creating a file object is the first step to reading or writing to a file
input_file = open(working_directory + file_name)
# What happens if we open a file that does not exist? Comment out the line after running.
input_test_file = open("Data/testing.csv")

# Now that we have a file object let's use it.
# If you look at the file it is split into two parts. Let's look at the first part. This will show you how to
# Read in a file line by line. Since their are only two lines we will read them individually. Please note that for most
# scripts you will write that involve reading line by line you will use a loop to dynamically read each line.
first_line = input_file.readline()
# Wow that was a tough one

print(first_line)

# The blue fox just does not sound right. Let's change it to brown.
better_first_line = first_line.replace("blue", "brown")
print(better_first_line)

# Much better. Now let's break the sentence apart.
first_line_split = better_first_line.strip().split(' ')
print(first_line_split)

# Count the occurances of  "the" in the first line
print(first_line_split.count("the"))
# But wait there are two. Python is case sensitive so we will use regex to allow for the first letter to be caps.
pattern = re.compile("the", re.IGNORECASE)
# Regex has a wide range of functionality when it comes to pattern matching
# The following works the same as the previous regex pattern. The characters in brackets are the characters that
# may exist in that location that would match our desired word.
pattern_2 = re.compile("[Tt]he")
# The regex findall will return a list of matches
print("Pattern 1:", re.findall(pattern, better_first_line))
print("Pattern 2:", re.findall(pattern_2, better_first_line))
# We can get the length of the list to get the number of "the" occurrences.
print(len(re.findall(pattern, better_first_line)))

# Challenge: list and count all words that end with an "e". The example below demonstrates how to find all words that
# end with an r
pattern_3 = re.compile("[a-zA-Z]*r[ ]")
print("Pattern 3:", re.findall(pattern_3, better_first_line))
print(len(re.findall(pattern_3, better_first_line)))

# That was only a simple introduction to regex. You should know that this tool exists for pattern recognition.
# Using a cheat sheet or Google makes it easy to generate patterns for finding and replacing text.

# Now let's read the next line.
second_line = input_file.readline()
# Why did it print the next line? Well Python is using a file pointer. Once a line is read it moves the pointer to the
# next line to be read.
print(second_line)

# Let's change brown fence to white fence.
better_second_line = second_line.replace("brown", "white")
print(better_second_line)
# Uh oh. The fox is now white. Let's change just the fox back to brown.
better_second_line = better_second_line.replace("white", "brown", 1)
# Replace has third parameter that let's you set the max occurances to replace
print(better_second_line)

# Challenge: Change only the fence to black
```

Now that you have done some text manipulation. Let's try some CSV manipulation using Pandas. 
Be sure too have Pandas installed on your machine.
#### Code Part 2.
```python
import pandas as pd
import numpy as np

# Skip the "--SKIP LINE--" line
next(input_file)

# Read the CSV portion into a Pandas DataFrame
data = pd.read_csv(input_file)
# Print out the first and only 5 rows
print(data.head(5))
# Create a column with the person's full name
data['fullName'] = data['firstName'] + " " + data['lastName']
# Display
print(data.head(5))

# Calculate the average age of the people in the DataFrame
print(sum(data['age']) / len(data['age']))

# Create a copy
data_backup = data.copy()

# That did not work. Why? Well it would appear as if we have a missing age. Let's clean the data to ensure no
# missing values are present.
# Set missing values to 0
data['age'] = data['age'].replace(np.NaN, 0)
print(data.head(5))

# Now the data is skewed because of the invalid entry defaulting to 0
print(sum(data['age']) / len(data['age']))

# Another option is to drop the row with the invalid data
data_backup = data_backup.dropna(how='any', axis=0)

print(data_backup.head(5))

print("\n\nPrinting rows dynamically.\n")
# 2 different ways that accomplish the same task.
print(data[data['school'] == 'Baylor'])

for index, row in data.iterrows():
    if "Baylor" in row['school']:
        print(row)

# Challenge: Replace Baylor with Baylor University

# Find average excluding bad values using for loop
sum_age = 0
count_age = 0
for value in data['age']:
    if value > 0:
        sum_age += value
        count_age = count_age + 1
print(sum_age / count_age)

# Export DataFrame to CSV file.
data.to_csv('day2_output.csv', index=None)
```
#### Conclusion
By now you should have a good understanding of the simple tools available when handling file I/O. File input/output is crucial to handling data. About 80% of Machine Learning work is spent handling data whether that be input data or output data. Manipulating data from files and being able to export is a valuable skill to know. There are many ways to do any one task in Python with an abundance of code snippits available online through Python's amazing community. Do not spend more than 10 minutes trying to remember syntax. Just Google it. As always spend some time practicing and playing around with the tools presented in these exercises.
