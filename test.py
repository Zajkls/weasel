import random
import string

score = 0
count = 0
trial = 0
best_score = 0
test = []
correct = "This string is extremely long, however, I think that I can manage to solve this within a few hundred tries oh my goodness gracious I need to up this number from 161 this is taking way to little time so I will ad to the string let's make it like a bajillion or like 200" #<-- This originally said thousand but I think it is hundred only 161 HOLY
line = []
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
line = Convert(correct)
print(line)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ", "B", "I", "T", ",", "1", "6","1","'","2", "0", "0"]
for i in range(len(correct)):
    test.append(random.choice(alphabet))
print(test)
count = 0


# Python program to convert a list to string

# Function to convert
def stringfromlist(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
best_test = []
for i in range(len(correct)):
    best_test.append(random.choice(alphabet))
    tries = 0
while score != len(correct):
    count = 0
    score = 0
    best_score = 0
    for i in range(len(test)):
        if test[count] == line[count]:
            score = score + 1
            best_test[count] = test[count]
        elif test[count] != line[count]:
            test[count] = random.choice(alphabet)
        count = count + 1
    if score > best_score:
        best_score = score
        best_test = test
    if tries%1 == 0:
        print(best_test)
        print("SCORE: ", best_score)
        print("STR: ", stringfromlist(best_test))
        print("TRIES ", tries)
    tries = tries + 1
    count = 0

print(score)
#for alphabet in line

