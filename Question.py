'''
Question in an IBM Test
-------------------------
Take in a string
Each letters how many times
Display the max number key
'''

string=input("Enter the string to evaluate:") # Taking in the string to evaluate
counter={} # The dictionary with letters and corresponding number of times they occur

for letter in string:
    if letter in counter:
        counter[letter]=counter[letter]+1 #We are seeing the counter more than once
    else:
        counter[letter]=1  #Its the first time we are seeing this letter in the string

print(counter)
print(max(counter.values())) #The max number of times the string is being repeated.


#Print the most occuring letter 

# Method 1: 
for letter in string:
    if counter[letter]==max(counter.values()):
        print(letter,": is the letter with max number of repeation")


#MEthod 2: 
max_so_far=0
most_occuring=""
for letter in counter:
    if counter[letter]> max_so_far:
        max_so_far=counter[letter]
        most_occuring=letter

print("The most occuring is :",most_occuring,"for", max_so_far,"times")
