# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


from unittest import result
import string
import re

# result = []
# for word in me:
#     result.append(word.strip("'"))





def read_file_content(filename):
    # [assignment] Add your code here 
    with open("story.txt", 'r') as fv:
        #read the file
        file = fv.read()
    
        return file

    # return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
        #assign the read file function to text variable

    text = read_file_content("story.txt")
        #strip trailing spaces 

    text = text.strip()
        #substitute any character that's not among the regex with ""

    cleaned_text =re.sub(r'[^\w\s\']+', "", text).upper()

    #split the cleaned text into individual words
    cleaned_text = re.split(r'\s+', cleaned_text)

    #strip cleaned text individual word of " ' " and store in temp_result
    temp_result =[]

    for word in cleaned_text:
        temp_result.append(word.strip("'"))
        
    result = {}

    #check for every word in temp_result count and add them to the result dictionary 
    for chunk in temp_result:
        if chunk in result:
            result[chunk] += 1
        else:
            result[chunk] = 1 

            #print the result
    for key, value in result.items():
        print(f"{key} : {value}")

#call the count_word function 
count_words()
   # return {"as": 10, "would": 20}