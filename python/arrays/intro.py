# Setup a variable with a simple list
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


#--------------------------------------------------------------
Practice Problems
#--------------------------------------------------------------
# Problem01 - Initialize a new list called a_list
a_list = ["item01", "item02", "item03"]
print("a_list is: ")
print(a_list)
