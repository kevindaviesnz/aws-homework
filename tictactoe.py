''''
Please produce python block of code to print out the layer of a tic tac toe.
You are expected to:
    Use some kind of loop
    Be able to configure how big your tic tac toe.
        eg n =2  => 2 hyphen, 2 vertical lines
Save into a file.

eg _|_|_
   _|_|_
    | |

Notes:

No matter the size of the board there will only be two rows of horizontal lines.

The first, middle, and last sets of rows will be always be vertical lines.

The number of rows between the first row and first row of horizontal lines, between the first row of horizontal lines and 
second row of horizontal lines, and between the second row of horizontal lines and last row will be equal to the size of each cell.

The number of spaces between each vertical line will always be equal to the size of each cell.

Each row containing horizontal lines will always be the same and each row containing vertical lines will always
be the same meaning that we can assign them to variables.

'''

size_of_each_cell = 2

output_file = 'tictactoe.txt'

### Generate the board rows and store into an array.
horizontal_space = f"{' ' * size_of_each_cell}"
vertical_line_row = f"{horizontal_space}|{horizontal_space}|{horizontal_space}"
# We need to take into account "_"s directly under vertical lines hence the extra '_' on either side.
horizontal_line_row = f"{'_'}{'_' * (size_of_each_cell * 3)}{'_'}"
# '*' in front of an array works like the javascript spread operator.
board_rows = [*[vertical_line_row] * size_of_each_cell, horizontal_line_row, *[vertical_line_row] * size_of_each_cell, horizontal_line_row, *[vertical_line_row] * size_of_each_cell] 

w = open(output_file, 'w')

for row in board_rows:
    print(row)
    w.write(row + '\n')




