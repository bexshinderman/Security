# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:28:03 2020

@author: Bex.0
"""


from collections import Counter
#plain text to perform cipher on
input_string = "abccc"

#predetermined monogram frequency table
probability = {
        "a": 0.08167,
        "b": 0.01492,
        "c": 0.02782
        }
#print monogram frequency probabilities
for i in probability:
    print(i, probability[i])
#find total length of phrase    
length = len(input_string)
print("length of input string =", length)

#Dictionary lookup to obtain monogram freq (needs to go in for loop)
letter = "A"
if letter in probability:
    print('probability of', letter, probability[letter])
    

for i in range(len(input_string)):
    position_number = i
    print("position number", position_number)
    position_character = input_string[i]
    print("position character", position_character)
    char_count = input_string.count(position_character)
    print("amount of ", position_character, "in", input_string, "is", char_count)

    char_count = input_string.count(position_character)
    print(char_count)
    letter = position_character
    chi_squared = {}
    if letter in probability:
        letter_probability = probability[letter]
        print(letter_probability)
        print("anythhingg")

        
    
    
    
#create dictionary with monogram frequencies
#count length of input phrase
#for each alphabetical character in input_string
    # find frequency of chaar
    #find alphabetical character's corresponding monogram frequency in dictionary i.e if letter is A probability is 0.08167
    #chi-squared = (letter freq in phrase - (length * monogramfreq)**2)/2
    #multiply chi-squared by 1000
#shift key = lowest chi-squared value 
    
#once the shift key is obtained:
    #foreach value in input_string
    #add shiftkey values to alphabet character
