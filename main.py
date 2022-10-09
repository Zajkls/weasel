import random
score = 0
count = 0
trial = 0
best_score = 0
test = []
line = "m,e,t,h,i,n,k,s, ,i,t, ,i,s, ,l,i,k,e, ,a, ,w,e,a,s,e,l"
line = line.split(",")
print(line)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
for i in range(28):
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


while score != 28:
    count = 0
    score = 0
    for i in range(28):
        if test[count] == line[count]:
            score = score + 1
        count = count + 1
    if score > best_score:
        best_score = score
        best_test = test
        print("\n", "CURRENT BEST SCORE: ", best_score)
        print(" CURRENT BEST: ", stringfromlist(best_test))
    else:
        pass
    if trial == 1:
        print(score)
        print(test)
    if trial%10000000 == 0:
        print("Try ", trial)
        print(stringfromlist(test))
    test = []
    for i in range(28):
        test.append(random.choice(alphabet))
    trial = trial + 1
print(score)
#for alphabet in line

