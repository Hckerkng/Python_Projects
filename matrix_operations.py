"""This Module is Based On Matrix Oprations using list Compression
Usages: python matrix_operations.py
"""
MATRIX = [[int(input(f"Enter value of {r}-{c}"))for r in range(3)] for c in range(3)]
print("*****Matrix is*****\n", MATRIX)
TMATRIX = [[MATRIX[c][r] for c in range(3)] for r in range(3)]
print("*****Transpose of the Matrix*****\n", TMATRIX)
ADDITION = [[MATRIX[r][c]+TMATRIX[r][c] for r in range(3)] for c in range(3)]
print("*****Addition of the Matrix*****\n", ADDITION)
SUB = [[MATRIX[r][c]-TMATRIX[r][c] for r in range(3)] for c in range(3)]
print("******Subtraction of the matrix*****\n", SUB)
