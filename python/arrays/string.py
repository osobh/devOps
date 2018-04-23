# #Setup a variable with a simple string
# s = "This is a string"
# print s[0]
# #prints "T"
#
# # find the length of the string
# len(s)

# --------------------------------------------------------------
# Practice Problems
# --------------------------------------------------------------
# Two ways to iterate over a string
# s = "abc"
#
# for character in s:
#     print(character)
#
# #prints the indices number
# for i in range(len(s)):
#     print i
#
# # --------------------------------------------------------------
#
# a_string = "ABC"
# print(a_string)
#
# b_string = "DEF"
# print b_string[1]
#
# c_string = "GHI"
# for character in c_string:
#     print character

# d_string = "PQR"
# for character in range(len(d_string)):
#     print d_string[character]

# string_1 = "ABC"
# string_2 = "CBA"
#
# def are_reverses(string_1, string_2):
#     for i in range(len(string_1)):
#         print string_1[i]
#         i_2 = len(string_2) - i - 1
#         print string_2[i_2]
#         if string_1[i] != string_2[i_2]:
#             print False
#             return False
#     print True
#     return True
#
# are_reverses(string_1,string_2)
