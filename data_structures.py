"""
Problem 1: Create a list of the first 10 positive integers.
Write a function to:
    Append the number 11 to the list.
    Remove the number 5 from the list.
    Print the list in reverse order.
"""

nums = [1,2,3,4,5,6,7,8,9,10] #Declare list
print("List is " + str(nums))
nums.append(11) #Append the number 11
nums.remove(5) #Remove the number 5
nums.reverse() #Reverse the order
print("Reversed and modified list is " + str(nums))


"""
Problem 2: Given a list of numbers, write a function to:
    Find and print the maximum and minimum numbers in the list.
    Calculate and print the average of the numbers in the list.
"""

nums_2 = [12,14,16,18,20,22,24] #Declare list
print("List is " + str(nums_2))
print("Maximum is " + str(max(nums_2))) #Determine max
print("Minimum is " + str(min(nums_2))) #Determine min
avg = sum(nums_2) / len(nums_2) #Determine average
print("Average is " + str(avg))


"""
Problem 3: Create a dictionary to store the names and ages of 5 people.
Write a function to:
    Add a new person to the dictionary.
    Remove a person from the dictionary by name.
    Print the average age of the people in the dictionary.
"""

dicti = {'Matt':20, 'Sally':30, 'Billy':20, 'Jesse':38, 'Sonya':26} #Declare dictionary
print("Dictionary is " + str(dicti))

def add(key,value): #Function to add person
	dicti[key]=value
	
def remove(name): #Function to remove person by name
	del dicti[name]
	
def average(dicti): #Function to determince average age
	print(sum(dicti.values()) / len(dicti))

add('Miriam',60)
remove('Matt')
print("Modified dictionary is " + str(dicti))
print("Average age is " )
(average(dicti))


"""
Problem 4: Given a dictionary with student names as keys and their scores as values,
write a function to:
    Print the name of the student with the highest score.
    Print the names of all students who scored above 80.
"""

dicti_2 = {'Matt':90, 'Sally':100, 'Billy':60, 'Jesse':70, 'Sonya':80} #Declare dictionary
print("Dictionary is " + str(dicti_2))

def highest(dicti_2): #Function for max score
	print(max(dicti_2, key=dicti_2.get))
	
def score80(dicti_2): #Function for all students scoring over 80
	above = [name for name, score in dicti_2.items() if score > 80]
	print(above)

print("Student with highest score is ")
highest(dicti_2)
print("Students scoring above 80: ")
score80(dicti_2)


"""
Problem 5: Create a tuple with the names of the days of the week.
Write a function to:
    Print the first and last days of the week.
    Check if "Wednesday" is in the tuple and print the result.
"""


#Declare tuple for days of week
days = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
print("Days of week are " + str(days))

#Function print first and last days and to verify that Wednesday is in the tuple

def print_and_check(days): 
    print("First day is " + days[0] + " and last day is " + days[6])
    if "Wednesday" in days:
        print("Wednesday is in the list")
    else:
        print("Wednesday is not in the list")

print_and_check(days)


"""
Problem 6: Given a tuple of numbers, write a function to:
    Convert the tuple to a list.
    Sort the list in ascending order.
    Convert the list back to a tuple and print it.
"""

#Declare tuple of numbers
number_set = (4, -100, 8, 7, 1, 22, -1)

#Function to convert tuple to a list,
#sort it,
#and convert back to tuple.

def convert_and_sort(number_set):
    number_list = list(number_set)
    number_list.sort()
    tuple_redux_sorted = tuple(number_list)
    return tuple_redux_sorted

print("Original number set is ", number_set)
print("Sorted number set is ", convert_and_sort(number_set))
 

"""
Problem 7: Create two sets of numbers. Write a function to:
    Find and print the union of the two sets.
    Find and print the intersection of the two sets.
    Find and print the difference between the two sets.
"""

#Declare two sets of numbers
s1={3,1,9,7,6}
s2={2,4,5,6,8}
print("set1 is " + str(s1))
print("set2 is " + str(s2))

union=s1.union(s2) #Determine union of sets
intersec=s1.intersection(s2) #Determine intersection of sets
diff1=s1.difference(s2) #Determine difference between set 1 and set 2
diff2=s2.difference(s1) #Determine difference between set 2 and set 1

print("Union is ", union)
print("Intersection is ", intersec)
print("Difference between set1 and set2 is ", diff1)
print("Difference between set2 and set1 is ", diff2)


"""
Problem 8: Given a set of words, write a function to:
    Add a new word to the set.
    Remove a word from the set.
    Print all the words in the set in alphabetical order.
"""

#Declare a set of words
s3={'alpha', 'beta', 'gamma', 'delta'}
print("set3 is " + str(s3))

s3.add('epsilon') #Add a word
s3.remove('alpha') #Remove a word
sorted_set=sorted(s3) #Sort the set

print("Modified and sorted set3 is " + str(sorted_set))

