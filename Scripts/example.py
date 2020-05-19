import pandas as pd
import os
import re

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
print "Pattern 1:", re.findall(pattern, better_first_line)
print "Pattern 2:", re.findall(pattern_2, better_first_line)
# We can get the length of the list to get the number of "the" occurrences.
print(len(re.findall(pattern, better_first_line)))

# Challenge: list and count all words that end with an "e". The example below demonstrates how to find all words that
# end with an r
pattern_3 = re.compile("[a-zA-Z]*r[ ]")
print "Pattern 3:", re.findall(pattern_3, better_first_line)
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



