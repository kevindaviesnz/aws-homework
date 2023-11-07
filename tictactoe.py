''''
Please produce python block of code to print out the layer of a tic tac toe.
You are expected to:
    Use some kind of loop
    Be able to configure how big your tic tac toe.
        eg n =2  => 2 hyphen, 2 vertical lines
Save into a file.
'''

'''
eg _|_|_
   _|_|_
    | |
Notes:

No matter the size of the board there will only be two rows of horizontal lines.

The first and last rows will be always be vertical lines.

The number of rows between the first row and first row of horizontal lines, between the first row of horizontal lines and 
second row of horizontal lines, and between the second row of horizontal lines and last row will be equal to n 
where n is an integer representing the size of the board.

The number of spaces between each vertical line will always be equal to n.

The rows containing horizontal lines will always be the same and the rows containing vertical lines will always
be the same meaning that we can assign them to variables.


'''
n = 2
horizontal_space = (' ' * n) # basically the width of each square - use to make things more readable.
vertical_line_row = horizontal_space + '|' + horizontal_space + '|' + horizontal_space
horizontal_line_row = '_' * n * 4 # the horizontal rows have no spaces
rows = [vertical_line_row, horizontal_line_row, vertical_line_row, horizontal_line_row, vertical_line_row * n]
print(rows)