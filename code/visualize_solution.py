#def variable(r,c,v):
#    return r * 81 + c * 9 + v

# get solution from zchaff answer

import sys
from lib.utils import *

def retrieve(variable):
    variable -= 1
    row = variable/81
    column = (variable%81)/9
    value = variable - (81*row) - (9*column)
    return (row+1, column+1, value+1)

def test_retrieve():
    for row in range(0, 9):
        for col in range(0, 9):
            for value in range (1, 10):
                var = variable(row,col,value)
                print(var)
                retrieved = retrieve(var)
                print(retrieved)

def translate_solution(filename):
    variables = []
    answer = open(filename, 'r')
    for line in answer.readlines():
        for i in line.split(" "):
            if i != '':
                int(i)
                variables.append(i)
    positives = filter(lambda x: int(x) > 0, variables)

    solution = []
    for pos in positives:
        pos = int(pos)
        var = retrieve(pos)
        solution.append(var[2])
    return solution

def visualize(solution):
    print('-------------------------------------')
    for j in range(0,73,9):
        row = '|'
        for i in range(j, j+9):
            row += ' ' + str(solution[i]) + ' |'
        print(row)       
        print('-------------------------------------')

def visualize_givens(givens):
    list_givens = []
    for i, v in enumerate(givens):
        if v == '.':
            value = ' '
        else:
            value = int(v)
        list_givens.append(value)
    visualize(list_givens)
        
#visualize_givens('....8.5....3.1.86.16.....7.....79.8..3.4..9.......6....5......44..1......72.3..1.')
#sol = translate_solution('testsudoku_solution.txt')
#visualize(sol)


def main():
    if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" 'sudoku SAT solution file'"
        #print "Example: '....8.5....3.1.86.16.....7.....79.8..3.4..9.......6....5......44..1......72.3..1.'"
        sys.exit(2)
    filename = sys.argv[1]
    sol = translate_solution(filename)
    visualize(sol)
 

if __name__ == "__main__":
    main()


