# File computes squareroot.py

#get value from the user

val = eval(input('Enter Number:'))

#Compute a provisional Sqaure Root

root = 1.0,

diff = root*2 - val


while diff > 0.00000001 or diff < -0.000000001:
     root = (root + val/root) /2
     print(root,'square is',root*root)

     diff = root*2 -val

print('Square root of', val, '=', root)
