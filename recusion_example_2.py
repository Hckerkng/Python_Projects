def solve_me(num):
    if num == 1:
        return 0
    return num + solve_me(num-1)
x = solve_me(5)
print(x)
print("my name is mayank")