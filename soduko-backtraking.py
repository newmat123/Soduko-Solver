import pygame

#pip install pygame is needed for this project.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 20
HEIGHT = 20

MARGIN = 5


pygame.init()

WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)



def draw(grid, isdone):

    done = False

    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont("monospace", 20)

    while not done:
        # Draw the grid
        for row in range(9):
            for column in range(9):
                color = GREEN

                if grid[row][column] == 0:
                    color = WHITE

                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                label = myfont.render(str(grid[row][column]), 1, BLACK)
                screen.blit(label, [(MARGIN + WIDTH) * column + MARGIN+5, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                pygame.draw.line(screen, RED, [77, 0], [77, 250], 2)
                pygame.draw.line(screen, RED, [152, 0], [152, 250], 2)

                pygame.draw.line(screen, RED, [0, 77], [250, 77], 2)
                pygame.draw.line(screen, RED, [0, 151], [250, 151], 2)

        clock.tick(60)

        pygame.display.flip()

        if(not isdone):
            done = True


#printer det færdige grip
def print_grid(arr):
    for i in range(9):
        if(i % 3 == 0 and i != 0):
            print("---------------")

        for j in range(9):
            if(j % 3 == 0 and j != 0):
                print(" | ", end='')
            print (arr[i][j], end='')
        print ('')
    print("")
    print("")
    print("")



def find_empty_location(arr,l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False

# Returns a boolean which indicates whether any assigned entry
# in the specified row matches the given number.
def used_in_row(arr,row,num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

def used_in_col(arr,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

def used_in_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False


def check_location_is_safe(arr,row,col,num):
    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr, row - row%3, col - col%3, num)



def solve_sudoku(arr):

    draw(arr, False)
    print_grid(arr)

    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function
    l=[0,0]

    # If there is no unassigned location, we are done
    if(not find_empty_location(arr,l)):
        return True

    # Assigning list values to row and col that we got from the above Function
    row=l[0]
    col=l[1]

    # consider digits 1 to 9
    for num in range(1,10):

        if(check_location_is_safe(arr,row,col,num)):

            # make tentative assignment
            arr[row][col]=num

            # return, if success, ya!
            if(solve_sudoku(arr)):
                return True

            # failure, unmake & try again
            arr[row][col] = 0

    # this triggers backtracking
    return False


if __name__=="__main__":

    # creating a 2D array for the grid
    grid=[[0 for x in range(9)]for y in range(9)]

    grid=[[3,0,6,5,0,8,4,0,0],
    [5,2,0,0,0,0,0,0,0],
    [0,8,7,0,0,0,0,3,1],
    [0,0,3,0,1,0,0,8,0],
    [9,0,0,8,6,3,0,0,5],
    [0,5,0,0,9,0,6,0,0],
    [1,3,0,0,0,0,2,5,0],
    [0,0,0,0,0,0,0,7,4],
    [0,0,5,2,0,6,3,0,0]]

    if(solve_sudoku(grid)):
        print_grid(grid)
        print("done")
        draw(grid, True)
    else:
        print ("No solution exists")
        draw(grid, True)
