#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 07:59:44 2020

@author: iancancel
"""


# Comment each line to predict the output before running the script.
print ("I will now check some inventory:") # It will show "I will now check some inventor"
print ("Bikes", 25 + 30 / 6) #It will show bikes and next to it the result of the operation being 30
print ("Helmets", 100 - 25 * 3 % 4) #It will show helmets and next to it the result of the operation being 97

print ("Now I will count the number of sales:")

#this math may seem wrong. Try exploring floating point numbers. Document the differences.
print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6) #So the main thing is order of operation vs placement of numbers also 4? I was wrong, 6.75

print ( "Is it true that 5 + 2 < 3 - 7?") #no it isnt, 7 is more than -4

print (5 + 2 < 3 - 7) #honestly not sure what this did, it looks like a restatement

print ("what is 5 + 2?" , 5 + 2) # this will print out the question then the answer next to it, I think

print ("What is 3 - 7?" , 3 - 7) #this will print the questiona and then the answer next to it, which is -4

print (" Oh that's why it's false") # lol not sure what to comment, I mean yes? 

print ("Let's look at a few more.")

print (" Is it greater than?" , 5> -2)# yes, 5 is greater than -2
print (" Is it greater than or equal to?" ,5 >= -2) # yes, this is true
print (" Is it less than or equal?" , 5 <= -2) #yes, this is true

#Explore the differences

print ("3" + str(2)) #I expect this to show 3, it just errors, ok I changed it
print ("3" + str(2)) # So this one might add the 2 to the 3 or just print the operation but not do anything with it. It just placed it next to it?
print ("3", 2) # It will just print the number next to the 3
print ("3 + 2") # It will print everything inside the ()
print ("3" + "2") #It will print the numbers but not the +, I was wrong it was the same as an earlier one
print ("3" , "2") # it will only print numbers, yes!

# Notes:
# - % is the modulus operator. It calculates a remainder
# - There are multiple ways to print things. Using () is typically best practices for readability purposes

#Formating


string_a = "There are %d types of people." % 10 # I sense you are going somewhere with this
binary = "binary" #ok...
no_binary = "don't" # yes...
string_b = "Those who know %s and those who %s." % (binary, no_binary) #oh...

print(string_a) #will print string_a
print(string_b) #will print string_b, guess not for both

# Using %r gives the raw data. Great for debugging.
print("What was that? %r" % string_a) 
print("No the other part. '%s'" % string_b) #please stop

corny = True
joke_rating = "Was that joke horrible? %r"
print(joke_rating % corny) #it was corny

left = "Left" #prints left
middle = "-" #prints _
right = "Right" #prints right
print(left + middle + right) #organizes the order of the text that is being printed

#I was jamming to Smooth Criminal by Micheal Jackson at this point, thought I'd let you know lol

format_str = "Hi my name is {}!".format("Bob") #not sure what the formatting is doing here, I'll look it up
format_str_2 = "Hi my name is {name}!".format(name="Bob") #ok I get it
format_str_3 = "Hi my name is {name} and I am {age} years old looking for a job at {job}".format(name="John", age=17,  # I can't tell if the placement is important at a first glance, but I get the idea
                              
                                                                                                    job="Baylor")
print(format_str) #asking to print the above defined format
print(format_str_2) #asking to print the above defined format
print(format_str_3) #asking to print the above defined format

names = ["Chris", "Ian", "Scott", "Bob"] #defining names
for name in names: #for statement
    print("Hi my name is {}".format(name)) #Prints hi my name is then follows the format

people = {"Chris": 22, "Ian": 19, "Scott": 23, "Bob": 12} #adds another aspect of the format, age
for person in people: #for statement
    print("Hi my name is {name} and I am {age} years old!".format(name=person, age=people[person])) #I will need to practice doing more stuff like this, it's simple formatting but took me a bit to get. 
    
    #Final thoughts about day 1: This took more time than I thought but that is not bad. It was great! You did a fantastic job with this! I had to think at least a bit for all of them.
    #Forcing the user to write all the lines helped greatly with practice. It's a simple yet effective introduction, I guess you said that you had taught people before
    #It shows based on this, I'm looking forward to the next days. 
    


