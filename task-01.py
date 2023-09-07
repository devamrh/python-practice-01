def thue_morse(n):
    if n == 0:
        return "0"
    else:
        prev_tn = thue_morse(n - 1)
        inverse_prev_tn = ""
        for x in prev_tn:
            if x == '0':
                inverse_prev_tn += '1'
            else:
                inverse_prev_tn += '0'
        return prev_tn + inverse_prev_tn

n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative integer for n.")
else:
    result = thue_morse(n)
    print(f"The {n}th term of the Thue–Morse sequence is: {result}")
