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
# given_2d = [[1,2,3], [4,5,6], [7,8,9]]
#
# def diagonal_sum(given_2d):
#     total = 0
#     for i in range(len(given_2d)):
#         total += given_2d[i][i]
#     print total
#     return total
#
# diagonal_sum(given_2d)

#-----------------------------------------------
#Sample interview Question, Are rooks on a chessboard safe. Take the 2D array and check to see if they are within range of each otherself.
#-----------------------------------------------
def rooks_are_safe(chessboard):
    n = len(chessboard)
    #give us each row index
    for row_i in range(n):
        #Count the number of rooks in each row, use variable to keep track of rooks seen so far.
        row_count = 0
        #iterate through each item in the row
        for col_i in range(n):
            row_count += chessboard[row_i][col_i]
            #when positive we will have a value for row_count
        if row_count > 1:
            print False
            return False

    #Now we do the same for the columns
    for col_i in range(n):
         col_count = 0
         for row_i in range(n):
             col_count += chessboard[row_i][col_i]
         if col_count >1:
             return False
    print True
    return True

rooks_are_safe([[1,0,0,0],
                [0,1,0,0],
                [0,0,0,1],
                [0,0,0,0]])
