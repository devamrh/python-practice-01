def count_squares(s):
    count_squares = 0
    
    for x in range(len(s) - 1):
        if s[x] == s[x + 1]:
            count_squares += 1
        
    return count_squares

s = '123123356789921'
result = count_squares(s)
print(f'The number of squares in "{s}" is: {result}')
