# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(grid):
    #Need to check the first row and column at the same time. Then the second row and second column
    numberofRows = len(grid) #Take the length of the list aka the number of rows
    numberofColumns = len(grid[0]) #Check the number of columns
    if not (numberofColumns == numberofRows):
        return False
    i = 0
    while i < numberofRows:
        j = 0
        while j < numberofRows:
            if grid[i][j] == grid[j][i]:
                j += 1
            else:
                return False
        i += 1
    return True


print(symmetric([1,2,3]))
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
#>>> True

print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]]))
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False