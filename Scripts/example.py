#import pandas as pd
import os

# When working in Windows the filepath slashes are flipped
# Example path in Windows. Note that there are two back slashes. This is because a backslash is the escape
# character and is used to represent other test items (\t for tab, \n for new line etc.)
windows_example_filepath = "Data\\test.csv"

# Simple variables to find the file
working_directory = "../Data/"
file_name = "test.txt"

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






