'''
author = "Jan Hodánek"
'''
# take look at the texts

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
# the one im gonna use
TEXT=  ["""Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley. """, """At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.""", """The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present."""]

registred_users = {"bob":  "123", "ann": "pass123", "mike": "sss", "liz": "pass123"}

separatorr = 60 * "="
print(separatorr)
print("Hello user, this is a text analyzer app, you can choose from 3 preset texts")
print(separatorr)
print("Now please enter your username and password")

user_input_username = input("Enter your username to verify: ")
user_input_password = input("Enter your password: ")

# checking if the user is registred, using if statment to do so

if registred_users.get(user_input_username) == user_input_password:
    print("you may enter")
else:
    print("unregistered user, terminating the program..")
    quit()


separated_lists = []

#separated lists in category of their own

for listt in TEXT:
    separated_lists.append(listt.split(","))

#print(separated_lists)

# i have to convert the lists to strings so i can use some string methods to get single words

text_1 = str(separated_lists[0])
text_2 = str(separated_lists[1])
text_3 = str(separated_lists[2])

#print(text_1)
#print(text_2)
#print(text_3)

#single words lists

single_words_text_1 = []
single_words_text_2 = []
single_words_text_3 = []

# looping thru lists to get single words from list 1
for text in text_1.split():
    single_words_text_1.append(text.strip("''"))

#print(single_words_text_1)

# loop list single words 2
for text in text_2.split():
    single_words_text_2.append(text.strip("''"))

#print(single_words_text_2)

# loop list single words 3
for text in text_3.split():
    single_words_text_3.append(text)

#print(single_words_text_3)

#the instances of words showing up in the texts

word_count_1 = dict()
word_count_2 = dict()
word_count_3 = dict()


#loop for counting words in text 1

for word in single_words_text_1:
    if word not in word_count_1:
        word_count_1.setdefault(word, 1)
    else:
        word_count_1[word] += 1

#print(word_count_1)

five_most_common_1 = sorted(word_count_1.values(), reverse=True)[:5]

#print(five_most_common_1)

results_1 = []

for word in word_count_1:
    if word_count_1[word] in five_most_common_1:
        results_1.append((word_count_1[word], word))

#print(results_1)
#loop 2 for top 5 words
for word in single_words_text_2:
    if word not in word_count_2:
        word_count_2.setdefault(word, 1)
    else:
        word_count_2[word] += 1

#print(word_count_2)
five_most_common_2 = sorted(word_count_2.values(), reverse=True)[:5]

#print(five_most_common_2)

results_2 = []

for word in word_count_2:
    if word_count_2[word] in five_most_common_2:
        results_2.append((word_count_2[word], word))

#print(results_2)

# loop 3 for counting words

for word in single_words_text_3:
    if word not in word_count_3:
        word_count_3.setdefault(word, 1)
    else:
        word_count_3[word] += 1

#print(word_count_3)

five_most_common_3 = sorted(word_count_3.values(), reverse=True)[:5]

#print(five_most_common_3)

results_3 = []

for word in word_count_3:
    if word_count_3[word] in five_most_common_3:
        results_3.append((word_count_3[word], word))

#print(results_3)
# tasks now:
# first number of words obvl (done)
#then
# 1.  number of words starting with capital letter. (done, needs tweak)
# 2.  number of words writen in capital letters. (done)
# 3.  number of words writen by small letters. (done)
# 4.  how many numbers there are in the texts. (done)
# 5.  number you get when you combine all numbers in texts. (done)
# 6. randomn lenghts of strings in the text, written in a cute little graph

#print(single_words_text_1)
#print(single_words_text_2)
#print(single_words_text_3)



# 1. loop for counting all words in text 1

all_words_number_1_count = 0

for word in single_words_text_1:
    if word.isalpha():
        all_words_number_1_count += 1

#print(all_words_number_1_count)

# 2. loop for counting all words in text 2

all_words_number_2_count = 0

for word in single_words_text_2:
    if word.isalpha():
        all_words_number_2_count += 1

#print(all_words_number_2_count)

# 3. loop for counting all words in text 3

all_words_number_3_count = 0

for word in single_words_text_3:
    if word.isalpha():
        all_words_number_3_count += 1

#print(all_words_number_3_count)


# loop for counting all capital starting words in text 1
#CAPITAL FIRST LETTER
#CAPITAL FIRST LETTER
#CAPITAL FIRST LETTER
#CAPITAL FIRST LETTER
first_capital_words_number_1 = 0

for word in single_words_text_1:
    for letter in word:
        if letter.isupper():
            #rint(letter)
            first_capital_words_number_1 += 1

#print(first_capital_words_number_1)

# loop for counting all capital starting words in text 2

first_capital_words_number_2 = 0

for word in single_words_text_2:
    for letter in word:
        if letter.isupper():
            #print(letter)
            first_capital_words_number_2 += 1

#print(first_capital_words_number_2)

# loop for counting all capital starting words in text 3

first_capital_words_number_3 = 0

for word in single_words_text_3:
    for letter in word:
        if letter.isupper():
            #print(letter)
            first_capital_words_number_3 += 1

#print(first_capital_words_number_3)

# now i will loop for words writen in fully capital letters in text 1
# CAPITAL WORDS
# CAPITAL WORDS

capital_words_number_1 = 0

for word in single_words_text_1:
    if word.isupper() and word.isalpha():
        capital_words_number_1 += 1

#print(capital_words_number_1)

#capital words in text 2

capital_words_number_2 = 0

for word in single_words_text_2:
    if word.isupper():
        capital_words_number_2 += 1

#print(capital_words_number_2)

#capital words in text 3

capital_words_number_3 = 0

for word in single_words_text_3:
    if word.isupper():
        capital_words_number_3 += 1

#print(capital_words_number_3)

# WORDS WRITTEN IN ALL SMALL LETTERS
# WORDS WRITTEN IN ALL SMALL LETTERS

# LOOP SMALL LETTERS 1

small_words_number_1 = 0

for word in single_words_text_1:
    if word.islower():
        small_words_number_1 += 1

#print(small_words_number_1)

##################################
#LOOP SMALL LETTERS 2

small_words_number_2 = 0

for word in single_words_text_2:
    if word.islower():
        small_words_number_2 += 1

#print(small_words_number_2)

small_words_number_3 = 0

#LOOP SMALL LETTERS 3

for word in single_words_text_3:
    if word.islower():
        #print(word)
        small_words_number_3 += 1

#print(small_words_number_3)

#LOOP FOR COUNTING NUMBERS IN TEXTS (HOW MANY THERE ARE)

# LOOP NUMBERS 1

numbers_words_number_1 = 0

for word in single_words_text_1:
    if word.isnumeric():
        numbers_words_number_1 += 1

#print(numbers_words_number_1)

# LOOP NUMBERS 2

numbers_words_number_2 = 0

for word in single_words_text_2:
    if word.isnumeric():
        numbers_words_number_2 += 1

#print(numbers_words_number_2)

# LOOP NUMBERS 3

numbers_words_number_3 = 0

for word in single_words_text_3:
    if word.isnumeric():
        numbers_words_number_3 += 1

#print(numbers_words_number_3)

# loop for sum numbers in texts 1

numbers_sum_1 = [i for i in single_words_text_1 if i.isnumeric()]
#print(numbers_sum_1)
sum_num_1 = sum(map(int, numbers_sum_1))
#print(sum_num_1)

# loop for sum numbers in texts 2

numbers_sum_2 = [i for i in single_words_text_2 if i.isnumeric()]
#print(numbers_sum_2)
sum_num_2 = sum(map(int, numbers_sum_2))
#print(sum_num_2)

# loop for sum numbers in texts 1

numbers_sum_3 = [i for i in single_words_text_3 if i.isnumeric()]
#print(numbers_sum_3)
sum_num_3 = sum(map(int, numbers_sum_3))
#print(sum_num_3)

# user inputs to choose texts that he wants
# if statments to find out what text user wants to analyze

#print(separatorr)
user_input_for_choosing_text = input("Now you can choose from the texts number 1 - 3, if u write in anyother number the program will shout down: ")


if user_input_for_choosing_text == "1":
    print(separatorr)
    print(f"There are {all_words_number_1_count} words in the text")
    print(f"There are {first_capital_words_number_1} words starting with capital letter")
    print(f"There are {capital_words_number_1} words written in all capital letters")
    print(f"There are {small_words_number_1} words written in all small letters")
    print(f"There are {numbers_words_number_1} numbers in the text")
    print(f"The Sum of all numbers in the text is {sum_num_1}")
    #print(f"Top 5 words {results_1}")
    print(separatorr)
    for index, wordnumber in enumerate(sorted(results_1, reverse=True), 1):
        print(separatorr,
              f"|{index}.|{wordnumber[1]:^12}|{wordnumber[0]}x|",
              sep="\n")

if user_input_for_choosing_text == "2":
    print(separatorr)
    print(f"There are {all_words_number_2_count} words in the text")
    print(f"There are {first_capital_words_number_2} words starting with capital letter")
    print(f"There are {capital_words_number_2} words written in all capital letters")
    print(f"There are {small_words_number_2} words written in all small letters")
    print(f"There are {numbers_words_number_2} numbers in the text")
    print(f"The Sum of all numbers in the text is {sum_num_2}")
    #print(f"Top 5 words {results_1}")
    print(separatorr)
    for index, wordnumber in enumerate(sorted(results_2, reverse=True), 1):
        print(separatorr,
              f"|{index}.|{wordnumber[1]:^12}|{wordnumber[0]}x|",
              sep="\n")

if user_input_for_choosing_text == "3":
    print(separatorr)
    print(f"There are {all_words_number_3_count} words in the text")
    print(f"There are {first_capital_words_number_3} words starting with capital letter")
    print(f"There are {capital_words_number_3} words written in all capital letters")
    print(f"There are {small_words_number_3} words written in all small letters")
    print(f"There are {numbers_words_number_3} numbers in the text")
    print(f"The Sum of all numbers in the text is {sum_num_3}")
    print(separatorr)
    #print(f"Top 5 words {results_3}")
    for index, wordnumber in enumerate(sorted(results_3, reverse=True), 1):
        print(separatorr,
              f"|{index}.|{wordnumber[1]:^12}|{wordnumber[0]}x|",
              sep="\n")
else:
    print("you didnt choose number 1 - 3. logging out")
