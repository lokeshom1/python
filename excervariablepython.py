i,j,k=eval(input('Enter the values of the i,j&k: '))
if i < j:
     if j < k:
          i = j
     else:
          j = k
else:
     if j > k:
          j=i
     else:
          i = k
print('i =', i, 'j=', j,'k=', k)


print('Other Program ')
val = eval(input())
if val < 10:
     if val != 5:
          print('WoW',end='')
     else:
          val += 1
else:
     if val == 17:
          val +=10
     else:
          print('Whoa',end='')
print(val)
