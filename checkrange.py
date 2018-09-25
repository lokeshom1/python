value = eval(input('Please enter an integer value in the range of 0...10'))
if value >=0:
     if value <=10:
          print('In Range')
     else:
          print('Out of Range')         
print('Done')



print('##New Check Range Function ####')
if (value >= 0 and value <= 10):
     print('In Range')
else:
     print('Out Of Range')
print('Done2')


print('####Enhanced Chcek Range ####')
if value >=0:
     if value <=10:
          print(value,'In Range')
     else:
          print(value,'is too large')
else:
     print(value,'is tooo small')
print('Done')
