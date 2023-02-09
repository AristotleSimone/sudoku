'''
the goal of this project is to further my coding ability
i want to challenge myself with simple projects that push me to learn new tricks and skills 

the next step i want to add to this is a way to generate random numbers of a random qty and then fill the board out randomly
it would check if the numbers would be placed in a spot where it conflicts with sudoku rulesets and then place or not place

once the board is built (or if i manually add it - i may need to at first)
then the program will start solving the board.

the main challenge at this time i see is dealing with the squares, the cols will be the outer loop, the rows will be the in loop
'''

def make_board():
    bucket = []

    # makes list of column elements
    for i in range(6):
        bucket.append('|')
        if (i+1) % 2 == 0:
            bucket.append('#')

    # prints columns as a row
    for k in range(9):
        if k == 0:
            print('#####################################')        
        for l in range(9):
            if l == 0:
                print('#', end =' ')            
            print(' ', bucket[l], end=' ')
        print()
        if (k+1) % 3 == 0 and i != 9:
            print('#####################################')
