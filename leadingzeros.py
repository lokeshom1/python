num = eval(input('Enter the values between 0 to 9999'))
if num < 0:
     num = 0
if num > 9999:
     num = 9999
print("[")
digit = num // 1000 # Thousnd's Place
print(digit, end='')
num %= 1000

digit = num //100 # Hundredth place
print(digit, end='')
num %=100

digit= num //10 # Tenth place
print(digit,end='')
num %=10

print(num,end='')
print(']')
