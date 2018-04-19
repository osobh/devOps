#Setup a variable with a simple list
a = ["item01", "item02", "item03"]

# loop over each item in the list
# useful for going over a single list
for value in a:
    print(value)

#This would print:
#item01
#item02
#item03

#Useful for iterating across multiple lists at the same time
#understanding the range function
for i in range(len(a)):
    print (a[i])

# --------------------------------------------------------------
# Practice Problems
# --------------------------------------------------------------
Problem01 - Initialize a new list called a_list
a_list = ["item01", "item02", "item03"]
print("a_list is: ")
print(a_list)

# Change the second element of b_list
b_list = [0,0,0]
b_list[1]=1
print("b_list is: ")
print(b_list)

c_list = ["item01","item02","item03"]
for element in c_list:
    print c_list

# Iterate over each element in d_list and print it using the "for i in range" syntax
d_list = ["item01","item02","item03"]
for i in range(len(d_list)):
    print d_list[i]

# Find the sum of e_list
e_list = [32,55,710,1]
total = 0
for i in range(len(e_list)):
     total += e_list[i]
     print total

# Sample interview question #1
Given the list [1,3,4,5,0,2] , return the second largest number
masterarray = [1,3,4,5,0,2]
largest = 0
secondlargest = 0
for i in range(len(masterarray)):
    if masterarray[i] > largest:
        secondlargest = largest
        largest = masterarray[i]
        print largest
        print secondlargest
