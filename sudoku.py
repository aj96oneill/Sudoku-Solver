"""sudoku CpSolver

    a1 a2 a3  b1 b2 b3  c1 c2 c3
    a4 a5 a6  b4 b5 b6  c4 c5 c6
    a7 a8 a9  b7 b8 b9  c7 c8 c9

    d1 d2 d3  e1 e2 e3  f1 f2 f3
    d4 d5 d6  e4 e5 e6  f4 f5 f6
    d7 d8 d9  e7 e8 e9  f7 f8 f9

    g1 g2 g3  h1 h2 h3  i1 i2 i3
    g4 g5 g6  h4 h5 h6  i4 i5 i6
    g7 g8 g9  h7 h8 h9  i7 i8 i9
"""
from __future__ import print_function
from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count

    # def print_puzzle(self):
    #     print(self.__variables)
    #     print(self.Value(self.__variables[0]))
    #     # for i in self.__variables:
    #     #     print(i)
    #     #     print(self.Value(i))


def SolveSudoku():
    """Solve the sudoku puzzle."""
    # Constraint programming engine
    model = cp_model.CpModel()

    a1 = model.NewIntVar(1, 9, 'a1')
    a2 = model.NewIntVar(1, 9, 'a2')
    a3 = model.NewIntVar(1, 9, 'a3')
    a4 = model.NewIntVar(1, 9, 'a4')
    a5 = model.NewIntVar(1, 9, 'a5')
    a6 = model.NewIntVar(1, 9, 'a6')
    a7 = model.NewIntVar(1, 9, 'a7')
    a8 = model.NewIntVar(1, 9, 'a8')
    a9 = 1

    b1 = model.NewIntVar(1, 9, 'b1')
    b2 = model.NewIntVar(1, 9, 'b2')
    b3 = model.NewIntVar(1, 9, 'b3')
    b4 = model.NewIntVar(1, 9, 'b4')
    b5 = model.NewIntVar(1, 9, 'b5')
    b6 = 3
    b7 = model.NewIntVar(1, 9, 'b7')
    b8 = 2
    b9 = model.NewIntVar(1, 9, 'b9')

    c1 = model.NewIntVar(1, 9, 'c1')
    c2 = model.NewIntVar(1, 9, 'c2')
    c3 = model.NewIntVar(1, 9, 'c3')
    c4 = model.NewIntVar(1, 9, 'c4')
    c5 = 8
    c6 = 5
    c7 = model.NewIntVar(1, 9, 'c7')
    c8 = model.NewIntVar(1, 9, 'c8')
    c9 = model.NewIntVar(1, 9, 'c9')

    d1 = model.NewIntVar(1, 9, 'd1')
    d2 = model.NewIntVar(1, 9, 'd2')
    d3 = model.NewIntVar(1, 9, 'd3')
    d4 = model.NewIntVar(1, 9, 'd4')
    d5 = model.NewIntVar(1, 9, 'd5')
    d6 = 4
    d7 = model.NewIntVar(1, 9, 'd7')
    d8 = 9
    d9 = model.NewIntVar(1, 9, 'd9')

    e1 = 5
    e2 = model.NewIntVar(1, 9, 'e2')
    e3 = 7
    e4 = model.NewIntVar(1, 9, 'e4')
    e5 = model.NewIntVar(1, 9, 'e5')
    e6 = model.NewIntVar(1, 9, 'e6')
    e7 = model.NewIntVar(1, 9, 'e7')
    e8 = model.NewIntVar(1, 9, 'e8')
    e9 = model.NewIntVar(1, 9, 'e9')

    f1 = model.NewIntVar(1, 9, 'f1')
    f2 = model.NewIntVar(1, 9, 'f2')
    f3 = model.NewIntVar(1, 9, 'f3')
    f4 = 1
    f5 = model.NewIntVar(1, 9, 'f5')
    f6 = model.NewIntVar(1, 9, 'f6')
    f7 = model.NewIntVar(1, 9, 'f7')
    f8 = model.NewIntVar(1, 9, 'f8')
    f9 = model.NewIntVar(1, 9, 'f9')

    g1 = 5
    g2 = model.NewIntVar(1, 9, 'g2')
    g3 = model.NewIntVar(1, 9, 'g3')
    g4 = model.NewIntVar(1, 9, 'g4')
    g5 = model.NewIntVar(1, 9, 'g5')
    g6 = 2
    g7 = model.NewIntVar(1, 9, 'g7')
    g8 = model.NewIntVar(1, 9, 'g8')
    g9 = model.NewIntVar(1, 9, 'g9')

    h1 = model.NewIntVar(1, 9, 'h1')
    h2 = model.NewIntVar(1, 9, 'h2')
    h3 = model.NewIntVar(1, 9, 'h3')
    h4 = model.NewIntVar(1, 9, 'h4')
    h5 = 1
    h6 = model.NewIntVar(1, 9, 'h6')
    h7 = model.NewIntVar(1, 9, 'h7')
    h8 = 4
    h9 = model.NewIntVar(1, 9, 'h9')

    i1 = model.NewIntVar(1, 9, 'i1')
    i2 = 7
    i3 = 3
    i4 = model.NewIntVar(1, 9, 'i4')
    i5 = model.NewIntVar(1, 9, 'i5')
    i6 = model.NewIntVar(1, 9, 'i6')
    i7 = model.NewIntVar(1, 9, 'i7')
    i8 = model.NewIntVar(1, 9, 'i8')
    i9 = 9

    # We need to group variables in a list to use the constraint AllDifferent.
    block1 = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
    block2 = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    block3 = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
    block4 = [d1,d2,d3,d4,d5,d6,d7,d8,d9]
    block5 = [e1,e2,e3,e4,e5,e6,e7,e8,e9]
    block6 = [f1,f2,f3,f4,f5,f6,f7,f8,f9]
    block7 = [g1,g2,g3,g4,g5,g6,g7,g8,g9]
    block8 = [h1,h2,h3,h4,h5,h6,h7,h8,h9]
    block9 = [i1,i2,i3,i4,i5,i6,i7,i8,i9]

    row1 = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    row2 = [a4, a5, a6, b4, b5, b6, c4, c5, c6]
    row3 = [a7, a8, a9, b7, b8, b9, c7, c8, c9]
    row4 = [d1, d2, d3, e1, e2, e3, f1, f2, f3]
    row5 = [d4, d5, d6, e4, e5, e6, f4, f5, f6]
    row6 = [d7, d8, d9, e7, e8, e9, f7, f8, f9]
    row7 = [g1, g2, g3, h1, h2, h3, i1, i2, i3]
    row8 = [g4, g5, g6, h4, h5, h6, i4, i5, i6]
    row9 = [g7, g8, g9, h7, h8, h9, i7, i8, i9]

    col1 = [a1, a4, a7, d1, d4, d7, g1, g4, g7]
    col2 = [a2, a5, a8, d2, d5, d8, g2, g5, g8]
    col3 = [a3, a6, a9, d3, d6, d9, g3, g6, g9]
    col4 = [b1, b4, b7, e1, e4, e7, h1, h4, h7]
    col5 = [b2, b5, b8, e2, e5, e8, h2, h5, h8]
    col6 = [b3, b6, b9, e3, e6, e9, h3, h6, h9]
    col7 = [c1, c4, c7, f1, f4, f7, i1, i4, i7]
    col8 = [c2, c5, c8, f2, f5, f8, i2, i5, i8]
    col9 = [c3, c6, c9, f3, f6, f9, i3, i6, i9]

    variables = [a1,a2,a3,a4,a5,a6,a7,a8,a9,
                b1,b2,b3,b4,b5,b6,b7,b8,b9,
                c1,c2,c3,c4,c5,c6,c7,c8,c9,
                d1,d2,d3,d4,d5,d6,d7,d8,d9,
                e1,e2,e3,e4,e5,e6,e7,e8,e9,
                f1,f2,f3,f4,f5,f6,f7,f8,f9,
                g1,g2,g3,g4,g5,g6,g7,g8,g9,
                h1,h2,h3,h4,h5,h6,h7,h8,h9,
                i1,i2,i3,i4,i5,i6,i7,i8,i9]

    model.AddAllDifferent(block1)
    model.AddAllDifferent(block2)
    model.AddAllDifferent(block3)
    model.AddAllDifferent(block4)
    model.AddAllDifferent(block5)
    model.AddAllDifferent(block6)
    model.AddAllDifferent(block7)
    model.AddAllDifferent(block8)
    model.AddAllDifferent(block9)
    model.AddAllDifferent(row1)
    model.AddAllDifferent(row2)
    model.AddAllDifferent(row3)
    model.AddAllDifferent(row4)
    model.AddAllDifferent(row5)
    model.AddAllDifferent(row6)
    model.AddAllDifferent(row7)
    model.AddAllDifferent(row8)
    model.AddAllDifferent(row9)
    model.AddAllDifferent(col1)
    model.AddAllDifferent(col2)
    model.AddAllDifferent(col3)
    model.AddAllDifferent(col4)
    model.AddAllDifferent(col5)
    model.AddAllDifferent(col6)
    model.AddAllDifferent(col7)
    model.AddAllDifferent(col8)
    model.AddAllDifferent(col9)
    
    ### Solve model.
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter(variables)
    status = solver.SearchForAllSolutions(model, solution_printer)

    print()
    print('Statistics')
    print('  - status          : %s' % solver.StatusName(status))
    print('  - conflicts       : %i' % solver.NumConflicts())
    print('  - branches        : %i' % solver.NumBranches())
    print('  - wall time       : %f s' % solver.WallTime())
    print('  - solutions found : %i' % solution_printer.solution_count())
    #print(solution_printer.print_puzzle())

if __name__ == '__main__':
    SolveSudoku()
