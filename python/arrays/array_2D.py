# # 2 - Dimensional Arrays
# # First method of iteration
#
# a_2d = [[1,2,3], [5,6,7]]
# print a_2d
#
# #replace the number 6 with 99
# b_2d = [[1,2,3], [5,6,7]]
# b_2d[1][1] = 99
# print b_2d[1][1]
#
# #iterate over each item in c_2d and print it using the "for row in"
# c_2d = [['a','b','c'], ['x','y','z']]
#
# for row in c_2d:
#     for item in row:
#         print item
#
# #iterate over each item in d_2d and print it using the "for range in (len())"
#
# d_2d = [['a','b','c'], ['x','y','z']]
#
# for i in range(len(d_2d)):
#     for j in range(len(d_2d[i])):
#         print(d_2d[i][j])
#
# # Write a function that adds up the diagonal elements and returns the sum
given_2d = [[1,2,3], [4,5,6], [7,8,9]]

def diagonal_sum(given_2d):
    total = 0
    for i in range(len(given_2d)):
        total += given_2d[i][i]
    print total
    return total

diagonal_sum(given_2d)
