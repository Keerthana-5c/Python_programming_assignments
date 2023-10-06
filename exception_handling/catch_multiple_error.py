a = int(input('Enter a numerator: '))
b= int(input('Enter a denominator: '))
try:
    ans = a / b
    print(f'Answer is: {ans}')
except (ZeroDivisionError, ValueError):
    print('Please enter number greater than zero')